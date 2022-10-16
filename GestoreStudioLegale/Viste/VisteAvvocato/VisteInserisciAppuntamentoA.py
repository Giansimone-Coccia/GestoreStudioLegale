import datetime

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QMessageBox, \
    QComboBox, QCalendarWidget

from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools


class VisteInserisciAppuntamentoA(QWidget):

    appuntamentiList = []
    clientiList = []
    nomi = []
    tool = Tools()
    year = None
    month = None
    day = None

    def __init__(self, parent=None):
        super(VisteInserisciAppuntamentoA, self).__init__(parent)
        gLayout = QGridLayout()
        gLayout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
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
        self.menuClienti = QComboBox()
        self.menuClienti.addItems(self.sceltaClienti())
        self.labelName4 = QLabel('<font size="4"> Cliente appuntamento </font>')
        self.procedimento = QComboBox()
        procedimenti = ['Penale', 'Civile', 'Amministrativo', 'Giudiziario', 'Minorile']
        self.procedimento.addItems(procedimenti)
        self.labelName5 = QLabel('<font size="4"> Tipo procedimento </font>')
        self.calendar = QCalendarWidget()
        self.calendar.clicked.connect(self.selezionaData)
        self.dataSelezionata = None
        gLayout.addWidget(confirmButton, 5, 1)
        gLayout.addWidget(self.labelName3, 0, 1)
        gLayout.addWidget(self.labelName, 1, 0)
        gLayout.addWidget(self.labelName2, 2, 0)
        gLayout.addWidget(self.ora, 2, 1)
        gLayout.addWidget(self.menuClienti, 4, 1)
        gLayout.addWidget(self.labelName4, 4, 0)
        gLayout.addWidget(self.procedimento, 3, 1)
        gLayout.addWidget(self.calendar, 1, 1)
        gLayout.addWidget(self.labelName5, 3, 0)
        self.setLayout(gLayout)
        self.resize(800, 500)
        self.setWindowTitle("Prenotazione appuntamenti")
        self.show()

    def sceltaClienti(self):
        tool=Tools()
        self.avvocatiList = tool.loadAvvocati()
        for avvocato in self.avvocatiList:
            if avvocato.codiceFiscale == tool.leggi().rsplit()[0]:
                self.clientiList = avvocato.clienti

        self.nomi = []
        for cliente in self.clientiList:
            self.nomi.append(cliente.nome+' '+cliente.cognome)
        return self.nomi

    def selezionaData(self):
        self.dataSelezionata = self.calendar.selectedDate()
        self.year = self.dataSelezionata.year()
        self.day = self.dataSelezionata.day()
        self.month = self.dataSelezionata.month()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeAppuntamentiA import VistaHomeAppuntamentiA
        self.vistaAppuntameti = VistaHomeAppuntamentiA()
        self.vistaAppuntameti.show()
        self.close()

    def confermaAppuntamento(self):
        client = Cliente()
        clienti = self.menuClienti.currentText()
        hour = self.ora.currentText()
        self.appuntamentiList = self.tool.loadAppuntamenti()
        if not self.convalida():
            hourDT = datetime.datetime.strptime(hour, "%H:%M")
            oraFine = hourDT+datetime.timedelta(minutes = 30)
            self.pyDate = datetime.datetime(int(self.year), int(self.month), int(self.day))
            dateS = self.pyDate.strftime("%d/%m/%Y")
            dataOraInizio = dateS+','+hour
            dataOraFine = dateS+','+oraFine.strftime("%H:%M")
            for appuntamento in self.appuntamentiList:
                if appuntamento.dataOraInizio == self.pyDate:
                    self.problema()
                    return
                else:
                    cliente = Cliente()
                    cliente1 = Cliente()
                    tool = Tools()
                    for avvocato in self.avvocatiList:
                        if avvocato.codiceFiscale == tool.leggi().rsplit()[0]:
                            self.avv = avvocato
                    appuntamento.creaAppuntamento(cliente.ricercaUtilizzatoreNomeCognome(nome =self.menuClienti.currentText().rsplit()[0], cognome = self.menuClienti.currentText().rsplit()[1]), self.avv, dataOraInizio, dataOraFine, self.tool.IdGenerator('A'), self.procedimento.currentText())

                    self.avvocatiList = tool.loadAvvocati()

                    for avvocato in self.avvocatiList:
                        if avvocato.codiceFiscale == self.tool.leggi().rsplit()[0]:
                            for app in avvocato.appuntamentiAvvocato:
                                if app.dataOraInizio == appuntamento.dataOraInizio:
                                    msg = QMessageBox()
                                    msg.setWindowTitle("Orario non disponibile")
                                    msg.setText("Questo orario è già occupato")
                                    msg.setIcon(QMessageBox.Information)
                                    msg.exec_()
                                    return
                            avvocato.appuntamentiAvvocato.append(appuntamento)
                            avvocato.aggiornaAvvocato()
                    self.conferma()
                    return

    def conferma(self):
        msg = QMessageBox()
        msg.setWindowTitle("Appuntamento confermato")
        msg.setText("Il suo appuntamento è stato confermato")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeAppuntamentiA import VistaHomeAppuntamentiA
        self.vistaH = VistaHomeAppuntamentiA()
        self.vistaH.show()
        self.close()

    def problema(self):
        msg = QMessageBox()
        msg.setWindowTitle("Problema")
        msg.setText("Range occupato, provare un orario o data differente")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

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