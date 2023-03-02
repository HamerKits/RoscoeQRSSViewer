#Author: John Hamer
#Copyright: 2023
#License: MIT License - See LICENSE.md

from PySide2 import QtWidgets
from PySide2.QtWidgets import QFileDialog, QMessageBox
import ui.captureSettings_ui
import os
import settings

class form(QtWidgets.QDialog, ui.captureSettings_ui.Ui_Dialog):
    def __init__(self, settings):
        super(form, self).__init__()
        self.setupUi(self)  #setup user interface
        self.settings = settings
        self.btnBrowse.clicked.connect(self.selectFolder)
        self.cbCapture.addItem("Capture 1") #add caputre 1 to combo box
        self.cbCapture.addItem("Capture 2") #add caputre 1 to combo box
        self.cbCapture.activated.connect(self.updateSettings)
        self.captureFolder = [self.settings.get("capture1Path", os.path.expanduser("~")), self.settings.get("capture2Path", os.path.expanduser("~"))]
        self.imageName = [self.settings.get("capture1ImageName", "Capture"), self.settings.get("capture2ImageName", "Capture")]
        self.captureInterval = [int(self.settings.get("capture1Interval", "30")), int(self.settings.get("capture2Interval", "30"))]
        self.indexEnabled = [self.settings.get("capture1IndexEnabled", "True") == "True", self.settings.get("capture2IndexEnabled", "False") == "True"]

        #set initial textbox values
        self.txtImageName.setText(self.imageName[0])
        self.txtCaptureInterval.setText(str(self.captureInterval[0]))

        #set temporary variables
        self.captureFolderTemp = [self.captureFolder[0], self.captureFolder[1]]
        self.imageNameTemp = [self.imageName[0], self.imageName[1]]
        self.captureIntervalTemp = [self.captureInterval[0], self.captureInterval[1]]
        self.indexEnabledTemp = [self.indexEnabled[0], self.indexEnabled[1]]
        self.changed = [False, False]

    def show(self):
        super(form, self).show()
        #reset inputs
        self.cbCapture.setCurrentIndex(0)   #show capture 1
        self.captureFolderTemp = [self.captureFolder[0], self.captureFolder[1]]
        self.imageNameTemp = [self.imageName[0], self.imageName[1]]
        self.captureIntervalTemp = [self.captureInterval[0], self.captureInterval[1]]
        self.indexEnabledTemp = [self.indexEnabled[0], self.indexEnabled[1]]
        self.lblFolder.setText(self.captureFolderTemp[self.cbCapture.currentIndex()])
        self.txtImageName.setText(self.imageNameTemp[self.cbCapture.currentIndex()])
        self.txtCaptureInterval.setText(str(self.captureIntervalTemp[self.cbCapture.currentIndex()]))
        self.cbIncrement.setChecked(self.indexEnabledTemp[self.cbCapture.currentIndex()])
        self.changed = [False, False]   #reset changed on show
        self.activateWindow() #make sure window shows right away

    def accept(self):   #override OK button
        if (self.checkAndStoreSettings(self.cbCapture.currentIndex()) == False):    #make sure settings are ok
            return  #dont allow exit until fixed

        self.checkIfChanged(self.cbCapture.currentIndex())

        #apply changes
        if (self.changed[0] == True):    #see if need to update capture 1
            self.captureFolder[0] = self.captureFolderTemp[0]
            self.imageName[0] = self.imageNameTemp[0]
            self.captureInterval[0] = self.captureIntervalTemp[0]
            self.indexEnabled[0] = self.indexEnabledTemp[0] 

            #update settings file
            self.settings.set("capture1Path", self.captureFolder[0])
            self.settings.set("capture1ImageName", self.imageName[0])
            self.settings.set("capture1Interval", str(self.captureInterval[0]))
            self.settings.set("capture1IndexEnabled", str(self.indexEnabled[0]))
        if (self.changed[1] == True):    #see if need to update capture 2
            self.captureFolder[1] = self.captureFolderTemp[1]
            self.imageName[1] = self.imageNameTemp[1]
            self.captureInterval[1] = self.captureIntervalTemp[1]
            self.indexEnabled[1] = self.indexEnabledTemp[1] 

            #update settings file
            self.settings.set("capture2Path", self.captureFolder[1])
            self.settings.set("capture2ImageName", self.imageName[1])
            self.settings.set("capture2Interval", str(self.captureInterval[1]))
            self.settings.set("capture2IndexEnabled", str(self.indexEnabled[1]))
 
        super(form, self).accept()  #continue closing dialog

    def selectFolder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Select Folder', dir = self.captureFolderTemp[self.cbCapture.currentIndex()])
        if(folder != ""):   #don't update if pressed cancel
            self.captureFolderTemp[self.cbCapture.currentIndex()] = folder  #set folder
        self.lblFolder.setText(self.captureFolderTemp[self.cbCapture.currentIndex()])   #update folder label

    def checkAndStoreSettings(self, index): #error check for invalid entries
        #check that a file name was given
        self.txtImageName.setText("".join( x for x in self.txtImageName.text() if (x.isalnum() or x in "._- "))) #remove invalid file name characters
        if (len(self.txtImageName.text()) < 1):   #make sure there is at least one character
            QMessageBox.about(self, "Error", "No image name given") #display error
            return False

        #check that interval is correct
        interval = self.txtCaptureInterval.text()
        interval.strip()    #remove spaces from interval
        self.txtCaptureInterval.setText(interval)   #update interval with no spaces
        if (self.txtCaptureInterval.text().isdigit() == False):  #make sure a positive integer
            QMessageBox.about(self, "Error", "Interval must be a number") #display error
            return False

        #update temporary variables
        self.imageNameTemp[index] = self.txtImageName.text()
        self.captureIntervalTemp[index] = int(self.txtCaptureInterval.text())
        self.indexEnabledTemp[index] = self.cbIncrement.isChecked()
        return True

    def updateSettings(self):
        if (self.cbCapture.currentIndex() == 0):
            if (self.checkAndStoreSettings(1) == False):  #see if all settings are ok
                self.cbCapture.setCurrentIndex(1)   #don't allow change
                return
            self.checkIfChanged(1)  #see if anything changed
        else:
            if (self.checkAndStoreSettings(0) == False):  #see if all settings are ok
                self.cbCapture.setCurrentIndex(0)   #don't allow change
                return
            self.checkIfChanged(0)  #see if anything changed

        #update user settable values
        self.lblFolder.setText(self.captureFolderTemp[self.cbCapture.currentIndex()])
        self.txtImageName.setText(self.imageNameTemp[self.cbCapture.currentIndex()])
        self.txtCaptureInterval.setText(str(self.captureIntervalTemp[self.cbCapture.currentIndex()]))
        self.cbIncrement.setChecked(self.indexEnabledTemp[self.cbCapture.currentIndex()])

    def checkIfChanged(self, index):
        changed = False

        #see if any of the user inputs changed
        if (self.captureFolder[index] != self.captureFolderTemp[index]):
            changed = True
        if (self.imageName[index] != self.imageNameTemp[index]):
            changed = True
        if (self.captureInterval[index] != self.captureIntervalTemp[index]):
            changed = True
        if (self.indexEnabled[index] != self.indexEnabledTemp[index]):
            changed = True

        if (changed == True):   #see if any values changed
            self.changed[index] = True  #record this has been changed

    def getCapturePath(self, index):
        if (self.indexEnabled[index] == True):
            imageIndex = 0
            dirList = os.listdir(self.captureFolder[index]) #grab all files from capture directory
            for x in dirList:
                filename = str(x)
                if (filename.find(".jpg") != -1): #look for images
                    if (filename.find(self.imageName[index]) != -1):    #look for files with same name as image name
                        filename = filename.replace(".jpg", "")  #remove extension
                        filename = filename.replace(self.imageName[index], "")  #remove image name
                        if (filename.isdigit() == True):    #see if what is left is an integer
                            if (int(filename) > imageIndex):    #find largest index
                                imageIndex = int(filename)  #store the index

            return self.captureFolder[index] + "/" + self.imageName[index] + str(imageIndex + 1) + ".jpg"
        else:
            return self.captureFolder[index] + "/" + self.imageName[index] + ".jpg"

    def getCaptureInterval(self, index):
        return self.captureInterval[index]