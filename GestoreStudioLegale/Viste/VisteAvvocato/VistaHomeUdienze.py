from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QMainWindow, QScrollArea, QHBoxLayout

from GestoreStudioLegale.Utilities.Utilities import Tools

from GestoreStudioLegale.Viste.VisteAvvocato.VistaEliminaUdienze import VistaEliminaUdienze


class VistaHomeUdienze(QMainWindow):

    tool = Tools()

    def __init__(self, parent=None):
        super(VistaHomeUdienze, self).__init__(parent)

        self.cWidget = QWidget()
        self.outerLayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.scroll = QScrollArea()
        self.widget = QWidget()

        self.grifLayout = QGridLayout()

        self.outerLayout.addWidget(self.tool.rewindButton(self.rewind1), 1)
        self.outerLayout.addLayout(self.button_layout, 1)
        self.outerLayout.addWidget(self.scroll, 8)
        self.button_layout.addWidget(self.tool.createButton("Inserisci", self.aggiungiUdienza))
        self.button_layout.addWidget(self.tool.createButton("Cerca", self.cercaUdienza))
        self.cWidget.setLayout(self.outerLayout)

        self.getDatiU()
        self.widget.setLayout(self.grifLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.cWidget)
        self.setGeometry(600, 100, 1000, 900)
        self.resize(800, 600)
        self.setWindowTitle("Udienze")
        self.show()

    def getDatiU(self):
        self.udienzeList = self.tool.loadUdienze()
        self.avvocatiList = self.tool.loadAvvocati()
        self.clientiList = self.tool.loadClienti()
        tool = Tools()
        ud = []
        i=1

        for avvocato in self.avvocatiList:
            if avvocato.codiceFiscale == self.tool.leggi().rsplit()[0]:
               clienti = avvocato.getDatiAvvocato()['clienti']
               for cliente in clienti:
                   for udienza in self.udienzeList:
                      if udienza.Cliente.codiceFiscale == cliente.codiceFiscale:
                         ud.append(udienza)
        for u in ud:
            label = QLabel()
            textLabel2 = QLabel()
            print(u.getDatiUdienza()['Cliente'].getDatiCliente()['Nome'])
            print(u.getDatiUdienza()['Cliente'])
            textLabel2.setText(
                'Cliente: ' + '\n' + 'NOME: ' + f"{u.getDatiUdienza()['Cliente'].getDatiCliente()['Nome']}" + '\n' + 'COGNOME: ' + f"{u.getDatiUdienza()['Cliente'].getDatiCliente()['Cognome']}" + '\n' + 'ID: ' + f"{u.getDatiUdienza()['Cliente'].getDatiCliente()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{u.getDatiUdienza()['Cliente'].getDatiCliente()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{u.getDatiUdienza()['Cliente'].getDatiCliente()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{u.getDatiUdienza()['Cliente'].getDatiCliente()['Numero telefono']}")
            textLabel2.setGeometry(QRect(0, 0, 350, 20))
            textLabel2.setFont(QFont('Arial', 10))
            textLabel2.setStyleSheet("border: 1px solid black;")
            self.grifLayout.addWidget(textLabel2, i, 1, 1,2)
            i += 1
            dataIn = u.getDatiUdienza()['Data e Ora Inizio'].strftime("%m/%d/%Y, %H:%M:%S")
            dataFin = u.getDatiUdienza()['Data e Ora Fine'].strftime("%m/%d/%Y, %H:%M:%S")
            label.setText(
               'Udienza: ' + '\n' + 'CITTA TRIBUNALE: ' + f"{u.getDatiUdienza()['Città Tribunale']}" + '\n' + 'TIPO TRIBUNALE: ' + f"{u.getDatiUdienza()['Tipo Tribunale']}" + '\n' + 'ID: ' + f"{u.getDatiUdienza()['ID']}" + '\n' + 'DATA ORA INIZIO: ' + f"{dataIn}" + '\n' + 'DATA ORA FINE: ' + f"{dataFin}")
            label.setGeometry(QRect(0, 0, 350, 20))
            label.setFont(QFont('Arial', 10))
            label.setStyleSheet("border: 1px solid black;")
            self.grifLayout.addWidget(label,i,1,1,2)
            i += 1
            self.grifLayout.addWidget(tool.createButton("Modifica", lambda checked,  a = u: self.aggiornaUdienza(a)), i, 1)
            self.grifLayout.addWidget(
                tool.createButton("Elimina", lambda checked, a = u.getDatiUdienza()['ID']: self.rimuoviUdienza(a)),i,2)
            i += 1

    def aggiungiUdienza(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaIserisciUdienza import VistaInserisciUdienza
        self.vistaInserimento = VistaInserisciUdienza()
        self.vistaInserimento.show()
        self.close()

    def aggiornaUdienza(self, udienza):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaAggiornaUdienza import VistaAggiornaUdienza
        self.vistaAggiorna = VistaAggiornaUdienza()
        self.vistaAggiorna.udienza = udienza
        self.vistaAggiorna.show()
        self.close()

    def rimuoviUdienza(self, id):
        self.subWindow = VistaEliminaUdienze()
        self.subWindow.setData(id)
        self.subWindow.show()
        self.close()

    def cercaUdienza(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.RicercaUdienze import RicercaUdienze
        self.ricerca = RicercaUdienze()
        self.ricerca.show()
        self.close()

    def getDatiC(self):
        self.clientiList = self.tool.loadClienti()
        tool = Tools()
        print(tool.leggi())
        for cliente in self.clientiList:
            if cliente.codiceFiscale == str(tool.leggi()).rsplit()[0]:
                    return cliente.getDatiCliente()

    def rewind1(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeAvvocato import VistaHomeAvvocato
        self.vistaHome = VistaHomeAvvocato()
        self.vistaHome.show()
        self.close()