#!/usr/bin/env python3
"""Copy the news-image artwork to the make.fun output file.

Reads artwork.jpg next to this script, validates it (JPEG magic bytes,
size at most 1 MiB, dimensions exactly 1024x1024 parsed from a JPEG
start-of-frame segment), then copies it byte-for-byte to entry.png
inside $MAKEFUN_OUTPUT_DIR (created if needed), or to a local output/
directory when the variable is unset. Standard library only; no network.
"""

import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "artwork.jpg")
MAX_BYTES = 1024 * 1024
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def fail(message):
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def jpeg_dimensions(data):
    """Return (width, height) from the first start-of-frame segment."""
    if len(data) < 2 or data[0] != 0xFF or data[1] != 0xD8:
        return None
    pos = 2
    while pos + 1 < len(data):
        if data[pos] != 0xFF:
            pos += 1
            continue
        marker = data[pos + 1]
        if marker == 0xD9:  # end of image
            return None
        if marker == 0x01 or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        if pos + 4 > len(data):
            return None
        length = struct.unpack(">H", data[pos + 2:pos + 4])[0]
        if length < 2 or pos + 2 + length > len(data):
            return None
        # SOF markers: C0-C3, C5-C7, C9-CB, CD-CF. C4 (DHT), C8 (JPG)
        # and CC (DAC) are not frame markers and are skipped like the rest.
        if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                      0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            segment = data[pos + 4:pos + 2 + length]
            if len(segment) < 5:
                return None
            height = struct.unpack(">H", segment[1:3])[0]
            width = struct.unpack(">H", segment[3:5])[0]
            return (width, height)
        pos += 2 + length
    return None


def main():
    if not os.path.isfile(SOURCE):
        fail("artwork.jpg not found next to main.py")
    with open(SOURCE, "rb") as handle:
        data = handle.read()
    if len(data) > MAX_BYTES:
        fail("artwork.jpg is %d bytes, over the 1 MiB limit" % len(data))
    dimensions = jpeg_dimensions(data)
    if dimensions is None:
        fail("could not parse JPEG dimensions from artwork.jpg")
    width, height = dimensions
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        fail("artwork.jpg is %dx%d, expected 1024x1024" % (width, height))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(HERE, "output")
    os.makedirs(out_dir, exist_ok=True)
    destination = os.path.join(out_dir, "entry.png")
    with open(destination, "wb") as handle:
        handle.write(data)
    print("wrote %s (1024x1024, %d bytes)" % (destination, len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
