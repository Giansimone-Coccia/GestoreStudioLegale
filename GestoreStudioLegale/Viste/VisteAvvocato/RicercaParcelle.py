from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout, QCalendarWidget)

from GestoreStudioLegale.Servizi.Parcella import *

import sys


class RicercaParcelle(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(RicercaParcelle, self).__init__()

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
        self.formGroupBox = QGroupBox("Cerca una parcella")

        self.layout.insertRow(1, "Codice fiscale (cliente):", self.textIn)

        self.formGroupBox.setLayout(self.layout)

        self.formGroupBox.setLayout(self.layout)

    def indexScelta(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.ParcellaRicercata import ParcellaRicercata

        self.code = self.textIn.text()

        cliente = Cliente()
        parcella = Parcella()
        risultatoRicerca = parcella.ricercaParcellaIdentificativo(self.code)


        self.subWindow = ParcellaRicercata(risultatoRicerca)
        self.subWindow.show()
        self.close()