# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\programming\python\image\projet.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_image_processing(object):
    def setupUi(self, image_processing):
        image_processing.setObjectName("image_processing")
        image_processing.setWindowModality(QtCore.Qt.NonModal)
        image_processing.setEnabled(True)
        image_processing.resize(1200, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(image_processing.sizePolicy().hasHeightForWidth())
        image_processing.setSizePolicy(sizePolicy)
        image_processing.setMinimumSize(QtCore.QSize(900, 400))
        image_processing.setMaximumSize(QtCore.QSize(1200, 700))
        image_processing.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        image_processing.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        image_processing.setAutoFillBackground(False)
        image_processing.setStyleSheet("")
        image_processing.setSizeGripEnabled(False)
        self.btn1 = QtWidgets.QPushButton(image_processing)
        self.btn1.setGeometry(QtCore.QRect(320, 19, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn1.setFont(font)
        self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn1.setStyleSheet("background: #ffa31a ;color : black;\n"
" border-radius: 10px ;")
        self.btn1.setObjectName("btn1")
        self.label2 = QtWidgets.QLabel(image_processing)
        self.label2.setEnabled(True)
        self.label2.setGeometry(QtCore.QRect(780, 60, 400, 400))
        self.label2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label2.setStyleSheet("border-top-left-radius : 10px;\n"
"color: rgb(255, 0, 0);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"text-align: center;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0,stop:0 rgba(116, 200, 255, 255), stop:1 rgba(39, 80, 220, 255));")
        self.label2.setText("")
        self.label2.setTextFormat(QtCore.Qt.AutoText)
        self.label2.setScaledContents(False)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.btn2 = QtWidgets.QPushButton(image_processing)
        self.btn2.setEnabled(False)
        self.btn2.setGeometry(QtCore.QRect(780, 20, 91, 41))
        self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn2.setAutoFillBackground(False)
        self.btn2.setStyleSheet("background: #C0C0C0 ;border-radius: 10px ;\n"
"")
        self.btn2.setText("")
        self.btn2.setAutoDefault(False)
        self.btn2.setDefault(False)
        self.btn2.setObjectName("btn2")
        self.cmb1 = QtWidgets.QComboBox(image_processing)
        self.cmb1.setEnabled(False)
        self.cmb1.setGeometry(QtCore.QRect(625, 200, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmb1.setFont(font)
        self.cmb1.setEditable(False)
        self.cmb1.setDuplicatesEnabled(False)
        self.cmb1.setObjectName("cmb1")
        self.cmb1.addItem("")
        self.cmb1.addItem("")
        self.cmb1.addItem("")
        self.cmb1.addItem("")
        self.cmb1.addItem("")
        self.cmb1.addItem("")
        self.cmb1.addItem("")
        self.cmb1.addItem("")
        self.cmb1.addItem("")
        self.rd1 = QtWidgets.QRadioButton(image_processing)
        self.rd1.setGeometry(QtCore.QRect(450, 50, 160, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rd1.setFont(font)
        self.rd1.setChecked(True)
        self.rd1.setObjectName("rd1")
        self.rd2 = QtWidgets.QRadioButton(image_processing)
        self.rd2.setGeometry(QtCore.QRect(450, 100, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rd2.setFont(font)
        self.rd2.setObjectName("rd2")
        self.rd3 = QtWidgets.QRadioButton(image_processing)
        self.rd3.setGeometry(QtCore.QRect(450, 150, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rd3.setFont(font)
        self.rd3.setObjectName("rd3")
        self.rd4 = QtWidgets.QRadioButton(image_processing)
        self.rd4.setGeometry(QtCore.QRect(450, 200, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rd4.setFont(font)
        self.rd4.setObjectName("rd4")
        self.rd5 = QtWidgets.QRadioButton(image_processing)
        self.rd5.setGeometry(QtCore.QRect(450, 250, 175, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rd5.setFont(font)
        self.rd5.setObjectName("rd5")
        self.rd6 = QtWidgets.QRadioButton(image_processing)
        self.rd6.setGeometry(QtCore.QRect(450, 310, 175, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rd6.setFont(font)
        self.rd6.setObjectName("rd6")
        self.rd7 = QtWidgets.QRadioButton(image_processing)
        self.rd7.setGeometry(QtCore.QRect(450, 370, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rd7.setFont(font)
        self.rd7.setObjectName("rd7")
        self.rd8 = QtWidgets.QRadioButton(image_processing)
        self.rd8.setGeometry(QtCore.QRect(450, 420, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rd8.setFont(font)
        self.rd8.setObjectName("rd8")
        self.cmb2 = QtWidgets.QComboBox(image_processing)
        self.cmb2.setEnabled(False)
        self.cmb2.setGeometry(QtCore.QRect(645, 420, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmb2.setFont(font)
        self.cmb2.setObjectName("cmb2")
        self.cmb2.addItem("")
        self.cmb2.addItem("")
        self.cmb2.addItem("")
        self.cmb2.addItem("")
        self.cmb2.addItem("")
        self.cmb2.addItem("")
        self.btn3 = QtWidgets.QPushButton(image_processing)
        self.btn3.setEnabled(False)
        self.btn3.setGeometry(QtCore.QRect(160, 510, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn3.setFont(font)
        self.btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn3.setStyleSheet("background: #C0C0C0; border-radius: 10px ;")
        self.btn3.setObjectName("btn3")
        self.label1 = QtWidgets.QLabel(image_processing)
        self.label1.setEnabled(True)
        self.label1.setGeometry(QtCore.QRect(20, 60, 400, 400))
        self.label1.setStyleSheet("border-radius: 10px;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(39, 80, 220, 255) stop:1 rgba(116, 200, 255, 255),);")
        self.label1.setText("")
        self.label1.setScaledContents(False)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.btn5 = QtWidgets.QPushButton(image_processing)
        self.btn5.setEnabled(False)
        self.btn5.setGeometry(QtCore.QRect(790, 510, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.btn5.setFont(font)
        self.btn5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn5.setStyleSheet("background: #C0C0C0 ; border-radius: 10px ;")
        self.btn5.setObjectName("btn5")
        self.btn4 = QtWidgets.QPushButton(image_processing)
        self.btn4.setEnabled(False)
        self.btn4.setGeometry(QtCore.QRect(1050, 510, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn4.setFont(font)
        self.btn4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn4.setStyleSheet("background: #C0C0C0 ;border-radius: 10px ;")
        self.btn4.setObjectName("btn4")
        self.spinbox1 = QtWidgets.QSpinBox(image_processing)
        self.spinbox1.setEnabled(False)
        self.spinbox1.setGeometry(QtCore.QRect(630, 320, 60, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinbox1.setFont(font)
        self.spinbox1.setWrapping(True)
        self.spinbox1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spinbox1.setMaximum(255)
        self.spinbox1.setObjectName("spinbox1")
        self.spinbox2 = QtWidgets.QSpinBox(image_processing)
        self.spinbox2.setEnabled(False)
        self.spinbox2.setGeometry(QtCore.QRect(710, 320, 60, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinbox2.setFont(font)
        self.spinbox2.setWrapping(True)
        self.spinbox2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spinbox2.setMaximum(255)
        self.spinbox2.setObjectName("spinbox2")
        self.spinbox3 = QtWidgets.QSpinBox(image_processing)
        self.spinbox3.setEnabled(False)
        self.spinbox3.setGeometry(QtCore.QRect(670, 380, 60, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinbox3.setFont(font)
        self.spinbox3.setWrapping(True)
        self.spinbox3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spinbox3.setMaximum(255)
        self.spinbox3.setObjectName("spinbox3")
        self.label = QtWidgets.QLabel(image_processing)
        self.label.setGeometry(QtCore.QRect(630, 290, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(image_processing)
        self.label_2.setGeometry(QtCore.QRect(710, 290, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(image_processing)
        self.label_3.setGeometry(QtCore.QRect(670, 350, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(image_processing)
        QtCore.QMetaObject.connectSlotsByName(image_processing)

    def retranslateUi(self, image_processing):
        _translate = QtCore.QCoreApplication.translate
        image_processing.setWindowTitle(_translate("image_processing", "test"))
        self.btn1.setText(_translate("image_processing", "Browse"))
        self.cmb1.setItemText(0, _translate("image_processing", "Given range"))
        self.cmb1.setItemText(1, _translate("image_processing", "0,1,3,...,119,...,253,255"))
        self.cmb1.setItemText(2, _translate("image_processing", "0,3,7,...,119,...,251,255"))
        self.cmb1.setItemText(3, _translate("image_processing", "0,7,15,..,119,..,247,255"))
        self.cmb1.setItemText(4, _translate("image_processing", "0,15,31,..,111,..,239,255"))
        self.cmb1.setItemText(5, _translate("image_processing", "0,31,63,..,127,..,223,255"))
        self.cmb1.setItemText(6, _translate("image_processing", "0,63,127,255"))
        self.cmb1.setItemText(7, _translate("image_processing", "0,127,255"))
        self.cmb1.setItemText(8, _translate("image_processing", "0,255"))
        self.rd1.setText(_translate("image_processing", "RGB to gray scale"))
        self.rd2.setText(_translate("image_processing", "HSV to gray scale"))
        self.rd3.setText(_translate("image_processing", "RGB to HSV"))
        self.rd4.setText(_translate("image_processing", "Quantize image"))
        self.rd5.setText(_translate("image_processing", "gray-level histogram"))
        self.rd6.setText(_translate("image_processing", "adjust image dynamic"))
        self.rd7.setText(_translate("image_processing", "histogram equalization"))
        self.rd8.setText(_translate("image_processing", "Remove noise"))
        self.cmb2.setItemText(0, _translate("image_processing", "Filter matrix"))
        self.cmb2.setItemText(1, _translate("image_processing", "3 * 3"))
        self.cmb2.setItemText(2, _translate("image_processing", "5 * 5"))
        self.cmb2.setItemText(3, _translate("image_processing", "7 * 7"))
        self.cmb2.setItemText(4, _translate("image_processing", "9 * 9"))
        self.cmb2.setItemText(5, _translate("image_processing", "11 * 11 "))
        self.btn3.setText(_translate("image_processing", "process"))
        self.btn5.setText(_translate("image_processing", "show in pyplot"))
        self.btn4.setText(_translate("image_processing", "Save"))
        self.label.setText(_translate("image_processing", "min range"))
        self.label_2.setText(_translate("image_processing", "max range"))
        self.label_3.setText(_translate("image_processing", "max value"))
