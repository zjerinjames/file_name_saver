import os
import openpyxl
import tkinter as tk
from tkinter import filedialog
import subprocess
from PIL import Image, ImageTk
from file_rename import file_rename

# subprocess.run(["pip", "install", "openpyxl"])


def browse_folder():
    folder_path = filedialog.askdirectory()  # Open a folder selection dialog
    if folder_path:
        folder_path_entry.delete(0, tk.END)  # Clear the current entry
        folder_path_entry.insert(
            0, folder_path
        )  # Insert the selected folder path into the entry field


def browse_save_location():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")],
    )
    if file_path:
        save_file_entry.delete(0, tk.END)  # Clear the current entry
        save_file_entry.insert(
            0, file_path
        )  # Insert the selected file path into the entry field


def list_files_to_excel():
    folder_path = folder_path_entry.get()
    excel_file_path = save_file_entry.get()

    if not excel_file_path:
        excel_file_path = os.path.join(folder_path, "file_list.xlsx")
    # Create a new Excel workbook
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Set the column header
    sheet["A1"] = "File Names"
    # Using os.walk to get all file names and subfolder names
    folder_path = "/home/exmachina/dev/file_name_saver/test_folder"
    for folder_path, subfolders, file_names in os.walk(folder_path):
        main_dir = [os.path.basename(folder_path)]
        file_names.sort()
        print(file_names)
        print("!!!!!!!!!!11")
        for i, file_name in enumerate(file_names):
            # print(i, ' ', file_name)
            print(file_names[i])
            file_names[i] = file_rename(file_name)
            file_names[i]
        for file_name in main_dir + file_names:
            sheet.append([file_name])

    # Save the Excel file
    workbook.save(excel_file_path)
    workbook.close()
    result_label.config(text=f"Saved :\n{excel_file_path}")


# Create a Tkinter window
window = tk.Tk()
window.title("File List to Excel")

# Adjust size
window.geometry("400x400")
# Load the image file using Pillow
image = Image.open("img/bg.png")
image = image.resize((400, 300), Image.LANCZOS)  # Fit image to Canvas
background_image = ImageTk.PhotoImage(image)  # Convert to PhotoImage

# Create Canvas
canvas1 = tk.Canvas(window, width=400, height=400)
canvas1.pack(fill="both", expand=True)
# Display image
canvas1.create_image(0, 0, image=background_image, anchor="nw")

# Create and pack GUI elements
folder_path_label = tk.Label(window, text="Folder Path:")
folder_path_entry = tk.Entry(window)
browse_button = tk.Button(window, text="Browse", command=browse_folder)
save_file_label = tk.Label(window, text="Save File:")
save_file_entry = tk.Entry(window)
browse_save_button = tk.Button(window, text="Browse",
                               command=browse_save_location)
list_button = tk.Button(window, text="Save",
                        command=list_files_to_excel, fg="orange")
result_label = tk.Label(window, text="", wraplength=400)

folder_path_label_canvas = canvas1.create_window(
    20, 280, anchor="nw", window=folder_path_label
)
folder_path_entry_canvas = canvas1.create_window(
    120, 280, anchor="nw", window=folder_path_entry
)
browse_button_canvas = canvas1.create_window(
    280, 280, anchor="nw", window=browse_button
)
save_file_label_canvas = canvas1.create_window(
    20, 310, anchor="nw", window=save_file_label
)
save_file_entry_canvas = canvas1.create_window(
    120, 310, anchor="nw", window=save_file_entry
)
browse_save_button_canvas = canvas1.create_window(
    280, 310, anchor="nw", window=browse_save_button
)
list_button_canvas = canvas1.create_window(280, 340, anchor="nw",
                                           window=list_button)
result_label_canvas = canvas1.create_window(10, 360, anchor="nw",
                                            window=result_label)
# Start the Tkinter main loop
window.mainloop()
