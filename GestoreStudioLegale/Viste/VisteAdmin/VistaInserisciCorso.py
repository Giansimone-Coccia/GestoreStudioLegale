import datetime
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QComboBox, QLineEdit, QCalendarWidget, QMessageBox

from GestoreStudioLegale.Sistema.CorsoAggiornamento import CorsoAggiornamento
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaInserisciCorso(QWidget):

    tool = Tools()
    avvocatiList = []
    corsoAvv = {}
    year = None
    month = None
    day = None

    def __init__(self, parent=None):
        super(VistaInserisciCorso, self).__init__(parent)
        gLayout = QGridLayout()
        gLayout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
        self.labelName = QLabel('<font size="4"> ID Corso aggiornamento </font>')
        self.labelName2 = QLabel('<font size="4"> Nome corso </font>')
        self.confirmButton = self.tool.createButton('Conferma corso', self.corsoOK)
        self.labelName4 = QLabel('<font size="4"> Avvocato corso </font>')
        self.labelCR = QLabel('<font size="4"> Crediti </font>')
        self.labelType = QLabel('<font size="4"> Tipo corso aggiornamento </font>')
        self.labelCRText = QLineEdit()
        self.labelCRText.setPlaceholderText("Inserisci numero crediti")
        self.labelTypeText = QLineEdit()
        self.labelTypeText.setPlaceholderText("Inserisci tipologia")
        self.labelID = QLabel('<font size="4"> Generato automaticamente </font>')
        self.labelNomeText = QLineEdit()
        self.labelNomeText.setPlaceholderText("Inserisci nome corso aggiornamento")
        self.ora = QComboBox()
        orari = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00',
                 '14:30', '15:00', '15:30', '16:00', '16:30', '17:00']
        self.ora.addItems(orari)
        self.calendar = QCalendarWidget()
        self.calendar.clicked.connect(self.selezionaData)
        self.dataSelezionata = None
        self.labelData = QLabel('<font size="4"> Data iniziale </font>')
        self.labelOra = QLabel('<font size="4"> Ora iniziale </font>')
        gLayout.addWidget(self.confirmButton, 8, 1)
        gLayout.addWidget(self.labelName, 2, 0)
        gLayout.addWidget(self.labelID, 2, 1)
        gLayout.addWidget(self.labelName2, 3, 0)
        gLayout.addWidget(self.labelNomeText, 3, 1)
        gLayout.addWidget(self.labelCR, 4, 0)
        gLayout.addWidget(self.labelCRText, 4, 1)
        gLayout.addWidget(self.labelType, 6, 0)
        gLayout.addWidget(self.labelTypeText, 6, 1)
        gLayout.addWidget(self.calendar, 1, 1)
        gLayout.addWidget(self.labelData, 1, 0)
        gLayout.addWidget(self.labelOra, 7, 0)
        gLayout.addWidget(self.ora, 7, 1)
        self.setLayout(gLayout)
        self.resize(800, 500)
        self.setWindowTitle("Inserimento corso")
        self.show()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeCorsoAgg import VistaHomeCorsoAgg
        self.vistaHome1 = VistaHomeCorsoAgg()
        self.vistaHome1.show()
        self.close()

    def corsoOK(self):
        corsoA = CorsoAggiornamento()
        hour = self.ora.currentText()
        if not self.convalida():
            hourDT = datetime.datetime.strptime(hour, "%H:%M")
            oraFine = hourDT + datetime.timedelta(hours=1)
            self.pyDate = datetime.datetime(int(self.year), int(self.month), int(self.day))
            dateF = self.pyDate + datetime.timedelta(weeks=4)
            dateIS = self.pyDate.strftime("%d/%m/%Y")
            dataOraInizio = dateIS + ',' + hour
            dataOraFine = dateF.strftime("%d/%m/%Y") + ',' + oraFine.strftime("%H:%M")
            corsoA.creaCorso(self.labelNomeText.text(), self.labelCRText.text(), self.tool.IdGenerator('CO'), dataOraInizio, dataOraFine, self.labelTypeText.text())
            self.conferma()
        else:
            self.problema()

    def conferma(self):
        msg = QMessageBox()
        msg.setWindowTitle("Corso confermato")
        msg.setText("Il suo corso è stato aggiunto correttamente")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeCorsoAgg import VistaHomeCorsoAgg
        self.vistaH2 = VistaHomeCorsoAgg()
        self.vistaH2.show()
        self.close()

    def problema(self):
        msg = QMessageBox()
        msg.setWindowTitle("Problema")
        msg.setText("Qualcosa è andato storto, riprova")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()


    def selezionaData(self):
        self.dataSelezionata = self.calendar.selectedDate()
        self.year = self.dataSelezionata.year()
        self.day = self.dataSelezionata.day()
        self.month = self.dataSelezionata.month()

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