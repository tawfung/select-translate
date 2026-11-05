# Build select-translate.exe, embed assets\icon.ico, copy to dist\.   Run: powershell -NoProfile -File build.ps1
# (GNU toolchain: this machine has no Windows SDK for MSVC, and rust-mingw ships no windres,
#  so the icon goes in after linking with the Win32 UpdateResource API.)
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
$env:PATH = "$env:USERPROFILE\.cargo\bin;$env:PATH"
cargo +stable-x86_64-pc-windows-gnu build --release
if ($LASTEXITCODE) { exit $LASTEXITCODE }

Add-Type -TypeDefinition @'
using System; using System.IO; using System.Runtime.InteropServices;
public static class IconRes {
    [DllImport("kernel32", SetLastError = true, CharSet = CharSet.Unicode)] static extern IntPtr BeginUpdateResource(string f, bool del);
    [DllImport("kernel32", SetLastError = true)] static extern bool UpdateResource(IntPtr h, IntPtr type, IntPtr name, ushort lang, byte[] data, uint size);
    [DllImport("kernel32", SetLastError = true)] static extern bool EndUpdateResource(IntPtr h, bool discard);
    // ICO file -> RT_ICON (ids 1..n) + RT_GROUP_ICON id 1 (the exe icon; the app loads it as resource 1)
    public static void Set(string exe, string ico) {
        byte[] f = File.ReadAllBytes(ico);
        int n = BitConverter.ToUInt16(f, 4);
        var grp = new MemoryStream(); var g = new BinaryWriter(grp);
        g.Write((ushort)0); g.Write((ushort)1); g.Write((ushort)n);
        IntPtr h = BeginUpdateResource(exe, false);
        if (h == IntPtr.Zero) throw new Exception("BeginUpdateResource " + Marshal.GetLastWin32Error());
        for (int i = 0; i < n; i++) {
            int e = 6 + 16 * i;
            int size = BitConverter.ToInt32(f, e + 8), off = BitConverter.ToInt32(f, e + 12);
            byte[] img = new byte[size]; Array.Copy(f, off, img, 0, size);
            if (!UpdateResource(h, (IntPtr)3, (IntPtr)(i + 1), 0, img, (uint)size)) throw new Exception("RT_ICON " + Marshal.GetLastWin32Error());
            g.Write(f, e, 12); g.Write((ushort)(i + 1));
        }
        byte[] gb = grp.ToArray();
        if (!UpdateResource(h, (IntPtr)14, (IntPtr)1, 0, gb, (uint)gb.Length)) throw new Exception("RT_GROUP_ICON " + Marshal.GetLastWin32Error());
        if (!EndUpdateResource(h, false)) throw new Exception("EndUpdateResource " + Marshal.GetLastWin32Error());
    }
}
'@
$exe = "$PSScriptRoot\target\release\select-translate.exe"
[IconRes]::Set($exe, "$PSScriptRoot\assets\icon.ico")
New-Item -ItemType Directory -Force dist | Out-Null
Copy-Item $exe dist\ -Force
"built: dist\select-translate.exe  $((Get-Item dist\select-translate.exe).Length) bytes"

# Release files for GitHub Releases: MSI installer (WiX 5, fetched into .tools on first build) + portable zip
$ver = (Select-String -Path Cargo.toml -Pattern '^version\s*=\s*"(.+)"').Matches[0].Groups[1].Value
$wix = "$PSScriptRoot\.tools\wix.exe"
if (-not (Test-Path $wix)) {
    dotnet tool install wix --version 5.0.2 --tool-path .tools
    if ($LASTEXITCODE) { exit $LASTEXITCODE }
    & $wix extension add WixToolset.Util.wixext/5.0.2
}
$msi = "dist\select-translate-$ver-x64.msi"
& $wix build installer\select-translate.wxs -ext WixToolset.Util.wixext -d Version=$ver -arch x64 -o $msi
if ($LASTEXITCODE) { exit $LASTEXITCODE }
Remove-Item dist\*.wixpdb -ErrorAction SilentlyContinue
"release: $msi  $((Get-Item $msi).Length) bytes"
$zip = "dist\select-translate-$ver-portable.zip"
Compress-Archive $exe, README.md $zip -Force
"release: $zip  $((Get-Item $zip).Length) bytes"
