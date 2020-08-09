import csv , json , os , pandas as pd
import importlib
import chardet
import sys
# importlib.reload(sys)
# sys.setdefaultencoding("ISO-8859-1")

csvFilePath = "data/la_restaurants.csv"
jsonFilePath = "data/data.json"

# df=pd.read_csv("data/prep_w_cols_sample.csv", encoding="utf-16", )
# print(df)

# pass

data = []
#read the csv and add the arr to a arrayn
#  first commented out line is for machine learning file
# with open (csvFilePath, encoding="utf-16", errors='ignore') as csvFile:
with open (csvFilePath) as csvFile:   
    csvReader = csv.DictReader(csvFile)
    print(csvReader)
    for csvRow in csvReader:
        data.append(csvRow)

print(data[2])

# write the data to a json file
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent = 4))

    # helpful: 
    # https://stackoverflow.com/questions/22216076/unicodedecodeerror-utf8-codec-cant-decode-byte-0xa5-in-position-0-invalid-s
    # https://stackoverflow.com/questions/7105441/how-to-set-default-encoding-in-python-setdefaultencoding-function-does-not-ex
    # https://www.usessionbuddy.com/post/how-to-fix-error-UnicodeDecodeError-utf-8-codec-cant-decode-byte/