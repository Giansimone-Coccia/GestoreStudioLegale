from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, \
    QLineEdit, QPushButton, QMessageBox


from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaRicercaCliente(QWidget):

    tool = Tools()

    def __init__(self, parent=None):
        super(VistaRicercaCliente, self).__init__(parent)

        self.setWindowTitle('Ricerca cliente')
        self.resize(500, 120)
        layout = QGridLayout()
        layout.addWidget(self.tool.rewindButton(self.rewind), 0, 0)
        textLabel = QLabel()
        textLabel.setText(f"Inserisci l'id del cliente da ricercare:")
        textLabel.setGeometry(QRect(100, 120, 350, 40))
        textLabel.setFont(QFont('Arial', 10))
        layout.addWidget(textLabel, 1, 0,1,3)
        self.labelIdC = QLabel('<font size="4"> Id cliente </font>')
        self.lineEditIdC = QLineEdit()
        self.lineEditIdC.setPlaceholderText("Inserisci l'id dell'cliente")
        layout.addWidget(self.labelIdC, 2, 0)
        layout.addWidget(self.lineEditIdC, 2, 1)
        self.buttonLogin = QPushButton('Conferma')
        layout.addWidget(self.buttonLogin, 3, 0, 1, 3)
        layout.setRowMinimumHeight(2, 75)
        self.buttonLogin.clicked.connect(self.ricercaCliente)
        self.setLayout(layout)

    def ricercaCliente(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VisteAdminCliente.VistaClienteRicercato import VistaClienteRicercato
        cliente = Cliente()

        if cliente.ricercaUtilizzatoreId(self.lineEditIdC.text()) is None:
            msg = QMessageBox()
            msg.setWindowTitle('Cliente non trovato')
            msg.setText('Non esiste alcun cliente con questo id')
            msg.exec()
            return
        else:
            self.subWindow = VistaClienteRicercato()
            cliente = cliente.ricercaUtilizzatoreId(self.lineEditIdC.text())
            self.subWindow.setData(cliente)
            self.subWindow.show()
            self.close()




    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VisteAdminCliente.VistaVisualizzaClienti import VistaVisualizzaClienti
        self.vistaHome = VistaVisualizzaClienti()
        self.vistaHome.show()
        self.close()