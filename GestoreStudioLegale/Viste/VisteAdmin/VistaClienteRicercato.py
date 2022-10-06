from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout

from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaClienti import VistaVisualizzaClienti


class VistaClienteRicercato(QWidget):

    cliente = Cliente()

    def __init__(self, parent=None):
        super(VistaClienteRicercato, self).__init__(parent)

        self.vistaVis = VistaVisualizzaClienti()
        self.tool = Tools()
        self.setWindowTitle('Ricerca cliente')
        self.resize(500, 120)
        self.grifLayout = QGridLayout()
        self.grifLayout.addWidget(self.tool.rewindButton(self.rewind), 0, 1)


    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaRicercaCliente import VistaRicercaCliente
        self.vistaHome = VistaRicercaCliente()
        self.vistaHome.show()
        self.close()

    def setData(self, cliente):
        self.cliente = cliente
        textLabel = QLabel()
        textLabel.setText(
            'Cliente: ' + '\n' + 'NOME: ' + f"{self.cliente.getDatiCliente()['Nome']}" + '\n' + 'COGNOME: ' + f"{self.cliente.getDatiCliente()['Cognome']}" + '\n' + 'DATA DI NASCITA: ' + f"{self.cliente.getDatiCliente()['Data nascita']}" + '\n' + 'ID: ' + f"{self.cliente.getDatiCliente()['Id']}" + '\n' + 'CODICE FISCALE: ' + f"{self.cliente.getDatiCliente()['Codice fiscale']}" + '\n' + 'EMAIL: ' + f"{self.cliente.getDatiCliente()['Email']}" + '\n' + 'NUMERO TELEFONO: ' + f"{self.cliente.getDatiCliente()['Numero telefono']}" + '\n' + 'PASSWORD: ' + f"{self.cliente.getDatiCliente()['Password']}")
        textLabel.setGeometry(QRect(0, 0, 350, 20))
        textLabel.setFont(QFont('Arial', 10))
        textLabel.setStyleSheet("border: 1px solid black;")
        self.grifLayout.addWidget(textLabel, 1, 1, 1, 2)
        self.grifLayout.addWidget(
            self.tool.createButton("Aggiorna", lambda checked, a=self.cliente: self.vistaVis.aggiornaCliente(a),method2=self.close), 2, 1)
        self.grifLayout.addWidget(
            self.tool.createButton("Elimina", lambda checked, b=self.cliente.getDatiCliente()['Id']: self.vistaVis.eliminaCliente(b),method2=self.close),2, 2)
        self.setLayout(self.grifLayout)