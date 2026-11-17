# select-translate: continue here

State on 2026-11-17 (repo `D:\tools\select-translate`, branch `main`).

## Done
- 1.3.0 (committed f0a776e): cancel a running translation, 90 s stall timeout, hooks on their own thread, CLI pre-start, daily Claude model list, tray icon after Explorer restart, cache key with effort, panic log.
- 1.3.1: pet comes back by itself (`pet_keep`: hidden / off-screen / covered / display change), translation popup can be dragged.
- 1.4.0–1.4.1: "Tóm tắt" button (summary instead of translation; selections of 3,000–20,000 characters are summed up straight away).
- 1.4.2 (installed): summary prompt tightened to at most 2 short sentences, about 40 words.

## Pending
- Nothing after f0a776e is committed. No GitHub release for 1.3.1 / 1.4.x yet (attach `dist\select-translate-x64.msi` and `dist\select-translate-portable.zip`, keep the names).
- Not tested live: tray icon after an Explorer restart, the 90 s stall timeout, pet after really unplugging a monitor or sleep.
- Log shows `pet brought back: covered=true` several times a day: another always-on-top window covers the pet; which one is unknown.

## Commands
- Build exe: `cargo +stable-x86_64-pc-windows-gnu build --release`
- Tests: `cargo +stable-x86_64-pc-windows-gnu test --release`; `target\release\select-translate.exe --selftest codex|claude`
- Release files: `powershell -NoProfile -File build.ps1` (close the running app first: it locks the exe)
- App log: `%TEMP%\select-translate\log.txt`
