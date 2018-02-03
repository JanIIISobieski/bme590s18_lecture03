import os
import pandas
import numpy
import glob

#def main():
filenames = collect_csv_files();
isbad     = check_CSV_exceptions(filenames[0])
print(filenames[0])
print(isbad)
# student_data = cat_data()
# write_data()
#return filename


def collect_csv_files():
    csvLoc = get_CSV_folder() + "*.csv"
    filename = []
    for CSVfile in glob.glob(csvLoc):
        filename.append(CSVfile)
    return filename

def cat_data():
    pass

def check_CSV_exceptions(csvName):
    name_exceptions = ["mlp6.csv"]  #can expand the list of bad files
    checkall = []
    for badnames in name_exceptions:
        checkall.append(badnames in csvName)
    return any(checkall)

def check_spaces():
    pass

def count_CamelCase():
    pass

def write_data():
    # CSV or JSON
    pass

def get_CSV_folder():
    scriptDirectory = os.path.dirname(__file__)
    relativeCSVPath = "../CSVFiles/"
    csvPath = os.path.join(scriptDirectory, relativeCSVPath)
    return csvPath

def get_JSON_folder():
    scriptDirectory = os.path.dirname(__file__)
    relativeJSONPath = "../JSONFiles/"
    jsonPath = os.path.join(scriptDirectory, relativeJSONPath)
    return jsonPath

if __name__ == "__main__":
    main()