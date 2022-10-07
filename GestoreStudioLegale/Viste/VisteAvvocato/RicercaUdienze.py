from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout, QCalendarWidget, QMessageBox)

from GestoreStudioLegale.Servizi.Parcella import Parcella
from GestoreStudioLegale.Servizi.Cliente import Cliente

import sys

from GestoreStudioLegale.Utilities.Utilities import Tools


class RicercaUdienze(QDialog):
    NumGridRows = 3
    NumButtons = 4


    def __init__(self):
        super(RicercaUdienze, self).__init__()

        self.tool = Tools()
        self.udienzeList = self.tool.loadUdienze()


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
        self.formGroupBox = QGroupBox("Cerca un udienza")

        self.layout.insertRow(1, "Codice fiscale (cliente):", self.textIn)

        self.formGroupBox.setLayout(self.layout)

        self.formGroupBox.setLayout(self.layout)

    def indexScelta(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.UdienzaRicercata import UdienzaRicercata

        self.code = self.textIn.text()
        #print(self.code)

        cliente = Cliente()

        self.risultatoRicerca = cliente.ricercaUtilizzatoreCC(self.code) #FUNZIONA

        if self.risultatoRicerca is None:
            msg = QMessageBox()
            msg.setWindowTitle('Cliente non trovato')
            msg.setText('Non esiste alcun cliente con questo codice fiscale. Riprova')
            msg.exec()
            return

        udienze = []

        for udienza in self.udienzeList:
            if udienza.Cliente.codiceFiscale == self.risultatoRicerca.codiceFiscale:
                udienze.append(udienza)
                #print("stampa le udienze")
                #print(udienza.getDatiUdienza())


        #self.subWindow = ParcellaRicercata(risultatoRicerca.getDatiCliente()["parcelle"])
        self.subWindow = UdienzaRicercata(udienze)
        self.subWindow.show()
        self.close()