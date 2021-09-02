import sys

from ParserBase import ParserBase

# must be imported for all types of parsers otherwise it wont retrieved by calling ParserBase.__subclasses(),
# im sure it could be loaded dynamically somehow

from Parsers.CSVParser import CSVParser
from Parsers.XMLParser import XMLParser


def main():
    if len(sys.argv) < 4:
        sys.exit('Usage : parser.py <format> <output destination> <file1> <file2> ....<file5>')

    # on run time, retrieve all classes which implement ParserBase class, then initialize an instance of each and
    # check it its the correct parser before using it to parse the input file/files, this approach is sub-optmizal
    # because u will create unnecessary objects with max of ( n = number of parser classes ) , another solution is to
    # force a naming convention on everyone who wants to implement his own parser as <Extension>Parser so that I wont
    # have to create an instance to know what extenion the parser supports, i went with the sub optimal design choice
    # since i believe parser classes wont be huge in number, but either ways is valid.

    # get all sub classes
    subs = ParserBase.__subclasses__()
    for cls in subs:
        # create instance from the type
        instance = globals()[cls.__name__]()
        # check if current instance supports the input format
        if instance.GetFormatExtension() == str(sys.argv[1]).strip().lower():
            # check if the input args lengths matches the parser definition ( not counting the exe path and the
            # extension arg)
            if instance.GetPathArgsCount() == len(sys.argv) - 3:
                paths = []
                for i in range(3, len(sys.argv)):
                    paths.append(sys.argv[i])
                instance.Parse(paths, sys.argv[2].strip().lower())
                sys.exit('Success')

            sys.exit(f'The Require Path Args for {sys.argv[1]} Format is {instance.GetPathArgsCount()}')

    sys.exit(f'Cant Find Corresponding Format to {sys.argv[1]}')


if __name__ == "__main__":
    main()
