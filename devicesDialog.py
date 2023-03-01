from PySide2 import QtWidgets
import ui.devicesDialog_ui
import input.audio

class form(QtWidgets.QDialog, ui.devicesDialog_ui.Ui_Dialog):
    def __init__(self):
        super(form, self).__init__()
        self.setupUi(self)  #setup user interface
        self.currentDevice = 0  #set default device
        self.buttonBox.accepted.connect(self.btnOk_callback)

    def show(self, audio: input.audio.audio):
        self.lstDevices.clear()
        for i in range (0, audio.getDeviceCount()):
            devName = audio.getDeviceName(i)
            if (devName != ""):
                self.lstDevices.addItem(devName)
        self.lstDevices.setCurrentRow(self.currentDevice)
        super(form, self).show()    #show dialog
        self.activateWindow() #make sure window shows right away

    def btnOk_callback(self):
        self.currentDevice = self.lstDevices.currentRow()

    def getCurrentDevice(self):
        return self.currentDevice
