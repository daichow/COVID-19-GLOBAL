from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

from design import Ui_MainWindow
import qtmodern.styles
import qtmodern.windows
from covid_data import CovidData

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.covid = CovidData()
        self.covid.do_fuzzy_search("canada")
        self.covid.updateJSONData()
        self.covid.loadJSONData()
        self.covid.populate_variables()
        self.covid.populate_world_variables()

        self.searchStackSetup()
        
        # self.PushButton1.clicked.connect(self.OpenWindow1)
        # self.PushButton2.clicked.connect(self.OpenWindow2)

        # self.PushButton3.clicked.connect(self.GoToMain)
        # self.PushButton4.clicked.connect(self.OpenWindow2)

        # self.PushButton5.clicked.connect(self.GoToMain)
        # self.PushButton6.clicked.connect(self.OpenWindow1)


    # def OpenWindow1(self):
    #     self.QtStack.setCurrentIndex(1)

    # def OpenWindow2(self):
    #     self.QtStack.setCurrentIndex(2)

    # def GoToMain(self):
    #     self.QtStack.setCurrentIndex(0)
    def searchStackSetup(self):
        # movie = QtGui.QMovie("loa.gif")
        # self.appTitleLabel.setMovie(movie)
        # self.appTitleLabel.resize(100, 100)
        # movie.start()
        title = QtGui.QPixmap("title.jpg")
        self.appTitleLabel.setPixmap(title)

        self.totalWCasesLabel.setText("<h2>Global Cases: {}</h2>".format(self.covid.total_world_cases))
        self.totalWCasesLabel.setWordWrap(True)
        self.totalWCasesLabel.setTextFormat(QtCore.Qt.RichText)
        self.totalWCasesLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.totalWCasesLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.totalWCasesLabel.setLineWidth(1)
        self.totalWCasesLabel.setStyleSheet(
            "QLabel{background-color : #2A82DA;color:white;}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    showMain = Main()

    qtmodern.styles.dark(app)
    showMain = qtmodern.windows.ModernWindow(showMain)
    
    showMain.show()
    sys.exit(app.exec_())

    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())