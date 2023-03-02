#Author: John Hamer
#Copyright: 2023
#License: MIT License - See LICENSE.md

import numpy
import time
from PySide2.QtCore import QThread

class fft():
    def __init__(self):
        self.bf = 0 #placeholder
        self.buffer = numpy.array([], dtype=numpy.int16)    #make empty buffer
        self.inputLevel = 0 #input level from audio
        self.bufferCleared = True
        self.fftCallTime = 0

    def clearBuffer(self):
        self.buffer = numpy.array([], dtype=numpy.int16)    #make empty buffer
        self.bufferCleared = True

    def addData(self, data : numpy.ndarray):    #add audio data to buffer
        self.buffer = numpy.append(self.buffer, data)  #append data to buffer
        self.inputLevel = numpy.amax(data / 255)

    def checkOutputSize(self, outputSize, bufferSize):   #returns output size appropriate for runFFT
        if (outputSize < bufferSize):   #see if outputSize is less than sample size
            return outputSize   #no issue, return outputSize
        scale = int(outputSize / bufferSize)   #determine scale
        bufferSize = int(outputSize / scale) #calculate bufferSize
        if ((bufferSize % 2) != 0):
            bufferSize += 1 #make sure buffersize is even
        return bufferSize * scale   #adjust for FFT

    def runFFT(self, outputSize, bufferSize, sampleSize): #callback with data
        if(len(self.buffer) == 0):
            return numpy.array([], dtype=numpy.int16)
        elif(len(self.buffer) >= bufferSize):
            data = self.buffer[0:bufferSize].copy()    #fill buffer to data
            self.buffer = self.buffer[(len(self.buffer) - (bufferSize - sampleSize)):]   #remove old data
        else:
            data = self.buffer[0:].copy()  #copy buffer to data
            data.resize(bufferSize)

        resize = 0

        if (outputSize < len(data)):
            scale = int(len(data) / outputSize)
            data.resize(int(outputSize * scale))  #resize the buffer for proper frequency display with minimal data loss
            resize = 1
        elif (outputSize > len(data)):
            scale = int(outputSize / len(data))
            data.resize(int(outputSize / scale))  #resize the buffer for proper frequency display with minimal data loss
            resize = 2

        self.fft = numpy.fft.fft(data) / len(data)     # Normalize amplitude

        self.fft = self.fft[range(int(len(self.fft) / 2))] # Exclude sampling frequency
        self.fft = numpy.hanning(len(self.fft))*self.fft
        self.fft = numpy.abs(self.fft)  #get amplitude

        if (resize == 1):   #see if need to average the data to output size
            self.fft = numpy.resize(self.fft,[int(outputSize / 2), int(scale)])    #break into rows
            self.fft = self.fft.swapaxes(0,1)
            self.fft = numpy.mean(self.fft.reshape(int(scale), -1), axis=0)  #average data into outputSize
        elif (resize == 2): #see if need to expand the data to output size
            self.fft = numpy.resize(self.fft, [int(scale), int(len(self.fft))])
            self.fft = self.fft.swapaxes(0,1)
            self.fft = self.fft.reshape(int(outputSize / 2))

            #smooth the data since it is blocky
            smoothFactor = scale * 2
            kernel = numpy.ones(smoothFactor) / smoothFactor
            self.fft = numpy.convolve(self.fft, kernel, mode='same')

        return self.fft