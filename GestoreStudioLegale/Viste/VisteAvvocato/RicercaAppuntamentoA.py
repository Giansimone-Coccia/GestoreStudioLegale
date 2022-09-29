from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout, QCalendarWidget)

from GestoreStudioLegale.Servizi.Appuntamento import *

import sys


class RicercaAppuntamentoA(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def _init_(self):
        super(RicercaAppuntamentoA, self).__init__()
        self.textIn = QLineEdit()
        self.calendar = QCalendarWidget()
        self.combo = QComboBox()

        self.layout = QFormLayout()

        self.createFormGroupBox()

        self.app1 = Appuntamento()

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
        #self.layout.addRow(QLabel("Ricerca:"), self.textIn)
        #self.layout.addRow(QLabel("Filtro:"), self.combo)
        #self.combo.activated.connect(self.indexScelta)
        #self.combo.currentIndexChanged.connect(self.view)
        self.formGroupBox.setLayout(self.layout)

    def indexScelta(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.AppuntamentoRicercatoA import AppuntamentoRicercatoA
        self.cindex = self.combo.currentIndex()
        self.code = self.textIn.text()
        #appuntamento = Appuntamento()
        print(self.cindex)

        if self.cindex == 0:
            #code = self.textIn.text()
            print(self.code)
            print("sas")
            self.subWindow = AppuntamentoRicercatoA()
            print("1")
            app = self.app1.ricercaAppuntamentoID(self.code)
            #self.subWindow.setData(app)
            print("2")
            #self.subWindow.show()
            #self.close()

        #elif self.cindex == 1:
            #self.dataSelezionata = self.calendar.selectedDate()
            #self.subWindow = AppuntamentoRicercatoA()
            #self.subWindow.setData(lambda: Appuntamento.ricercaAppuntamentoDataInizio(dataSelezionata))
            #self.subWindow.show()
            #self.close()

    def changeview(self):

        self.cindex = self.combo.currentIndex()

        if self.cindex == 0:
            #print(self.layout.getWidgetPosition(self.calendar))
            self.layout.removeRow(self.calendar)
            self.layout.insertRow(1,"ID:", self.textIn) #PROBLEMA QUI
            #print(self.layout.getWidgetPosition(self.calendar))
        elif self.cindex == 1:
            #self.layout.removeRow(1)
            self.layout.removeRow(self.textIn)
            self.layout.insertRow(1,"Calendario:", self.calendar)


    def selezionaData(self):
        self.dataSelezionata = self.calendar.selectedDate()
        self.year = self.dataSelezionata.year()
        self.day = self.dataSelezionata.day()
        self.month = self.dataSelezionata.month()