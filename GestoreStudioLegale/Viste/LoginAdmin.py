from PyQt5 import QtCore, QtGui, QtWidgets
from GestoreStudioLegale.Gestione.GestoreSistema import GestoreSistema
from GestoreStudioLegale.Viste.LoginAvvocato import Ui_Form


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(399, 300)
        Form.setStyleSheet("background-color: rgb(255, 240, 186);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 30, 161, 41))
        self.label.setStyleSheet("font: 30pt \"Arial\";")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(140, 100, 241, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 229);")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 117, 16))
        self.label_2.setStyleSheet("font: 14pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(170, 200, 221, 20))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 230, 174, 32))
        self.pushButton.setStyleSheet("border-width: 2px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"min-width: 10em; \n"
"background-color: rgb(255, 255, 229);")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 91, 16))
        self.label_4.setStyleSheet("font: 14pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(140, 160, 241, 31))
        self.textEdit_3.setStyleSheet("\n"
"background-color: rgb(255, 255, 229);")
        self.textEdit_3.setObjectName("textEdit_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "LOGIN"))
        self.label_2.setText(_translate("Form", "USER"))
        self.label_5.setText(_translate("Form", "codice fiscale e/o password errata! "))
        self.pushButton.setText(_translate("Form", "ACCEDI"))
        self.label_4.setText(_translate("Form", "PASSWORD"))

    window = Ui_Form()


    def convalida(self):
        username = str(self.textEdit)
        password = str(self.textEdit_3)
        #self.label_5(GestoreSistema.loginAdmin(username, password))
        self.pushButton.clicked(GestoreSistema.loginAdmin(username, password))