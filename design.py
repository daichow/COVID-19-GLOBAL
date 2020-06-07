# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        ####################################################################
        # SETTING UP MAIN WINDOW
        ####################################################################
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(534, 363)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vLayoutCentral = QtWidgets.QVBoxLayout(self.centralwidget)
        self.vLayoutCentral.setObjectName("vLayoutCentral")
        ####################################################################
        # SETS UP A STACKED WIDGET INTERFACE
        ####################################################################
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        ####################################################################
        self.searchStack()
        ####################################################################
        self.countryStack()
        ####################################################################
        self.graphStack()
        ###################################################################
        self.vLayoutCentral.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        ####################################################################
        # FINALIZING MAIN WINDOW
        ####################################################################
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Covid19 Global"))

    def searchStack(self):
        self.mainScreenStack = QtWidgets.QWidget()
        self.mainScreenStack.setObjectName("mainScreenStack")
        self.vLayoutMainStack = QtWidgets.QVBoxLayout(self.mainScreenStack)
        self.vLayoutMainStack.setObjectName("vLayoutMainStack")

        self.appTitleLabel = QtWidgets.QLabel(self.mainScreenStack)
        self.appTitleLabel.setObjectName("label")
        self.vLayoutMainStack.addWidget(self.appTitleLabel)
        # self.appTitleLabel.setText("<h1 style='color:red;'><center>Covid19 Global</h1>")

        ####################################################################
        self.gridLayoutGlobData = QtWidgets.QGridLayout()
        self.gridLayoutGlobData.setObjectName("gridLayoutGlobData")

        self.totalWCasesLabel = QtWidgets.QLabel(self.mainScreenStack)
        self.totalWCasesLabel.setObjectName("totalWCasesLabel")
        self.gridLayoutGlobData.addWidget(self.totalWCasesLabel, 0, 0, 1, 1)

        self.newWCasesLabel = QtWidgets.QLabel(self.mainScreenStack)
        self.newWCasesLabel.setObjectName("newWCasesLabel")
        self.gridLayoutGlobData.addWidget(self.newWCasesLabel, 0, 1, 1, 1)

        self.totalWDeathsLabel = QtWidgets.QLabel(self.mainScreenStack)
        self.totalWDeathsLabel.setObjectName("totalWDeathsLabel")
        self.gridLayoutGlobData.addWidget(self.totalWDeathsLabel, 1, 0, 1, 1)

        self.newWDeathsLabel = QtWidgets.QLabel(self.mainScreenStack)
        self.newWDeathsLabel.setObjectName("newWDeathsLabel")
        self.gridLayoutGlobData.addWidget(self.newWDeathsLabel, 1, 1, 1, 1)

        self.vLayoutMainStack.addLayout(self.gridLayoutGlobData)
        ####################################################################
        self.hLayoutSearch = QtWidgets.QHBoxLayout()
        self.hLayoutSearch.setObjectName("hLayoutSearch")

        self.searchBar = QtWidgets.QLineEdit(self.mainScreenStack)
        self.searchBar.setObjectName("searchBar")
        self.hLayoutSearch.addWidget(self.searchBar)

        self.searchButton = QtWidgets.QPushButton(self.mainScreenStack)
        self.searchButton.setObjectName("searchButton")
        self.hLayoutSearch.addWidget(self.searchButton)

        self.vLayoutMainStack.addLayout(self.hLayoutSearch)
        ####################################################################

        self.stackedWidget.addWidget(self.mainScreenStack)


    def countryStack(self):
        self.countryScreenStack = QtWidgets.QWidget()
        self.countryScreenStack.setObjectName("countryScreenStack")
        ####################################################################
        self.gLayoutCountryStack = QtWidgets.QGridLayout(self.countryScreenStack)
        self.gLayoutCountryStack.setObjectName("gLayoutCountryStack")
        ####################################################################
        self.vLayoutPanel4 = QtWidgets.QVBoxLayout()
        self.vLayoutPanel4.setObjectName("vLayoutPanel4")

        self.demographicsLabel = QtWidgets.QLabel(self.countryScreenStack)
        self.demographicsLabel.setObjectName("demographicsLabel")
        self.vLayoutPanel4.addWidget(self.demographicsLabel)

        self.popLabel = QtWidgets.QLabel(self.countryScreenStack)
        self.popLabel.setObjectName("popLabel")
        self.vLayoutPanel4.addWidget(self.popLabel)

        self.popDensityLabel = QtWidgets.QLabel(self.countryScreenStack)
        self.popDensityLabel.setObjectName("popDensityLabel")
        self.vLayoutPanel4.addWidget(self.popDensityLabel)

        self.ageLabel = QtWidgets.QLabel(self.countryScreenStack)
        self.ageLabel.setObjectName("ageLabel")
        self.vLayoutPanel4.addWidget(self.ageLabel)

        self.gdpLabel = QtWidgets.QLabel(self.countryScreenStack)
        self.gdpLabel.setObjectName("gdpLabel")
        self.vLayoutPanel4.addWidget(self.gdpLabel)

        self.gLayoutCountryStack.addLayout(self.vLayoutPanel4, 1, 1, 1, 1)
        ####################################################################
        self.vLayoutPanel3 = QtWidgets.QVBoxLayout()
        self.vLayoutPanel3.setObjectName("vLayoutPanel3")

        self.healthFactsLabel = QtWidgets.QLabel(self.countryScreenStack)
        self.healthFactsLabel.setObjectName("healthFactsLabel")
        self.vLayoutPanel3.addWidget(self.healthFactsLabel)

        self.cvdDeathRateLabel = QtWidgets.QLabel(self.countryScreenStack)
        self.cvdDeathRateLabel.setObjectName("cvdDeathRateLabel")
        self.vLayoutPanel3.addWidget(self.cvdDeathRateLabel)

        self.diabetesLabel = QtWidgets.QLabel(self.countryScreenStack)
        self.diabetesLabel.setObjectName("diabetesLabel")
        self.vLayoutPanel3.addWidget(self.diabetesLabel)

        self.handWashFacLabel = QtWidgets.QLabel(self.countryScreenStack)
        self.handWashFacLabel.setObjectName("handWashFacLabel")
        self.vLayoutPanel3.addWidget(self.handWashFacLabel)

        self.hospitalBedsLabel = QtWidgets.QLabel(self.countryScreenStack)
        self.hospitalBedsLabel.setObjectName("hospitalBedsLabel")
        self.vLayoutPanel3.addWidget(self.hospitalBedsLabel)

        self.gLayoutCountryStack.addLayout(self.vLayoutPanel3, 1, 0, 1, 1)
        ####################################################################
        self.vLayoutPanel2 = QtWidgets.QVBoxLayout()
        self.vLayoutPanel2.setObjectName("vLayoutPanel2")

        self.locationLabel = QtWidgets.QLabel(self.countryScreenStack)
        self.locationLabel.setObjectName("locationLabel")
        self.vLayoutPanel2.addWidget(self.locationLabel)

        self.flagLabel = QtWidgets.QLabel(self.countryScreenStack)
        self.flagLabel.setObjectName("flagLabel")
        self.vLayoutPanel2.addWidget(self.flagLabel)

        self.gLayoutCountryStack.addLayout(self.vLayoutPanel2, 0, 1, 1, 1)
        ####################################################################
        self.vLayoutPanel1 = QtWidgets.QVBoxLayout()
        self.vLayoutPanel1.setObjectName("vLayoutPanel1")

        self.covidFactsLabel = QtWidgets.QLabel(self.countryScreenStack)
        self.covidFactsLabel.setObjectName("covidFactsLabel")
        self.vLayoutPanel1.addWidget(self.covidFactsLabel)

        self.totalCasesLabel = QtWidgets.QLabel(self.countryScreenStack)
        self.totalCasesLabel.setObjectName("totalCasesLabel")
        self.vLayoutPanel1.addWidget(self.totalCasesLabel)

        self.newCasesLabel = QtWidgets.QLabel(self.countryScreenStack)
        self.newCasesLabel.setObjectName("newCasesLabel")
        self.vLayoutPanel1.addWidget(self.newCasesLabel)

        self.totalDeathsLabel = QtWidgets.QLabel(self.countryScreenStack)
        self.totalDeathsLabel.setObjectName("totalDeathsLabel")
        self.vLayoutPanel1.addWidget(self.totalDeathsLabel)

        self.newDeathsLabel = QtWidgets.QLabel(self.countryScreenStack)
        self.newDeathsLabel.setObjectName("newDeathsLabel")
        self.vLayoutPanel1.addWidget(self.newDeathsLabel)

        self.gLayoutCountryStack.addLayout(self.vLayoutPanel1, 0, 0, 1, 1)
        ####################################################################
        self.levelOfConcernLabel = QtWidgets.QLabel(self.countryScreenStack)
        self.levelOfConcernLabel.setObjectName("levelOfConcernLabel")
        self.gLayoutCountryStack.addWidget(self.levelOfConcernLabel, 2, 0, 1, 1)
        ####################################################################
        self.stackedWidget.addWidget(self.countryScreenStack)

    def graphStack(self):
        self.graphScreenStack = QtWidgets.QWidget()
        self.graphScreenStack.setObjectName("graphScreenStack")
        self.vLayoutScreenStack = QtWidgets.QVBoxLayout(self.graphScreenStack)
        self.vLayoutScreenStack.setObjectName("vLayoutScreenStack")
        self.stackedWidget.addWidget(self.graphScreenStack)

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
