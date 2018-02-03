import os
import pandas
import numpy
import glob

def main():
    CSVloc = get_CSV_folder() + "*.csv"
    print(CSVloc)
        # filenames = collect_csv_files()
        # student_data = cat_data()
        # write_data()


def collect_csv_files():
    CSVwildcard = "/*.csv"
    #get_CSV_folder().
    pass

def cat_data():
    pass

def write_():
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
