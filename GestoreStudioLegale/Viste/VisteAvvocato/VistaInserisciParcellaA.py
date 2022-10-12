import datetime

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QComboBox, QLineEdit, QCalendarWidget, QMessageBox

from GestoreStudioLegale.Servizi.Avvocato import Avvocato
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Servizi.Parcella import Parcella
from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeParcelle import VistaHomeParcelle


class VistaInserisciParcellaA(QWidget):
    tool = Tools()
    clientiList = []
    nomi = []

    def __init__(self, parent=None):
        super(VistaInserisciParcellaA, self).__init__(parent)
        gLayout = QGridLayout()
        gLayout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
        self.labelName = QLabel('<font size="4"> ID Parcella </font>')
        self.labelName2 = QLabel('<font size="4"> Intestatario Parcella </font>')
        self.confirmButton = self.tool.createButton('Conferma parcella', self.parcellaOK)
        self.menuClienti = QComboBox()
        self.menuClienti.addItems(self.sceltaClienti())
        self.labelName4 = QLabel('<font size="4"> Cliente parcella </font>')
        self.labelImporto = QLabel('<font size="4"> Importo </font>')
        self.labelIdent = QLabel('<font size="4"> Identificativo </font>')
        self.labelImportoText = QLineEdit()
        self.labelImportoText.setPlaceholderText("Inserisci importo parcella")
        self.labelIdentText = QLineEdit()
        self.labelIdentText.setPlaceholderText("Inserisci identificativo parcella")
        self.labelID = QLabel('<font size="4"> Generata automaticamente </font>')
        self.labelIntestText = QLineEdit()
        self.labelIntestText.setPlaceholderText("Inserisci intestatario parcella")
        gLayout.addWidget(self.confirmButton, 6, 1)
        gLayout.addWidget(self.labelName, 1, 0)
        gLayout.addWidget(self.labelID, 1, 1)
        gLayout.addWidget(self.labelName2, 2, 0)
        gLayout.addWidget(self.labelIntestText, 2, 1)
        gLayout.addWidget(self.menuClienti, 4, 1)
        gLayout.addWidget(self.labelName4, 4, 0)
        gLayout.addWidget(self.labelImporto, 3, 0)
        gLayout.addWidget(self.labelImportoText, 3, 1)
        gLayout.addWidget(self.labelIdent, 5, 0)
        gLayout.addWidget(self.labelIdentText, 5, 1)
        self.setLayout(gLayout)
        self.resize(700, 300)
        self.setWindowTitle("Parcelle")
        self.show()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeParcelle import VistaHomeParcelle
        self.vistaPHome = VistaHomeParcelle()
        self.vistaPHome.show()
        self.close()

    def sceltaClienti(self):
        self.clientiList = self.tool.loadClienti()
        self.nomi = []
        for cliente in self.clientiList:
            self.nomi.append(cliente.nome + ' ' + cliente.cognome)
        return self.nomi

    def parcellaOK(self):
        parcella = Parcella()
        ID = self.tool.IdGenerator('PA')
        cliente = self.ottieniCliente()
        if not self.convalida():    #Una volta creata una dalla vista, crasha e non parte neanche più il visualizza
            parcella.creaParcella(cliente, ID, int(self.labelIdentText.text()), int(self.labelImportoText.text()), self.labelIntestText.text())
            self.conferma()
            return

    def conferma(self):
        msg = QMessageBox()
        msg.setWindowTitle("Parcella confermata")
        msg.setText("la parcella è stata presa in carico")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        self.vistaH = VistaHomeParcelle()
        self.vistaH.show()
        self.close()

    def problema(self, messaggio):
        msg = QMessageBox()
        msg.setWindowTitle("Problema")
        msg.setText(messaggio)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def ottieniCliente(self):
        cliente = Cliente()
        nomeCognome = self.menuClienti.currentText()
        nome = nomeCognome.rsplit()[0]
        cognome = nomeCognome.rsplit()[1]
        return cliente.ricercaUtilizzatoreNomeCognome(nome, cognome)

    def convalida(self):
        try:
            if self.labelIntestText.text() == '':
                self.problema("Instestatario vuoto, riprova")
                return True
            elif self.labelIdentText.text() == '':
                self.problema("Identificativo vuoto, riprova")
                return True
            elif self.labelImportoText.text() == '':
                self.problema("Importo non inserito, riprova")
                return True
            elif not self.labelImportoText.text().isdigit():
                self.problema("L'importo non è intero, rirprova")
                return True
            elif not self.labelIdentText.text().isdigit():
                self.problema("Identificativo non intero, riprova")
                return True
        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle("ERRORE")
            msg.setText("Riprova")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            return