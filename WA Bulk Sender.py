from random import randint
from typing import Text, Type
from PyQt5 import QtCore, QtGui, QtWidgets
import LoadFile
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException, NoAlertPresentException
from time import sleep
from urllib.parse import quote
from sys import platform

class Thread(QtCore.QThread):
    single = QtCore.pyqtSignal(int)
    
    def __init__(self, ):
        super(Thread,self).__init__()
    
    def __del__(self,):
        self.wait()
    
    def run(self):
        count = 0
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 511)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(300, 300))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleFrame = QtWidgets.QFrame(self.centralwidget)
        self.titleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleFrame.setObjectName("titleFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.titleFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.titleFrame)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.titleFrame)
        self.MainWindow_2 = QtWidgets.QFrame(self.centralwidget)
        self.MainWindow_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainWindow_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainWindow_2.setObjectName("MainWindow_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MainWindow_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pathBox = QtWidgets.QLineEdit(self.MainWindow_2)
        self.pathBox.setText("")
        self.pathBox.setFrame(True)
        self.pathBox.setDragEnabled(True)
        self.pathBox.setClearButtonEnabled(False)
        self.pathBox.setObjectName("pathBox")
        self.horizontalLayout.addWidget(self.pathBox)
        self.browseBtn = QtWidgets.QPushButton(self.MainWindow_2)
        self.browseBtn.setObjectName("browseBtn")
        self.horizontalLayout.addWidget(self.browseBtn)
        self.verticalLayout.addWidget(self.MainWindow_2)
        self.control = QtWidgets.QFrame(self.centralwidget)
        self.control.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.control.setFrameShadow(QtWidgets.QFrame.Raised)
        self.control.setObjectName("control")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.control)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.loadBtn = QtWidgets.QPushButton(self.control)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.loadBtn.setFont(font)
        self.loadBtn.setObjectName("loadBtn")
        self.horizontalLayout_3.addWidget(self.loadBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        # self.delayLabel = QtWidgets.QLabel('Time Delay')
        # self.horizontalLayout_3.addWidget(self.delayLabel)
        # self.timeDelay = QtWidgets.QSpinBox(self.control)
        # self.timeDelay.setValue(30)
        # self.horizontalLayout_3.addWidget(self.timeDelay)
        self.verticalLayout.addWidget(self.control)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.sendbtn = QtWidgets.QPushButton(self.centralwidget)
        self.sendbtn.setObjectName("sendbtn")
        self.verticalLayout.addWidget(self.sendbtn)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.reportbtn = QtWidgets.QPushButton(self.centralwidget)
        self.reportbtn.setObjectName("reportbtn")
        self.verticalLayout.addWidget(self.reportbtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 27))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.menuMenu.addAction(self.actionexit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # init variables
        self.filePath = ''
        
        # Connecting buttons
        self.browseBtn.clicked.connect(self.loadPath)
        self.loadBtn.clicked.connect(self.loadFile)
        self.sendbtn.clicked.connect(self.sendMessage)
        # self.sendbtn.clicked.connect(self.testfun)
        self.reportbtn.clicked.connect(self.savefile)


    def testfun(self):
        text = self.plainTextEdit.toPlainText()
        print(text)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WhatsApp Message Sender"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">WA Bulk Message Sender</span></p></body></html>"))
        # self.delayLabel.setText(_translate("MainWindow", "Time Delay(Sec) "))
        self.browseBtn.setText(_translate("MainWindow", "Browse"))
        self.loadBtn.setText(_translate("MainWindow", "Load Numbers"))
        self.label_2.setText(_translate("MainWindow", "Enter Message"))
        self.sendbtn.setText(_translate("MainWindow", "Send Messages"))
        self.reportbtn.setText(_translate("MainWindow", "Genrate Report"))
        self.label_3.setText(_translate("MainWindow", "Result"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionexit.setText(_translate("MainWindow", "Exit"))
    
    def loadPath(self):
        # try:
        
        self.filePath, _ = QtWidgets.QFileDialog.getOpenFileName(caption='Mobile Number File',directory='./', filter='*.csv')
        self.pathBox.setText(self.filePath)
        # except AttributeError as e:
        #     print(e)

    def savefile(self):
        import xlwt
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(caption='Save File', directory='./', filter=".xls(*.xls)")   
        print(filename)
        try:
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            self.add2(sheet)
            wbk.save(filename)
        except TypeError as e:
            print(e)

    def add2(self, sheet):
        for currentColumn in range(self.tableView.columnCount()):
            for currentRow in range(self.tableView.rowCount()):
                try:
                    teext = str(self.tableView.item(currentRow, currentColumn).text())
                    sheet.write(currentRow, currentColumn, teext)
                except AttributeError:
                    pass

    def loadFile(self):
        try:
            self.numbersList = LoadFile.CSVloadNumbers(self.filePath)
            header = []

            self.tableView.edit
            self.tableView.setColumnCount(3)
            self.tableView.setColumnWidth(0,200)
            self.tableView.setColumnWidth(1,200)
            self.tableView.setRowCount(len(self.numbersList['Mobile Number']))

            for n, key in enumerate(sorted(self.numbersList.keys())):
                header.append(key)
                for m, item in enumerate(self.numbersList[key]):
                    self.tableView.setItem(m,n,QtWidgets.QTableWidgetItem(item))

            self.tableView.setHorizontalHeaderLabels(header)
            self.tableView.resizeColumnsToContents()
            self.tableView.resizeRowsToContents()
            self.tableView.show()
        except TypeError as e:
            print(e)

    def sendMessage(self):
        import random, time
        option = Options()
        # option.add_argument('--user-data-dir=./User_Data')
        message = self.plainTextEdit.toPlainText()
        numbers = self.numbersList['Mobile Number']
        delay = 5
        if(message != ''):
            driver = webdriver.Chrome("chromedriver.exe", options=option)
            print("When Sign is success")
            driver.get("https://web.whatsapp.com")
            sleep(10)
            
            for idx, number in  enumerate(numbers):
                
                startTime = time.asctime(time.localtime(time.time()))   
                if number == "":
                    continue
                try:
                    url = 'https://web.whatsapp.com/send?phone='+ str(number) +'&text=' + str(message)
                    driver.get(url)
                    
                    try:
                        # click_btn = WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.CLASS_NAME,'_2SGGH')))
                        # click_btn.click()
                        click_btn = WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.CLASS_NAME,'_2Ujuu')))
                        # driver.find_element_by_class_name('_2Ujuu').click()
                    except(UnexpectedAlertPresentException, NoAlertPresentException) as e:
                        # print(e)
                        Alert(driver).accept()
                        return Exception

                    sleep(1)
                    click_btn.click()
                    
                    self.tableView.setItem(idx,1,QtWidgets.QTableWidgetItem('Sent'))
                    self.tableView.setItem(idx,2,QtWidgets.QTableWidgetItem(startTime))
                    sleep(1)
                    print("Message Sent to "+ str(idx+1) +" : " + str(number) + "\t" + str(startTime))

                except Exception as e:
                    self.tableView.setItem(idx,1,QtWidgets.QTableWidgetItem('Failed'))
                    self.tableView.setItem(idx,2,QtWidgets.QTableWidgetItem(startTime))
                    print('Failed to send message to '+ idx+ " : " + str(number))
            print("Process Complete")
            driver.close()


            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
