import csv

def parse_csv(reader_obj: _csv.reader) -> list:
    return list(reader_obj)