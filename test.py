import os
import pandas as pd
import openpyxl


folder_path = "/home/exmachina/dev/file_name_saver/test_folder"
# for folder_path, subfolders, file_names in os.walk(folder_path):
#     print("Current Folder:", folder_path)
#     print("Subfolder Names:", subfolders)
#     print("File Names:", file_names)
#     print("--------------------")

print('########################################')
folder_path = "/home/exmachina/dev/file_name_saver/test_folder"
for folder_path, subfolders, file_names in os.walk(folder_path):
    print("Current Folder:", folder_path)
    if subfolders != []:
        print("Subfolder Names:", subfolders)
    if file_names != []:
        print("File Names:", file_names)
    print("--------------------")

# Create a new Excel workbook
workbook = openpyxl.Workbook()
sheet = workbook.active

# Set the column header
sheet['A1'] = "File Names"

# Using os.walk to get all file names and subfolder names
# folder_path = "/home/exmachina/dev/file_name_saver/test_folder"
# for folder_path, subfolders, file_names in os.walk(folder_path):
#     for file_name in file_names + subfolders:
#         sheet.append([file_name])

# Using os.walk to get all file names and subfolder names
folder_path = "/home/exmachina/dev/file_name_saver/test_folder"
for folder_path, subfolders, file_names in os.walk(folder_path):
    main_dir = [os.path.basename(folder_path)]
    file_names.sort()
    for file_name in main_dir + file_names:
        sheet.append([file_name])

df = pd.DataFrame(workbook.active.values)
print(df)