"""
Auther: Terry Caviness
Date:  6-30-22
Version: 1.0
Descrpition: The was made to just get Market Data to be viewed and Convert to CSV file or Execel file by using pandas libaery for the converstion.
all stock data comes from yfinance libaery with is not the best api libaery to get this data from but it is free that why I usesed it. I like free.
"""
__Auther__ = "Terry Caviness"

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QPlainTextEdit
import yfinance as yf
import pandas as pa


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
         #Setup Combo Boxs Values in a List
        combo2 = ['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max']
        combo1 =["1m","2m","5m","15m","30m","60m","90m","1h","1d","5d","1wk","1mo","3mo"]
        
        #setup the Main Window of the Program.
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1045, 587)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("background=rgb(57, 219, 255)")
        #Setup Show Data Button
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_data = QtWidgets.QPushButton(self.centralwidget)
        self.btn_data.setGeometry(QtCore.QRect(418, 470, 141, 61))
        self.btn_data.clicked.connect(self.showdata)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_data.setFont(font)
        self.btn_data.setObjectName("btn_data")
        #Setup Convert to Execel Button 
        self.btn_Cexexel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Cexexel.setGeometry(QtCore.QRect(588, 470, 161, 61))
        self.btn_Cexexel.clicked.connect(self.conExecl)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Cexexel.setFont(font)
        self.btn_Cexexel.setObjectName("btn_Cexexel")
        self.btn_Ccvs = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Ccvs.setGeometry(QtCore.QRect(780, 470, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        #Setup Convert to CSV Button
        self.btn_Ccvs.setFont(font)
        self.btn_Ccvs.setObjectName("btn_Ccvs")
        self.btn_Ccvs.clicked.connect(self.conCSV)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        #Setup Lables and Frames
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 100, 271, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(4)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        #Setup Combo Boxes and add the List to objects within the Frame
        self.cb_Per = QtWidgets.QComboBox(self.frame)
        self.cb_Per.setGeometry(QtCore.QRect(130, 50, 121, 22))
        self.cb_Per.setEditable(False)
        self.cb_Per.setDuplicatesEnabled(False)
        self.cb_Per.setObjectName("cb_Per")
        self.cb_Per.addItems(combo2)
        self.cb_Val = QtWidgets.QComboBox(self.frame)
        self.cb_Val.addItems(combo1)
        self.cb_Val.setGeometry(QtCore.QRect(130, 120, 121, 22))
        self.cb_Val.setObjectName("cb_Val")
        
        self.ck_enable = QtWidgets.QCheckBox(self.frame)
        self.ck_enable.setGeometry(QtCore.QRect(30, 10, 211, 31))
        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        #Setup the Object for the check box. 
        self.ck_enable.setFont(font)
        self.ck_enable.setObjectName("ck_enable")
        self.ck_enable.toggled.connect(lambda: self.checked(self.ck_enable))
        
        self.date_start = QtWidgets.QDateEdit(self.frame)
        self.date_start.setEnabled(False)
        self.date_start.setGeometry(QtCore.QRect(20, 210, 211, 31))
        self.date_start.setObjectName("date_start")
        self.date_end = QtWidgets.QDateEdit(self.frame)
        self.date_end.setEnabled(False)
        self.date_end.setGeometry(QtCore.QRect(20, 280, 211, 31))
        self.date_end.setObjectName("date_end")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        #text box for stock symble
        self.txt_stcok = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_stcok.setGeometry(QtCore.QRect(160, 60, 141, 31))
        self.txt_stcok.setObjectName("txt_stcok")
        #text box to display the stock data
        self.txtb_display = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtb_display.setGeometry(QtCore.QRect(330, 60, 691, 401))
        self.txtb_display.setAcceptDrops(False)
        self.txtb_display.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.txtb_display.setLineWidth(1)
        self.txtb_display.setUndoRedoEnabled(False)
        self.txtb_display.setReadOnly(True)
        self.txtb_display.setBackgroundVisible(False)
        self.txtb_display.setCenterOnScroll(False)
        self.txtb_display.setObjectName("txtb_display")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 26))
        self.menubar.setObjectName("menubar")
        self.mu_file = QtWidgets.QMenu(self.menubar)
        self.mu_file.setObjectName("mu_file")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.mu_file.menuAction())      
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

   #shows data in the display text box
    def showdata(self):
       obj = yf.Ticker(self.txt_stcok.text())
       if self.ck_enable.isChecked() == False:
            data = obj.history()  
            self.txtb_display.insertPlainText(str(data))
       else:
            data = obj.history(interval=str(self.cb_Per.currentText()), start=str(self.date_start.text()), end=str(self.date_end.text()))
            self.txtb_display.insertPlainText(str(data))
        
    #converts data to execl file
    def conExecl(self):
      datafrme = self.txtb_display.toPlainText()
      data = datafrme.split()
      print("Data is being put on file.")
      df = pa.DataFrame(data)
      df.to_excel('output.xlsx', index=False)
      
        
    #converts data to csv file
    def conCSV(self):
       dataframe = self.txtb_display.toPlainText()
       data = dataframe.split()
       print("Data is being put on file.")
       df = pa.DataFrame(data)
       df.to_csv('output.csv', index=False)

   #when checked will enable this object on windows
    def checked(self, b):
         if b.isChecked()== True:
             self.date_end.setEnabled(True)
             self.date_start.setEnabled(True)
         else:
             self.date_end.setEnabled(False)
             self.date_start.setEnabled(False)

 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stcok App"))
        self.btn_data.setText(_translate("MainWindow", "See Scock Data"))
        self.btn_Cexexel.setText(_translate("MainWindow", "Convert To Excel"))
        self.btn_Ccvs.setText(_translate("MainWindow", "Convert To CSV"))
        self.label.setText(_translate("MainWindow", "Stock Symble: "))
        self.ck_enable.setText(_translate("MainWindow", "Enable Avanded Search"))
        self.date_start.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.date_end.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.label_2.setText(_translate("MainWindow", "Period:"))
        self.label_3.setText(_translate("MainWindow", "Intervel: "))
        self.label_4.setText(_translate("MainWindow", "Start Date:"))
        self.label_5.setText(_translate("MainWindow", "End Date:"))
        self.mu_file.setTitle(_translate("MainWindow", "File"))

         

if __name__ == "__main__":
    import sys   
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


   
