import argparse
import csv
from utils import parse_csv, column_types

parser = argparse.ArgumentParser(description='Provide descriptive statistical measures for CSV files.')
parser.add_argument('input_file', type=argparse.FileType('r'), 
                   help='Input file to process')

args = parser.parse_args()

# Use the file objects directly
with args.input_file as infile:
    # Basic reading line by line
    reader = csv.reader(infile)
    
    #parse csv to be more easily analyzed and manipulated
    data = parse_csv(reader)

    #define column headers
    column_headers= data[0]

    #define column types

    #print column headers & dtypes
    print("Columns:")
    for column_header in column_headers:
        print(column_header)

