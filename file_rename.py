import os
import re
from datetime import datetime


current_date = datetime.now().strftime("%y%m%d")


def file_rename(name):
    input_string, ext = os.path.splitext(name)
    # Define a pattern to match the desired combination
    pattern = re.compile(r"(\d{6})[ _]?([A-Za-z]+)")
    # Search for the pattern in the input string
    match = pattern.search(input_string)
    if match:
        # Get the matched date and HS
        date_part = match.group(1)
        hs_part = match.group(2)
        date_start, hs_end = match.start(1), match.end(2)
    else:
        # add date and initial
        date_initial = "_" + current_date + "_" + "HS"
        input_string += date_initial
        new_string = input_string
    # Check if the matched groups are at the end of the string
    try:
        if hs_end == len(input_string):
            # update date and initial
            date_initial = "_" + current_date + "_" + "HS"
            new_string = input_string[:date_start] + date_initial
        else:
            # Move the matched groups to the last part of the string
            new_string = input_string[:date_start] + input_string[hs_end:]
            new_string += "_" + date_part + "_" + hs_part
    except UnboundLocalError:
        pass
    new_string = new_string.replace(" ", "_")
    # Replace multiple consecutive underscores with a single underscore
    new_string = re.sub(r"_+", "_", new_string)
    new_string += ext
    return new_string


if __name__ == "__main__":
    names = [
        "HRH Villa _ Basement_Report 231207 HS.dwg",
        "BL RCP 231208 HS-Layout1.txt",
        "A2.04 231219 LD.txt",
        "D22-57-DAE-AR-PIM-ALL-001 - Sheet - ALL-1102 -  Ground"
        " Floor Plan Controls 231218 LD.txt",
        "A2.04_231219_LD.txt",
        "A2.04231219LD.txt",
        "A2.0423AB1967.txt",
        "Floor Plan Controls 231218 ld.txt",
    ]

    for name in names:
        print(f"Old: {name}")
        new_name = file_rename(name)
        print(f"New: {new_name}")
