import csv
import sys
import os
import pkgutil
from ParserBase import ParserBase


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage : parser.py <format> <file>")

    subs = ParserBase.__subclasses__()
    for cls in subs:
        instance = globals()[cls.__name__]()
        if instance.GetFormat() == str(sys.argv[1]).strip().lower():
            instance.Parse(sys.argv[2])


if __name__ == "__main__":
    main()
