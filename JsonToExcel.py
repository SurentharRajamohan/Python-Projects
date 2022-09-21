import pandas as pd

#read the json file from the location specified
df = pd.read_json(r"C:\Users\User\VSCode Projects\51114.json", orient='index')

#df.transpose() to turn the columns into rows and rows into columns
#USE CASE: when the first column is supposed to be the header row
df = df.transpose()

#change to excel and save in the location specified. Make sure the file type at the end is .xlsx if u wanna change to excel
df.to_excel(r"C:\Users\User\Desktop\ALL DOCUMENTS\Z-OTHERS\TEST JSON FILE\output2.xlsx")
