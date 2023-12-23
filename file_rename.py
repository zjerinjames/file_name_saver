import os
from datetime import datetime

import re

current_date = datetime.now().strftime("%y%m%d")        

def is_initial_check(initial):
    return initial.isalpha() and len(initial) == 2

def is_valid_date(date_string):
        try:
            datetime.strptime(date_string, "%y%m%d")
            return True
        except ValueError:
            return False

def date_check(date_str):
        # Check if the second last content is datetime if not add date else 
        # update it
        if is_valid_date(date_str):
            is_date_flag =  True
        else:
            is_date_flag = False
        date_str = current_date
        return date_str, is_date_flag

def file_rename(name):
    
    # Extract the file name and extension
    name, ext = os.path.splitext(name)
    parts = name.split(' ')

    # If no space in the filename
    if len(parts) <= 1:    
        # in case not seperated by sapce but with '_'
        # try: 
        parts = name.split('_')
        no_space_flag = False
        # if there is no seperation char
        if len(parts) <= 1:    
        # except:
            no_space_flag =  True
            initial = name[-2:]
            date_str = name[-8:-2]
            is_initial_flag = is_initial_check(initial)
            is_date_flag = date_check(date_str)
            parts = []
            parts = [name[:-8], date_str, initial]
            if not(is_initial_flag and is_date_flag):
                initial = 'HS'
                date_str = ''
                parts.append(date_str)
                parts.append(initial)
    else:
        no_space_flag = 'space'
    # else:
    initial = parts[-1]
    date_str = parts[-2]

    # Check if it is date and update the date
    date_str, is_date_flag = date_check(date_str)
    if is_date_flag:
        parts[-2] = date_str
    else:
        parts.insert(-2, date_str)

    # Check if it is initial by checking the length is 2 and they are alphabets
    is_initial_flag = is_initial_check(initial)
    if is_initial_flag:
        # TODO: Handle 'HS-Layout1' case
        # If 'HS' is not present, add it 
        if initial != 'HS':    
            initial = 'HS'
            parts[-1] = initial
    else:
        initial = 'HS'
        parts[-1], parts[-2] = parts[-2], parts[-1]
        parts.append(initial)
    
    new_name = '_'.join(parts) + ext

    # Replace multiple consecutive underscores with a single underscore
    my_string = re.sub(r'_+', '_', new_name)

    # TODO: REMOVE INITIAL inital comes always after date
    # DONE: USE '_' TO SEPERATE
    return my_string


if __name__ == "__main__":
    names =["HRH Villa _ Basement_Report 231207 HS.dwg", 
            "BL RCP 231208 HS-Layout1.txt", "A2.04 231219 LD.txt", 
            "D22-57-DAE-AR-PIM-ALL-001 - Sheet - ALL-1102 -  Ground"
            " Floor Plan Controls 231218 LD.txt", 
            "A2.04_231219_LD.txt", "A2.04231219LD.txt",
            "A2.0423AB1967.txt"]

    for name in names:    
        print(f'Old: {name}')
        new_name = file_rename(name)
        print(f'New: {new_name}')
        print('!!!!!!!!!!!')