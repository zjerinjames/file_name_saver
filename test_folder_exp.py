# script to open excelm sheet created
import pandas as pd

df = pd.read_excel("file.xlsx")
print(df.head(10))

# Iterate through each row and print the row data
for index, row in df.iterrows():
    print(f"Index: {index}, Name: {row['File Names']}")