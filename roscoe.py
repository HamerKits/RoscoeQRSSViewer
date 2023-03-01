import sys
from PySide2.QtWidgets import QApplication
import mainWindow

def main():
    app = QApplication(sys.argv)    #make an app
    
    print("loading modules")

    window = mainWindow.form()  #main window
    window.show()   #show main window

    ret = app.exec_()  #start app
    sys.exit(ret)   #return app state

if __name__ == '__main__':
    main()