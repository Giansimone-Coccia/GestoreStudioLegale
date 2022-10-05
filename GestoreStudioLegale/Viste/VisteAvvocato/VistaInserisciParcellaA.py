import datetime

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QComboBox, QLineEdit, QCalendarWidget, QMessageBox

from GestoreStudioLegale.Servizi.Avvocato import Avvocato
from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeParcelle import VistaHomeParcelle


class VistaInserisciParcellaA(QWidget):
    tool = Tools()
    clientiList = []
    nomi = []
    udienzeList = []

    def __init__(self, parent=None):
        super(VistaInserisciParcellaA, self).__init__(parent)
        gLayout = QGridLayout()
        gLayout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
        self.labelName = QLabel('<font size="4"> ID Parcella </font>')
        self.labelName2 = QLabel('<font size="4"> Intestatario Parcella </font>')
        #self.ora = QComboBox()
        #orari = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00',
         #        '14:30', '15:00', '15:30', '16:00', '16:30', '17:00']
        #self.ora.addItems(orari)
        print("ciao34")
        self.confirmButton = self.tool.createButton('Conferma parcella', self.parcellaOK)
        print("ciao35")
        self.menuClienti = QComboBox()
        self.menuClienti.addItems(self.sceltaClienti())
        self.labelName4 = QLabel('<font size="4"> Cliente parcella </font>')
        #self.procedimento = QComboBox()
        #procedimenti = ['Penale', 'Civile', 'Amministrativo', 'Giudiziario', 'Minorile']
        #self.procedimento.addItems(procedimenti)
        self.labelImporto = QLabel('<font size="4"> Importo </font>')
        self.labelIdent = QLabel('<font size="4"> Identificativo </font>')
        self.labelImportoText = QLineEdit()
        self.labelImportoText.setPlaceholderText("Inserisci importo parcella")
        self.labelIDText = QLineEdit()
        self.labelIDText.setPlaceholderText("Inserisci ID parcella")
        self.labelIntestText = QLineEdit()
        self.labelIntestText.setPlaceholderText("Inserisci intestatario parcella")
        #self.calendar = QCalendarWidget()
        #self.calendar.clicked.connect(self.selezionaData)
        #self.dataSelezionata = None
        gLayout.addWidget(self.confirmButton, 6, 1)
        gLayout.addWidget(self.labelName, 1, 0)
        gLayout.addWidget(self.labelIDText, 1, 1)
        gLayout.addWidget(self.labelName2, 2, 0)
        gLayout.addWidget(self.labelIntestText, 2, 1)
        #gLayout.addWidget(self.ora, 2, 1)
        gLayout.addWidget(self.menuClienti, 4, 1)
        gLayout.addWidget(self.labelName4, 4, 0)
        gLayout.addWidget(self.labelImporto, 3, 0)
        gLayout.addWidget(self.labelImportoText, 3, 1)
        #gLayout.addWidget(self.calendar, 1, 1)
        #gLayout.addWidget(self.labelName5, 3, 0)
        #gLayout.addWidget(self.labelCitta, 5, 0)
        #gLayout.addWidget(self.labelCittaText, 5, 1)
        self.setLayout(gLayout)
        self.resize(700, 300)
        self.setWindowTitle("Parcelle")
        self.show()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeParcelle import VistaHomeParcelle
        self.vistaPHome = VistaHomeParcelle()
        self.vistaPHome.show()
        self.close()

    #def selezionaData(self):
        #self.dataSelezionata = self.calendar.selectedDate()
        #self.year = self.dataSelezionata.year()
        #self.day = self.dataSelezionata.day()
        #self.month = self.dataSelezionata.month()

    def sceltaClienti(self):
        self.clientiList = self.tool.loadClienti()
        for cliente in self.clientiList:
            self.nomi.append(cliente.nome + ' ' + cliente.cognome)
        return self.nomi

    def parcellaOK(self):
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
                print(udienza.getDatiUdienza())
                if udienza.dataOraInizio == self.pyDate:
                    self.problema()
                    return
                else:
                    udienza.creaUdienza(avvocato.ricercaUtilizzatoreCC(str(self.tool.leggi()).rsplit()[0]),
                                        self.labelCittaText.text(), self.menuClienti.currentText(), dataOraInizio,
                                    dataOraFine, ID, self.procedimento.currentText())
                    # print(udienza.getDatiUdienza())
                    self.conferma()
                    return

    def conferma(self):
        msg = QMessageBox()
        msg.setWindowTitle("Udienza confermata")
        msg.setText("L'udienza è stata presa in carico")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        self.vistaH = VistaHomeParcelle()
        self.vistaH.show()
        self.close()

    def problema(self):
        msg = QMessageBox()
        msg.setWindowTitle("Problema")
        msg.setText("Problema con l'inserimento, riprovare")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def convalida(self):
        if self.year is None and self.month is None and self.day is None:
            msg = QMessageBox()
            print("ecco 7")
            msg.setWindowTitle("ERRORE")
            msg.setText("Data non selezionata, riprova")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            # self.rewind()
            return True
        try:
            print(self.year)
            print(self.day)
            print(self.month)
            date = self.pyDate = datetime.datetime(int(self.year), int(self.month), int(self.day))
            hour = self.ora.currentText()
            hourT = datetime.datetime.strptime(hour, "%H:%M")
            timeMin = datetime.datetime.strptime('09:00', '%H:%M')
            timeMax = datetime.datetime.strptime('17:00', '%H:%M')
            condition = False
            # while condition:
            if date < datetime.datetime.now():
                print("nel primo if")
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
            return