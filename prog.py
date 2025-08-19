import argparse
import csv

parser = argparse.ArgumentParser(description='Provide descriptive statistical measures for CSV files.')
parser.add_argument('input_file', type=argparse.FileType('r'), 
                   help='Input file to process')

args = parser.parse_args()

# Use the file objects directly
with args.input_file as infile:
    # Basic reading line by line
    reader = csv.reader(infile)
    print(type(reader))