import os

class settings():
    def __init__(self):
        self.settingsFile = os.path.expanduser("~/.roscoeSettings")
        self.settingsDict = {}
        self.readSettings()

    def __del__(self):
        self.saveSettings()

    def readSettings(self):
        if (os.path.exists(self.settingsFile) == False):
            print("No settings file found, using defaults")
            return

        readFile = open(self.settingsFile, "r") #open settings file for reading
        readLine = 0

        for row in readFile:
            if (row.strip != ""):
                try:
                    readLine += 1   #increment readline
                    seperator = row.find("=")   #find location of seperator
                    if (seperator != -1):    #make sure line contains seperator
                        key = row[:seperator].strip()   #get the key
                        value = row[seperator + 1:].strip() #get the value
                        self.settingsDict.update({key: value}) #add the setting to the dictionary
                    else:
                        print("Error reading settings file line " + str(readLine))
                        print(row)
                except:
                    print("Error reading settings file line " + str(readLine))
                    print(row)
        readFile.close()

    def saveSettings(self):
        writeFile = open(self.settingsFile, "w") #open settings file for writing
        for line in range(len(self.settingsDict)):  #loop through all dictionaly items
            key = list(self.settingsDict.keys())[line]    #get the key for the line
            writeFile.write(key + "=" + self.settingsDict.get(key) + "\n") #write setting to dictionary
        writeFile.close()

    def get(self, key, default):  #try to get setting by key
        try:
            return self.settingsDict[key]   #see if key exists
        except:
            self.settingsDict.update({key: default}) #add the default to the dictionary
            return default

    def set(self, key, value):  #set dictionart value
        self.settingsDict.update({key: str(value)})

