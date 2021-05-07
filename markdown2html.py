#!/usr/bin/python3
"""x"""

import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        out = "Usage: ./markdown2html.py README.md README.html"
        print(out, file=sys.stderr)
        exit(1)
    try:
        with open(sys.argv[1], "r") as f:
            data = f.read()
    except FileNotFoundError:
        print("Missing {:s}".format(sys.argv[1]), file=sys.stderr)
        exit(1)
    with open(sys.argv[2], "w") as f:
        f.write(data)
        exit(0)
