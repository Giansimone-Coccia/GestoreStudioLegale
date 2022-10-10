from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout, QCalendarWidget, QMessageBox)

from GestoreStudioLegale.Servizi.Appuntamento import *

import sys

from GestoreStudioLegale.Utilities.Utilities import Tools


class RicercaAppuntamentoA(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(RicercaAppuntamentoA, self).__init__()

        self.textIn = QLineEdit()

        self.layout = QFormLayout()

        self.createFormGroupBox()


        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.indexScelta)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)

        self.setLayout(mainLayout)

        self.setWindowTitle("Ricerca")
        self.resize(400, 120)

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Cerca un appuntamento")

        self.layout.insertRow(1, "ID:", self.textIn)

        self.formGroupBox.setLayout(self.layout)

        self.formGroupBox.setLayout(self.layout)

    def indexScelta(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.AppuntamentoRicercatoA import AppuntamentoRicercatoA

        self.code = self.textIn.text()
        tool = Tools()
        avvocatiList = tool.loadAvvocati()

        self.risultatoRicerca = None

        appuntamento = Appuntamento()
        for avvocato in avvocatiList:
            if avvocato.codiceFiscale == tool.leggi().rsplit()[0]:
                for app in avvocato.appuntamentiAvvocato:
                    if app.ID == self.code:
                        self.risultatoRicerca = appuntamento.ricercaAppuntamentoID(self.code)

        if self.risultatoRicerca is None:
            msg = QMessageBox()
            msg.setWindowTitle('Appuntamento non trovato')
            msg.setText('Non esiste alcun appuntamento con questo id')
            msg.exec()
            return


        self.subWindow = AppuntamentoRicercatoA()
        self.subWindow.initUI(self.risultatoRicerca)
        self.subWindow.show()
        self.close()