import datetime
import os
import pickle

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QMessageBox, QComboBox, \
    QCalendarWidget
from GestoreStudioLegale.Servizi.Appuntamento import Appuntamento
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAvvocato.VisteAvvocatoAppuntamento.VistaHomeAppuntamentiA import VistaHomeAppuntamentiA


class VistaAggiornaAppuntamentoA(QWidget):


    tool = Tools()
    appuntamento = Appuntamento()
    appuntamentiList = tool.loadAppuntamenti()
    cliente = Cliente()

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
        confirmButton = self.tool.createButton('Conferma appuntamento', self.confermaAppuntamento)
        #confirmButton = self.tool.createButton('Conferma appuntamento', lambda checked, a = self.appuntamento: self.confermaAppuntamento(a))
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

    def conferma(self):
        msg = QMessageBox()
        msg.setWindowTitle("Appuntamento confermato")
        msg.setText("Il suo appuntamento è stato modificato con successo")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        self.vistaPrima = VistaHomeAppuntamentiA()
        self.vistaPrima.show()
        self.close()

    def confermaAppuntamento(self):
        for appuntamento in self.appuntamentiList:
            if appuntamento.ID == self.appuntamento.ID:
                hour = self.ora.currentText()
                if not self.convalida():
                    hourDT = datetime.datetime.strptime(hour, "%H:%M")
                    #oraFine = hourDT+datetime.timedelta(hours = 1) #FAI MINUTI SE OGNI MEZZ'ORA
                    oraFine = hourDT + datetime.timedelta(minutes=30)
                    self.pyDate = datetime.datetime(int(self.year), int(self.month), int(self.day))
                    dateS = self.pyDate.strftime("%d/%m/%Y")
                    dataOraInizio = dateS + ',' + hour
                    dataOraFine = dateS + ',' + oraFine.strftime("%H:%M")
                    appuntamento.dataOraInizio = datetime.datetime.strptime(dataOraInizio, "%d/%m/%Y,%H:%M")
                    appuntamento.dataOraFine = datetime.datetime.strptime(dataOraFine, "%d/%m/%Y,%H:%M")
                    if os.path.isfile('GestoreStudioLegale/Dati/Appuntamenti.pickle'):
                        with open('GestoreStudioLegale/Dati/Appuntamenti.pickle', 'wb') as f1:
                            pickle.dump(self.appuntamentiList, f1, pickle.HIGHEST_PROTOCOL)
                    self.avocatiList = self.tool.loadAvvocati()
                    for avvocato in self.avocatiList:
                        if avvocato.codiceFiscale == self.tool.leggi().rsplit()[0]:
                            for app in avvocato.appuntamentiAvvocato:
                                if app.ID == self.appuntamento.ID:
                                    avvocato.appuntamentiAvvocato.remove(app)
                                    avvocato.appuntamentiAvvocato.append(appuntamento)
                            avvocato.aggiornaAvvocato()
                    self.conferma()

    def convalida(self):
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
        msg.setWindowTitle("ERRORE")
        msg.setText("Non è possibile modificarlo per questo giorno, riprovi")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
        self.vistaPrec = VistaHomeAppuntamentiA()
        self.vistaPrima.show()
        self.close()

    def rewind(self):
        self.vistaHome = VistaHomeAppuntamentiA()
        self.vistaHome.show()
        self.close()

    def selezionaData(self):
        self.dataSelezionata = self.calendar.selectedDate()
        self.year = self.dataSelezionata.year()
        self.day = self.dataSelezionata.day()
        self.month = self.dataSelezionata.month()