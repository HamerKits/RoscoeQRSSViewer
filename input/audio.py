import pyaudio

FORMAT = pyaudio.paInt16
DEFAULT_RATE = 44100
DEFAULT_SIZE = 4096

class audio():
    def __init__(self):
        self.pAudio = pyaudio.PyAudio() #make audio
        self.sampleRate = DEFAULT_RATE    #set default sampleRate
        self.sampleSize = DEFAULT_SIZE    #set default sample size
        self.audioRunning = False

    def terminate(self):
        self.pAudio.terminate() #terminate audio class

    def callback(self, in_data, frame_count, time_info, status):
        self.mainWindowCallback(in_data, status)    #call callback
        return (None, pyaudio.paContinue)   #continue collecting data

    def getDeviceCount(self):
        self.info = self.pAudio.get_host_api_info_by_index(0)   #get device information
        return self.info.get('deviceCount') #get device count

    def getDeviceName(self, id):
        inputChannels = self.pAudio.get_device_info_by_host_api_device_index(0, id).get('maxInputChannels') #get number of input channels
        channelName = self.pAudio.get_device_info_by_host_api_device_index(0, id).get('name')   #get name of device
        if inputChannels > 0:   #make sure there are input channels
            return(str(id) + ": " + channelName )   ##return input channel name
        return "" #display error

    def setParameters(self, sampleRate, sampleSize):
        self.sampleRate = sampleRate
        self.sampleSize = sampleSize
        if (self.audioRunning == True):  #see if need to reset stream
            self.stopStream()  #stop the stream
            self.startStream(self.device, self.mainWindowCallback)    #restart the stream

    def startStream(self, device, callback):
        self.mainWindowCallback = callback  #set callback
        self.device = device
        self.stream = self.pAudio.open(format=FORMAT, channels=1, rate=self.sampleRate, input=True, frames_per_buffer=self.sampleSize, stream_callback=self.callback, input_device_index=(int(device)))  #open audio
        self.stream.start_stream()  #start stream
        self.audioRunning = True

    def stopStream(self):
        self.stream.close() #close stream
        self.audioRunning = False