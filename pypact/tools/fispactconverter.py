#!/usr/bin/env python3
import sys
import argparse
from pypact.reader.reader import Reader


def main():
    # Command line argument support
    parser = argparse.ArgumentParser(description='Fispact Output Converter')
    parser.add_argument('outputfile', type=argparse.FileType('r'),
                        help='The fispact output (.out) file to be read')
    parser.add_argument('jsonoutputfile', type=argparse.FileType('w'),
                        help='The fispact output file in JSON format to be written')
    args = parser.parse_args()

    filename = args.outputfile.name

    try:
        reader = Reader()
        jsonout = reader(filename).json_serialize()

        with open(args.jsonoutputfile.name, 'w') as jsonfile:
            jsonfile.write(jsonout)

    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError as err:
        print(err)
    except:
        print("Unexpected error:", sys.exc_info()[0])


if __name__ == "__main__":
    main()