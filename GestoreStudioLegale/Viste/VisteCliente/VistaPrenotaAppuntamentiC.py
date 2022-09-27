import datetime

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QGroupBox, QFormLayout, \
    QComboBox, QMainWindow, QCalendarWidget

from GestoreStudioLegale.Servizi.Appuntamento import Appuntamento
from GestoreStudioLegale.Servizi.Avvocato import Avvocato
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools

from GestoreStudioLegale.Viste.VisteCliente.VistaVisualizzaAppuntamento import VistaVisualizzaAppuntamento


class VistaPrenotaAppuntamentiC(QWidget):

    appuntamentiList = []
    avvocatiList = []
    nomi = []
    tool = Tools()
    year = None
    month = None
    day = None

    def __init__(self, parent=None):
        super(VistaPrenotaAppuntamentiC, self).__init__(parent)
        gLayout = QGridLayout()
        gLayout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
        self.labelName3 = QLabel('<font size="4"> Il sistema controllerà la disponibilità della data inserita </font>')
        self.labelName3.setStyleSheet("border: 1px solid black;")
        self.labelName = QLabel('<font size="4"> Data appuntamento </font>')
        self.labelName2 = QLabel('<font size="4"> Orario appuntamento </font>')
        self.lineEditOra = QLineEdit()
        self.lineEditOra.setPlaceholderText('Inserisci orario appuntamento')
        #self.ora = QComboBox()
        #orari = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00',
                 #'14:30', '15:00', '15:30', '16:00', '16:30', '17:00']
        #self.ora.addItems(orari)
        confirmButton = QPushButton()
        confirmButton = self.tool.createButton('Conferma appuntamento', self.confermaAppuntamento)
        self.menuAvvocati = QComboBox()
        self.menuAvvocati.addItems(self.sceltaAvv())
        self.labelName4 = QLabel('<font size="4"> Avvocato appuntamento </font>')
        self.lineEditType = QLineEdit()
        self.lineEditType.setPlaceholderText('Inserisci tipo procedimento(Penale,  civile...)')
        #self.procedimento = QComboBox()
        #procedimenti = ['Penale', 'Civile', 'Amministrativo', 'Giudiziario', 'Minorile']
        #self.procedimento.addItems(procedimenti)
        self.labelName5 = QLabel('<font size="4"> Tipo procedimento </font>')
        self.calendar = QCalendarWidget()
        self.calendar.clicked.connect(self.selezionaData)
        self.dataSelezionata = None
        gLayout.addWidget(confirmButton, 5, 1)
        gLayout.addWidget(self.labelName3, 0, 1)
        gLayout.addWidget(self.labelName, 1, 0)
        gLayout.addWidget(self.labelName2, 2, 0)
        gLayout.addWidget(self.lineEditOra, 2, 1)
        gLayout.addWidget(self.menuAvvocati, 4, 1)
        gLayout.addWidget(self.labelName4, 4, 0)
        gLayout.addWidget(self.lineEditType, 3, 1)
        gLayout.addWidget(self.calendar, 1, 1)
        gLayout.addWidget(self.labelName5, 3, 0)
        self.setLayout(gLayout)
        self.resize(800, 500)
        self.setWindowTitle("Prenotazione appuntamenti")
        self.show()

    def sceltaAvv(self):
        self.avvocatiList = self.tool.loadAvvocati()
        for avvocato in self.avvocatiList:
            self.nomi.append(avvocato.nome+' '+avvocato.cognome)
        return self.nomi

    def selezionaData(self):
        self.dataSelezionata = self.calendar.selectedDate()
        self.year = self.dataSelezionata.year()
        self.day = self.dataSelezionata.day()
        self.month = self.dataSelezionata.month()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteCliente.VistaHomeAppuntamentiC import VistaHomeAppuntamentiC
        self.vistaAppuntameti = VistaHomeAppuntamentiC()
        self.vistaAppuntameti.show()
        self.close()

    def confermaAppuntamento(self): #PERFETTO, AGGIUNGE AL FILE.pickle MA DOPO NON VISUALIZZA
        appuntamento = Appuntamento()
        client = Cliente()
        avvocato = Avvocato()
        avvocato = self.menuAvvocati.currentData(self.menuAvvocati.currentIndex())
        #print(avvocato)
        self.appuntamentiList = self.tool.loadAppuntamenti()
        if not self.convalida():
            #hour = str(self.ora.lineEdit().text())
            hour = self.lineEditOra.text()
            hourDT = datetime.datetime.strptime(hour, "%H:%M")
            oraFine = hourDT+datetime.timedelta(hours = 1)
            self.pyDate = datetime.datetime(int(self.year), int(self.month), int(self.day))
            dateS = self.pyDate.strftime("%d/%m/%Y")
            dataOraInizio = dateS+','+hour
            dataOraFine = dateS+','+oraFine.strftime("%H:%M")
            #id = 1234 #provvisorio
            for appuntamento in self.appuntamentiList:
                print(appuntamento.getDatiAppuntamento())
                if appuntamento.dataOraInizio == self.pyDate:
                    self.problema()
                    return
                else:
                    appuntamento.creaAppuntamento(client.ricercaUtilizzatoreCC(str(self.tool.leggi()).rsplit()[0]), avvocato, dataOraInizio, dataOraFine, self.tool.IdGenerator('A'), self.lineEditType.text())
                    self.conferma()
                    return

    def conferma(self):
        msg = QMessageBox()
        msg.setWindowTitle("Appuntamento confermato")
        msg.setText("Il suo appuntamento è stato confermato")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        self.vistaH = VistaVisualizzaAppuntamento()
        self.vistaH.show()
        self.close()

    def problema(self):
        msg = QMessageBox()
        msg.setWindowTitle("Problema")
        msg.setText("Range occupato, provare un orario o data differente")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def convalida(self):
          if self.year == None and self.month == None and self.day == None:
              msg = QMessageBox()
              msg.setWindowTitle("ERRORE")
              msg.setText("Data non selezionata, riprova")
              msg.setIcon(QMessageBox.Critical)
              msg.exec_()
              return
          try:
            date = self.pyDate = datetime.datetime(int(self.year), int(self.month), int(self.day))
            #hour = str(self.ora.lineEdit().text())
            hour = self.lineEditOra.text()
            hourT = datetime.datetime.strptime(hour, "%H:%M")
            timeMin = datetime.datetime.strptime('09:00', '%H:%M')
            timeMax = datetime.datetime.strptime('17:00', '%H:%M')
            condition = False
        #while condition:

            if date < datetime.datetime.now():
                msg = QMessageBox()
                msg.setWindowTitle("ERRORE")
                msg.setText("Data precedente all'attuale, riprova")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                condition = True
                return condition
            elif not date.__format__("%d/%m/%Y"):
                print('ciaoooooo')
                msg = QMessageBox()
                msg.setWindowTitle("ERRORE")
                msg.setText("Formato data errato, riprova (%d/%m/%Y)")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                condition = True
                return condition
            elif not hourT.__format__('%H:%M'):
                msg = QMessageBox()
                msg.setWindowTitle("ERRORE")
                msg.setText("Formato orario errato, riprova (%H:%M)")
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
            elif date.weekday() == 5 or date == 6:
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

