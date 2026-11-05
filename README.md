<p align="center"><img src="assets/icon-preview.png" width="96" alt="Select Translate"></p>

<h1 align="center">Select Translate</h1>

<p align="center">
Bôi đen chữ ở bất kỳ app nào trên Windows để dịch <b>Việt · English · 中文</b> bằng <b>Claude</b> hoặc <b>ChatGPT (Codex)</b>.<br>
Tool dùng tài khoản đã đăng nhập sẵn trên máy, không cần API key.
</p>

<p align="center">
<a href="https://github.com/tawfung/select-translate/releases/latest/download/select-translate-x64.msi"><b>⬇ Tải bộ cài (.msi)</b></a>
&nbsp;·&nbsp;
<a href="https://github.com/tawfung/select-translate/releases/latest/download/select-translate-portable.zip">Bản portable (.zip)</a>
&nbsp;·&nbsp;
<a href="https://github.com/tawfung/select-translate/releases">Tất cả phiên bản</a>
</p>

<p align="center"><img src="assets/pet-preview.png" width="420" alt="Pet: chờ · bật dịch · đang dịch · tạm dừng"></p>

## Tính năng

- **Bôi đen là dịch**: popup hiện cạnh vùng chọn, mặc định dịch sang tiếng Việt, chữ hiện dần khi model đang trả lời.
- **VI / EN / 中文**: bấm EN hoặc 中文 để viết lại sang ngôn ngữ đó. Nếu chữ đã là ngôn ngữ đó, tool chỉ sửa chính tả và câu chữ.
- **Dán thay**: thay đoạn đang bôi đen bằng bản dịch, tiện khi soạn tin nhắn.
- **Claude Code hoặc Codex CLI**: đổi model và effort ngay trên popup; danh sách model lấy theo tài khoản trên máy.
- **Nhanh và nhẹ**: CLI chạy nền liên tục nên mỗi lần dịch mất khoảng 1–3 giây. Exe khoảng 650 KB, dùng khoảng 12 MB RAM, không cần runtime.

## Cài đặt

1. Cài ít nhất một CLI và đăng nhập. Cần [Node.js](https://nodejs.org) để cài qua npm.

   | CLI | Gói tài khoản | Cài | Đăng nhập |
   |---|---|---|---|
   | Claude Code | Claude Pro/Max | `npm i -g @anthropic-ai/claude-code` | `claude auth login` |
   | Codex | ChatGPT Plus/Pro | `npm i -g @openai/codex` | `codex login` |

   Nếu quên đăng nhập, popup sẽ có nút **Đăng nhập** để mở trình duyệt.

2. Tải [**select-translate-x64.msi**](https://github.com/tawfung/select-translate/releases/latest/download/select-translate-x64.msi) rồi double-click.
   - Không cần quyền admin. Tool được cài vào `%LOCALAPPDATA%\Programs\SelectTranslate`, có shortcut trong Start Menu, tự chạy cùng Windows và tự mở sau khi cài.
   - Cài bản mới đè lên bản cũ vẫn giữ cấu hình.
   - Không muốn tự chạy cùng Windows thì cài bằng lệnh: `msiexec /i select-translate-x64.msi AUTOSTART=0`.
   - Windows SmartScreen có thể cảnh báo vì file chưa ký số. Bấm **More info → Run anyway**.

Bản portable: giải nén [select-translate-portable.zip](https://github.com/tawfung/select-translate/releases/latest/download/select-translate-portable.zip) rồi chạy `select-translate.exe`.

Gỡ cài đặt: vào *Settings → Apps → Select Translate → Uninstall*.

## Sử dụng

**Những thao tác tính là bôi đen**

| Cách | Thao tác |
|---|---|
| Chuột | kéo, double-click, triple-click, Shift+click |
| Bàn phím | Shift + mũi tên / Home / End / PgUp / PgDn (dịch khi nhả Shift), Ctrl+A (dịch khi nhả Ctrl) |

**Nút trên popup**

| Nút | Tác dụng |
|---|---|
| VI · EN · 中文 | Dịch sang ngôn ngữ đó, hoặc sửa chính tả nếu chữ đã là ngôn ngữ đó |
| Copy | Copy bản dịch |
| Dán thay | Thay đoạn đang bôi đen bằng bản dịch |
| Model ▾ | Đổi backend, model, effort |

**Pet: khi nào thì dịch**

| Trạng thái | Kết quả |
|---|---|
| Pet tắt | Bôi đen trong các app ở danh sách `apps` (mặc định iMe) là dịch luôn |
| Pet bật, màu xám | Không dịch |
| Pet bật, màu xanh ngọc (đã click) | Bôi đen ở mọi app đều dịch, cho đến khi click pet lần nữa |

- Pet màu xanh dương có ba chấm nghĩa là đang dịch. Màu xám đậm, mắt nhắm nghĩa là tạm dừng.
- Kéo pet đi đâu cũng được; thả gần mép màn hình thì pet tự hít vào mép.
- Chuột phải vào pet để mở menu.

**Phím tắt**

| Phím | Tác dụng |
|---|---|
| `Ctrl+Alt+P` | Bật/tắt pet |
| `Ctrl+Alt+T` | Tạm dừng |
| `Ctrl+Alt+Q` | Thoát |

Menu ở khay hệ thống có: Pet, Tạm dừng, Model / effort, Mở config.json, Đăng nhập Claude/Codex, Thoát.

## Cấu hình

File `config.json` nằm cạnh exe. Chọn trong menu Model thì file tự cập nhật.

| Khóa | Mặc định | Ghi chú |
|---|---|---|
| `backend` | `claude` | `claude` hoặc `codex` |
| `claude_model`, `claude_effort` | `claude-sonnet-5-5`, `low` | effort: `low`, `medium`, `high` |
| `codex_model`, `codex_effort` | `gpt-6.1-terra`, `low` | effort: `minimal`, `low`, `medium`, `high` |
| `apps` | `["ime.exe"]` | Dùng khi pet tắt. Thêm ví dụ `"telegram.exe"`; `[]` = mọi app |
| `pet` | `true` | Vị trí pet (`pet_x`, `pet_y`) tự lưu khi kéo |
| `claude_path`, `codex_path` | trống | Điền đường dẫn exe nếu CLI cài ở chỗ lạ |

Dòng lệnh:

```bat
select-translate.exe --models              :: liệt kê model tài khoản dùng được
select-translate.exe --selftest [codex]    :: dịch thử 4 câu mẫu
select-translate.exe --login claude|codex  :: mở cửa sổ đăng nhập CLI
```

## Quyền riêng tư

- Tool tự gửi `Ctrl+C` để lấy chữ được bôi đen, rồi trả lại nội dung clipboard cũ (chỉ phần chữ).
- Chữ chỉ được gửi tới Anthropic hoặc OpenAI qua CLI và tài khoản của bạn; tool không có server riêng.
- CLI chạy ở chế độ không tool, không MCP, không lưu phiên; config CLI của bạn không bị sửa.
- Log lỗi ở `%TEMP%\select-translate\log.txt`, không chứa nội dung đã dịch.

**Giới hạn**

- Nếu clipboard đang chứa ảnh hoặc file thì nội dung đó sẽ mất khi bạn bôi đen.
- App chạy quyền admin và một số game chặn `Ctrl+C` giả lập, nên tool không lấy được chữ ở đó.

## Build từ source

Cần [Rust](https://rustup.rs) với toolchain GNU (không cần Visual Studio) và [.NET SDK](https://dotnet.microsoft.com/download) 6 trở lên (để chạy WiX 5 tạo MSI; WiX tự tải vào `.tools\` ở lần build đầu).

```powershell
rustup toolchain install stable-x86_64-pc-windows-gnu
powershell -NoProfile -File build.ps1
```

Kết quả nằm trong `dist\`: `select-translate.exe`, `select-translate-x64.msi` và `select-translate-portable.zip`.

**Phát hành bản mới**

1. Tăng `version` trong `Cargo.toml`. Bước này bắt buộc: MSI chỉ nâng cấp đè lên bản cũ khi số version lớn hơn.
2. Chạy `build.ps1`.
3. Tạo GitHub Release với tag `vX.Y.Z` và đính kèm 2 file `.msi` và `.zip`. Tên file giữ nguyên qua các bản, nên link tải ở đầu README luôn trỏ tới bản mới nhất.

| Đường dẫn | Nội dung |
|---|---|
| `src/main.rs` | Toàn bộ app (Win32 qua `windows-sys`) |
| `installer/select-translate.wxs` | Bộ cài MSI (WiX 5) |
| `assets/` | Icon (`make_icon.py` vẽ bằng Pillow) và ảnh minh hoạ |
