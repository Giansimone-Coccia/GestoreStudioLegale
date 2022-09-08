import datetime

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton

from GestoreStudioLegale.Utilities.Utilities import Tools
import os
import pickle


class VistaPrenotaAppuntamentiC(QWidget):

    appuntamentiList = []
    def __init__(self, parent=None):
        super(VistaPrenotaAppuntamentiC, self).__init__(parent)
        tool = Tools()
        gLayout = QGridLayout()
        gLayout.addWidget(tool.rewindButton(self.rewind), 0, 0)
        self.labelName3 = QLabel('<font size="4"> Il sistema controllerà la disponibilità della data inserita </font>')
        self.labelName3.setStyleSheet("border: 1px solid black;")
        self.labelName = QLabel('<font size="4"> Data appuntamento </font>')
        self.lineEditDate = QLineEdit()
        self.lineEditDate.setPlaceholderText('Inserisci data appuntamento')
        self.labelName2 = QLabel('<font size="4"> Orario appuntamento </font>')
        self.lineEditOra = QLineEdit()
        self.lineEditOra.setPlaceholderText('Inserisci orario appuntamento')
        confirmButton = QPushButton()
        confirmButton = tool.createButton('Conferma appuntamento', self.confermaAppuntamento)
        #confirmButton.setSizePolicy(5, 5)
        gLayout.addWidget(confirmButton, 3, 1)
        gLayout.addWidget(self.labelName3, 0, 1)
        gLayout.addWidget(self.labelName, 1, 0)
        gLayout.addWidget(self.labelName2, 2, 0)
        gLayout.addWidget(self.lineEditDate, 1, 1)
        gLayout.addWidget(self.lineEditOra, 2, 1)
        self.setLayout(gLayout)
        self.resize(400, 200)
        self.setWindowTitle("Prenotazione appuntamenti")
        self.show()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteCliente.VistaHomeAppuntamentiC import VistaHomeAppuntamentiC
        self.vistaAppuntameti = VistaHomeAppuntamentiC()
        self.vistaAppuntameti.show()
        self.close()

    def confermaAppuntamento(self):# Da rivedere
        self.loadDateA()
        date = datetime.datetime.strptime(str(self.lineEditDate), "%d/%m/%Y")
        hour = datetime.datetime.strptime(str(self.lineEditOra), "%H:%M")
        dateHour = str(date)+' '+str(hour)
        dateHour1 = datetime.datetime.strptime(dateHour, "%d/%m/%Y %H:%M")
        for appuntamento in self.appuntamentiList:
            print(appuntamento.dataOraInizio)
            if appuntamento.dataOraInizio == dateHour1:
                print("non va bene")
            else:
                print("ok")

    def loadDateA(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Appuntamenti.pickle'):
            with open('GestoreStudioLegale/Dati/Appuntamenti.pickle', 'rb') as f:
                self.appuntamentiList = list(pickle.load(f))