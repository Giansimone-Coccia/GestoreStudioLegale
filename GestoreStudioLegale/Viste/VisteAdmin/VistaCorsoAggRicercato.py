from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QMainWindow, QScrollArea

from GestoreStudioLegale.Utilities.Utilities import Tools

from GestoreStudioLegale.Viste.VisteAdmin.VistaHomeCorsoAgg import VistaHomeCorsoAgg

class VistaCorsoAggRicercato(QMainWindow):

    corsiAggList = []
    #avvocatiList = []
    #clientiList = []
    tool = Tools()

    def __init__(self, corsiAgg,parent=None):
        super(VistaCorsoAggRicercato, self).__init__(parent)
        tool = Tools()

        self.corsiTrovati = []

        for corso in corsiAgg:
            self.corsiTrovati.append(corso)


        self.cWidget = QWidget()
        self.outerLayout = QVBoxLayout()
        #self.button_layout = QHBoxLayout()
        self.scroll = QScrollArea()
        self.widget = QWidget()

        self.grifLayout = QGridLayout()

        self.outerLayout.addWidget(tool.rewindButton(self.rewind1), 1)
        #self.outerLayout.addLayout(self.button_layout, 1)
        self.outerLayout.addWidget(self.scroll, 9)
        #self.button_layout.addWidget(tool.createButton("Inserisci", self.aggiungiParcella))
        #self.button_layout.addWidget(tool.createButton("Cerca", self.cercaParcella))
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
        self.avvocatiList = self.tool.loadAvvocati()
        tool = Tools()
        i=1

        for corso in self.corsiTrovati:
            label = QLabel()
            label.setText(
                'Corso di aggiornamento: '+'\n'+ 'NOME CORSO: '+f"{corso.getDatiCorso['Nome']}"+ '\n'+'CREDITI: '+f"{corso.getDatiCorso['Crediti']}"+ '\n'+'ID: '+f"{corso.getDatiCorso['ID']}"+'\n'+'DATA E ORA INIZIO: '+f"{corso.getDatiCorso['Data e Ora Inizio']}"+ '\n'+'DATA E ORA FINE: '+f"{corso.getDatiCorso['Data e Ora Fine']}"+ '\n'+'TIPOLOGIA: '+f"{corso.getDatiCorso['Tipo Corso']}")
            label.setGeometry(QRect(0, 0, 350, 20))
            label.setFont(QFont('Arial', 10))
            label.setStyleSheet("border: 1px solid black;")
            self.grifLayout.addWidget(label,i,1,1,2)
            i += 1
            #self.grifLayout.addWidget(tool.createButton("Modifica", lambda checked,  a = corso: self.aggiornaCorso(a)), i, 1)
            self.grifLayout.addWidget(tool.createButton("Elimina", self.rimuoviCorso),i,1)
            i += 1

    '''
    def aggiornaCorso(self, corso):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaAggiornaParcella import VistaAggiornaParcella
        self.vistaAggiorna = VistaAggiornaParcella()
        self.vistaAggiorna.parcella = corso
        self.vistaAggiorna.show()
        self.close()
    '''

    def rimuoviCorso(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaEliminaCorsoAgg import VistaEliminaCorsoAgg
        self.elimina = VistaEliminaCorsoAgg()
        self.elimina.show()
        self.close()

    '''def getDatiC(self):
        self.clientiList = self.tool.loadClienti()
        tool = Tools()
        for cliente in self.clientiList:
            if cliente.codiceFiscale == str(tool.leggi()).rsplit()[0]:
                    return cliente.getDatiCliente()
    '''
    def rewind1(self):
        self.vistaHome = VistaHomeCorsoAgg()
        self.vistaHome.show()
        self.close()