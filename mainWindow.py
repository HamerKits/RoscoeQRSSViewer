from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QPixmap, QPainter, qRgb
from PySide2.QtCore import Qt, QTimer
from PySide2.QtWidgets import QMessageBox, QActionGroup, QInputDialog
from datetime import datetime, timezone
import ui.mainWindow_ui
import devicesDialog
import captureSettings
import numpy
import input.audio
import waterfall
import settings
import fft
import string        
import time
import os
import math

class form(QtWidgets.QMainWindow, ui.mainWindow_ui.Ui_MainWindow):
    def __init__(self):

        self.version = "1.0"

        super(form, self).__init__()
        self.setupUi(self)  #setup user interface
        self.settings = settings.settings() #read settings file
        self.devicesDialog = devicesDialog.form()   #make devices dialog
        self.captureSettings = captureSettings.form()   #make capture settings form
        self.setWindowTitle("Roscoe QRSS Viewer V" + self.version)  #set the title

        #set widget callbacks
        self.btnStart.clicked.connect(self.btnConnect_callback) #set connect button callback
        self.btnSetFrequency.clicked.connect(self.btnSetFrequency_callback) #set frequenct callback
        self.actionSelect_Input.triggered.connect(self.menuSelectInput) #set menu select input callback
        self.actionCapture_Settings.triggered.connect(self.menuCaptureSettings)
        self.actionExit.triggered.connect(self.exitButton)
        self.actionWaterfall_Note.triggered.connect(self.editNote)
        self.sliderSpeed.valueChanged.connect(self.speedChanged_callback)

        self.audio = input.audio.audio()    #make audio
        self.waterfall = waterfall.waterfall(800, 400)  #make a waterfall
        self.fft = fft.fft()    #make an fft

        #setup timer for waterfall update
        self.wfTimer = QTimer() #make waterfall timer
        self.wfTimer.timeout.connect(self.waterfallUpdate)   #update paint event on timeout

        self.capture1Timer = QTimer()   #timer for capture 1
        self.capture1Timer.timeout.connect(self.capture1)
        self.capture1LastInterval = 0   #used to detect interval change

        self.capture2Timer = QTimer()   #timer for capture 2
        self.capture2Timer.timeout.connect(self.capture2)
        self.capture2LastInterval = 0   #used to detect interval change

        self.imageTimer = QTimer() #make waterfall timer
        self.imageTimer.timeout.connect(self.drawWaterfall)   #update paint event on timeout

        #set initial window size
        self.resize(775, 530)   #set start size

        #set initial frequency settings
        self.sampleFreq = 44100 #audio sample frequency
        self.sampleSize = 2048 #Sample size
        self.bufferSize = 2048  #buffer size for FFT
        self.outputSize = 800   #size to scale FFT to
        self.wfSpeed = 4    #speed of FFT update
        self.speedChanged = False
        self.wfText1 = "Roscoe QRSS Viewer"
        self.wfText2 = ""
        self.startLocation = 0    #start location in array
        self.freqStart = 0

        #update settings from settings file
        self.notes = self.settings.get("notes", "")
        self.minSpan = int(self.settings.get("minSpan", "1000"))
        self.freqSpan = int(self.settings.get("freqSpan", "22050"))  #span in Hz
        self.freqOffset = float(self.settings.get("freqOffset", "0.0"))
        self.mode = self.settings.get("mode", "")
        centerFrequency = self.settings.get("freqCenter", "11025")

        self.txtCenterFrequency.setText(str(int(centerFrequency)))
        self.txtFrequencySpan.setText(str(self.freqSpan))
        self.txtOffset.setText(str(int(self.freqOffset)))
        self.btnSetFrequency_callback()
        self.cbAGC.setChecked(True)

        self.running = False    #not running yet
        self.setFrequencyBox()  #set frequency box initial values
        self.imageTimer.start(200)
        self.newAudioData = False

        #setup mode checkboxes
        self.modeGroup = QActionGroup(self)
        self.modeGroup.addAction(self.actionFull_Speed)
        self.modeGroup.addAction(self.actionQRSS3)
        self.modeGroup.addAction(self.actionQRSS10)
        self.modeGroup.addAction(self.actionQRSS20)
        self.modeGroup.addAction(self.actionQRSS30)
        self.modeGroup.addAction(self.actionQRSS60)
        self.modeGroup.addAction(self.actionQRSS120)
        
        self.actionFull_Speed.triggered.connect(self.setMode)
        self.actionQRSS3.triggered.connect(self.setMode)
        self.actionQRSS10.triggered.connect(self.setMode)
        self.actionQRSS20.triggered.connect(self.setMode)
        self.actionQRSS30.triggered.connect(self.setMode)
        self.actionQRSS60.triggered.connect(self.setMode)
        self.actionQRSS120.triggered.connect(self.setMode)
        if (self.mode == "QRSS3"):
            self.actionQRSS3.setChecked(True)
        elif (self.mode == "QRSS10"):
            self.actionQRSS10.setChecked(True)
        elif (self.mode == "QRSS20"):
            self.actionQRSS20.setChecked(True)
        elif (self.mode == "QRSS30"):
            self.actionQRSS30.setChecked(True)
        elif (self.mode == "QRSS60"):
            self.actionQRSS60.setChecked(True)
        elif (self.mode == "QRSS120"):
            self.actionQRSS120.setChecked(True)
        else:
            self.actionFull_Speed.setChecked(True)
        self.setMode()

    def editNote(self):
        text, ok = QInputDialog.getText(self, 'Waterfall Note', 'Enter a note to display on the waterfall screen', text=self.notes)
        if ok:
            self.notes = str(text)  #set note text
            self.settings.set("notes", self.notes)  #update notes

    def exitButton(self):
        quit()  #quit the program

    def closeEvent(self, event):
        if (self.running == True):  #see if running when closed
            self.audio.stopStream() #stop stream
        self.audio.terminate()  #terminate audio
        self.devicesDialog.close()
        self.captureSettings.close()
        event.accept()

    def btnConnect_callback(self):
        if (self.running == False): #see if running
            try:
                self.audio.startStream(self.devicesDialog.currentDevice, self.audioCallback)    #start audio stream
                self.wfTimer.start(10) #start update timer
                self.running = True #set running state
                self.btnStart.setText("Stop")   #update button text
                self.waterfall.resetAGC()   #reset AGC buffer
            except:
                print("Error opening stream")   #display stream error
        else:
            self.audio.stopStream() #stop stream
            self.btnStart.setText("Start")  #update button text
            self.wfTimer.stop() #stop update timer
            self.running = False    #set running state
            self.capture1Timer.stop()   #stop capture timer
            self.capture2Timer.stop()   #stop capture timer
            self.fft.clearBuffer()  #clear buffer for next start

    def capture1(self):
        print ("saving capture1 ", self.captureSettings.getCapturePath(0))
        self.waterfall.saveWaterfall(self.captureSettings.getCapturePath(0)) #save waterfall image

    def capture2(self):
        print ("saving capture2 ", self.captureSettings.getCapturePath(1))
        self.waterfall.saveWaterfall(self.captureSettings.getCapturePath(1)) #save waterfall image

    def btnSetFrequency_callback(self):
        #check frequency span box
        if (self.txtFrequencySpan.text().isdigit()):
            #make sure span is valid
            if (int(self.txtFrequencySpan.text()) > self.sampleFreq / 2):
                QMessageBox.about(self, "Error", "Frequency plus span must be smaller than " + str(self.freqSpan) + ".")
                self.setFrequencyBox()  #reset frequency boxes
                return

            if (int(self.txtFrequencySpan.text()) < self.minSpan):   #clamp minimum span
                self.txtFrequencySpan.setText(str(self.minSpan))  
        else:
            QMessageBox.about(self, "Error", "Frequency span must be a number.")
            self.setFrequencyBox()  #reset frequency boxes
            return

        #check start frequency box
        if (self.txtCenterFrequency.text().isdigit()):
            #make sure frequency is valid
            if (int(self.txtCenterFrequency.text()) - (int(self.txtFrequencySpan.text()) / 2) < 0):
                self.txtCenterFrequency.setText(str(math.ceil((int(self.txtFrequencySpan.text()) / 2) - 0.5)))  #change to valid integer

            if (int(self.txtCenterFrequency.text()) + (int(self.txtFrequencySpan.text()) / 2) > (self.sampleFreq / 2)):
                QMessageBox.about(self, "Error", "Frequency plus span must be smaller than " + str(self.freqSpan) + ".")
                self.setFrequencyBox()  #reset frequency boxes
                return
            
        else:
            QMessageBox.about(self, "Error", "Center frequency must be a number.")
            self.setFrequencyBox()  #reset frequency boxes
            return

        try:
            self.freqOffset = float(self.txtOffset.text())
        except:
            QMessageBox.about(self, "Error", "Frequency offset must be a number.")
            if (self.freqOffset == int(self.freqOffset)):
                self.txtOffset.setText(str(int(self.freqOffset)))
            else:
                self.txtOffset.setText(str(self.freqOffset))
            return

        self.freqSpan = int(self.txtFrequencySpan.text())  #span in Hz
        self.freqStart = int(self.txtCenterFrequency.text()) - (self.freqSpan / 2)  #start frequenct in Hz
        self.outputSize = self.fft.checkOutputSize(int(((self.sampleFreq) / self.freqSpan) * self.waterfall.height), self.bufferSize)   #calculate size needed for fft
        
        self.settings.set("freqCenter", self.txtCenterFrequency.text())
        self.settings.set("freqSpan", str(self.freqSpan))  #span in Hz
        self.settings.set("freqOffset", str(self.freqOffset))

        if (self.freqStart == 0):
            self.startLocation = 0
        else:
            self.startLocation = int((self.outputSize / 2) / ((self.sampleFreq / 2) / self.freqStart))  #calculate start position in fft array
        self.fft.clearBuffer()  #clear previous data
        self.waterfall.resetAGC()   #reset AGC buffer
        self.audio.setParameters(self.sampleFreq, self.sampleSize)    #set audio buffer size

    def setMode(self):
        #calculate QRSS.1
        QRSSp1 = int(self.sampleFreq / (self.waterfall.width / 30))

        if (self.actionFull_Speed.isChecked()):
            self.sliderSpeed.setEnabled(False)
            self.bufferSize = int(QRSSp1)
            self.sampleSize = int(self.bufferSize)
            self.mode = ""
            self.minSpan = 3000
        if (self.actionQRSS3.isChecked()):
            self.sliderSpeed.setEnabled(True)
            self.bufferSize = int(QRSSp1 * 30)
            self.sampleSize = int(self.bufferSize  / self.wfSpeed)
            self.mode = "QRSS3"
            self.minSpan = 300
        if (self.actionQRSS10.isChecked()):
            self.sliderSpeed.setEnabled(True)
            self.bufferSize = int(QRSSp1 * 100)
            self.sampleSize = int(self.bufferSize  / self.wfSpeed)
            self.mode = "QRSS10"
            self.minSpan = 30
        if (self.actionQRSS20.isChecked()):
            self.sliderSpeed.setEnabled(True)
            self.bufferSize = int(QRSSp1 * 200)
            self.sampleSize = int(self.bufferSize  / self.wfSpeed)
            self.mode = "QRSS20"
            self.minSpan = 15
        if (self.actionQRSS30.isChecked()):
            self.sliderSpeed.setEnabled(True)
            self.bufferSize = int(QRSSp1 * 300)
            self.sampleSize = int(self.bufferSize  / self.wfSpeed)
            self.mode = "QRSS30"
            self.minSpan = 7
        if (self.actionQRSS60.isChecked()):
            self.sliderSpeed.setEnabled(True)
            self.bufferSize = int(QRSSp1 * 600)
            self.sampleSize = int(self.bufferSize  / self.wfSpeed)
            self.mode = "QRSS60"
            self.minSpan = 5
        if (self.actionQRSS120.isChecked()):
            self.sliderSpeed.setEnabled(True)
            self.bufferSize = int(QRSSp1 * 1200)
            self.sampleSize = int(self.bufferSize  / self.wfSpeed)
            self.mode = "QRSS120"
            self.minSpan = 2

        self.settings.set("minSpan", str(self.minSpan))
        self.settings.set("mode", self.mode)
        
        self.btnSetFrequency_callback()  #recalculate fft settings

    def speedChanged_callback(self):
        self.speedChanged = True

    def setFrequencyBox(self):  #fill frequency and span data boxes
        self.txtFrequencySpan.setText(str(self.freqSpan))
        self.txtCenterFrequency.setText(str(math.ceil(self.freqStart + (self.freqSpan / 2) - 0.5)))

    def audioCallback(self, in_data, status):
        if (status == 2):   #see if we have a buffer overrun
            self.fft.clearBuffer()  #clear corrupted data
            print("Buffer Overrun")
        self.fft.addData(numpy.frombuffer(in_data, dtype=numpy.int16))   #add audio data to fft
        self.newAudioData = True

    def menuSelectInput(self):
        self.devicesDialog.show(self.audio) #show device dialog

    def menuCaptureSettings(self):
        self.captureSettings.show()

    def waterfallUpdate(self):
        if (self.speedChanged == True): #see if need to update speed
            self.wfSpeed = 12 / (5 - self.sliderSpeed.value())    #calculate speed
            self.setMode()  #update speed
            self.speedChanged = False
        if (self.newAudioData == True):
            newData = self.fft.runFFT(self.outputSize, self.bufferSize, self.sampleSize)   #run the FFT
            if(len(newData) != 0):   #make sure the FFT returned data
                self.waterfall.addData(newData, self.startLocation, self.sliderBase.value(), self.sliderContrast.value(), self.cbAGC.isChecked()) #add fft data to waterfall
            self.newAudioData = False
            
    def updateWFText(self):
        self.wfText1 = "Roscoe QRSS Viewer V" + self.version + "    "
        self.wfText1 += str(datetime.now(timezone.utc).month) + "/"
        self.wfText1 += str(datetime.now(timezone.utc).day) + "/"
        self.wfText1 += str(datetime.now(timezone.utc).year) + "  "
        self.wfText1 += str("{:02d}".format(datetime.now(timezone.utc).hour)) + ":"
        self.wfText1 += str("{:02d}".format(datetime.now(timezone.utc).minute)) + ":"
        self.wfText1 += str("{:02d}".format(datetime.now(timezone.utc).second)) + " UTC    "
        self.wfText1 += self.mode
        self.wfText2 = self.notes

    def drawWaterfall(self):
        self.updateWFText() #get latest waterfall text
        self.lblImage.setPixmap(self.waterfall.getWaterfall(self.freqStart, self.freqSpan, self.cbInvert.isChecked(), self.freqOffset, self.wfText1, self.wfText2))  #update waterfall image
        self.pvSignal.setValue(int(self.fft.inputLevel)) #update input level bar
        self.lblGradient.setPixmap(self.waterfall.getGradient(self.sliderBase.value(), self.sliderContrast.value()))

        if (self.running == True):
            #see if need to start capture 1 timer
            if (self.cbCapture1.isChecked() == True):   #see if capture 1 enabled
                if (self.capture1Timer.isActive() == False): #see if timer is running
                    self.capture1Timer.start(self.captureSettings.getCaptureInterval(0) * 1000) #start capture timer
                    self.capture1LastInterval = self.captureSettings.getCaptureInterval(0) * 1000  #set last capture interval
                else:
                    if (self.capture1LastInterval != self.captureSettings.getCaptureInterval(0) * 1000): #see if interval changed
                        self.capture1Timer.stop()   #stop the timer
                        self.capture1Timer.start(self.captureSettings.getCaptureInterval(0) * 1000) #start capture timer with new interval
                        self.capture1LastInterval = self.captureSettings.getCaptureInterval(0) * 1000  #set last capture interval
            else:
                if (self.capture1Timer.isActive() == True): #see if timer is running
                    self.capture1Timer.stop()   #stop the timer
            
            #see if need to start capture 1 timer
            if (self.cbCapture2.isChecked() == True):   #see if capture 2 enabled
                if (self.capture2Timer.isActive() == False): #see if timer is running
                    self.capture2Timer.start(self.captureSettings.getCaptureInterval(1) * 1000) #start capture timer
                    self.capture2LastInterval = self.captureSettings.getCaptureInterval(1) * 1000  #set last capture interval
                else:
                    if (self.capture2LastInterval != self.captureSettings.getCaptureInterval(1) * 1000): #see if interval changed
                        self.capture2Timer.stop()   #stop the timer
                        self.capture2Timer.start(self.captureSettings.getCaptureInterval(1) * 1000) #start capture timer with new interval
                        self.capture2LastInterval = self.captureSettings.getCaptureInterval(1) * 1000  #set last capture interval
            else:
                if (self.capture2Timer.isActive() == True): #see if timer is running
                    self.capture2Timer.stop()   #stop the timer
        else:
            if (self.capture1Timer.isActive() == True): #see if timer is running
                self.capture1Timer.stop()   #stop the timer
            if (self.capture2Timer.isActive() == True): #see if timer is running
                self.capture2Timer.stop()   #stop the timer

