def ConvertToCSV(data):
    pass

def ConvertToJSON(data):
    pass

def ConvertToXML(data):
    pass

def formatData(repositoryType, data):
    if repositoryType == "csv":
        csvData = ConvertToCSV(data)
        return csvData
        
    elif repositoryType == "JSON":
        jsonData = ConvertToJSON(data)
        return jsonData
        
    elif repositoryType == "XML":
        xmlData = ConvertToXML(data)
        return xmlData

    else:
        raise Exception("Repositoty Type is not supported")
