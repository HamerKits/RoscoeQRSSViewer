#Author: John Hamer
#Copyright: 2023
#License: MIT License - See LICENSE.md

import numpy
from PySide2.QtGui import QPixmap, QPainter, qRgb, QImage, QFont
from PySide2.QtCore import Qt

class waterfall():
    def __init__(self, width, height):
        self.updateImageSize(width, height) #update size variables
        self.waterfallUpdated = False
        self.agcRunning = False
        self.average = numpy.array([], dtype=numpy.uint16)    #make empty buffer
        self.AGCInc = 0.00001

    def makeGradient(self, array):
        retVal = numpy.array([[],[],[]])
        for x in array:
            if (x <= 85):
                r = 0
                g = 0
                b = x * (128 / 85)
            elif (x <= 170):
                x -= 85
                r = x * (255 / 85)
                g = 0
                b = 128 - (x * (128 / 85))
            else:
                x -= 170
                r = 255
                g = x * (255 / 85)
                b = x * (255 / 85)
            retVal = numpy.append(retVal, [[r],[g],[b]], axis=1)
        return retVal

    def updateImageSize(self, width, height):   #update array size
        self.width = width  #set width
        self.height = height    #set height
        self.wfFreqWidth = 150  #set frequency label width
        self.wfWidth = self.width - self.wfFreqWidth    #calculate waterfall width
        self.wfDataWidth = self.wfWidth * 3 #calculate data width
        self.wfFreqDataWidth = self.wfFreqWidth * 3 #calculate data width
        self.wfArrayWidth = self.wfDataWidth + self.wfFreqDataWidth #calculate array width
        self.waterfall = numpy.zeros((self.height + 12, self.wfArrayWidth), dtype=numpy.uint8)  #make array for image
        self.waterfallOutput = numpy.zeros((self.height + 60, self.wfArrayWidth), dtype=numpy.uint8)  #make array for image

    def updateFrequency(self, freqStart, freqSpan): #update calculations for drawing frequency bar
        #calculate frequency bar parameters
        multiplier = 1  #set default multiplier
        if (freqSpan < 10):  #see if need multiplier
            multiplier = 10 #add a decimal point
        freqSpan *= multiplier  #incorperate multiplier
        majorCount = self.height / 40    #use major count every 40 pixels as starting point
        self.frequencyStep = int((freqSpan / majorCount)  + 0.5)   #get starting frequency count
        majorCountCorrected = freqSpan / self.frequencyStep    #recalculate major count
        self.majorStepSize = ((majorCount / majorCountCorrected) * self.height) / majorCount   #calculate major step size
        self.minorStepSize = self.majorStepSize / 10    #10 minor steps between major steps
        self.startFrequency = freqStart #store start frequency
        self.frequencyStep /= multiplier

    def resetAGC(self):
        self.agcRunning = False

    def addData(self, data, start, base, contrast, AGC): #callback with data
        data = data[start:(start + self.height)]
        
        #AGC
        correction = numpy.amax(data) / 65535   #calculate correction factor for 0 to 65535
        if (correction == 0):
            correction = 1
        
        if (self.agcRunning == False):
            self.AGC = correction   #set correction
            self.agcRunning = True
        else:
            self.AGC = ((self.AGC * 0.90) + (correction * 0.10))   #average agc correction

        if (AGC == True):
            data = data / self.AGC    #apply slow agc
        else:
            data = data / correction    #apply fast agc
            self.agcRunning = False     #reset slow AGC

        data -= base * 655.35 #base adjust
        data[data < 0] = 0  #clamp data at 0

        correction2 = numpy.amax(data) / 255   #calculate correction factor for 0 to 254
        if (correction2 == 0):
            correction2 = 1

        data = data / (correction2 * (contrast / 100))    #contrast adjust up to gain of 10

        data[data > 255] = 255  #clamp at 255 

        if (len(self.average) != len(data)):
            self.average = numpy.uint16(data)   #set initial array
        else:
            self.average += numpy.uint16(data)  #add data to average
            self.average = numpy.uint16(self.average / 2)   #take average
        data = numpy.uint8(self.average)    #set data to average"""

        data = numpy.uint8(self.makeGradient(data))
        data = numpy.swapaxes(data, 0, 1)   #convert to RGB888 dimentional array on y axis

        self.waterfall[6:self.height + 6, :self.wfDataWidth - 3] = self.waterfall[6:self.height + 6, 3:self.wfDataWidth] #shift data to the left by 3
        self.waterfall[6:self.height + 6, self.wfDataWidth - 3:self.wfDataWidth] = data #add new data to last line

        self.waterfallUpdated = True

    def getGradient(self, base, contrast):
        gradient = numpy.zeros((100), dtype=numpy.uint8)  #make array for image

        start = (base / 100) * 100  #calculate gradient start point
        end = start + ((100 - start) * (((contrast / 100) * 100) / 100))    #calculate gradient end point

        for x in range(100):    #make gradient array
            if (x <= int(start)):
                gradient[x] = 0
            elif (x <= int(end)):
                gradient[x] = int((x - start) / (end - start) * 255)
            else:
                gradient[x] = 255

        gradient = numpy.uint8(self.makeGradient(gradient)) #convert to RGB with palette
        gradient = numpy.swapaxes(gradient, 0, 1)   #convert to RGB888 dimentional array on y axis
        gradient = numpy.reshape(gradient,[1,300])  #convert to one line of RGB
        gradient = numpy.resize(gradient,[20, 300]) #add some height

        return QPixmap.fromImage(QImage(gradient, 100, 20, QImage.Format_RGB888))    #convert gradient data to image

    def saveWaterfall(self, path):
        self.wfImgOut.save(path)    #save the image

    def getWaterfall(self, freqStart, freqSpan, invert, offset, wfText1, wfText2): #returns waterfall image with labels
        #make waterfall from data
        wf = self.waterfall.copy()
        wfImg = QImage(wf, self.width, self.height + 12, QImage.Format_RGB888)    #convert wf data to image

        if (invert == False):   #image inverted naturally
            wfImg = wfImg.mirrored(vertical=True)

        #update calculations for drwaing frequency bar
        self.updateFrequency(freqStart, freqSpan)   #temporary location for testing

        #draw frequencie bar
        qp = QPainter(wfImg)
        qp.setBrush(Qt.NoBrush) #set brush to single pixel line
        qp.setPen(Qt.white) #set brush color
        qp.setFont(QFont("lato", 12))

        #draw frequency bar divider
        qp.drawLine(self.wfWidth, 6, self.wfWidth, self.height + 6) #draw vertical line

        #draw majors
        freqText = self.startFrequency + offset
        
        if (invert == True):
            majorStep = 6
            minorStep = 6
            while ((majorStep <= self.height + 6) or (minorStep <= self.height + 6)):
                while (int(minorStep) < int(majorStep)):
                    qp.drawLine(self.wfWidth, int(minorStep), self.wfWidth + 5, int(minorStep))  #draw minor line
                    minorStep += self.minorStepSize  #increment minor step
                qp.drawLine(self.wfWidth, int(majorStep), self.wfWidth + 10, int(majorStep))  #draw major line
                qp.drawText(self.wfWidth + 12, int(majorStep) + 6, str(round(freqText, 2)) + "Hz")   #draw frequency
                majorStep += self.majorStepSize  #increment step
                minorStep += self.minorStepSize  #increment minor step
                freqText += self.frequencyStep    #increment frequency
        else:
            majorStep = self.height + 6
            minorStep = self.height + 6
            while ((majorStep > 6) or (minorStep > 6)):
                while (int(minorStep) > int(majorStep)):
                    qp.drawLine(self.wfWidth, int(minorStep), self.wfWidth + 5, int(minorStep))  #draw minor line
                    minorStep -= self.minorStepSize  #increment minor step
                qp.drawLine(self.wfWidth, int(majorStep), self.wfWidth + 10, int(majorStep))  #draw major line
                qp.drawText(self.wfWidth + 12, int(majorStep) + 6, str(round(freqText, 2)) + "Hz")   #draw frequency
                majorStep -= self.majorStepSize  #increment step
                minorStep -= self.minorStepSize  #increment minor step
                freqText += self.frequencyStep    #increment frequency
        qp.end()

        self.waterfallOutput = numpy.zeros((self.height + 60, self.wfArrayWidth), dtype=numpy.uint8)  #clear waterfall array for image
        self.wfImgOut = QImage(self.waterfallOutput, self.width, self.height + 60, QImage.Format_RGB888)    #convert wf data to image
        qp2 = QPainter(self.wfImgOut)
        qp2.setBrush(Qt.NoBrush) #set brush to single pixel line
        qp2.setPen(Qt.white) #set brush color
        qp2.setFont(QFont("lato", 12))

        #add waterfall to output image
        qp2.drawImage(0, 40, wfImg)

        #draw border
        qp2.drawRect(0,0,self.width - 1, self.height + 59)

        #draw text
        qp2.drawText(30,18,wfText1)
        qp2.drawText(30,38,wfText2)

        qp2.end()
        return QPixmap.fromImage(self.wfImgOut)    #return image

    def updated(self):
        if (self.waterfallUpdated == True):
            self.waterfallUpdated = False   #reset update flag
            return True
        return False