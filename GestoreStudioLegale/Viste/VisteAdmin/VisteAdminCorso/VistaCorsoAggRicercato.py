from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QMainWindow, QScrollArea

from GestoreStudioLegale.Utilities.Utilities import Tools

from GestoreStudioLegale.Viste.VisteAdmin.VisteAdminCorso.VistaHomeCorsoAgg import VistaHomeCorsoAgg

class VistaCorsoAggRicercato(QMainWindow):

    corsiAggList = []
    tool = Tools()

    def __init__(self, corsiAgg,parent=None):
        super(VistaCorsoAggRicercato, self).__init__(parent)
        self.corsiTrovati = []

        for corso in corsiAgg:
            self.corsiTrovati.append(corso)

        self.cWidget = QWidget()
        self.outerLayout = QVBoxLayout()
        self.scroll = QScrollArea()
        self.widget = QWidget()

        self.grifLayout = QGridLayout()

        self.outerLayout.addWidget(self.tool.rewindButton(self.rewind), 1)
        self.outerLayout.addWidget(self.scroll, 9)
        self.cWidget.setLayout(self.outerLayout)

        self.getDatiCo()
        self.widget.setLayout(self.grifLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.cWidget)
        self.setGeometry(600, 100, 1000, 900)
        self.resize(800, 600)
        self.setWindowTitle("Corsi Aggiornamento")
        self.show()

    def getDatiCo(self):
        self.corsiAggList = self.tool.loadCorsiAggiornamento()
        tool = Tools()
        i=1

        for corso in self.corsiTrovati:
            label = QLabel()
            label.setText(
                'Corso di aggiornamento: '+'\n'+ 'NOME CORSO: '+f"{corso.nome}"+ '\n'+'CREDITI: '+f"{corso.crediti}"+ '\n'+'ID: '+f"{corso.ID}"+'\n'+'DATA E ORA INIZIO: '+f"{corso.dataOraInizio}"+ '\n'+'DATA E ORA FINE: '+f"{corso.dataOraFine}"+ '\n'+'TIPOLOGIA: '+f"{corso.tipo}")
            label.setGeometry(QRect(0, 0, 350, 20))
            label.setFont(QFont('Arial', 10))
            label.setStyleSheet("border: 1px solid black;")
            self.grifLayout.addWidget(label,i,1,1,2)
            i += 1
            self.grifLayout.addWidget(tool.createButton("Elimina", lambda checked, a=corso.ID: self.rimuoviCorso(a)), i, 1)
            i += 1

    def rimuoviCorso(self,id):
        from GestoreStudioLegale.Viste.VisteAdmin.VisteAdminCorso.VistaEliminaCorsoAgg import VistaEliminaCorsoAgg
        self.vistaE = VistaEliminaCorsoAgg()
        self.vistaE.setData(id)
        self.vistaE.show()
        self.close()

    def rewind(self):
        self.vistaHome = VistaHomeCorsoAgg()
        self.vistaHome.show()
        self.close()