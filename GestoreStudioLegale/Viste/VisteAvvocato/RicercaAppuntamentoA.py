from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout, QCalendarWidget)

from GestoreStudioLegale.Servizi.Appuntamento import Appuntamento

import sys


class RicercaAppuntamentoA(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(RicercaAppuntamentoA, self).__init__()
        self.textIn = QLineEdit()

        self.combo = QComboBox()
        self.calendar = QCalendarWidget()
        self.layout = QFormLayout()

        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.indexScelta)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)

        self.combo.currentIndexChanged.connect(self.changeview)

        self.setLayout(mainLayout)

        self.setWindowTitle("Ricerca")
        self.resize(400, 120)

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Cerca un appuntamento")
        #self.combo.addItem("Nome cliente")
        self.combo.addItem("ID appuntamento")
        self.combo.addItem("Data Inizio")
        self.layout.insertRow(0, "Filtro:", self.combo)
        self.layout.insertRow(1, "ID:", self.textIn)
        #self.combo.activated.connect(self.indexScelta)
        self.formGroupBox.setLayout(self.layout)
        layout.addRow(QLabel("Ricerca:"), self.textIn)
        layout.addRow(QLabel("Filtro:"), self.combo)
        self.combo.activated.connect(self.indexScelta)
        self.combo.currentIndexChanged.connect(self.view)
        self.formGroupBox.setLayout(layout)

    def indexScelta(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.AppuntamentoRicercatoA import AppuntamentoRicercatoA
        cindex = self.combo.currentIndex()
        code = self.textIn.text()

        if cindex == 0:
            #code = self.textIn.text()
            self.subWindow = AppuntamentoRicercatoA()
            self.subWindow.setData(lambda: Appuntamento.ricercaAppuntamentoID(code))
            self.subWindow.show()
            self.close()

        elif cindex == 1:
            self.dataSelezionata = self.calendar.selectedDate()
            self.subWindow = AppuntamentoRicercatoA()
            #self.subWindow.setData(lambda: Appuntamento.ricercaAppuntamentoDataInizio(dataSelezionata))
            self.subWindow.show()
            self.close()

    def changeview(self):
        cindex = self.combo.currentIndex()
        if cindex == 0:
            #print(self.layout.getWidgetPosition(self.calendar))
            self.layout.removeRow(1)
            self.layout.insertRow(1,"ID:", self.textIn) #PROBLEMA INSERIMENTO QUI
            #print(self.layout.getWidgetPosition(self.calendar))
        elif cindex == 1:
            self.layout.removeRow(1)
            self.layout.insertRow(1,"Calendario:", self.calendar)


    def selezionaData(self):
        self.dataSelezionata = self.calendar.selectedDate()
        self.year = self.dataSelezionata.year()
        self.day = self.dataSelezionata.day()
        self.month = self.dataSelezionata.month()
