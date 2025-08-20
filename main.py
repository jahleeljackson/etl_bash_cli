import argparse
import csv
from utils import column_type
from FileTypeChecker import FileTypeWithExtensionCheck

parser = argparse.ArgumentParser(description='Data analysis and manipulation tool for CSV files.')
parser.add_argument('read', type=FileTypeWithExtensionCheck('r', valid_extensions=('.csv', '.CSV')), 
                   help='CSV file to process')

args = parser.parse_args()

with args.read as infile:
    
    # Basic reading line by line
    reader = csv.reader(infile)
    
    #parse csv to be more easily analyzed and manipulated
    data = list(reader)
    #define column headers
    column_headers= data[0]

    #define column types

    #print column headers & dtypes
    print("Columns:")
    for column_header in column_headers:
        print(column_header)

