import json

class StudentDb:

    def __init__(self):
        self.__data=None

    
    def connect(self, dataFile):
        with open(dataFile) as jsonFile:
            self.__data=json.load(jsonFile)

    def getData(self, name):
        for s in self.__data['students']:
            if s['name']==name:
                return s

    def close(self):
        pass
