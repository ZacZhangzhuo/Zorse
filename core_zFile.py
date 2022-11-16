import json
import os

def writeJson(filePath, fileName, dataAsList,sortKeys):
    if fileName[-5:] != ".json":
        fileName = fileName + ".json"
    filename = os.path.join(filePath, fileName)

    with open(filename, 'w') as f:
        f.write(json.dumps(dataAsList, sortKeys))
    
    return None