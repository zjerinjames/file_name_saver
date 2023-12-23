import os
import pandas as pd
import openpyxl
from datetime import datetime
import re

# input_string = "BL RCP 231208 HS-Layout1.txt"

def pattern_finder(name):
    input_string, ext = os.path.splitext(name)

    # Define a pattern to match the desired combination
    pattern = re.compile(r'(\d{6})[ _]?([A-Za-z]+)')

    # Search for the pattern in the input string
    match = pattern.search(input_string)

    if match:
        # Get the matched date and HS
        date_part = match.group(1)
        hs_part = match.group(2)

        # print("Date:", date_part)
        # print("HS:", hs_part)
    else:
        print("Pattern not found.")

    if match:
        # Get the starting and ending positions of the matched groups
        date_start, date_end = match.start(1), match.end(1)
        hs_start, hs_end = match.start(2), match.end(2)

        # print("Date Position:", (date_start, date_end))
        # print("HS Position:", (hs_start, hs_end))
    else:
        print()


    # Check if the matched groups are at the end of the string
    if hs_end == len(input_string):
        print("Matched groups are already at the end.")
    else:
        # Move the matched groups to the last part of the string
        new_string = input_string[:date_start] + input_string[hs_end:]
        new_string += '_' + date_part + '_' + hs_part
        #new_string = input_string[:date_start] + input_string[hs_start:]
        #new_string += input_string[date_start:hs_start] + input_string[hs_end:]
        print("Modified String:", new_string)

names =["HRH Villa _ Basement_Report 231207 HS.dwg", 
            "BL RCP 231208 HS-Layout1.txt", "A2.04 231219 LD.txt", 
            "D22-57-DAE-AR-PIM-ALL-001 - Sheet - ALL-1102 -  Ground"
            " Floor Plan Controls 231218 LD.txt", 
            "A2.04_231219_LD.txt", "A2.04231219LD.txt",
            "A2.0423AB1967.txt"]

for name in names:
    print(name)
    pattern_finder(name)

# current_date = datetime.now().strftime("%y%m%d")

# def is_valid_date(date_string):
#     try:
#         datetime.strptime(date_string, "%y%m%d")
#         return True
#     except ValueError:
#         return False
    
# def date_check(date_str):
#     Check if the second last content is datetime if not add date else update it
#     if is_valid_date(date_str):
#         is_date_flag =  True
#     else:
#         is_date_flag = False
#     date_str = current_date
#     return date_str, is_date_flag



# # test names
# name = "HRH Villa _ Basement_Report 231207 HS.dwg"
# name = "BL RCP 231208 HS-Layout1.txt"
# name = "A2.04 231219 LD.txt"
# name = "D22-57-DAE-AR-PIM-ALL-001 - Sheet - ALL-1102 -  Ground Floor Plan Controls 231218 LD.txt"

# Extract the file name and extension
# name, ext = os.path.splitext(name)
# parts = name.split(' ')
# initial = parts[-1]
# date_str = parts[-2]

# Check if it is date and update the date
# date_str, is_date_flag = date_check(date_str)
# if is_date_flag:
#     parts[-2] = date_str
# else:
#     parts.insert(-2, date_str)

# Check if it is initial by checking the length is 2 and they are alphabets
# is_initial = initial.isalpha() and len(initial) == 2
# if is_initial:
#     TODO: 'HS-Layout1' if possible chek how to handle this
#     If 'HS' is not present, add it 
#     if initial != 'HS':    
#         initial = 'HS'
#         parts[-1] = initial
# else:
#     initial = 'HS'
#     parts[-1], parts[-2] = parts[-2], parts[-1]
#     parts.append(initial)

# new_name = ' '.join(parts)

# print(name)
# print(new_name)
# new_name = f'{name} {date_str} {initial} {ext}'

# else:
#     If 'HS' is present, update the date to the current date
#     parts = name.split(' ')
#     parts[-2] = current_date
#     new_name = ' '.join(parts) + ext

# print(new_name)
# print('!!!')


# # Rename the file
# old_path = os.path.join(directory, filename)
# new_path = os.path.join(directory, new_name)
# os.rename(old_path, new_path)


# folder_path = "/home/exmachina/dev/file_name_saver/test_folder"
# for folder_path, subfolders, file_names in os.walk(folder_path):
#     print("Current Folder:", folder_path)
#     print("Subfolder Names:", subfolders)
#     print("File Names:", file_names)
#     print("--------------------")

# print('########################################')
# folder_path = "/home/exmachina/dev/file_name_saver/test_folder"
# for folder_path, subfolders, file_names in os.walk(folder_path):
#     print("Current Folder:", folder_path)
#     if subfolders != []:
#         print("Subfolder Names:", subfolders)
#     if file_names != []:
#         print("File Names:", file_names)
#     print("--------------------")

# Create a new Excel workbook
# workbook = openpyxl.Workbook()
# sheet = workbook.active

# Set the column header
# sheet['A1'] = "File Names"

# Using os.walk to get all file names and subfolder names
# folder_path = "/home/exmachina/dev/file_name_saver/test_folder"
# for folder_path, subfolders, file_names in os.walk(folder_path):
#     main_dir = [os.path.basename(folder_path)]
#     file_names.sort()
#     for file_name in main_dir + file_names:
#         print(file_name)
#         sheet.append([file_name])

# df = pd.DataFrame(workbook.active.values)
# print(df)