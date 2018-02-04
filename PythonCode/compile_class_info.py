import os
import pandas
import glob

def main():
    filenames = collect_csv_files()
    allGoodCSVFiles = cat_data(filenames)
    write_CSV(allGoodCSVFiles)
    return 

def collect_csv_files():
    csvLoc = get_CSV_folder() + "*.csv"
    filename = []
    for csvFile in glob.glob(csvLoc):
        filename.append(csvFile)
    return filename

def cat_data(filenames):
    everyDataFrameArray = []  
    expectedColumns = 5
    camelCaseCount = 0
    
    for csvFile in filenames:
        
        readFile =  pandas.read_csv(csvFile, names=['FirstName', 'LastName', 'NetID', 'Github', 'TeamName'], skipinitialspace = True)
    
        if check_import_exceptions(csvFile):
            print(os.path.basename(csvFile) + " is ignored")
            continue
        if bad_size(readFile, expectedColumns):
            print(os.path.basename(csvFile) + " has wrong shape")
            continue
        if teamname_has_spaces(readFile):
            print(os.path.basename(csvFile) + " team name contains a space")
        if is_CamelCase:
            camelCaseCount += 1   
        
        write_JSON(csvFile, readFile)
        everyDataFrameArray.append(readFile)

    print("Camel case count: {}".format(camelCaseCount))
    everyDataFrame = pandas.concat(everyDataFrameArray)
    return everyDataFrame

def check_import_exceptions(csvName):
    name_exceptions = ["mlp6.csv", "everyone.csv"]  #can expand the list of bad files
    checkall = []
    for badnames in name_exceptions:
        checkall.append(badnames == os.path.basename(csvName))
    return any(checkall)

def bad_size(readFile, expectedSize):
    isBadSize = readFile.size != expectedSize
    return isBadSize

def teamname_has_spaces(readFile):
    hasSpace = readFile.loc[0].TeamName.find(" ") is not -1
    return hasSpace

def is_CamelCase(readFile):
    isCamelCase = readFile.loc[0].TeamName.islower() is False and readFile.loc[0].TeamName.isupper() is False
    return isCamelCase

def write_CSV(concatDataFrame):
    saveLoc = get_CSV_folder()
    fileSaveName = "everyone.csv"
    fullSavePath = os.path.join(saveLoc, fileSaveName)
    
    concatDataFrame.to_csv(fullSavePath, index_label = False, index = False)
    return

def write_JSON(csvFile, readFile):
    saveLoc = get_JSON_folder()
    importedFileName = os.path.basename(csvFile)
    fileSaveName = importedFileName[0:-3] + ".json"
    fullSavePath = os.path.join(saveLoc, fileSaveName)
    
    readFile.to_json(fullSavePath, orient = "records")
    return

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