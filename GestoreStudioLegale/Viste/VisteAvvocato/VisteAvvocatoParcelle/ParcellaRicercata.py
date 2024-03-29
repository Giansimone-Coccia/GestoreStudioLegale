from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QMainWindow, QScrollArea

from GestoreStudioLegale.Utilities.Utilities import Tools

from GestoreStudioLegale.Viste.VisteAvvocato.VisteAvvocatoParcelle.VistaHomeParcelle import VistaHomeParcelle

class ParcellaRicercata(QMainWindow):

    avvocatiList = []
    clientiList = []
    parcelleList = []
    tool = Tools()

    def __init__(self, parcelle,parent=None):
        super(ParcellaRicercata, self).__init__(parent)
        tool = Tools()
        self.parcelleTrovate = []
        for parcella in parcelle:
            self.parcelleTrovate.append(parcella)

        self.cWidget = QWidget()
        self.outerLayout = QVBoxLayout()
        self.scroll = QScrollArea()
        self.widget = QWidget()

        self.grifLayout = QGridLayout()

        self.outerLayout.addWidget(tool.rewindButton(self.rewind), 1)
        self.outerLayout.addWidget(self.scroll, 9)
        self.cWidget.setLayout(self.outerLayout)

        self.getDatiP()
        self.widget.setLayout(self.grifLayout)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.cWidget)
        self.setGeometry(600, 100, 1000, 900)
        self.resize(800, 600)
        self.setWindowTitle("Parcelle")
        self.show()

    def aggiornaParcella(self, parcella):
        from GestoreStudioLegale.Viste.VisteAvvocato.VisteAvvocatoParcelle.VistaAggiornaParcella import VistaAggiornaParcella
        self.vistaAggiorna = VistaAggiornaParcella()
        self.vistaAggiorna.parcella = parcella
        self.vistaAggiorna.show()
        self.close()

    def getDatiC(self):
        self.clientiList = self.tool.loadClienti()
        tool = Tools()
        for cliente in self.clientiList:
            if cliente.codiceFiscale == str(tool.leggi()).rsplit()[0]:
                return cliente.getDatiCliente()

    def getDatiP(self):
        self.parcelleList = self.tool.loadParcelle()
        self.avvocatiList = self.tool.loadAvvocati()
        tool = Tools()
        i=1

        for par in self.parcelleTrovate:
            label = QLabel()
            textLabel2 = QLabel()
            textLabel2.setText(
                'Cliente: ' + '\n' + 'NOME: ' + f"{par.getDatiParcellaCliente()['Cliente'].getDatiCliente()['Nome']}" + '\n' + 'COGNOME: ' + f"{par.getDatiParcellaCliente()['Cliente'].getDatiCliente()['Cognome']}" + '\n' + 'ID: ' + f"{par.getDatiParcellaCliente()['Cliente'].getDatiCliente()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{par.getDatiParcellaCliente()['Cliente'].getDatiCliente()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{par.getDatiParcellaCliente()['Cliente'].getDatiCliente()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{par.getDatiParcellaCliente()['Cliente'].getDatiCliente()['Numero telefono']}")
            textLabel2.setGeometry(QRect(0, 0, 350, 20))
            textLabel2.setFont(QFont('Arial', 10))
            textLabel2.setStyleSheet("border: 1px solid black;")
            self.grifLayout.addWidget(textLabel2, i, 1, 1, 2)
            i += 1
            label.setText(
                'Parcella: '+'\n'+ 'INTESTATARIO: '+f"{par.getDatiParcellaCliente()['intestatario']}"+ '\n'+'IMPORTO: '+f"{par.getDatiParcellaCliente()['importo']}"+'€'+'\n'+'ID: '+f"{par.getDatiParcellaCliente()['ID']}"+'\n'+'IDENTIFICATIVO: '+f"{par.getDatiParcellaCliente()['identificativo']}")
            label.setGeometry(QRect(0, 0, 350, 20))
            label.setFont(QFont('Arial', 10))
            label.setStyleSheet("border: 1px solid black;")
            self.grifLayout.addWidget(label,i,1,1,2)
            i += 1
            self.grifLayout.addWidget(tool.createButton("Modifica", lambda checked,  a = par: self.aggiornaParcella(a)), i, 1)
            self.grifLayout.addWidget(
                tool.createButton("Elimina", self.rimuoviParcella),i,2)
            i += 1

    def rewind(self):
        self.vistaHome = VistaHomeParcelle()
        self.vistaHome.show()
        self.close()

    def rimuoviParcella(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VisteAvvocatoParcelle.VistaEliminaParcelle import VistaEliminaParcelle
        self.elimina = VistaEliminaParcelle()
        self.elimina.show()
        self.close()