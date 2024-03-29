from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QComboBox, QCalendarWidget, QLineEdit, \
    QMessageBox

from GestoreStudioLegale.Servizi.Avvocato import Avvocato
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAvvocato.VisteAvvocatoUdienza.VistaHomeUdienze import VistaHomeUdienze
import datetime


class VistaInserisciUdienza(QWidget):

    clientiList = []
    nomi = []
    udienzeList = []
    tool = Tools()
    year = None
    month = None
    day = None

    def __init__(self, parent=None):
        super(VistaInserisciUdienza, self).__init__(parent)
        gLayout = QGridLayout()
        gLayout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
        self.labelName = QLabel('<font size="4"> Data udienza </font>')
        self.labelName2 = QLabel('<font size="4"> Orario udienza </font>')
        self.ora = QComboBox()
        orari = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00',
                 '14:30', '15:00', '15:30', '16:00', '16:30', '17:00']
        self.ora.addItems(orari)
        self.confirmButton = self.tool.createButton('Conferma udienza', self.udienzaOK)
        self.menuClienti = QComboBox()
        self.menuClienti.addItems(self.sceltaClienti())
        self.labelName4 = QLabel('<font size="4"> Cliente udienza </font>')
        self.procedimento = QComboBox()
        procedimenti = ['Penale', 'Civile', 'Amministrativo', 'Giudiziario', 'Minorile']
        self.procedimento.addItems(procedimenti)
        self.labelName5 = QLabel('<font size="4"> Tipo procedimento </font>')
        self.labelCitta = QLabel('<font size="4"> Città tribunale </font>')
        self.labelCittaText = QLineEdit()
        self.labelCittaText.setPlaceholderText("Inserisci città tribunale")
        self.calendar = QCalendarWidget()
        self.calendar.clicked.connect(self.selezionaData)
        self.dataSelezionata = None
        gLayout.addWidget(self.confirmButton, 6, 1)
        gLayout.addWidget(self.labelName, 1, 0)
        gLayout.addWidget(self.labelName2, 2, 0)
        gLayout.addWidget(self.ora, 2, 1)
        gLayout.addWidget(self.menuClienti, 4, 1)
        gLayout.addWidget(self.labelName4, 4, 0)
        gLayout.addWidget(self.procedimento, 3, 1)
        gLayout.addWidget(self.calendar, 1, 1)
        gLayout.addWidget(self.labelName5, 3, 0)
        gLayout.addWidget(self.labelCitta, 5, 0)
        gLayout.addWidget(self.labelCittaText, 5, 1)
        self.setLayout(gLayout)
        self.resize(800, 500)
        self.setWindowTitle("Udienza")
        self.show()

    def conferma(self):
        msg = QMessageBox()
        msg.setWindowTitle("Udienza confermata")
        msg.setText("L'udienza è stata presa in carico")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        self.vistaH = VistaHomeUdienze()
        self.vistaH.show()
        self.close()

    def convalida(self):

        if self.labelCittaText.text() == "":
            msg = QMessageBox()
            msg.setWindowTitle("ERRORE")
            msg.setText("Città non selezionata, riprova")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            return True

        if self.year is None and self.month is None and self.day is None:
            msg = QMessageBox()
            msg.setWindowTitle("ERRORE")
            msg.setText("Data non selezionata, riprova")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            return True
        try:
            date = self.pyDate = datetime.datetime(int(self.year), int(self.month), int(self.day))
            hour = self.ora.currentText()
            hourT = datetime.datetime.strptime(hour, "%H:%M")
            timeMin = datetime.datetime.strptime('09:00', '%H:%M')
            timeMax = datetime.datetime.strptime('17:00', '%H:%M')
            condition = False
            if date < datetime.datetime.now():
                msg = QMessageBox()
                msg.setWindowTitle("ERRORE")
                msg.setText("Data precedente all'attuale, riprova")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                condition = True
                return condition
            elif hourT < timeMin or hourT > timeMax:
                msg = QMessageBox()
                msg.setWindowTitle("ERRORE")
                msg.setText("Lo studio rimarrà aperto dalle 09:00 alle 17:00")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                condition = True
                return condition
            elif date.weekday() == 5 or date.weekday() == 6:
                msg = QMessageBox()
                msg.setWindowTitle("ERRORE")
                msg.setText("Lo studio è chiuso durante il week-end")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                condition = True
                return condition
        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle("ERRORE")
            msg.setText("Riprova")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            return

    def problema(self):
        msg = QMessageBox()
        msg.setWindowTitle("Problema")
        msg.setText("Problema con l'inserimento, riprovare")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def rewind(self):
        self.vistaUdienzeHome = VistaHomeUdienze()
        self.vistaUdienzeHome.show()
        self.close()

    def sceltaClienti(self):
        tool = Tools()
        self.nomi = []
        self.avvocatiList = tool.loadAvvocati()
        for avvocato in self.avvocatiList:
            if avvocato.codiceFiscale == tool.leggi().rsplit()[0]:
                self.clientiList = avvocato.clienti

        for cliente in self.clientiList:
            self.nomi.append(cliente.nome + ' ' + cliente.cognome)
        return self.nomi

    def selezionaData(self):
        self.dataSelezionata = self.calendar.selectedDate()
        self.year = self.dataSelezionata.year()
        self.day = self.dataSelezionata.day()
        self.month = self.dataSelezionata.month()

    def udienzaOK(self):
        avvocato = Avvocato()
        hour = self.ora.currentText()
        self.udienzeList = self.tool.loadUdienze()
        if not self.convalida():
            hourDT = datetime.datetime.strptime(hour, "%H:%M")
            oraFine = hourDT + datetime.timedelta(minutes=30)
            self.pyDate = datetime.datetime(int(self.year), int(self.month), int(self.day))
            dateS = self.pyDate.strftime("%d/%m/%Y")
            dataOraInizio = dateS + ',' + hour
            dataOraFine = dateS + ',' + oraFine.strftime("%H:%M")
            ID = self.tool.IdGenerator('UD')
            for udienza in self.udienzeList:
                if udienza.dataOraInizio == self.pyDate:
                    self.problema()
                    return
                else:
                    cliente1 = Cliente()
                    stringa = self.menuClienti.currentText().rsplit()
                    udienza.creaUdienza(avvocato.ricercaUtilizzatoreCC(str(self.tool.leggi()).rsplit()[0]), self.labelCittaText.text(), cliente1.ricercaUtilizzatoreNomeCognome(nome =self.menuClienti.currentText().rsplit()[0],cognome = self.menuClienti.currentText().rsplit()[1]), dataOraInizio, dataOraFine, ID, self.procedimento.currentText())
                    self.conferma()
                    return