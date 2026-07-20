#!/usr/bin/env python3
"""Render a self-contained HTML pack to PDF.

Usage:
    python3 html_to_pdf.py input.html [output.pdf]
"""
import sys
from pathlib import Path

from weasyprint import HTML


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    src = Path(sys.argv[1])
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".pdf")

    HTML(filename=str(src)).write_pdf(str(dst))
    print(f"wrote {dst}")


if __name__ == "__main__":
    main()
