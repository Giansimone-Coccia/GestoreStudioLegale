from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit, QLabel, QMessageBox, QComboBox, \
    QCalendarWidget
from datetime import datetime, timedelta, time
from GestoreStudioLegale.Gestione.GestoreSistema import GestoreSistema
from GestoreStudioLegale.Servizi.Appuntamento import Appuntamento
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaAggiornaAppuntamentoA(QWidget):

    cliente = Cliente()
    tool = Tools()
    appuntamento = Appuntamento()
    appuntamentiList = tool.loadAppuntamenti()

    def __init__(self,parent = None):
        super(VistaAggiornaAppuntamentoA, self).__init__(parent)
        gLayout = QGridLayout()
        gLayout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
        self.label1 = QLabel('<font size="4"> Modifica data inizio </font>')
        self.labelName3 = QLabel('<font size="4"> Il sistema controllerà la disponibilità della data inserita </font>')
        self.labelName3.setStyleSheet("border: 1px solid black;")
        self.labelName = QLabel('<font size="4"> Data appuntamento </font>')
        self.labelName2 = QLabel('<font size="4"> Orario appuntamento </font>')
        self.ora = QComboBox()
        orari = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00',
                 '14:30', '15:00', '15:30', '16:00', '16:30', '17:00']
        self.ora.addItems(orari)
        confirmButton = QPushButton()
        #confirmButton = self.tool.createButton('Conferma appuntamento', self.confermaAppuntamento)
        confirmButton = self.tool.createButton('Conferma appuntamento', lambda checked, a = self.appuntamento: self.confermaAppuntamento(a))
        self.calendar = QCalendarWidget()
        self.calendar.clicked.connect(self.selezionaData)
        self.dataSelezionata = None
        gLayout.addWidget(confirmButton, 4, 1)
        gLayout.addWidget(self.labelName3, 0, 1)
        gLayout.addWidget(self.labelName, 1, 0)
        gLayout.addWidget(self.labelName2, 2, 0)
        gLayout.addWidget(self.ora, 2, 1)
        gLayout.addWidget(self.label1, 4, 0)
        gLayout.addWidget(self.calendar, 1, 1)
        self.setLayout(gLayout)
        self.resize(800, 400)
        self.setWindowTitle("Modifica appuntamenti")
        self.show()

    def rewind(self):
        self.vistaHome = VistaAggiornaAppuntamentoA()
        self.vistaHome.show()
        self.close()

    def error(self, name):
        self.msg = QMessageBox()
        self.msg.setWindowTitle('ERRORE')
        self.msg.setText(name)
        self.msg.exec()

    def selezionaData(self):
        self.dataSelezionata = self.calendar.selectedDate()
        self.year = self.dataSelezionata.year()
        self.day = self.dataSelezionata.day()
        self.month = self.dataSelezionata.month()

    def confermaAppuntamento(self, appuntamento):
        for appuntamento in self.appuntamentiList:
            if appuntamento.ID == True: #appuntamento acquisito
                pass
