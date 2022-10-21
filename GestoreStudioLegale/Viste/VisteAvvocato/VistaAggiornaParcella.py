from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from GestoreStudioLegale.Servizi.Parcella import Parcella
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeParcelle import VistaHomeParcelle


class VistaAggiornaParcella(QWidget):

    tool = Tools()
    parcella = Parcella()
    parcelleList = tool.loadParcelle()
    cliente = Cliente()

    def __init__(self, parent = None):
        super(VistaAggiornaParcella, self).__init__(parent)
        self.setWindowTitle('Modifica Parcella')
        self.resize(500, 120)
        self.layout = QGridLayout()
        self.layout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)

        self.labelIntestatario = QLabel('<font size="4"> Nuovo intestatario </font>')
        self.labelImporto = QLabel('<font size="4"> Nuovo importo </font>')
        self.labelIntestTex = QLineEdit()
        self.labelIntestTex.setPlaceholderText("Inserisci nuovo intestatario")
        self.labelImportoTex = QLineEdit()
        self.labelImportoTex.setPlaceholderText("Inserisci nuovo importo")

        self.confirmButton = QPushButton()
        self.confirmButton = self.tool.createButton('Conferma Parcella', self.confermaParcella)

        self.layout.addWidget(self.confirmButton, 3, 1, 1, 2)
        self.layout.addWidget(self.labelIntestatario, 1, 0)
        self.layout.addWidget(self.labelImporto, 2, 0)
        self.layout.addWidget(self.labelIntestTex, 1, 2,)
        self.layout.addWidget(self.labelImportoTex, 2, 2)
        self.setLayout(self.layout)

    def rewind(self):
        self.vistaHome = VistaHomeParcelle()
        self.vistaHome.show()
        self.close()

    def confermaParcella(self):

        for parcella in self.parcelleList:
            if parcella.ID == self.parcella.ID:
                nuovoIntestatario = self.labelIntestTex.text()
                nuovoImporto = self.labelImportoTex.text()
                parcella1 = Parcella()
                parcella1 = parcella
                condizione1 = self.labelIntestTex.text() != str(self.parcella.intestatario)
                condizione2 = self.labelImportoTex.text() != str(self.parcella.importo)
                condizione3 = self.labelImportoTex.text().isdigit()
                if (condizione1 or condizione2):
                    if (condizione3):
                        parcella1.importo = nuovoImporto
                        parcella1.intestatario = nuovoIntestatario
                        parcella.rimuoviParcella(self.parcella.ID)
                        parcella1.creaParcella(self.parcella.Cliente, self.parcella.ID, self.parcella.identificativo,
                                               nuovoImporto, nuovoIntestatario)
                        self.conferma()
                    else:
                        self.problema("Importo non intero")
                else:
                    self.problema("Immessi gli stessi dati")


    def conferma(self):
        msg = QMessageBox()
        msg.setWindowTitle("Parcella confermata")
        msg.setText("La sua parcella è stata modificata con successo")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        self.vistaPrima = VistaHomeParcelle()
        self.vistaPrima.show()
        self.close()

    def problema(self, messaggio):
        msg = QMessageBox()
        msg.setWindowTitle("ERRORE")
        msg.setText(messaggio)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()