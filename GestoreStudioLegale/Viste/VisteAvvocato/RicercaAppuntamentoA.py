from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout)

from GestoreStudioLegale.Servizi.Appuntamento import Appuntamento
import sys


class RicercaAppuntamentoA(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(RicercaAppuntamentoA, self).__init__()
        self.text = QLineEdit()
        self.combo = QComboBox()

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
        layout = QFormLayout()
        self.combo.addItem("Nome cliente")
        self.combo.addItem("Data inizio")
        self.combo.addItem("ID appuntamento")
        layout.addRow(QLabel("Ricerca:"), self.text)
        layout.addRow(QLabel("Filtro:"), self.combo)
        #self.combo.activated.connect(self.indexScelta)
        self.formGroupBox.setLayout(layout)

    def indexScelta(self):
        cindex = self.combo.currentIndex()
        if cindex == 2:
            Appuntamento.ricercaAppuntamentoID(self.text)
        else:
            pass