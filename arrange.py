import sys
import re
import os
import pandas as pd

def excelRead():
    try:
        # Prompt user to enter path of Excel file
        excel = pd.ExcelFile("Networking_Template.xlsx", engine='openpyxl')
        if "ipad_profile" in excel.sheet_names:
            df = pd.read_excel(excel, sheet_name="ipad_profile", usecols=[0, 1, 2])
            col1 = df.iloc[:, 0]
            col2 = df.iloc[:, 1]
            col3 = df.iloc[:, 2]
            
            
            # Convert col1 to a string data type
            col1_str = col1.astype(str)
            
            # Combine the two columns
            combined_column = col1_str + ' ' + col2
            
            # Print the combined column data
            print(combined_column)
            print(col3)
        else:
            print("Error: Sheet 'ipad_profile' not found in Excel file")
    except IndexError:
        print("Error: Excel file path not specified")

excelRead()