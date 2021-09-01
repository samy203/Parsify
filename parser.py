import sys

from ParserBase import ParserBase


# must be imported for all types of parsers otherwise it wont retrieved by calling ParserBase.__subclasses(),
# im sure it could be loaded dynamically somehow


def main():
    if len(sys.argv) < 3:
        sys.exit('Usage : parser.py <format> <file1> <file2> ....<file5>')

    subs = ParserBase.__subclasses__()
    for cls in subs:
        instance = globals()[cls.__name__]()
        # check if current instance matches the input format
        if instance.GetFormatExtension() == str(sys.argv[1]).strip().lower():
            # check if the input args lengths matches the parser definition ( not counting the exe path and the
            # extension arg)
            if instance.GetPathArgsCount() == len(sys.argv) - 2:
                paths = []
                for i in range(2, len(sys.argv)):
                    paths.append(sys.argv[i])
                instance.Parse(paths)
                sys.exit('Success')

            sys.exit(f'The Require Path Args for {sys.argv[1]} Format is {instance.GetPathArgsCount()}')

    sys.exit(f'Cant Find Corresponding Format to {sys.argv[1]}')


if __name__ == "__main__":
    main()
