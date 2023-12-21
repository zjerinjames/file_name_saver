# script to open excelm sheet created
import pandas as pd

df = pd.read_excel("file.xlsx")
print(df.head(10))
