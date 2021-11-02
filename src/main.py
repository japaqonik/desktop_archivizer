#! python3

import sys
import argparse
import archivizer

parser = argparse.ArgumentParser()
parser.add_argument("archive_name", type=str, help="Name of directory that will be created on Desktop. It will keep each day archive.")
parser.add_argument("-s", "--silent", action="store_true", help="do not print progress bar")
parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")

def main() -> int:
    args = parser.parse_args()

    archivizer.move_files(args.archive_name, args.silent, args.verbose)

    return 0

if __name__ == '__main__':
    sys.exit(main())