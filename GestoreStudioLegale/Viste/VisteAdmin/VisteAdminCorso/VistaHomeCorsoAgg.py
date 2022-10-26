from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QScrollArea, QGridLayout, QLabel

from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaHomeCorsoAgg(QMainWindow):

    tool = Tools()

    def __init__(self, parent=None):
        super(VistaHomeCorsoAgg, self).__init__(parent)

        self.cWidget = QWidget()
        self.outerLayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.scroll = QScrollArea()
        self.widget = QWidget()

        self.grifLayout = QGridLayout()

        self.outerLayout.addWidget(self.tool.rewindButton(self.rewind), 1)
        self.outerLayout.addLayout(self.button_layout, 1)
        self.outerLayout.addWidget(self.scroll, 8)
        self.button_layout.addWidget(self.tool.createButton("Inserisci", self.inserisciCorso))
        self.button_layout.addWidget(self.tool.createButton("Cerca", self.cercaCorso))
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
        self.setWindowTitle("Corsi aggiornamento")
        self.show()

    def cercaCorso(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VisteAdminCorso.VistaRicercaCorsoAgg import VistaRicercaCorsoAgg
        self.vistaCorso = VistaRicercaCorsoAgg()
        self.vistaCorso.show()
        self.close()

    def getDatiCorso(self):
        self.corsiList = self.tool.loadCorsiAggiornamento()
        self.avvocatiList = self.tool.loadAvvocati()
        i = 1

        for corso in self.corsiList:
            textLabel2 = QLabel()
            textLabel2.setText(
                'Corso aggiornamento: ' + '\n' + 'NOME: ' + f"{corso.getDatiCorso()['Nome']}" + '\n' + 'CREDITI: ' + f"{corso.getDatiCorso()['Crediti']}" + '\n' + 'ID: ' + f"{corso.getDatiCorso()['ID']}" + '\n' + 'DATA ORA INIZIO: ' + f"{corso.getDatiCorso()['Data e Ora Inizio']}" + '\n' + 'DATA ORA FINE: ' + f"{corso.getDatiCorso()['Data e Ora Fine']}" + '\n' + 'TIPO CORSO: ' + f"{corso.getDatiCorso()['Tipo Corso']}")
            textLabel2.setGeometry(QRect(0, 0, 350, 20))
            textLabel2.setFont(QFont('Arial', 10))
            textLabel2.setStyleSheet("border: 1px solid black;")
            self.grifLayout.addWidget(textLabel2, i, 1, 1, 2)
            i += 1
            self.grifLayout.addWidget(self.tool.createButton("Elimina", lambda checked, a=corso.getDatiCorso()['ID']: self.rimuoviCorso(a)), i, 2)
            i += 1

    def inserisciCorso(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VisteAdminCorso.VistaInserisciCorso import VistaInserisciCorso
        self.vistaIn = VistaInserisciCorso()
        self.vistaIn.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeAdmin import VistaHomeAdmin
        self.vistaHome = VistaHomeAdmin()
        self.vistaHome.show()
        self.close()

    def rimuoviCorso(self, id):
        from GestoreStudioLegale.Viste.VisteAdmin.VisteAdminCorso.VistaEliminaCorsoAgg import VistaEliminaCorsoAgg
        self.vistaE = VistaEliminaCorsoAgg()
        self.vistaE.setData(id)
        self.vistaE.show()
        self.close()