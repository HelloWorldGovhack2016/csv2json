#!/usr/bin/env python3

"""
GovHack 2016 CSV parser for files following this structure:

    Year,2006,2007,...,2016
    FooBars,1,2,...,3

This is a hack project, and comes with no guarantees whatsoever.
"""

import csv
from json import dump, dumps


class CSVParser:
    """Provide functionality to turn CSV file buffers into JSON objects."""

    def __init__(self, lines):
        """Initialize CSVParser with csv.DictReader for expected format.

        :param lines: iterator over CSV lines (e.g. a file-like object)
        """
        next(lines)  # seek to second line / throw away the header
        csv_reader = csv.DictReader(lines, fieldnames=['name'], restkey='data')
        self.data = list(csv_reader)

    def json(self, file=None):
        """Dump out json from self.csv_reader.

        :param file: dump to this file if present
        """
        if file is None:
            return dumps(self.data)
        else:
            return dump(self.data, file)


if __name__ == '__main__':
    from sys import argv, stderr

    if len(argv) < 2 or argv[1] in ('-h', '--help'):
        print("Usage: {} input_file [output_file]".format(argv[0]), file=stderr)
        exit(1)

    with open(argv[1]) as file:
        parser = CSVParser(file)

    if len(argv) == 3:
        with open(argv[2], 'w') as file:
            parser.json(file)
    else:
        print(parser.json())
