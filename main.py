#!/usr/bin/env python3
"""Copy the shipped passport spread to the output directory.

Stdlib only: the grading sandbox is Python 3.13 with nothing installed,
no network, a read-only repository and a writable output directory.
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path

ENTRY = "entry.png"


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    src = Path(__file__).resolve().parent / ENTRY
    dst = Path(out_dir) / ENTRY
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    if sha256_file(src) != sha256_file(dst):
        print("error: copied image is not byte-identical to the shipped one",
              file=sys.stderr)
        sys.exit(1)
    print(f"wrote {dst} ({dst.stat().st_size} bytes, sha256 verified)")


if __name__ == "__main__":
    main()
