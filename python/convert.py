import csv , json , os , pandas as pd
import importlib
import chardet
import sys
# importlib.reload(sys)
# sys.setdefaultencoding("ISO-8859-1")

csvFilePath = "data/prep_w_cols_sample.csv"
jsonFilePath = "data/data.json"

# df=pd.read_csv("data/prep_w_cols_sample.csv", encoding="utf-16", )
# print(df)

# pass

data = []
#read the csv and add the arr to a arrayn

with open (csvFilePath, encoding="utf-16", errors='ignore') as csvFile:
    
    csvReader = csv.DictReader(csvFile)
    print(csvReader)
    for csvRow in csvReader:
        data.append(csvRow)

print(data[2])

# write the data to a json file
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent = 4))