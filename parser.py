import csv
import sys
import os
import pkgutil
from ParserBase import ParserBase
from Parsers.XMLParser import XMLParser


def main():
    if len(sys.argv) < 3:
        sys.exit('Usage : parser.py <format> <file1> <file2> ....<file5>')

    subs = ParserBase.__subclasses__()
    for cls in subs:
        instance = globals()[cls.__name__]()
        if instance.GetFormatExtension() == str(sys.argv[1]).strip().lower():
            paths = []
            for i in range(2, len(sys.argv)):
                paths.append(sys.argv[i])
            instance.Parse(paths)
            sys.exit('Success')

    sys.exit(f'Cant Find Corresponding Format to {sys.argv[1]}')


if __name__ == "__main__":
    main()
