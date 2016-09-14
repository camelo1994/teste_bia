# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\raptor_dev\eric_tesste_4\formulario1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(681, 574)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(50, 40, 551, 441))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_READ = QtWidgets.QPushButton(self.tab)
        self.pushButton_READ.setGeometry(QtCore.QRect(140, 70, 75, 23))
        self.pushButton_READ.setObjectName("pushButton_READ")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 70, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(100, 200, 311, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(100, 230, 311, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(100, 260, 321, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(70, 70, 42, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(9999)
        self.spinBox.setObjectName("spinBox")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(160, 60, 251, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 100, 251, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 140, 251, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(30, 60, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(30, 100, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(30, 140, 81, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton_ADD = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_ADD.setGeometry(QtCore.QRect(160, 260, 75, 23))
        self.pushButton_ADD.setObjectName("pushButton_ADD")
        self.label_Feedback = QtWidgets.QLabel(self.tab_2)
        self.label_Feedback.setGeometry(QtCore.QRect(50, 340, 431, 16))
        self.label_Feedback.setText("")
        self.label_Feedback.setObjectName("label_Feedback")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_READ.setText(_translate("Form", "LER"))
        self.label.setText(_translate("Form", "Id"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.label_5.setText(_translate("Form", "nome do pai"))
        self.label_6.setText(_translate("Form", "xablau do pai"))
        self.label_7.setText(_translate("Form", "tamanho do pai"))
        self.pushButton_ADD.setText(_translate("Form", "adicona"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

