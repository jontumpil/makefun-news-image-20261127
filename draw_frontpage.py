# draw_frontpage.py -- Pure-stdlib newspaper renderer for news-image-20261127.
# Draws a 1024x1024 front page: masthead, title, DATE CHECK box, schematic
# world map, UTC timeline, 5 large illustrated scenes, 8 small pictograms,
# and 47 stories in 5 dense newspaper columns. No third-party code.
# PNG is written by hand with zlib + struct so the output is deterministic.

import struct
import zlib

W, H = 1024, 1024

PAPER = (253, 246, 227)
INK = (26, 26, 26)
RED = (178, 34, 34)
BLUE = (30, 64, 120)
GREY = (110, 110, 100)
OCEAN = (205, 224, 238)
LAND = (146, 168, 118)
SAND = (214, 186, 140)
SKY = (135, 190, 225)
FLAME = (230, 110, 20)
SMOKE = (120, 120, 120)


def png_bytes(rgb):
    # rgb: bytes of W*H*3. Returns a complete PNG file (deterministic).
    raw = bytearray()
    for y in range(H):
        raw.append(0)
        raw += rgb[y * W * 3:(y + 1) * W * 3]
    comp = zlib.compress(bytes(raw), 9)

    def chunk(tag, data):
        c = struct.pack(">I", len(data)) + tag + data
        c += struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
        return c

    ihdr = struct.pack(">IIBBBBB", W, H, 8, 2, 0, 0, 0)
    out = b"\x89PNG\r\n\x1a\n"
    out += chunk(b"IHDR", ihdr)
    out += chunk(b"IDAT", comp)
    out += chunk(b"IEND", b"")
    return out


class Canvas:
    def __init__(self):
        self.px = bytearray(PAPER) * (W * H)

    def set(self, x, y, c):
        if 0 <= x < W and 0 <= y < H:
            i = (y * W + x) * 3
            self.px[i] = c[0]
            self.px[i + 1] = c[1]
            self.px[i + 2] = c[2]

    def rect(self, x, y, w, h, c):
        x0 = max(0, x)
        y0 = max(0, y)
        x1 = min(W, x + w)
        y1 = min(H, y + h)
        for yy in range(y0, y1):
            base = (yy * W + x0) * 3
            for xx in range(x0, x1):
                i = base + (xx - x0) * 3
                self.px[i] = c[0]
                self.px[i + 1] = c[1]
                self.px[i + 2] = c[2]

    def hline(self, x, y, w, c, t=1):
        self.rect(x, y, w, t, c)

    def vline(self, x, y, h, c, t=1):
        self.rect(x, y, t, h, c)

    def line(self, x0, y0, x1, y1, c):
        dx = abs(x1 - x0)
        dy = -abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        while True:
            self.set(x0, y0, c)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy

    def circle(self, cx, cy, r, c, fill=True):
        for yy in range(cy - r, cy + r + 1):
            for xx in range(cx - r, cx + r + 1):
                d = (xx - cx) ** 2 + (yy - cy) ** 2
                if fill:
                    if d <= r * r:
                        self.set(xx, yy, c)
                else:
                    if abs(d - r * r) <= r:
                        self.set(xx, yy, c)

    def tri(self, ax, ay, bx, by, cx, cy, c):
        # Filled triangle by scanline over its bounding box.
        minx, maxx = min(ax, bx, cx), max(ax, bx, cx)
        miny, maxy = min(ay, by, cy), max(ay, by, cy)
        den = (by - cy) * (ax - cx) + (cx - bx) * (ay - cy)
        if den == 0:
            return
        for yy in range(miny, maxy + 1):
            for xx in range(minx, maxx + 1):
                a = ((by - cy) * (xx - cx) + (cx - bx) * (yy - cy)) / den
                b = ((cy - ay) * (xx - cx) + (ax - cx) * (yy - cy)) / den
                cc = 1 - a - b
                if a >= 0 and b >= 0 and cc >= 0:
                    self.set(xx, yy, c)


# 5x7 display font: uppercase, digits, punctuation. Each glyph is 7 rows
# of 5 characters ('#' = ink, '.' = blank).
FONT5 = {
    "A": ("01110", "10001", "10001", "11111", "10001", "10001", "10001"),
    "B": ("11110", "10001", "10001", "11110", "10001", "10001", "11110"),
    "C": ("01110", "10001", "10000", "10000", "10000", "10001", "01110"),
    "D": ("11110", "10001", "10001", "10001", "10001", "10001", "11110"),
    "E": ("11111", "10000", "10000", "11110", "10000", "10000", "11111"),
    "F": ("11111", "10000", "10000", "11110", "10000", "10000", "10000"),
    "G": ("01110", "10001", "10000", "10111", "10001", "10001", "01111"),
    "H": ("10001", "10001", "10001", "11111", "10001", "10001", "10001"),
    "I": ("01110", "00100", "00100", "00100", "00100", "00100", "01110"),
    "J": ("00111", "00010", "00010", "00010", "00010", "10010", "01100"),
    "K": ("10001", "10010", "10100", "11000", "10100", "10010", "10001"),
    "L": ("10000", "10000", "10000", "10000", "10000", "10000", "11111"),
    "M": ("10001", "11011", "10101", "10101", "10001", "10001", "10001"),
}

FONT5.update({
    "N": ("10001", "11001", "10101", "10011", "10001", "10001", "10001"),
    "O": ("01110", "10001", "10001", "10001", "10001", "10001", "01110"),
    "P": ("11110", "10001", "10001", "11110", "10000", "10000", "10000"),
    "Q": ("01110", "10001", "10001", "10001", "10101", "10010", "01101"),
    "R": ("11110", "10001", "10001", "11110", "10100", "10010", "10001"),
    "S": ("01111", "10000", "10000", "01110", "00001", "00001", "11110"),
    "T": ("11111", "00100", "00100", "00100", "00100", "00100", "00100"),
    "U": ("10001", "10001", "10001", "10001", "10001", "10001", "01110"),
    "V": ("10001", "10001", "10001", "10001", "10001", "01010", "00100"),
    "W": ("10001", "10001", "10001", "10101", "10101", "11011", "10001"),
    "X": ("10001", "10001", "01010", "00100", "01010", "10001", "10001"),
    "Y": ("10001", "10001", "01010", "00100", "00100", "00100", "00100"),
    "Z": ("11111", "00001", "00010", "00100", "01000", "10000", "11111"),
    "0": ("01110", "10001", "10011", "10101", "11001", "10001", "01110"),
    "1": ("00100", "01100", "00100", "00100", "00100", "00100", "01110"),
    "2": ("01110", "10001", "00001", "00110", "01000", "10000", "11111"),
    "3": ("11111", "00010", "00100", "00010", "00001", "10001", "01110"),
    "4": ("00010", "00110", "01010", "10010", "11111", "00010", "00010"),
    "5": ("11111", "10000", "11110", "00001", "00001", "10001", "01110"),
    "6": ("00110", "01000", "10000", "11110", "10001", "10001", "01110"),
    "7": ("11111", "00001", "00010", "00100", "01000", "01000", "01000"),
    "8": ("01110", "10001", "10001", "01110", "10001", "10001", "01110"),
    "9": ("01110", "10001", "10001", "01111", "00001", "00010", "01100"),
    " ": ("00000", "00000", "00000", "00000", "00000", "00000", "00000"),
    ".": ("00000", "00000", "00000", "00000", "00000", "01100", "01100"),
    ",": ("00000", "00000", "00000", "00000", "01100", "00100", "01000"),
    "!": ("00100", "00100", "00100", "00100", "00100", "00000", "00100"),
    "?": ("01110", "10001", "00001", "00110", "00100", "00000", "00100"),
    "-": ("00000", "00000", "00000", "01110", "00000", "00000", "00000"),
    "'": ("00100", "00100", "01000", "00000", "00000", "00000", "00000"),
    '"': ("01010", "01010", "00000", "00000", "00000", "00000", "00000"),
    "/": ("00001", "00010", "00010", "00100", "01000", "01000", "10000"),
    "(": ("00010", "00100", "01000", "01000", "01000", "00100", "00010"),
    ")": ("01000", "00100", "00010", "00010", "00010", "00100", "01000"),
    "&": ("01100", "10010", "10100", "01000", "10101", "10010", "01101"),
    "%": ("11001", "11010", "00010", "00100", "01000", "01011", "10011"),
    "$": ("00100", "01111", "10100", "01110", "00101", "11110", "00100"),
    "#": ("01010", "01010", "11111", "01010", "11111", "01010", "01010"),
    "@": ("01110", "10001", "10111", "10101", "10110", "10000", "01110"),
    "+": ("00000", "00100", "00100", "11111", "00100", "00100", "00000"),
    "=": ("00000", "00000", "11111", "00000", "11111", "00000", "00000"),
    "*": ("00000", "10101", "01110", "10101", "00000", "00000", "00000"),
    ";": ("00000", "01100", "00000", "01100", "00100", "01000", "00000"),
    ":": ("00000", "01100", "00000", "01100", "00000", "00000", "00000"),
    "_": ("00000", "00000", "00000", "00000", "00000", "00000", "11111"),
    "[": ("01110", "01000", "01000", "01000", "01000", "01000", "01110"),
    "]": ("01110", "00010", "00010", "00010", "00010", "00010", "01110"),
    ">": ("10000", "01000", "00100", "00010", "00100", "01000", "10000"),
    "<": ("00010", "00100", "01000", "10000", "01000", "00100", "00010"),
})


def text5(cv, x, y, s, c, scale=1):
    # Draw uppercase 5x7 text; returns width in pixels.
    cx = x
    for ch in s:
        g = FONT5.get(ch.upper(), FONT5[" "])
        for r in range(7):
            row = g[r]
            for col in range(5):
                if row[col] == "1":
                    cv.rect(cx + col * scale, y + r * scale,
                            scale, scale, c)
        cx += 6 * scale
    return cx - x


def text5_w(s, scale=1):
    return len(s) * 6 * scale

# 4x5 micro font for dense summary columns. Each glyph is 5 rows of 4 chars.
FONT4 = {
    "a": ("0110", "1001", "0111", "0001", "0110"),
    "b": ("1000", "1000", "1110", "1001", "1110"),
    "c": ("0110", "1000", "1000", "1000", "0110"),
    "d": ("0001", "0001", "0111", "1001", "0111"),
    "e": ("0110", "1001", "1110", "1000", "0110"),
    "f": ("0110", "1000", "1110", "1000", "1000"),
    "g": ("0111", "1001", "0111", "0001", "0110"),
    "h": ("1000", "1000", "1110", "1001", "1001"),
    "i": ("0100", "0000", "0100", "0100", "0110"),
    "j": ("0010", "0000", "0010", "0010", "0110"),
    "k": ("1001", "1010", "1100", "1010", "1001"),
    "l": ("1000", "1000", "1000", "1000", "1000"),
    "m": ("0000", "0000", "1101", "1010", "1010"),
    "n": ("0000", "0000", "1110", "1001", "1001"),
    "o": ("0110", "1001", "1001", "1001", "0110"),
    "p": ("0000", "0000", "1110", "1001", "1110"),
    "q": ("0000", "0000", "0111", "1001", "0111"),
    "r": ("0000", "0000", "1011", "1100", "1000"),
    "s": ("0111", "1000", "0110", "0001", "1110"),
    "t": ("0100", "1110", "0100", "0100", "0110"),
    "u": ("0000", "0000", "1001", "1001", "0110"),
    "v": ("0000", "0000", "1001", "1001", "0100"),
    "w": ("0000", "0000", "1010", "1010", "0110"),
    "x": ("0000", "0000", "1001", "0110", "1001"),
    "y": ("0000", "0000", "1001", "0110", "0100"),
    "z": ("0000", "0000", "1110", "0100", "1110"),
    "A": ("0110", "1001", "1111", "1001", "1001"),
    "B": ("1110", "1001", "1110", "1001", "1110"),
    "C": ("0111", "1000", "1000", "1000", "0111"),
    "D": ("1110", "1001", "1001", "1001", "1110"),
    "E": ("1111", "1000", "1110", "1000", "1111"),
    "F": ("1111", "1000", "1110", "1000", "1000"),
    "G": ("0111", "1000", "1011", "1001", "0111"),
    "H": ("1001", "1001", "1111", "1001", "1001"),
    "I": ("1110", "0100", "0100", "0100", "1110"),
    "J": ("0111", "0010", "0010", "1010", "0100"),
    "K": ("1001", "1010", "1100", "1010", "1001"),
    "L": ("1000", "1000", "1000", "1000", "1111"),
    "M": ("1001", "1111", "1010", "1001", "1001"),
    "N": ("1001", "1101", "1010", "1001", "1001"),
    "O": ("0110", "1001", "1001", "1001", "0110"),
    "P": ("1110", "1001", "1110", "1000", "1000"),
    "Q": ("0110", "1001", "1001", "1010", "0101"),
    "R": ("1110", "1001", "1110", "1010", "1001"),
    "S": ("0111", "1000", "0110", "0001", "1110"),
    "T": ("1111", "0100", "0100", "0100", "0100"),
    "U": ("1001", "1001", "1001", "1001", "0110"),
    "V": ("1001", "1001", "1001", "0110", "0100"),
    "W": ("1001", "1001", "1010", "1111", "1001"),
    "X": ("1001", "1001", "0110", "1001", "1001"),
    "Y": ("1001", "1001", "0110", "0100", "0100"),
    "Z": ("1111", "0001", "0110", "1000", "1111"),
    "0": ("0110", "1001", "1001", "1001", "0110"),
    "1": ("0100", "1100", "0100", "0100", "0110"),
    "2": ("0110", "1001", "0010", "0100", "1111"),
    "3": ("1110", "0001", "0110", "0001", "1110"),
    "4": ("0010", "0110", "1010", "1111", "0010"),
    "5": ("1111", "1000", "1110", "0001", "1110"),
    "6": ("0110", "1000", "1110", "1001", "0110"),
    "7": ("1111", "0001", "0010", "0100", "0100"),
    "8": ("0110", "1001", "0110", "1001", "0110"),
    "9": ("0110", "1001", "0111", "0001", "0110"),
    " ": ("0000", "0000", "0000", "0000", "0000"),
    ".": ("0000", "0000", "0000", "0000", "0100"),
    ",": ("0000", "0000", "0000", "0100", "1000"),
    "!": ("0100", "0100", "0100", "0000", "0100"),
    "?": ("0110", "1001", "0010", "0000", "0100"),
    "-": ("0000", "0000", "1111", "0000", "0000"),
    "'": ("0100", "0100", "0000", "0000", "0000"),
    '"': ("1010", "1010", "0000", "0000", "0000"),
    "/": ("0001", "0010", "0010", "0100", "1000"),
    "(": ("0010", "0100", "0100", "0100", "0010"),
    ")": ("0100", "0010", "0010", "0010", "0100"),
    "&": ("0110", "1010", "0100", "1010", "0110"),
    "%": ("1010", "0010", "0100", "1000", "1010"),
    "$": ("0100", "0111", "1010", "0111", "0100"),
    "+": ("0000", "0100", "1110", "0100", "0000"),
    "=": ("0000", "1111", "0000", "1111", "0000"),
    "*": ("0000", "1010", "0100", "1010", "0000"),
    ";": ("0000", "0100", "0000", "0100", "1000"),
    ":": ("0000", "0100", "0000", "0100", "0000"),
    "_": ("0000", "0000", "0000", "0000", "1111"),
    "[": ("0110", "0100", "0100", "0100", "0110"),
    "]": ("0110", "0010", "0010", "0010", "0110"),
    ">": ("1000", "0100", "0010", "0100", "1000"),
    "<": ("0001", "0010", "0100", "0010", "0001"),
}


def text4(cv, x, y, s, c):
    # Draw 4x5 micro text; returns width in pixels. Advance is 5 px.
    cx = x
    for ch in s:
        g = FONT4.get(ch, FONT4[" "])
        for r in range(5):
            row = g[r]
            for col in range(4):
                if row[col] == "1":
                    cv.set(cx + col, y + r, c)
        cx += 5
    return cx - x


def text4_w(s):
    return len(s) * 5


def wrap(s, width_chars):
    # Greedy word wrap; returns list of lines, each <= width_chars.
    words = s.split(" ")
    lines = []
    cur = ""
    for w in words:
        if not cur:
            cur = w
        elif len(cur) + 1 + len(w) <= width_chars:
            cur += " " + w
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

# ---- Illustrated scenes: drawn with vector primitives only. ----

def scene_kuwait(cv, x, y, w, h):
    cv.rect(x, y, w, h, SKY)
    cv.rect(x, y + h - 18, w, 18, SAND)
    # facility blocks
    cv.rect(x + 14, y + h - 44, 34, 26, (90, 90, 90))
    cv.rect(x + 56, y + h - 36, 26, 18, (70, 70, 70))
    cv.rect(x + 92, y + h - 50, 30, 32, (110, 110, 110))
    cv.rect(x + 130, y + h - 30, 40, 12, (70, 70, 70))
    # drone silhouette
    dx, dy = x + w // 2, y + 16
    cv.rect(dx - 16, dy - 2, 32, 3, INK)
    cv.rect(dx - 4, dy - 5, 8, 8, INK)
    cv.circle(dx - 15, dy - 4, 3, INK)
    cv.circle(dx + 15, dy - 4, 3, INK)
    # explosion burst
    ex, ey = x + 108, y + h - 40
    cv.circle(ex, ey, 10, FLAME)
    cv.circle(ex, ey, 6, (250, 200, 60))
    cv.circle(ex - 16, ey - 6, 5, SMOKE)
    cv.circle(ex + 18, ey - 10, 5, SMOKE)


def scene_chess(cv, x, y, w, h):
    s = 7
    bx = x + (w - 56) // 2
    by = y + (h - 56) // 2
    for r in range(8):
        for c in range(8):
            col = PAPER if (r + c) % 2 == 0 else INK
            cv.rect(bx + c * s, by + r * s, s, s, col)
    cv.rect(bx - 1, by - 1, 58, 1, INK)
    cv.rect(bx - 1, by + 56, 58, 1, INK)
    # white king and black queen as discs with crowns
    cv.circle(bx + 3 * s + 4, by + 7 * s + 4, 5, (250, 250, 250))
    cv.circle(bx + 3 * s + 4, by + 7 * s + 4, 5, INK, fill=False)
    cv.circle(bx + 4 * s + 4, by + 0 * s + 4, 5, INK)
    cv.circle(bx + 5 * s + 4, by + 3 * s + 4, 3, RED)


def scene_ballot(cv, x, y, w, h):
    # ballot box
    cv.rect(x + w // 2 - 26, y + 22, 52, h - 30, (70, 90, 140))
    cv.rect(x + w // 2 - 30, y + 16, 60, 8, (50, 70, 110))
    cv.rect(x + w // 2 - 10, y + 12, 20, 6, PAPER)
    cv.line(x + w // 2 - 10, y + 12, x + w // 2 + 6, y + 26, INK)
    # two equal bars: 65 vs 65
    cv.rect(x + 12, y + h - 26, 60, 8, RED)
    cv.rect(x + w - 72, y + h - 26, 60, 8, BLUE)
    cv.circle(x + w // 2, y + h - 22, 3, INK)


def scene_jazan(cv, x, y, w, h):
    cv.rect(x, y, w, h, (40, 40, 48))
    # refinery towers, sized to stay inside the card
    for i, th in enumerate((18, 26, 14, 22)):
        tx = x + 18 + i * 34
        cv.rect(tx, y + h - 14 - th, 16, th, (150, 150, 150))
        cv.rect(tx + 4, y + h - 14 - th - 6, 8, 6, (120, 120, 120))
    cv.rect(x + 10, y + h - 14, w - 20, 6, (100, 100, 100))
    # flame and smoke on the second tower, inside the card
    fx = x + 52
    fy = y + h - 14 - 26 - 4
    cv.tri(fx - 7, fy + 8, fx + 7, fy + 8, fx, fy - 6, FLAME)
    cv.circle(fx + 2, fy - 8, 4, (250, 200, 60))
    cv.circle(fx - 14, fy - 6, 5, SMOKE)
    cv.circle(fx + 12, fy - 10, 5, SMOKE)


def scene_tanker(cv, x, y, w, h):
    cv.rect(x, y, w, h, SKY)
    # sea
    cv.rect(x, y + h - 26, w, 26, (40, 90, 140))
    cv.rect(x, y + h - 20, w, 3, (120, 190, 230))
    cv.rect(x, y + h - 12, w, 3, (120, 190, 230))
    # upturned hull
    hx, hy = x + w // 2, y + h - 30
    cv.rect(hx - 52, hy - 6, 104, 12, (60, 40, 30))
    cv.tri(hx - 52, hy - 6, hx + 52, hy - 6, hx, hy - 22, (60, 40, 30))
    cv.rect(hx - 52, hy + 6, 104, 4, RED)
    # smoke + small rescue boat
    cv.circle(hx + 40, hy - 16, 5, SMOKE)
    cv.circle(hx + 52, hy - 20, 5, SMOKE)
    cv.rect(x + 12, y + h - 16, 22, 6, (250, 250, 250))
    cv.rect(x + 12, y + h - 16, 22, 2, RED)


def scene_storm(cv, x, y, w, h):
    cv.rect(x, y, w, h, (60, 70, 90))
    # storm cloud
    cv.circle(x + w // 2 - 18, y + 20, 12, (40, 40, 48))
    cv.circle(x + w // 2 + 4, y + 14, 14, (40, 40, 48))
    cv.circle(x + w // 2 + 22, y + 22, 10, (40, 40, 48))
    cv.rect(x + w // 2 - 30, y + 18, 64, 12, (40, 40, 48))
    # lightning bolt
    lx = x + w // 2 + 2
    cv.tri(lx, y + 30, lx + 10, y + 30, lx + 2, y + 44, (250, 220, 60))
    cv.tri(lx + 2, y + 44, lx + 10, y + 44, lx - 2, y + 56, (250, 220, 60))
    # rain streaks
    for rx in (x + 16, x + 34, x + w - 40, x + w - 22):
        cv.line(rx, y + 34, rx - 4, y + 50, (150, 200, 240))
    # flooded street
    cv.rect(x, y + h - 10, w, 10, (40, 90, 140))


LARGE_SCENES_DRAW = {
    "kuwait": scene_kuwait,
    "chess": scene_chess,
    "ballot": scene_ballot,
    "jazan": scene_jazan,
    "tanker": scene_tanker,
    "storm": scene_storm,
}


def pic_gavel(cv, x, y):
    cv.line(x + 6, y + 22, x + 30, y + 4, INK)
    cv.rect(x + 4, y + 2, 16, 7, INK)
    cv.rect(x + 2, y + 22, 34, 3, INK)


def pic_scales(cv, x, y):
    cv.vline(x + 18, y + 2, 20, INK, 2)
    cv.hline(x + 4, y + 4, 28, INK, 2)
    cv.tri(x + 4, y + 8, x + 12, y + 8, x + 8, y + 18, INK)
    cv.tri(x + 24, y + 8, x + 32, y + 8, x + 28, y + 18, INK)
    cv.rect(x + 14, y + 22, 8, 2, INK)


def pic_gold(cv, x, y):
    cv.rect(x + 4, y + 16, 12, 6, (200, 160, 40))
    cv.rect(x + 20, y + 16, 12, 6, (200, 160, 40))
    cv.rect(x + 12, y + 8, 12, 6, (230, 190, 60))
    cv.rect(x + 4, y + 16, 12, 2, (240, 210, 90))
    cv.rect(x + 20, y + 16, 12, 2, (240, 210, 90))


def pic_pumpjack(cv, x, y):
    cv.line(x + 6, y + 22, x + 12, y + 6, INK)
    cv.line(x + 12, y + 6, x + 30, y + 8, INK)
    cv.line(x + 30, y + 8, x + 30, y + 16, INK)
    cv.rect(x + 4, y + 22, 28, 2, INK)
    cv.circle(x + 12, y + 8, 3, INK)


def pic_asteroid(cv, x, y):
    cv.circle(x + 18, y + 12, 10, (140, 140, 140))
    cv.circle(x + 14, y + 9, 3, (90, 90, 90))
    cv.circle(x + 22, y + 15, 2, (90, 90, 90))
    cv.circle(x + 26, y + 8, 4, FLAME)
    cv.line(x + 30, y + 4, x + 34, y + 0, FLAME)


def pic_rocket(cv, x, y):
    cv.tri(x + 18, y + 1, x + 12, y + 12, x + 24, y + 12, INK)
    cv.rect(x + 12, y + 12, 12, 8, INK)
    cv.tri(x + 12, y + 20, x + 18, y + 12, x + 18, y + 20, RED)
    cv.tri(x + 24, y + 20, x + 18, y + 12, x + 18, y + 20, RED)
    cv.tri(x + 15, y + 20, x + 21, y + 20, x + 18, y + 26, FLAME)


def pic_football(cv, x, y):
    cv.circle(x + 18, y + 12, 10, (250, 250, 250))
    cv.circle(x + 18, y + 12, 10, INK, fill=False)
    cv.circle(x + 18, y + 12, 3, INK)
    cv.set(x + 10, y + 6, INK)
    cv.set(x + 26, y + 6, INK)
    cv.set(x + 10, y + 18, INK)
    cv.set(x + 26, y + 18, INK)


def pic_globe(cv, x, y):
    cv.circle(x + 18, y + 12, 10, OCEAN)
    cv.circle(x + 18, y + 12, 10, BLUE, fill=False)
    cv.line(x + 18, y + 2, x + 18, y + 22, BLUE)
    cv.line(x + 8, y + 12, x + 28, y + 12, BLUE)
    cv.line(x + 28, y + 4, x + 36, y + 4, RED)
    cv.tri(x + 36, y + 1, x + 36, y + 7, x + 40, y + 4, RED)


SMALL_SCENES_DRAW = {
    "gavel": pic_gavel,
    "scales": pic_scales,
    "gold": pic_gold,
    "pumpjack": pic_pumpjack,
    "asteroid": pic_asteroid,
    "rocket": pic_rocket,
    "football": pic_football,
    "globe": pic_globe,
}

# ---- Top band: DATE CHECK box, schematic world map, UTC timeline. ----

def draw_date_check(cv, x, y, w, h, text):
    cv.rect(x, y, w, h, PAPER)
    cv.rect(x, y, w, 2, RED)
    cv.rect(x, y + h - 2, w, 2, RED)
    cv.rect(x, y, 2, h, RED)
    cv.rect(x + w - 2, y, 2, h, RED)
    text5(cv, x + 8, y + 8, "DATE CHECK", RED, 1)
    lines = wrap(text, (w - 16) // 5)
    yy = y + 20
    for ln in lines:
        text4(cv, x + 8, yy, ln, INK)
        yy += 6


def draw_map(cv, x, y, w, h):
    cv.rect(x, y, w, h, OCEAN)
    cv.rect(x, y, w, 1, INK)
    cv.rect(x, y + h - 1, w, 1, INK)
    cv.rect(x, y, 1, h, INK)
    cv.rect(x + w - 1, y, 1, h, INK)
    text4(cv, x + 6, y + 4, "WORLD MAP - WHERE TODAY'S NEWS HAPPENED", INK)
    ox, oy = x, y + 14
    # Schematic continents as block clusters (not to scale).
    na = [(18, 8, 52, 22), (30, 30, 30, 14), (62, 26, 16, 10)]
    sa = [(66, 48, 20, 30), (70, 78, 12, 12)]
    eu = [(168, 10, 26, 14), (182, 24, 18, 8)]
    af = [(178, 36, 34, 26), (186, 62, 22, 18), (196, 80, 10, 8)]
    asia = [(206, 8, 90, 22), (220, 30, 60, 18), (280, 48, 26, 12)]
    au = [(306, 74, 34, 14), (316, 88, 16, 6)]
    for group in (na, sa, eu, af, asia, au):
        for (rx, ry, rw, rh) in group:
            cv.rect(ox + rx, oy + ry, rw, rh, LAND)
    # Red dots for the biggest stories.
    dots = [
        (250, 44, "KUWAIT"), (238, 40, "GAZA"), (196, 18, "LONDON"),
        (192, 30, "IBIZA"), (52, 22, "NEW YORK"), (272, 38, "DELHI"),
        (312, 62, "JAKARTA"), (348, 88, "WELLINGTON"), (192, 56, "LAGOS"),
    ]
    for (dx, dy, _lbl) in dots:
        cv.circle(ox + dx, oy + dy, 3, RED)


def draw_timeline(cv, x, y, w, h, events):
    cv.rect(x, y, w, h, PAPER)
    cv.rect(x, y, w, 1, INK)
    cv.rect(x, y + h - 1, w, 1, INK)
    cv.rect(x, y, 1, h, INK)
    cv.rect(x + w - 1, y, 1, h, INK)
    text4(cv, x + 6, y + 4, "UTC TIMELINE - MORNING OF 27 NOV 2026", INK)
    ax0, ax1 = x + 14, x + w - 14
    ay = y + 62
    cv.hline(ax0, ay, ax1 - ax0, INK, 2)
    # Hour ticks 00:00 to 08:00.
    for hh in range(9):
        tx = ax0 + (ax1 - ax0) * hh // 8
        cv.vline(tx, ay - 3, 7, INK, 1)
        text4(cv, tx - 8, ay + 8, "%02d:00" % hh, GREY)
    for (utc, label, above) in events:
        hh = int(utc[:2])
        mm = int(utc[3:5])
        mins = hh * 60 + mm
        ex = ax0 + (ax1 - ax0) * mins // 480
        cv.circle(ex, ay, 3, RED)
        ly = ay - 26 if above else ay + 20
        lx = ex - len(label) * 5 // 2
        if lx < x + 2:
            lx = x + 2
        if lx + len(label) * 5 > x + w - 2:
            lx = x + w - 2 - len(label) * 5
        text4(cv, lx, ly, label, INK)
        text4(cv, lx, ly + 6 if above else ly - 7, utc, GREY)


# ---- Scene cards band. ----

SCENE_CARDS = [
    ("kuwait", "No.1 KUWAIT: DRONE STRIKE KILLS TWO ITALIANS"),
    ("chess", "No.23 GENEVA: GUKESH HOLDS SINDAROV IN GAME 3"),
    ("ballot", "No.36 WELLINGTON: NZ ELECTION DEADLOCKED 65-65"),
    ("jazan", "No.4 JAZAN: REFINERY STRIKE KILLS ONE WORKER"),
    ("tanker", "No.8 IBIZA: TANKER CAPSIZES, ONE DEAD"),
    ("storm", "No.18 USA: THANKSGIVING STORM FLOODS COASTS"),
]


def draw_scene_cards(cv, y, col_x, col_w):
    for i, (key, caption) in enumerate(SCENE_CARDS):
        x = col_x[i]
        cv.rect(x, y, col_w, 1, INK)
        cv.rect(x, y + 87, col_w, 1, INK)
        cv.rect(x, y, 1, 88, INK)
        cv.rect(x + col_w - 1, y, 1, 88, INK)
        LARGE_SCENES_DRAW[key](cv, x + 2, y + 2, col_w - 4, 58)
        lines = wrap(caption, col_w // 5)
        yy = y + 62
        for ln in lines[:2]:
            text4(cv, x + 4, yy, ln, INK)
            yy += 6

# ---- Story columns. ----

COL_Y0 = 284
COL_Y1 = 1018
COL_W = 161
COL_GAP = 6
COL_X0 = 14


def story_height(st, pic):
    head_w = 26 if not pic else 19
    head_lines = wrap(st["headline"], head_w)
    sum_lines = wrap(st["summary"], COL_W // 5)
    base = max(len(head_lines) * 7, 26 if pic else 0)
    return base + 2 + len(sum_lines) * 6 + 6 + 1


def draw_story(cv, x, y, st):
    pic = st.get("scene", "") in SMALL_SCENES_DRAW
    tx = x
    if pic:
        SMALL_SCENES_DRAW[st["scene"]](cv, x, y)
        tx = x + 42
    head_w = 26 if not pic else 19
    head_lines = wrap(st["headline"], head_w)
    yy = y
    for ln in head_lines:
        text5(cv, tx, yy, ln, INK, 1)
        yy += 7
    sum_lines = wrap(st["summary"], COL_W // 5)
    yy = y + max(len(head_lines) * 7, 26 if pic else 0) + 2
    for ln in sum_lines:
        text4(cv, x, yy, ln, INK)
        yy += 6
    src = st["source"] + " - " + st["tag"]
    text4(cv, x, yy, src, RED if st["tag"] == "CONFIRMED" else BLUE)
    yy += 6
    return yy - y + 1


def draw_region_header(cv, x, y, region):
    cv.rect(x, y, COL_W, 1, INK)
    text5(cv, x, y + 2, region, RED, 1)
    return 10


def column_breaks(heights, ncol, cap):
    # Partition the ordered story heights into at most ncol contiguous
    # groups whose height is as balanced as possible (binary search on
    # the max group height). Greedy packing alone wastes the tail of
    # every column; balancing removes that waste. Returns (groups, hmax)
    # where groups is a list of index lists. Raises if even the best
    # balance exceeds cap.
    n = len(heights)
    total = sum(heights)
    if max(heights) > cap:
        raise RuntimeError("single story taller than a column")

    def feasible(hmax):
        groups = 1
        cur = 0
        for h in heights:
            if cur + h > hmax:
                groups += 1
                cur = h
            else:
                cur += h
        return groups <= ncol

    lo, hi = max(max(heights), (total + ncol - 1) // ncol), total
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    hmax = lo
    if hmax > cap:
        raise RuntimeError("columns overflow: min max group %d" % hmax)
    groups = []
    cur = []
    cur_h = 0
    for idx, h in enumerate(heights):
        if cur and cur_h + h > hmax:
            groups.append(cur)
            cur = [idx]
            cur_h = h
        else:
            cur.append(idx)
            cur_h += h
    if cur:
        groups.append(cur)
    return groups, hmax


def render(stories, title, date_check):
    cv = Canvas()
    # Masthead.
    mt = "THE WORLD IN ONE DAY"
    text5(cv, (W - text5_w(mt, 3)) // 2, 8, mt, INK, 3)
    sub = "FRIDAY 27 NOVEMBER 2026  -  46 STORIES  -  7 REGIONS  -  MORNING EDITION"
    text5(cv, (W - text5_w(sub, 1)) // 2, 36, sub, INK, 1)
    cv.rect(12, 50, W - 24, 2, INK)
    cv.rect(12, 54, W - 24, 1, INK)
    # Formula title line.
    tw = text5_w(title, 1)
    text5(cv, max(12, (W - tw) // 2), 60, title, INK, 1)
    cv.rect(12, 72, W - 24, 1, INK)
    # Top band: DATE CHECK | map | UTC timeline.
    draw_date_check(cv, 12, 76, 280, 112, date_check)
    draw_map(cv, 300, 76, 380, 112)
    events = [
        ("00:08", "CHESS", True),
        ("00:22", "MIGRATION", False),
        ("01:03", "KUWAIT", True),
        ("02:06", "DART", False),
        ("02:26", "JAZAN", True),
        ("03:31", "IBIZA", False),
        ("03:46", "PMLA", True),
        ("05:15", "BAYERN", False),
    ]
    draw_timeline(cv, 688, 76, 324, 112, events)
    # Scene cards band.
    col_x = [COL_X0 + i * (COL_W + COL_GAP) for i in range(6)]
    draw_scene_cards(cv, 196, col_x, COL_W)
    # Story columns, flowing in region order, balanced by binary search.
    heights = []
    for i, st in enumerate(stories):
        pic = st.get("scene", "") in SMALL_SCENES_DRAW
        hh = story_height(st, pic)
        if i == 0 or st["region"] != stories[i - 1]["region"]:
            hh += 10
        heights.append(hh)
    groups, _hmax = column_breaks(heights, 6, COL_Y1 - COL_Y0)
    cur_region = None
    for gi, grp in enumerate(groups):
        y = COL_Y0
        for idx in grp:
            st = stories[idx]
            if st["region"] != cur_region:
                y += draw_region_header(cv, col_x[gi], y, st["region"])
                cur_region = st["region"]
            y += draw_story(cv, col_x[gi], y, st)
    # Footer.
    foot = "THE WORLD IN ONE DAY - 27 NOVEMBER 2026 - ALL 46 STORIES VERIFIED PUBLISHED 27 NOV 2026"
    text4(cv, (W - text4_w(foot)) // 2, 1018, foot, GREY)
    return bytes(cv.px)


def render_png(stories, title, date_check):
    return png_bytes(render(stories, title, date_check))
