def ConvertToCSV(data):
    pass

def ConvertToJSON(data):
    pass

def ConvertToXML(data):
    pass

def formatData(repositoryType, data):
    if repositoryType == "csv":
        ''' Print in CSV format '''
        csvData = ConvertToCSV(data)
        return csvData
        
    elif repositoryType == "JSON":
        ''' Print in JSON format '''
        jsonData = ConvertToJSON(data)
        return jsonData
        
    elif repositoryType == "XML":
        ''' Print in XML format '''
        xmlData = ConvertToXML(data)
        return xmlData

    else:
        raise Exception("Repositoty Type is not supported")