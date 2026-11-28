# draw_frontpage.py — renders THE WORLD IN ONE DAY (news-image-20261127 r5).
# Pure standard library: hand-built 5x7 bitmap font, raw PNG encoder
# (zlib + struct, no Pillow, no third-party code). Deterministic output:
# same input data always yields the same bytes.
# r5 layout: 40 stories instead of 57, so each story gets a 2px
# breathing gap below it (r4 squeezed stories together with 1px).

import struct
import zlib

from stories import (
    DATE_CHECK,
    PICTURES,
    REGIONS,
    STORIES,
    TIMELINE,
    TITLE,
    TOP_STORIES,
)

W = 1024
H = 1024

PAPER = (247, 242, 231)
INK = (20, 20, 20)
GREY = (90, 86, 78)
RED = (163, 18, 18)
BLUE = (29, 78, 137)
GOLD = (198, 158, 40)
DARK = (24, 28, 36)
LIGHT = (232, 226, 214)
GREEN = (31, 94, 58)

# ---------------------------------------------------------------- 5x7 font
# Each glyph is 7 rows of 5 cells ('#' = on). Lowercase letters sit on
# rows 2..6 with descenders on row 6, like a real newspaper face.
_G = {}


def _g(ch, rows):
    _G[ch] = rows


_g("A", [".###.", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"])
_g("B", ["####.", "#...#", "#...#", "####.", "#...#", "#...#", "####."])
_g("C", [".####", "#....", "#....", "#....", "#....", "#....", ".####"])
_g("D", ["####.", "#...#", "#...#", "#...#", "#...#", "#...#", "####."])
_g("E", ["#####", "#....", "#....", "####.", "#....", "#....", "#####"])
_g("F", ["#####", "#....", "#....", "####.", "#....", "#....", "#...."])
_g("G", [".####", "#....", "#....", "#.###", "#...#", "#...#", ".###."])
_g("H", ["#...#", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"])
_g("I", [".###.", "..#..", "..#..", "..#..", "..#..", "..#..", ".###."])
_g("J", ["..###", "...#.", "...#.", "...#.", "...#.", "#..#.", ".##.."])
_g("K", ["#...#", "#..#.", "#.#..", "##...", "#.#..", "#..#.", "#...#"])
_g("L", ["#....", "#....", "#....", "#....", "#....", "#....", "#####"])
_g("M", ["#...#", "##.##", "#.#.#", "#.#.#", "#...#", "#...#", "#...#"])
_g("N", ["#...#", "##..#", "#.#.#", "#..##", "#...#", "#...#", "#...#"])
_g("O", [".###.", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."])
_g("P", ["####.", "#...#", "#...#", "####.", "#....", "#....", "#...."])
_g("Q", [".###.", "#...#", "#...#", "#...#", "#.#.#", "#..#.", ".##.#"])
_g("R", ["####.", "#...#", "#...#", "####.", "#.#..", "#..#.", "#...#"])
_g("S", [".####", "#....", "#....", ".###.", "....#", "....#", "####."])
_g("T", ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."])
_g("U", ["#...#", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."])
_g("V", ["#...#", "#...#", "#...#", "#...#", "#...#", ".#.#.", "..#.."])
_g("W", ["#...#", "#...#", "#...#", "#.#.#", "#.#.#", "##.##", "#...#"])
_g("X", ["#...#", "#...#", ".#.#.", "..#..", ".#.#.", "#...#", "#...#"])
_g("Y", ["#...#", "#...#", ".#.#.", "..#..", "..#..", "..#..", "..#.."])
_g("Z", ["#####", "....#", "...#.", "..#..", ".#...", "#....", "#####"])
_g("a", [".....", ".....", ".###.", "....#", ".####", "#...#", ".####"])
_g("b", ["#....", "#....", "####.", "#...#", "#...#", "#...#", "####."])
_g("c", [".....", ".....", ".####", "#....", "#....", "#....", ".####"])
_g("d", ["....#", "....#", ".####", "#...#", "#...#", "#...#", ".####"])
_g("e", [".....", ".....", ".###.", "#...#", "#####", "#....", ".###."])
_g("f", ["..##.", ".#...", ".#...", "#####", ".#...", ".#...", ".#..."])
_g("g", [".....", ".....", ".####", "#...#", "#...#", ".###.", "....#"])
_g("h", ["#....", "#....", "####.", "#...#", "#...#", "#...#", "#...#"])
_g("i", [".....", "..#..", ".....", ".##..", "..#..", "..#..", ".###."])
_g("j", ["...#.", ".....", "...#.", "...#.", "...#.", "...#.", "..##."])
_g("k", ["#....", "#....", "#...#", "#..#.", "#.#..", "##...", "#..#."])
_g("l", ["..#..", "..#..", "..#..", "..#..", "..#..", "..#..", ".###."])
_g("m", [".....", ".....", "##.#.", "#.#.#", "#.#.#", "#...#", "#...#"])
_g("n", [".....", ".....", "####.", "#...#", "#...#", "#...#", "#...#"])
_g("o", [".....", ".....", ".###.", "#...#", "#...#", "#...#", ".###."])
_g("p", [".....", ".....", "####.", "#...#", "#...#", "####.", "#...."])
_g("q", [".....", ".....", ".####", "#...#", "#...#", ".####", "....#"])
_g("r", [".....", ".....", "#.##.", "##...", "#....", "#....", "#...."])
_g("s", [".....", ".....", ".####", "#....", ".###.", "....#", "####."])
_g("t", [".#...", ".#...", "#####", ".#...", ".#...", ".#...", ".#..."])
_g("u", [".....", ".....", "#...#", "#...#", "#...#", "#..##", ".##.#"])
_g("v", [".....", ".....", "#...#", "#...#", "#...#", ".#.#.", "..#.."])
_g("w", [".....", ".....", "#...#", "#.#.#", "#.#.#", "#.#.#", ".#.#."])
_g("x", [".....", ".....", "#...#", ".#.#.", "..#..", ".#.#.", "#...#"])
_g("y", [".....", ".....", "#...#", "#...#", ".####", "....#", "..##."])
_g("z", [".....", ".....", "#####", "...#.", "..#..", ".#...", "#####"])
_g("0", [".###.", "#...#", "#..##", "#.#.#", "##..#", "#...#", ".###."])
_g("1", ["..#..", ".##..", "..#..", "..#..", "..#..", "..#..", ".###."])
_g("2", [".###.", "#...#", "....#", "...#.", "..#..", ".#...", "#####"])
_g("3", ["####.", "....#", "....#", ".###.", "....#", "....#", "####."])
_g("4", ["...#.", "..##.", ".#.#.", "#..#.", "#####", "...#.", "...#."])
_g("5", ["#####", "#....", "####.", "....#", "....#", "#...#", ".###."])
_g("6", [".###.", "#....", "#....", "####.", "#...#", "#...#", ".###."])
_g("7", ["#####", "....#", "...#.", "...#.", "..#..", "..#..", "..#.."])
_g("8", [".###.", "#...#", "#...#", ".###.", "#...#", "#...#", ".###."])
_g("9", [".###.", "#...#", "#...#", ".####", "....#", "....#", ".###."])
_g(" ", [".....", ".....", ".....", ".....", ".....", ".....", "....."])
_g(".", [".....", ".....", ".....", ".....", ".....", ".##..", ".##.."])
_g(",", [".....", ".....", ".....", ".....", ".....", ".##..", ".#..."])
_g(":", [".....", ".##..", ".....", ".##..", ".....", ".##..", "....."])
_g(";", [".....", ".##..", ".....", ".##..", ".....", ".##..", ".#..."])
_g("'", ["..#..", "..#..", ".#...", ".....", ".....", ".....", "....."])
_g("-", [".....", ".....", ".....", "#####", ".....", ".....", "....."])
_g("(", ["...#.", "..#..", ".#...", ".#...", ".#...", "..#..", "...#."])
_g(")", [".#...", "..#..", "...#.", "...#.", "...#.", "..#..", ".#..."])
_g("%", ["#...#", "#..#.", "...#.", "..#..", ".#...", "#..#.", "#...#"])
_g("/", ["....#", "...#.", "...#.", "..#..", ".#...", "#....", "#...."])
_g("?", [".###.", "#...#", "....#", "...#.", "..#..", ".....", "..#.."])
_g("!", ["..#..", "..#..", "..#..", "..#..", "..#..", ".....", "..#.."])
_g("$", ["..#..", ".####", "#.#..", ".###.", "..#.#", "####.", "..#.."])
_g("+", [".....", ".....", "..#..", ".###.", "..#..", ".....", "....."])
_g("=", [".....", ".....", "#####", ".....", "#####", ".....", "....."])
_g('"', [".#.#.", ".#.#.", ".#.#.", ".....", ".....", ".....", "....."])
_g("&", [".###.", "#...#", "#.#..", ".#...", "#.#.#", "#..#.", ".##.#"])
_g("[", [".###.", ".#...", ".#...", ".#...", ".#...", ".#...", ".###."])
_g("]", [".###.", "...#.", "...#.", "...#.", "...#.", "...#.", ".###."])
_g("|", ["..#..", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."])

_MISSING = _G["?"]
_NORMALIZE = {
    "\u2013": "-",
    "\u2014": "-",
    "\u2019": "'",
    "\u201c": '"',
    "\u201d": '"',
    "\u20ac": "E",
    "\u00a0": " ",
}


def _clean(text):
    return "".join(_NORMALIZE.get(ch, ch) for ch in text)


def text_width(text, scale=1, adv=5):
    return len(_clean(text)) * adv * scale


def wrap_text(text, max_chars):
    """Greedy word wrap; returns a list of lines, each <= max_chars."""
    words = _clean(text).split(" ")
    lines = []
    cur = ""
    for word in words:
        if not cur:
            cur = word
        elif len(cur) + 1 + len(word) <= max_chars:
            cur = cur + " " + word
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


# ------------------------------------------------------------------- canvas
class Canvas:
    def __init__(self, w, h, bg):
        self.w = w
        self.h = h
        self.buf = bytearray(bg * (w * h))

    def _idx(self, x, y):
        return (y * self.w + x) * 3

    def px(self, x, y, color):
        if 0 <= x < self.w and 0 <= y < self.h:
            i = self._idx(x, y)
            self.buf[i:i + 3] = bytes(color)

    def rect(self, x, y, w, h, color):
        x0 = max(0, x)
        y0 = max(0, y)
        x1 = min(self.w, x + w)
        y1 = min(self.h, y + h)
        for yy in range(y0, y1):
            base = (yy * self.w + x0) * 3
            self.buf[base:(base + (x1 - x0) * 3)] = bytes(color) * (x1 - x0)

    def hline(self, x, y, w, color):
        self.rect(x, y, w, 1, color)

    def vline(self, x, y, h, color):
        self.rect(x, y, 1, h, color)

    def line(self, x0, y0, x1, y1, color):
        dx = abs(x1 - x0)
        dy = -abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        while True:
            self.px(x0, y0, color)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy

    def circle(self, cx, cy, r, color, fill=True):
        for yy in range(cy - r, cy + r + 1):
            for xx in range(cx - r, cx + r + 1):
                d = (xx - cx) ** 2 + (yy - cy) ** 2
                if fill:
                    if d <= r * r:
                        self.px(xx, yy, color)
                elif r * r - 2 * r <= d <= r * r:
                    self.px(xx, yy, color)

    def star(self, cx, cy, r, color):
        # 8-point starburst for explosions / stars.
        for k in range(8):
            ang = k * 3.14159 / 4.0
            x1 = int(cx + r * _cos(ang))
            y1 = int(cy + r * _sin(ang))
            self.line(cx, cy, x1, y1, color)
        self.circle(cx, cy, max(1, r // 3), color)

    def text(self, x, y, s, scale=1, color=INK, adv=5, bold=False):
        s = _clean(s)
        cx = x
        for ch in s:
            rows = _G.get(ch, _MISSING)
            for ry, row in enumerate(rows):
                for rx, cell in enumerate(row):
                    if cell == "#":
                        if scale == 1:
                            self.px(cx + rx, y + ry, color)
                            if bold:
                                self.px(cx + rx + 1, y + ry, color)
                        else:
                            self.rect(
                                cx + rx * scale, y + ry * scale,
                                scale, scale, color,
                            )
            cx += adv * scale
        return cx - x

    def text_center(self, y, s, scale=1, color=INK, adv=5, bold=False):
        w = text_width(s, scale, adv)
        return self.text((self.w - w) // 2, y, s, scale, color, adv, bold)


def _cos(a):
    # Small cosine via Taylor, good enough for starbursts.
    a2 = a * a
    return 1 - a2 / 2 + a2 * a2 / 24 - a2 * a2 * a2 / 720


def _sin(a):
    a2 = a * a
    return a - a * a2 / 6 + a * a2 * a2 / 120


# --------------------------------------------------------------------- PNG
def encode_png(canvas):
    def chunk(kind, data):
        out = struct.pack(">I", len(data)) + kind + data
        out += struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
        return out

    raw = bytearray()
    for y in range(canvas.h):
        raw.append(0)
        start = y * canvas.w * 3
        raw += canvas.buf[start:start + canvas.w * 3]
    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", struct.pack(">IIBBBBB", canvas.w, canvas.h,
                                      8, 2, 0, 0, 0))
    png += chunk(b"IDAT", zlib.compress(bytes(raw), 9))
    png += chunk(b"IEND", b"")
    return png


# ------------------------------------------------------------------- scenes
def draw_drones(cv, x, y, w, h):
    cv.rect(x, y, w, h, (16, 22, 38))
    for bx in range(x, y + h - 14, 3):
        pass
    # City skyline.
    heights = [16, 22, 12, 26, 18, 24, 14, 20, 11, 24, 16, 19]
    bx = x + 4
    for i, bh in enumerate(heights):
        bw = max(8, (w - 8) // len(heights) - 2)
        cv.rect(bx, y + h - bh - 8, bw, bh, (38, 44, 66))
        for wy in range(y + h - bh - 4, y + h - 10, 6):
            cv.rect(bx + 2, wy, 2, 2, (240, 200, 90))
        bx += bw + 2
    cv.rect(x, y + h - 8, w, 8, (10, 12, 20))
    # Explosions.
    for ex, ey, r in [(x + 40, y + 22, 9), (x + w - 46, y + 16, 7)]:
        cv.star(ex, ey, r, (255, 170, 40))
        cv.star(ex, ey, r // 2, (255, 230, 120))
    # Drones: small crosses with rotor discs.
    for dx, dy in [(x + w // 2 - 30, y + 14), (x + w // 2 + 12, y + 26),
                   (x + w // 2 + 44, y + 10)]:
        cv.rect(dx - 7, dy - 1, 14, 2, (200, 205, 215))
        cv.rect(dx - 1, dy - 5, 2, 10, (200, 205, 215))
        cv.circle(dx - 8, dy - 6, 3, (200, 205, 215), fill=False)
        cv.circle(dx + 8, dy - 6, 3, (200, 205, 215), fill=False)
        cv.px(dx, dy, (255, 80, 60))


def draw_eu(cv, x, y, w, h):
    cv.rect(x, y, w, h, (18, 52, 110))
    cx, cy = x + w // 2, y + h // 2 - 2
    ring = max(10, h // 2 - 8)
    for k in range(12):
        ang = k * 3.14159 / 6.0
        sx = int(cx + ring * _cos(ang))
        sy = int(cy + ring * _sin(ang))
        cv.star(sx, sy, 3, GOLD)
    # Cracked euro coin in the middle.
    cv.circle(cx, cy, 9, GOLD)
    cv.circle(cx, cy, 7, (18, 52, 110))
    cv.text(cx - 5, cy - 6, "E", scale=2, color=GOLD, adv=5)
    cv.line(cx - 2, cy - 9, cx + 4, cy + 9, (120, 20, 20))
    cv.rect(x, y + h - 14, w, 14, RED)
    cv.text_center(y + h - 12, "NO DEAL", scale=1, color=(255, 255, 255),
                   adv=5, bold=True)


def draw_parliament(cv, x, y, w, h):
    cv.rect(x, y, w, h, GREEN)
    # Chamber benches (3 rows, kept clear of the banner strip).
    for row in range(3):
        cv.rect(x + 10 + row * 4, y + 10 + row * 8, w - 20 - row * 8, 6,
                (46, 120, 76))
    # Balanced scales: 65 vs 65.
    midx = x + w // 2
    cv.vline(midx, y + 6, 18, GOLD)
    cv.hline(midx - 52, y + 10, 104, GOLD)
    cv.rect(midx - 58, y + 12, 16, 9, (255, 255, 255))
    cv.rect(midx + 42, y + 12, 16, 9, (255, 255, 255))
    cv.text(midx - 56, y + 13, "65", scale=1, color=INK, adv=5, bold=True)
    cv.text(midx + 44, y + 13, "65", scale=1, color=INK, adv=5, bold=True)
    cv.rect(x, y + h - 14, w, 14, (24, 28, 36))
    cv.text_center(y + h - 12, "DEADLOCK 65-65", scale=1,
                   color=(255, 255, 255), adv=5, bold=True)


def draw_chess(cv, x, y, w, h):
    cv.rect(x, y, w, h, (96, 64, 32))
    sq = max(2, (h - 18) // 8)
    ox = x + (w - 8 * sq) // 2
    oy = y + 2
    for r in range(8):
        for c in range(8):
            col = (240, 220, 190) if (r + c) % 2 == 0 else (60, 40, 24)
            cv.rect(ox + c * sq, oy + r * sq, sq, sq, col)
    # A few pieces as filled dots (letters only fit on larger boards).
    for (r, c, col) in [
        (0, 4, INK), (0, 3, INK), (1, 4, INK),
        (7, 4, (255, 255, 255)), (7, 3, (255, 255, 255)),
        (6, 4, (255, 255, 255)), (3, 4, INK),
    ]:
        px = ox + c * sq + sq // 2
        py = oy + r * sq + sq // 2
        cv.circle(px, py, max(1, sq // 2), col)
    cv.rect(x, y + h - 14, w, 14, (24, 28, 36))
    cv.text_center(y + h - 12, "SCORE 1.5 - 1.5", scale=1,
                   color=(255, 255, 255), adv=5, bold=True)


SCENES = {
    "drones": draw_drones,
    "eu": draw_eu,
    "parliament": draw_parliament,
    "chess": draw_chess,
}

# ------------------------------------------- picture-desk mini scenes
# Nine small panorama tiles (about 106x22) for the DAY IN PICTURES band.
# Same primitives as the big scenes; shapes stay bold and simple so they
# read at tile size.


def draw_storm(cv, x, y, w, h):
    cv.rect(x, y, w, h, (34, 40, 58))
    for cx, cy, r in [(x + 16, y + 5, 6), (x + 30, y + 4, 7),
                      (x + w - 30, y + 4, 7), (x + w - 16, y + 5, 6)]:
        cv.circle(cx, cy, r, (92, 98, 112))
    mx = x + w // 2
    cv.line(mx, y + 3, mx - 4, y + 11, GOLD)
    cv.line(mx - 4, y + 11, mx + 1, y + 11, GOLD)
    cv.line(mx + 1, y + 11, mx - 5, y + h - 2, GOLD)
    for rx in range(x + 6, x + w - 4, 12):
        cv.line(rx, y + h - 7, rx - 2, y + h - 3, (140, 165, 200))
    cv.rect(x, y + h - 2, w, 2, (10, 12, 20))


def draw_parade(cv, x, y, w, h):
    cv.rect(x, y, w, h, (165, 200, 232))
    cv.circle(x + 28, y + 10, 9, RED)
    cv.vline(x + 24, y + 2, 16, (255, 255, 255))
    cv.vline(x + 32, y + 2, 16, (255, 255, 255))
    cv.line(x + 24, y + 17, x + 27, y + h - 3, INK)
    cv.line(x + 32, y + 17, x + 29, y + h - 3, INK)
    cv.rect(x + 25, y + h - 4, 7, 3, (120, 80, 40))
    cv.circle(x + w - 24, y + 8, 6, GOLD)
    cv.line(x + w - 27, y + 13, x + w - 25, y + h - 3, INK)
    cv.line(x + w - 21, y + 13, x + w - 23, y + h - 3, INK)
    cv.rect(x + w - 28, y + h - 4, 7, 3, (120, 80, 40))
    cv.rect(x, y + h - 2, w, 2, (90, 95, 105))


def draw_tanker(cv, x, y, w, h):
    cv.rect(x, y, w, h, (150, 190, 220))
    cv.rect(x, y + h - 8, w, 8, (28, 74, 118))
    cv.rect(x + 14, y + h - 12, w - 28, 4, (30, 30, 34))
    for i, col in enumerate([RED, BLUE, GOLD, GREEN]):
        cv.rect(x + 20 + i * 12, y + h - 16, 10, 4, col)
    cv.vline(x + w // 2, y + 3, 8, (30, 30, 34))
    mx, my = x + w - 18, y + h - 5
    cv.circle(mx, my, 3, INK)
    for dx, dy in [(-5, 0), (5, 0), (0, -5), (-4, -4), (4, -4)]:
        cv.line(mx, my, mx + dx, my + dy, INK)
    for wx in range(x + 4, x + w - 8, 16):
        cv.hline(wx, y + h - 3, 7, (200, 225, 245))


def draw_virus(cv, x, y, w, h):
    cv.rect(x, y, w, h, (44, 32, 44))
    cx, cy = x + w // 2, y + h // 2
    for k in range(8):
        ang = k * 3.14159 / 4.0
        x1 = int(cx + 11 * _cos(ang))
        y1 = int(cy + 9 * _sin(ang))
        cv.line(cx, cy, x1, y1, (120, 170, 80))
        cv.circle(x1, y1, 2, (120, 170, 80))
    cv.circle(cx, cy, 6, (120, 170, 80))
    cv.circle(cx - 2, cy - 1, 2, (70, 110, 50))
    cv.rect(x + w - 13, y + 3, 7, 2, (235, 235, 235))
    cv.rect(x + w - 11, y + 1, 2, 7, (235, 235, 235))


def draw_chart(cv, x, y, w, h):
    cv.rect(x, y, w, h, DARK)
    cv.vline(x + 6, y + 2, h - 4, GREY)
    cv.hline(x + 6, y + h - 3, w - 10, GREY)
    for i, bh in enumerate([4, 7, 10, 14]):
        cv.rect(x + 12 + i * 16, y + h - 3 - bh, 9, bh, GREEN)
    pts = [(x + 16, y + h - 8), (x + 32, y + h - 11),
           (x + 48, y + h - 14), (x + 64, y + h - 18),
           (x + 84, y + 4)]
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        cv.line(ax, ay, bx, by, GOLD)
    cv.line(x + 84, y + 4, x + 78, y + 5, GOLD)
    cv.line(x + 84, y + 4, x + 83, y + 10, GOLD)


def draw_fire(cv, x, y, w, h):
    cv.rect(x, y, w, h, (56, 44, 38))
    cv.rect(x + 8, y + 5, 28, h - 5, (30, 28, 30))
    for wy in (y + 8, y + 13):
        for wx in (x + 12, x + 20, x + 28):
            cv.rect(wx, wy, 3, 3, (240, 200, 90))
    fx, fy = x + w - 28, y + h - 8
    cv.circle(fx, fy, 7, (235, 110, 30))
    cv.circle(fx - 3, fy - 4, 5, (245, 160, 40))
    cv.circle(fx - 3, fy - 5, 3, (255, 225, 130))
    cv.circle(fx + 8, fy - 10, 4, (130, 125, 120))
    cv.circle(fx + 13, fy - 13, 3, (150, 145, 140))


def draw_bank(cv, x, y, w, h):
    cv.rect(x, y, w, h, (206, 196, 168))
    cx = x + w // 2
    for i in range(7):
        cv.hline(cx - 21 + i * 3, y + 2 + i, 42 - i * 6, (150, 120, 60))
    for i in range(4):
        cv.rect(x + 16 + i * 20, y + 10, 5, h - 14, (245, 242, 235))
    cv.rect(x + 10, y + h - 4, w - 20, 2, (150, 120, 60))
    cv.rect(x + 6, y + h - 2, w - 12, 2, (120, 95, 48))


def draw_chip(cv, x, y, w, h):
    cv.rect(x, y, w, h, (22, 38, 30))
    bx, by, bw, bh = x + w // 2 - 13, y + 3, 26, h - 6
    cv.rect(bx, by, bw, bh, (40, 44, 48))
    cv.rect(bx + 4, by + 3, bw - 8, 1, GOLD)
    cv.rect(bx + 4, by + bh - 4, bw - 8, 1, GOLD)
    cv.rect(bx + 4, by + 3, 1, bh - 6, GOLD)
    cv.rect(bx + bw - 5, by + 3, 1, bh - 6, GOLD)
    for i in range(3):
        px = bx + 5 + i * 7
        cv.rect(px, by - 2, 2, 2, (190, 195, 200))
        cv.rect(px, by + bh, 2, 2, (190, 195, 200))
        py = by + 3 + i * 5
        cv.rect(bx - 2, py, 2, 2, (190, 195, 200))
        cv.rect(bx + bw, py, 2, 2, (190, 195, 200))
    cv.line(bx - 2, y + h // 2, x + 8, y + h // 2, GOLD)
    cv.line(bx + bw + 2, y + h // 2, x + w - 8, y + h // 2, GOLD)


def draw_treaty(cv, x, y, w, h):
    cv.rect(x, y, w, h, (150, 190, 220))
    cv.circle(x + w - 14, y + 6, 4, GOLD)
    cv.rect(x, y + h - 4, w, 4, (28, 74, 118))
    for px, col in [(x + 26, (110, 160, 220)), (x + w - 40, (28, 52, 110))]:
        cv.vline(px, y + 5, h - 9, (60, 50, 40))
        cv.rect(px + 1, y + 5, 14, 8, col)
        cv.px(px + 4, y + 7, (255, 255, 255))
        cv.px(px + 8, y + 9, (255, 255, 255))
        cv.px(px + 11, y + 7, (255, 255, 255))


MINIS = {
    "storm": draw_storm,
    "parade": draw_parade,
    "tanker": draw_tanker,
    "virus": draw_virus,
    "chart": draw_chart,
    "fire": draw_fire,
    "bank": draw_bank,
    "chip": draw_chip,
    "treaty": draw_treaty,
}

# ------------------------------------------------------------- map + layout
# Schematic continents as (x, y, w, h) blocks on a 360x64 map.
CONTINENTS = [
    (8, 10, 62, 26),    # North America
    (30, 38, 26, 22),   # South America
    (168, 8, 30, 20),   # Europe
    (172, 30, 34, 26),  # Africa
    (206, 8, 110, 30),  # Asia
    (300, 44, 34, 14),  # Oceania
]
MAP_DOTS = [
    (182, 16), (120, 22), (60, 24), (188, 40), (250, 22),
    (292, 26), (316, 50), (150, 14), (230, 34), (270, 18),
]


def story_height(story, text_w):
    chars = text_w // 5
    hl = wrap_text(story["headline"], chars)
    sm = wrap_text(story["summary"], chars)
    # Headline lines (7px pitch, bold caps sit tight) + summary lines
    # at 7px pitch (glyphs are 7px tall; lines touch but never
    # overlap) + source (7px) + breathing gap (2px).
    return len(hl) * 7 + len(sm) * 7 + 7 + 2


def _adjusted_heights(stories, text_w):
    """Per-story height plus 12px for the region header of each region's
    first story, so the partition accounts for headers too. The renderer
    draws a header exactly for those stories (see render_page)."""
    heights = []
    prev = None
    for s in stories:
        h = story_height(s, text_w)
        if s["region"] != prev:
            h += 10
            prev = s["region"]
        heights.append(h)
    return heights


def balance_columns(stories, ncols, text_w):
    """Contiguous partition into ncols columns minimising the tallest
    column (dynamic programming). A greedy cut overshoots by a whole
    story; the DP keeps the max column at ceil(total / ncols)."""
    heights = _adjusted_heights(stories, text_w)
    n = len(heights)
    prefix = [0]
    for h in heights:
        prefix.append(prefix[-1] + h)
    inf = float("inf")
    # dp[k][i] = min possible max column height for first i stories in k cols.
    dp = [[inf] * (n + 1) for _ in range(ncols + 1)]
    cut = [[0] * (n + 1) for _ in range(ncols + 1)]
    dp[0][0] = 0
    for k in range(1, ncols + 1):
        for i in range(1, n + 1):
            for j in range(k - 1, i):
                if dp[k - 1][j] == inf:
                    continue
                cand = max(dp[k - 1][j], prefix[i] - prefix[j])
                if cand < dp[k][i]:
                    dp[k][i] = cand
                    cut[k][i] = j
    cols = []
    i = n
    for k in range(ncols, 0, -1):
        j = cut[k][i]
        cols.append([(stories[t], heights[t]) for t in range(j, i)])
        i = j
    cols.reverse()
    return cols


def render_page():
    cv = Canvas(W, H, PAPER)
    # Thin outer frame.
    cv.rect(0, 0, W, 3, INK)
    cv.rect(0, H - 3, W, 3, INK)
    cv.rect(0, 0, 3, H, INK)
    cv.rect(W - 3, 0, 3, H, INK)

    # --- Masthead -------------------------------------------------------
    cv.rect(8, 6, W - 16, 30, DARK)
    cv.text_center(7, "THE WORLD IN ONE DAY", scale=4, color=(255, 255, 255),
                   adv=6)

    # --- Title formula line (carries the date, so no separate dateline) --
    y = 42
    for line in wrap_text(TITLE, 158):
        cv.text(12, y, line, scale=1, color=INK, adv=6, bold=True)
        y += 9

    # --- Top illustrated cards ------------------------------------------
    card_y = y
    card_h = 70
    card_w = (W - 24 - 3 * 6) // 4
    for i, top in enumerate(TOP_STORIES):
        cx = 12 + i * (card_w + 6)
        cv.rect(cx, card_y, card_w, card_h, (255, 255, 255))
        cv.rect(cx, card_y, card_w, 1, INK)
        cv.rect(cx, card_y + card_h - 1, card_w, 1, INK)
        cv.rect(cx, card_y, 1, card_h, INK)
        cv.rect(cx + card_w - 1, card_y, 1, card_h, INK)
        SCENES[top["scene"]](cv, cx + 3, card_y + 3, card_w - 6, 34)
        cv.text(cx + 4, card_y + 42, top["kicker"], scale=1, color=RED,
                adv=5, bold=True)
        hy = card_y + 52
        for line in wrap_text(top["headline"], (card_w - 8) // 5):
            cv.text(cx + 4, hy, line, scale=1, color=INK, adv=5, bold=True)
            hy += 9
        cv.text(cx + 4, hy, top["caption"], scale=1, color=GREY, adv=5)
    y = card_y + card_h + 3

    # --- DATE CHECK + map + timeline strip -------------------------------
    strip_y = y
    strip_h = 68
    cv.rect(12, strip_y, W - 24, strip_h, LIGHT)
    cv.rect(12, strip_y, W - 24, 1, INK)
    cv.rect(12, strip_y + strip_h - 1, W - 24, 1, INK)
    # DATE CHECK text, left ~640px.
    dx = 20
    dy = strip_y + 6
    cv.text(dx, dy, "DATE CHECK", scale=1, color=RED, adv=5, bold=True)
    dy += 10
    for line in wrap_text(DATE_CHECK, 118):
        cv.text(dx, dy, line, scale=1, color=INK, adv=5)
        dy += 8
    # Timeline, below the date check.
    dy += 2
    cv.text(dx, dy, "UTC TIMELINE", scale=1, color=RED, adv=5, bold=True)
    dy += 9
    tline = "  |  ".join(t + " " + label for t, label in TIMELINE)
    for line in wrap_text(tline, 118):
        cv.text(dx, dy, line, scale=1, color=INK, adv=5)
        dy += 8
    # Schematic world map, right ~330px.
    mx = W - 12 - 350
    my = strip_y + 4
    cv.text(mx, my, "WORLD MAP - 11 REGIONS", scale=1, color=INK, adv=5,
            bold=True)
    my += 8
    for (cx0, cy0, cw, ch) in CONTINENTS:
        cv.rect(mx + cx0, my + cy0, cw, ch, (150, 180, 205))
    for (px, py) in MAP_DOTS:
        cv.circle(mx + px, my + py, 2, RED)
    cv.text(mx, my + 58, "RED DOTS: TOP STORY REGIONS", scale=1,
            color=GREY, adv=5)
    y = strip_y + strip_h + 3

    # --- DAY IN PICTURES band: 9 mini scenes ----------------------------
    band_y = y
    cv.text(12, band_y, "THE DAY IN PICTURES", scale=1, color=RED, adv=5,
            bold=True)
    note = "13 DRAWN SCENES IN ALL: 4 CARDS + 9 TILES"
    cv.text(W - 12 - text_width(note, 1, 5), band_y, note, scale=1,
            color=GREY, adv=5)
    tile_y = band_y + 10
    tile_w = (W - 16 - 8 * 2) // 9
    tile_h = 33
    for i, (key, caption) in enumerate(PICTURES):
        tx = 8 + i * (tile_w + 2)
        cv.rect(tx, tile_y, tile_w, tile_h, (255, 255, 255))
        cv.rect(tx, tile_y, tile_w, 1, INK)
        cv.rect(tx, tile_y + tile_h - 1, tile_w, 1, INK)
        cv.rect(tx, tile_y, 1, tile_h, INK)
        cv.rect(tx + tile_w - 1, tile_y, 1, tile_h, INK)
        MINIS[key](cv, tx + 2, tile_y + 2, tile_w - 4, tile_h - 13)
        cv.rect(tx + 1, tile_y + tile_h - 10, tile_w - 2, 9, DARK)
        cw = text_width(caption, 1, 5)
        cv.text(tx + (tile_w - cw) // 2, tile_y + tile_h - 9, caption,
                scale=1, color=(255, 255, 255), adv=5, bold=True)
    y = tile_y + tile_h + 3

    # --- Stories in 5 balanced columns -----------------------------------
    stories_top = y
    stories_h = H - 7 - stories_top
    ncols = 5
    col_w = (W - 16 - (ncols - 1) * 2) // ncols
    text_w = col_w - 4
    cols = balance_columns(STORIES, ncols, text_w)
    max_h = 0
    # prev_region is NOT reset per column: a column that starts mid-region
    # draws no header, exactly matching the +12 in _adjusted_heights.
    prev_region = None
    for ci, col in enumerate(cols):
        cx = 8 + ci * (col_w + 2)
        cy = stories_top
        for story, sh in col:
            if story["region"] != prev_region:
                cv.rect(cx, cy, col_w, 10, DARK)
                cv.text(cx + 3, cy + 2, story["region"], scale=1,
                        color=(255, 255, 255), adv=5, bold=True)
                cy += 10
                prev_region = story["region"]
            hy = cy
            for line in wrap_text(story["headline"], text_w // 5):
                cv.text(cx + 2, hy, line, scale=1, color=INK, adv=5,
                        bold=True)
                hy += 7
            for line in wrap_text(story["summary"], text_w // 5):
                cv.text(cx + 2, hy, line, scale=1, color=INK, adv=5)
                hy += 7
            cv.text(cx + 2, hy, story["source"] + " - " + story["tag"],
                    scale=1, color=GREY, adv=5)
            hy += 7
            cy = hy + 2
        max_h = max(max_h, cy - stories_top)

    stats = {
        "stories": len(STORIES),
        "regions": len({s["region"] for s in STORIES}),
        "cards": len(TOP_STORIES),
        "scenes": len(TOP_STORIES) + len(PICTURES),
        "max_column_height": max_h,
        "stories_area_height": stories_h,
        "overflow": max_h > stories_h,
    }
    return encode_png(cv), stats


if __name__ == "__main__":
    from stories import check

    check()
    png, stats = render_page()
    print(stats)
    print("png bytes:", len(png))
    assert len(png) <= 1048576, len(png)
    assert not stats["overflow"], stats
