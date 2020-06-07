from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
import pycountry

from design import Ui_MainWindow
import qtmodern.styles
import qtmodern.windows
from covid_data import CovidData

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.center()
        
        self.covid = CovidData()
        self.covid.loadJSONData()
        self.covid.do_fuzzy_search(pycountry.countries.get(alpha_3=list(self.covid.data.keys())[0]).name.lower())
        # self.covid.updateJSONData()
        

        self.searchStackSetup()

        self.searchButton.clicked.connect(self.OpenWindow1)
        # self.PushButton2.clicked.connect(self.OpenWindow2)

        # self.PushButton3.clicked.connect(self.GoToMain)
        # self.PushButton4.clicked.connect(self.OpenWindow2)

        # self.PushButton5.clicked.connect(self.GoToMain)
        # self.PushButton6.clicked.connect(self.OpenWindow1)


    def OpenWindow1(self):

        self.covid.do_fuzzy_search(self.searchBar.text().lower())
        self.covid.updateJSONData()
        self.covid.loadJSONData()

        self.countryStackSetup()

        self.stackedWidget.setCurrentIndex(1)

    # def OpenWindow2(self):
    #     self.QtStack.setCurrentIndex(2)

    # def GoToMain(self):
    #     self.QtStack.setCurrentIndex(0)
    def searchStackSetup(self):
        # movie = QtGui.QMovie("loa.gif")
        # self.appTitleLabel.setMovie(movie)
        # self.appTitleLabel.resize(100, 100)
        # movie.start()
        self.covid.populate_world_variables()

        # title = QtGui.QPixmap("title.jpg")
        # self.appTitleLabel.setPixmap(title)
        self.appTitleLabel.setText("<img src = 'title.jpg'></img>")
        # self.appTitleLabel.setText("<h1>Covid-19 Global</h1>")
        self.appTitleLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.appDescriptionLabel.setText("""<h1>Today's Global Covid-19 Status</h1>""")
        self.appDescriptionLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.totalWCasesLabel.setText(
            "<h2 style='color:#2A82DA;'>Total Global Cases</h2> <h1 style ='color:lightgrey;'>{}</h1>".format(
                self.group(self.covid.total_world_cases)))
        self.totalWCasesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalWCasesLabel.setWordWrap(True)
        self.totalWCasesLabel.setTextFormat(QtCore.Qt.RichText)
        self.totalWCasesLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.totalWCasesLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.totalWCasesLabel.setLineWidth(1)
        # self.totalWCasesLabel.setStyleSheet(
        #     "QLabel{color : #2A82DA;}")

        self.newWCasesLabel.setText(
            "<h2 style='color:#2A82DA;'>New Global Cases</h2> <h1 style ='color:lightgrey;'>{}</h1>".format(self.group(self.covid.new_world_cases)))
        self.newWCasesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newWCasesLabel.setWordWrap(True)
        self.newWCasesLabel.setTextFormat(QtCore.Qt.RichText)
        self.newWCasesLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.newWCasesLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.newWCasesLabel.setLineWidth(1)
        # self.newWCasesLabel.setStyleSheet(
        #     "QLabel{color : #2A82DA;}")
        
        self.totalWDeathsLabel.setText(
            "<h2 style='color:#2A82DA;'>Total Global Deaths</h2> <h1 style ='color:lightgrey;'>{}</h1>".format(self.group(self.covid.total_world_deaths)))
        self.totalWDeathsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalWDeathsLabel.setWordWrap(True)
        self.totalWDeathsLabel.setTextFormat(QtCore.Qt.RichText)
        self.totalWDeathsLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.totalWDeathsLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.totalWDeathsLabel.setLineWidth(1)
        # self.totalWDeathsLabel.setStyleSheet(
        #     "QLabel{color : #2A82DA;}")

        self.newWDeathsLabel.setText(
            "<h2 style='color:#2A82DA;'>New Global Deaths</h2> <h1 style ='color:lightgrey;'>{}</h1>".format(self.group(self.covid.new_world_deaths)))
        self.newWDeathsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newWDeathsLabel.setWordWrap(True)
        self.newWDeathsLabel.setTextFormat(QtCore.Qt.RichText)
        self.newWDeathsLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.newWDeathsLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.newWDeathsLabel.setLineWidth(1)
        # self.newWDeathsLabel.setStyleSheet(
        #     "QLabel{color : #2A82DA;}")

    def countryStackSetup(self):
        self.covid.populate_variables()

        self.covidFactsLabel.setText("<br><br><h1 style='color:#2A82DA;'>Current Covid-19 Facts</h1>")
        self.covidFactsLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.totalCasesLabel.setText("<h3>Total Cases: {}</h3>".format(self.group(self.covid.total_cases[-1])))
        self.totalCasesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalCasesLabel.setStyleSheet("QLabel::hover{background-color : #2A82DA;}")
        self.totalCasesLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.newCasesLabel.setText("<h3>New Cases: {}</h3>".format(self.group(self.covid.new_cases[-1])))
        self.newCasesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newCasesLabel.setStyleSheet("QLabel::hover{background-color : #2A82DA;}")
        self.newCasesLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.totalDeathsLabel.setText("<h3>Total Deaths: {}</h3>".format(self.group(self.covid.total_deaths[-1])))
        self.totalDeathsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalDeathsLabel.setStyleSheet("QLabel::hover{background-color : #2A82DA;}")
        self.totalDeathsLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.newDeathsLabel.setText("<h3>New Deaths: {}</h3>".format(self.group(self.covid.new_deaths[-1])))
        self.newDeathsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newDeathsLabel.setStyleSheet("QLabel::hover{background-color : #2A82DA;}")
        self.newDeathsLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        ###################################################################################
        self.locationLabel.setText(
            "<br><br><h1 style='color:#2A82DA;'>{}, {}</h1>".format(self.covid.location.title(), self.covid.continent.title()))
        self.locationLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.flagLabel.setText("<img src = '{}.png'></img>".format(self.covid.location.lower().replace(" ", "-")))
        self.flagLabel.setAlignment(QtCore.Qt.AlignCenter)
        ###################################################################################
        self.healthFactsLabel.setText("<br><br><h1 style='color:#2A82DA;'>Current Health Facts</h1>")
        self.healthFactsLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.cvdDeathRateLabel.setText("<h3>Cardiovascular Death Rate: {}</h3>".format(self.covid.cvd_death_rate))
        self.cvdDeathRateLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.diabetesLabel.setText("<h3>Diabetes Prevalence in Population: {}%</h3>".format(self.covid.diabetes_prevalence))
        self.diabetesLabel.setAlignment(QtCore.Qt.AlignCenter)

        # self.handWashFacLabel.setText("<h3>Population with Access to Handwashing Facilites: {}</h3>".format(self.covid.handwashing_facilities))
        # self.handWashFacLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.hospitalBedsLabel.setText("<h3>Hospital Beds Per Thousands: {}</h3>".format(self.covid.hospital_beds_per_thousand))
        self.hospitalBedsLabel.setAlignment(QtCore.Qt.AlignCenter)
        ###################################################################################
        self.demographicsLabel.setText("<br><br><h1 style='color:#2A82DA;'>Current Country Demographics</h1>")
        self.demographicsLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.popLabel.setText("<h3>Population: {}</h3>".format(self.group(self.covid.population)))
        self.popLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.popDensityLabel.setText("<h3>Population Density: {} sqkm</h3>".format(self.group(self.covid.population_density)))
        self.popDensityLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.ageLabel.setText("<h3>Population Aged 65 Plus: {}%</h3>".format(self.covid.aged_65_older))
        self.ageLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.gdpLabel.setText("<h3>GDP Per Capita: {}</h3>".format(self.group(self.covid.gdp_per_capita)))
        self.gdpLabel.setAlignment(QtCore.Qt.AlignCenter)

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()
        # center point of screen
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    def group(self, number):
        s = '%d' % number
        groups = []
        while s and s[-1].isdigit():
            groups.append(s[-3:])
            s = s[:-3]
        return s + ','.join(reversed(groups))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    showMain = Main()

    qtmodern.styles.dark(app)
    showMain = qtmodern.windows.ModernWindow(showMain)

    # sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
    # w = int(sizeObject.width()/2)
    # h = int(sizeObject.height())
    # showMain.resize(w, h)
    
    showMain.show()
    sys.exit(app.exec_())

    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())