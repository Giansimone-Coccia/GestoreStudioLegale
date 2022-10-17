import os
import pickle

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea, \
    QMainWindow, QMessageBox

from GestoreStudioLegale.Sistema.CorsoAggiornamento import CorsoAggiornamento
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaSceltaCorso(QMainWindow):

    tool = Tools()
    avvoList = tool.loadAvvocati()

    def __init__(self, parent=None):
        super(VistaSceltaCorso, self).__init__(parent)
        self.cWidget = QWidget()
        self.outerLayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.scroll = QScrollArea()
        self.widget = QWidget()

        self.grifLayout = QGridLayout()

        self.outerLayout.addWidget(self.tool.rewindButton(self.rewind), 1)
        self.outerLayout.addLayout(self.button_layout, 1)
        self.outerLayout.addWidget(self.scroll, 8)
        self.cWidget.setLayout(self.outerLayout)

        self.getDatiCorso()
        self.widget.setLayout(self.grifLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.cWidget)
        self.setGeometry(600, 100, 1000, 900)
        self.resize(800, 600)
        self.setWindowTitle("Scelta corso aggiornamento")
        self.show()


    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeAvvocato import VistaHomeAvvocato
        self.vistaH3 = VistaHomeAvvocato()
        self.vistaH3.show()
        self.close()

    def getDatiCorso(self):
        self.corsiList = self.tool.loadCorsiAggiornamento()
        self.avvocatiList = self.tool.loadAvvocati()
        i = 1

        for corso in self.corsiList:
            self.textLabel2 = QLabel()
            self.textLabel2.setText(
                'Corso aggiornamento: ' + '\n' + 'NOME: ' + f"{corso.getDatiCorso()['Nome']}" + '\n' + 'CREDITI: ' + f"{corso.getDatiCorso()['Crediti']}" + '\n' + 'ID: ' + f"{corso.getDatiCorso()['ID']}" + '\n' + 'DATA ORA INIZIO: ' + f"{corso.getDatiCorso()['Data e Ora Inizio']}" + '\n' + 'DATA ORA FINE: ' + f"{corso.getDatiCorso()['Data e Ora Fine']}" + '\n' + 'TIPO CORSO: ' + f"{corso.getDatiCorso()['Tipo Corso']}")
            self.textLabel2.setGeometry(QRect(0, 0, 350, 20))
            self.textLabel2.setFont(QFont('Arial', 10))
            self.textLabel2.setStyleSheet("border: 1px solid black;")
            self.grifLayout.addWidget(self.textLabel2, i, 1, 1, 2)
            i += 1
            self.grifLayout.addWidget(
                self.tool.createButton("Seleziona", lambda checked, a=corso.getDatiCorso()['ID']: self.scegliCorso(a)), i, 2)
            i += 1

    def scegliCorso(self, id):
        if self.check():
            c = CorsoAggiornamento()
            for avvocato in self.avvoList:
                if self.tool.leggi().rsplit()[0] == avvocato.codiceFiscale:
                    avvocato.corsoAggiornamento = c.ricercaCorsoCodice(id)
                    avvocato.aggiornaAvvocato()
                    self.conferma()
        else:
            self.problema("Stai già seguendo un corso, terminalo prima di selezionarne uno nuovo")

    def check(self):
        for avvocato in self.avvoList:
            if self.tool.leggi().rsplit()[0] == avvocato.codiceFiscale:
                print(avvocato.corsoAggiornamento)
                print(type(avvocato.corsoAggiornamento))
                if avvocato.corsoAggiornamento == None:
                    return True
                else:
                    return False
        return False

    def conferma(self):
        msg = QMessageBox()
        msg.setWindowTitle("Corso confermato")
        msg.setText("Ha selezionato correttamente il corso")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeAvvocato import VistaHomeAvvocato
        self.vistaH4 = VistaHomeAvvocato()
        self.vistaH4.show()
        self.close()

    def problema(self, stringa):
        msg = QMessageBox()
        msg.setWindowTitle("Problema")
        msg.setText(stringa)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

