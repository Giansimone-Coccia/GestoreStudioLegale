from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaAggiungiClienteEsistente(QWidget):

    tool = Tools()

    def __init__(self,parent = None):
        super(VistaAggiungiClienteEsistente, self).__init__(parent)

        self.setWindowTitle('Ricerca cliente da aggiungere')
        self.resize(500, 120)
        layout = QGridLayout()
        layout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
        textLabel = QLabel()
        textLabel.setText(f"Inserisci l'id del cliente da aggiungere:")
        textLabel.setGeometry(QRect(100, 120, 350, 40))
        textLabel.setFont(QFont('Arial', 10))
        layout.addWidget(textLabel, 1, 0,1,3)
        self.labelIdC = QLabel('<font size="4"> Id cliente </font>')
        self.lineEditIdC = QLineEdit()
        self.lineEditIdC.setPlaceholderText("Inserisci l'id dell'cliente da aggiungere")
        layout.addWidget(self.labelIdC, 2, 0)
        layout.addWidget(self.lineEditIdC, 2, 1)
        self.buttonLogin = QPushButton('Conferma')
        layout.addWidget(self.buttonLogin, 3, 0, 1, 3)
        layout.setRowMinimumHeight(2, 75)
        self.buttonLogin.clicked.connect(self.aggiungiCliente)
        self.setLayout(layout)

    def aggiungiCliente(self):
        cliente = Cliente()
        self.tool =Tools()

        if cliente.ricercaUtilizzatoreId(self.lineEditIdC.text()) is None:
            msg = QMessageBox()
            msg.setWindowTitle('Cliente non trovato')
            msg.setText('Non esiste alcun cliente con questo id')
            msg.exec()
            return
        else:
            self.avvocatiList = self.tool.loadAvvocati()
            for avvocato in self.avvocatiList:
                if avvocato.codiceFiscale == self.tool.leggi().rsplit()[0]:
                    avvocato.clienti.append(cliente.ricercaUtilizzatoreId(self.lineEditIdC.text()))
                    avvocato.aggiornaAvvocato()
                    msg = QMessageBox()
                    msg.setWindowTitle('Cliente aggiunto')
                    msg.setText('Cliente aggiunto con successo')
                    msg.exec()
                    return

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VisteAvvocatoCliente.VistaAggiungiCliente import \
            VistaAggiungiCliente
        self.vistaH = VistaAggiungiCliente()
        self.vistaH.show()
        self.close()