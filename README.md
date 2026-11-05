<p align="center"><img src="assets/icon-preview.png" width="96" alt="Select Translate icon"></p>

<h1 align="center">Select Translate</h1>

<p align="center">Bôi đen chữ ở bất kỳ app nào trên Windows là có ngay bản dịch <b>Việt · English · 中文</b> bằng <b>Claude</b> hoặc <b>ChatGPT (Codex)</b>, dùng chính tài khoản đã đăng nhập trên máy, không cần API key.</p>

<p align="center"><img src="assets/pet-preview.png" width="480" alt="Pet: chờ · đang bật · đang dịch · tạm dừng"></p>

---

## Tính năng

- **Bôi đen là dịch**: popup nhỏ hiện cạnh vùng chọn, mặc định dịch sang tiếng Việt, chữ hiện dần khi model đang trả lời.
- **3 ngôn ngữ VI / EN / 中文**: bấm EN hoặc 中文 để viết lại sang ngôn ngữ đó cho đúng ngữ cảnh. Nếu chữ đã là ngôn ngữ đó thì tool chỉ sửa chính tả và câu chữ cho tự nhiên.
- **Dán thay**: thay đoạn đang bôi đen bằng bản dịch, tiện khi đang soạn tin nhắn.
- **Claude Code hoặc Codex CLI**: tool dùng login sẵn có của CLI. Chọn model và effort ngay trong popup, danh sách model lấy theo tài khoản trên máy.
- **Nhanh**: tiến trình CLI chạy nền liên tục, không mở phiên mới mỗi lần; mỗi lần dịch mất khoảng 1–3 giây.
- **Pet**: bong bóng nhỏ ở góc màn hình, click để bật hoặc tắt chế độ dịch, kéo đi đâu cũng được.
- **Nhẹ**: một file exe khoảng 650 KB, RAM khoảng 12 MB, không cần Python, .NET hay runtime nào khác.

## Yêu cầu

- Windows 10 hoặc 11, 64-bit.
- Ít nhất một trong hai CLI dưới đây, đã cài và đã đăng nhập (cần [Node.js](https://nodejs.org) để cài qua npm):

  | CLI | Cài đặt | Đăng nhập |
  |---|---|---|
  | Claude Code (gói Claude Pro/Max) | `npm i -g @anthropic-ai/claude-code` | `claude auth login` |
  | Codex (gói ChatGPT Plus/Pro) | `npm i -g @openai/codex` | `codex login` |

  Chưa đăng nhập cũng không sao: lần bôi đen đầu tiên, popup sẽ báo lỗi kèm nút **Đăng nhập**, bấm vào là trình duyệt mở trang đăng nhập.

## Cài đặt

Tải **`select-translate-<version>-x64.msi`** ở trang **Releases** rồi double-click. Không cần quyền admin, cài xong tool tự mở.

- Tool được cài vào `%LOCALAPPDATA%\Programs\SelectTranslate`, có shortcut trong Start Menu và tự chạy cùng Windows.
- Không muốn tự chạy cùng Windows thì cài bằng lệnh: `msiexec /i select-translate-<version>-x64.msi AUTOSTART=0`.
- Cài bản mới đè lên bản cũ được; `config.json` của bạn vẫn được giữ.

> File chưa ký số, nên Windows SmartScreen có thể cảnh báo. Bấm **More info → Run anyway**.

Bản portable (không cài): tải `select-translate-<version>-portable.zip`, giải nén rồi chạy `select-translate.exe`. File `config.json` sẽ được tạo cạnh exe.

## Cách dùng

### Bôi đen

Những thao tác sau đều tính là bôi đen:

| Cách | Thao tác |
|---|---|
| Chuột | kéo, double-click, triple-click, Shift+click |
| Bàn phím | Shift + mũi tên / Home / End / PgUp / PgDn (dịch khi nhả Shift), Ctrl+A (dịch khi nhả Ctrl) |

Các nút trên popup:

| Nút | Tác dụng |
|---|---|
| **VI · EN · 中文** | Dịch sang ngôn ngữ đó, hoặc sửa chính tả nếu chữ đã là ngôn ngữ đó |
| **Copy** | Copy bản dịch |
| **Dán thay** | Thay đoạn đang bôi đen bằng bản dịch |
| **Model ▾** | Đổi backend Claude/Codex, model, effort |
| **✕** | Đóng popup |

### Pet: khi nào thì dịch

| Trạng thái | Kết quả |
|---|---|
| Tool không chạy | Không dịch, không ảnh hưởng gì |
| Pet **tắt** | Bôi đen trong các app ở danh sách `apps` (mặc định iMe) là dịch luôn |
| Pet **bật**, chưa click (xám) | Không dịch |
| Pet **bật**, đã click (xanh ngọc) | Bôi đen ở **mọi app** đều dịch, cho đến khi click pet lần nữa |

- Ý nghĩa màu pet: xám là chờ, xanh ngọc là đang bật dịch, xanh dương có ba chấm là đang dịch, xám đậm nhắm mắt là tạm dừng (click để đánh thức).
- Kéo pet đi đâu cũng được; thả gần mép màn hình thì pet tự hít vào mép, và vị trí được nhớ.
- Chuột phải vào pet để mở menu.

### Phím tắt và khay hệ thống

| Phím | Tác dụng |
|---|---|
| `Ctrl+Alt+P` | Bật/tắt pet |
| `Ctrl+Alt+T` | Tạm dừng / chạy lại |
| `Ctrl+Alt+Q` | Thoát |

Icon ở khay hệ thống (góc phải taskbar) có menu: Pet, Tạm dừng, Model / effort, Mở config.json, Đăng nhập Claude / Codex, Thoát.

## Cấu hình

`config.json` nằm cạnh exe. Tool tạo file này ở lần chạy đầu; chọn trong menu Model thì file cũng được cập nhật theo.

| Khóa | Mặc định | Ý nghĩa |
|---|---|---|
| `backend` | `"claude"` | `"claude"` hoặc `"codex"` |
| `claude_model` / `claude_effort` | `claude-sonnet-5-5` / `low` | effort: `low`, `medium`, `high` |
| `codex_model` / `codex_effort` | `gpt-6.1-terra` / `low` | effort: `minimal`, `low`, `medium`, `high` |
| `apps` | `["ime.exe"]` | Khi pet tắt: tên process được bắt bôi đen, ví dụ thêm `"telegram.exe"`. `[]` = mọi app |
| `pet`, `pet_x`, `pet_y` | `true` | Bật pet; vị trí tự lưu khi kéo |
| `claude_path` / `codex_path` | `""` | Để trống thì tool tự tìm; điền đường dẫn exe nếu CLI cài ở chỗ lạ |

## Dòng lệnh

```bat
select-translate.exe --models              :: liệt kê model mà tài khoản trên máy dùng được
select-translate.exe --selftest [codex]    :: dịch thử 4 câu mẫu, in thời gian
select-translate.exe --login claude|codex  :: mở cửa sổ đăng nhập CLI
```

## Cách hoạt động và quyền riêng tư

- Khi phát hiện bôi đen, tool tự gửi `Ctrl+C`, đọc chữ, rồi trả lại nội dung clipboard cũ.
- Chữ được gửi tới **Anthropic** (Claude Code) hoặc **OpenAI** (Codex) qua CLI và tài khoản của bạn. Tool không có server riêng và không gửi dữ liệu đi đâu khác.
- Claude chạy bằng `claude -p` dạng stream-json, không tool, không MCP, không lưu session. Codex chạy bằng `codex app-server`, sandbox read-only, tắt hooks/MCP/plugin/skill chỉ cho tool này; config Codex của bạn không bị sửa.
- Prompt hệ thống dặn model coi chữ được bôi đen là dữ liệu cần dịch, không làm theo nội dung trong đó.
- Log lỗi nằm ở `%TEMP%\select-translate\log.txt`, không chứa nội dung đã dịch.

## Gỡ cài đặt

Vào *Settings → Apps → Select Translate → Uninstall*. Tool, shortcut, autostart và `config.json` đều được xoá.

## Build từ source

Cần:

- [Rust](https://rustup.rs) với toolchain GNU (không cần Visual Studio hay Windows SDK).
- [.NET SDK](https://dotnet.microsoft.com/download) 6 trở lên, để chạy WiX 5 tạo MSI. Lần build đầu, WiX tự được tải vào `.tools\`.

```powershell
rustup toolchain install stable-x86_64-pc-windows-gnu
powershell -NoProfile -File build.ps1
```

`build.ps1` build bản release, gắn icon `assets\icon.ico` vào exe, rồi tạo trong `dist\`:

- `select-translate.exe`
- `select-translate-<version>-x64.msi`: bộ cài, nguồn ở `installer\select-translate.wxs`.
- `select-translate-<version>-portable.zip`: gồm exe và README.

Upload file MSI và file zip lên Releases. Mỗi bản phát hành mới cần tăng `version` trong `Cargo.toml`, vì MSI chỉ nâng cấp đè lên bản cũ khi số version lớn hơn.

Icon được vẽ bằng `assets\make_icon.py` (Pillow): `py -3 assets\make_icon.py`.

## Giới hạn

- Clipboard chỉ được trả lại phần chữ; nếu clipboard đang chứa ảnh hoặc file thì nội dung đó sẽ mất khi bạn bôi đen.
- Một số app chặn `Ctrl+C` giả lập (app chạy quyền admin, một số game) thì tool không đọc được vùng chọn.
- Tốc độ và hạn mức phụ thuộc gói Claude/ChatGPT của tài khoản.
