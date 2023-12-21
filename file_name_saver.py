import os
import openpyxl
import tkinter as tk
from tkinter import filedialog
import subprocess

#subprocess.run(["pip", "install", "openpyxl"])

def browse_folder():
    folder_path = filedialog.askdirectory()  # Open a folder selection dialog
    if folder_path:
        folder_path_entry.delete(0, tk.END)  # Clear the current entry
        folder_path_entry.insert(0, folder_path)  # Insert the selected folder path into the entry field


def browse_save_location():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")]
    )
    if file_path:
        save_file_entry.delete(0, tk.END)  # Clear the current entry
        save_file_entry.insert(0, file_path)  # Insert the selected file path into the entry field

def list_files_to_excel():
    folder_path = folder_path_entry.get()
    excel_file_path = save_file_entry.get()
    
    if not excel_file_path:
        excel_file_path = os.path.join(folder_path, "file_list.xlsx")

    # Create a new Excel workbook
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Set the column header
    sheet['A1'] = "File Names"

    # Using os.walk to get all file names and subfolder names
    folder_path = "/home/exmachina/dev/file_name_saver/test_folder"
    for folder_path, subfolders, file_names in os.walk(folder_path):
        main_dir = [os.path.basename(folder_path)]
        file_names.sort()
        for file_name in main_dir + file_names:
            sheet.append([file_name])

    # Save the Excel file
    # excel_file_path = os.path.join(folder_path, excel_file_name)
    workbook.save(excel_file_path)

    # Close the workbook
    workbook.close()

    result_label.config(text=f"File names written to {excel_file_path} successfully.")

# Create a Tkinter window
window = tk.Tk()
window.title("File List to Excel")

# Set the window size (width x height)
window.geometry("400x300")

# Create and pack GUI elements
folder_path_label = tk.Label(window, text="Folder Path:")
folder_path_label.pack()
folder_path_entry = tk.Entry(window)
folder_path_entry.pack()

browse_button = tk.Button(window, text="Browse", command=browse_folder)
browse_button.pack()

save_file_label = tk.Label(window, text="Save Excel File As:")
save_file_label.pack()
save_file_entry = tk.Entry(window)
save_file_entry.pack()

browse_save_button = tk.Button(window, text="Browse Save Location", command=browse_save_location)
browse_save_button.pack()

# Add space between buttons
space_label = tk.Label(window, text="")
space_label.pack()

list_button = tk.Button(window, text="List Files to Excel", command=list_files_to_excel, fg="green")
list_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Start the Tkinter main loop
window.mainloop()