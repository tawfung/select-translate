"""Draws assets/icon.ico (16-256 px) + assets/icon-preview.png.  Run: py -3 assets/make_icon.py
Big sizes: blue tile with two chat bubbles ("A" behind, "文" in front). 32 px: one bubble. <=24 px: bold "文" only.
"""
import io, os, struct
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
TOP, BOTTOM, INK = (0x56, 0x8B, 0xFF), (0x2B, 0x4C, 0xD0), (0x2B, 0x4C, 0xD0)
LATIN, CJK = r'C:\Windows\Fonts\segoeuib.ttf', r'C:\Windows\Fonts\msyhbd.ttc'


def tile(S, margin, radius):
    grad = Image.new('RGBA', (S, S))
    d = ImageDraw.Draw(grad)
    for y in range(S):
        t = y / (S - 1)
        d.line([(0, y), (S, y)], fill=tuple(round(a + (b - a) * t) for a, b in zip(TOP, BOTTOM)) + (255,))
    mask = Image.new('L', (S, S))
    ImageDraw.Draw(mask).rounded_rectangle([margin, margin, S - 1 - margin, S - 1 - margin], radius, fill=255)
    out = Image.new('RGBA', (S, S))
    out.paste(grad, mask=mask)
    return out


def bubble(d, box, fill, tail_left, S):
    x0, y0, x1, y1 = box
    d.rounded_rectangle(box, radius=(y1 - y0) * 0.28, fill=fill)
    w = (x1 - x0) * 0.16
    if tail_left:
        tx = x0 + (x1 - x0) * 0.18
        d.polygon([(tx, y1 - 2), (tx + w, y1 - 2), (tx - w * 0.2, y1 + S * 0.09)], fill=fill)
    else:
        tx = x1 - (x1 - x0) * 0.18
        d.polygon([(tx - w, y1 - 2), (tx, y1 - 2), (tx + w * 0.2, y1 + S * 0.09)], fill=fill)


def glyph(d, text, font_path, size, center, fill):
    f = ImageFont.truetype(font_path, int(size))
    l, t, r, b = d.textbbox((0, 0), text, font=f)
    d.text((center[0] - (l + r) / 2, center[1] - (t + b) / 2), text, font=f, fill=fill)


def draw(px):
    S = px * 4  # supersample, then downscale for clean edges
    if px <= 24:
        im = tile(S, 0, S * 0.2)
        glyph(ImageDraw.Draw(im), '文', CJK, S * 0.78, (S / 2, S / 2), (255, 255, 255, 255))
    elif px <= 32:
        im = tile(S, S * 0.03, S * 0.21)
        d = ImageDraw.Draw(im)
        box = (S * 0.15, S * 0.17, S * 0.85, S * 0.72)
        bubble(d, box, (255, 255, 255, 255), False, S)
        glyph(d, '文', CJK, S * 0.42, ((box[0] + box[2]) / 2, (box[1] + box[3]) / 2), INK + (255,))
    else:
        im = tile(S, S * 0.04, S * 0.22)
        back = Image.new('RGBA', (S, S))
        bd = ImageDraw.Draw(back)
        b1 = (S * 0.13, S * 0.15, S * 0.60, S * 0.52)
        bubble(bd, b1, (255, 255, 255, 105), True, S)
        glyph(bd, 'A', LATIN, S * 0.27, ((b1[0] + b1[2]) / 2 - S * 0.04, (b1[1] + b1[3]) / 2), (255, 255, 255, 255))
        im = Image.alpha_composite(im, back)
        d = ImageDraw.Draw(im)
        b2 = (S * 0.36, S * 0.40, S * 0.87, S * 0.79)
        bubble(d, b2, (255, 255, 255, 255), False, S)
        glyph(d, '文', CJK, S * 0.27, ((b2[0] + b2[2]) / 2, (b2[1] + b2[3]) / 2), INK + (255,))
    return im.resize((px, px), Image.LANCZOS)


def write_ico(path, images):
    """ICO with one PNG-compressed image per size (Windows Vista+ reads these at every size)."""
    blobs = []
    for im in images:
        b = io.BytesIO()
        im.save(b, 'PNG')
        blobs.append(b.getvalue())
    head = struct.pack('<HHH', 0, 1, len(images))
    offset, entries = 6 + 16 * len(images), b''
    for im, blob in zip(images, blobs):
        w = im.width if im.width < 256 else 0
        entries += struct.pack('<BBBBHHII', w, w, 0, 0, 1, 32, len(blob), offset)
        offset += len(blob)
    with open(path, 'wb') as f:
        f.write(head + entries + b''.join(blobs))


if __name__ == '__main__':
    sizes = [16, 20, 24, 32, 40, 48, 64, 128, 256]
    imgs = [draw(s) for s in sizes]
    write_ico(os.path.join(HERE, 'icon.ico'), imgs)
    sheet = Image.new('RGBA', (sum(sizes) + 20 * len(sizes), 276), (31, 36, 48, 255))
    x = 10
    for s, im in zip(sizes, imgs):
        sheet.paste(im, (x, 10), im)
        x += s + 20
    sheet.save(os.path.join(HERE, 'icon-preview.png'))
    print('ok', sizes)
