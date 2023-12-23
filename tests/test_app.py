import unittest
import os

# Import the functions you want to test
from file_name_saver.file_name_saver import browse_folder, browse_save_location, list_files_to_excel

class TestYourScript(unittest.TestCase):

    def test_browse_folder(self):
        # You can't test filedialog.askdirectory directly, 
        # but you can check that it updates the folder_path_entry widget
        folder_path_entry = tk.Entry(tk.Tk())
        browse_folder()

        self.assertNotEqual(folder_path_entry.get(), "")  # Check that the entry is not empty after browsing

    def test_browse_save_location(self):
        # Similar to browse_folder, check that the save_file_entry widget is updated
        save_file_entry = tk.Entry(tk.Tk())
        browse_save_location()

        self.assertNotEqual(save_file_entry.get(), "")  # Check that the entry is not empty after browsing

    def test_list_files_to_excel(self):
        # Provide a folder path and check that the Excel file is created
        folder_path = "/path/to/your/test/folder"
        excel_file_path = "/path/to/your/test/output.xlsx"

        list_files_to_excel(folder_path, excel_file_path)

        # Check that the Excel file is created
        self.assertTrue(os.path.exists(excel_file_path))

        # Clean up the test file
        os.remove(excel_file_path)

if __name__ == '__main__':
    unittest.main()
