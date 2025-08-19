import csv
import numpy as np 

def parse_csv(reader_obj: csv.reader) -> list:
    '''Parses CSV into 2D Python list.'''
    return list(reader_obj)

def column_type(column: list) -> str:  # Changed return type to str
    '''Returns the data type of a column '''
    first_nonna = first_nonna_val_index(column)

    if first_nonna == -1:  # Fixed: use the variable, not the function name
        return "All null values"
    
    # Get the first non-null value
    first_val = column[first_nonna]
    assumed_dtype = type(first_val)
    
    # Default answer is assumed data type
    res = str(assumed_dtype)

    for example in column:
        # Skip None values
        if example is None:
            continue
            
        # Handle NaN values specifically
        if isinstance(example, float) and np.isnan(example):
            continue
            
        # Check if type matches
        if type(example) != assumed_dtype:
            res = "Inconsistent dtypes"
            break

    return res

def first_nonna_val_index(column: list) -> int:
    '''Helper to column_type(). Returns first index of non null value.'''
    for i in range(len(column)):
        if column[i] is not None:  # Use 'is not' for None comparison
            return i 
    return -1