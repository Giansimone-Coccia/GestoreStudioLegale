import datetime

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from GestoreStudioLegale.Utilities.Utilities import Tools
import os
import pickle

from GestoreStudioLegale.Viste.VisteCliente.VistaVisualizzaAppuntamento import VistaVisualizzaAppuntamento


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

    def confermaAppuntamento(self):
        self.loadDateA()
        if not self.convalida():
            date = self.lineEditDate.text()
            hour = self.lineEditOra.text()
            dateHour = date+' '+hour
            dateHour1 = datetime.datetime.strptime(dateHour, "%d/%m/%Y %H:%M")
            for appuntamento in self.appuntamentiList:
                print(appuntamento.dataOraInizio)
                if appuntamento.dataOraInizio == dateHour1:
                    self.problema()
                    return
                else:
                    self.conferma()
                    return

    def loadDateA(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Appuntamenti.pickle'):
            with open('GestoreStudioLegale/Dati/Appuntamenti.pickle', 'rb') as f:
                self.appuntamentiList = list(pickle.load(f))

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
        date = self.lineEditDate.text()
        hour = self.lineEditOra.text()
        dateT = datetime.datetime.strptime(date, "%d/%m/%Y")
        hourT = datetime.datetime.strptime(hour, "%H:%M")
        timeMin = datetime.datetime.strptime('09:00', '%H:%M')
        timeMax = datetime.datetime.strptime('17:00', '%H:%M')
        condition = False
        #while condition:
        try:
            if dateT < datetime.datetime.now():
                msg = QMessageBox()
                msg.setWindowTitle("ERRORE")
                msg.setText("Data precedente all'attuale, riprova")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                condition = True
                return condition
            elif not dateT.__format__("%d/%m/%Y"):
                msg = QMessageBox()
                msg.setWindowTitle("ERRORE")
                msg.setText("Formato data errato, riprova (%d/%m/%Y)")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                condition = True
                return condition
            elif not hourT.__format__("%H:%M"):
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
            elif dateT.weekday() == 5 or dateT == 6:
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

