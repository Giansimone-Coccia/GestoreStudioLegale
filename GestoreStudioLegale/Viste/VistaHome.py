from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel

from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAdmin.LoginAdmin import LoginAdmin
from GestoreStudioLegale.Viste.VisteAvvocato.LoginAvvocato import LoginAvvocato
from GestoreStudioLegale.Viste.VisteCliente.LoginCliente import LoginCliente


class VistaHome(QWidget):

    tool = Tools()

    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        gLayout = QGridLayout()
        textLabel = QLabel()
        textLabel.setText("Accedi come:")
        textLabel.setGeometry(QRect(100, 120, 350, 40))
        textLabel.setFont(QFont('Arial', 12))
        gLayout.addWidget(textLabel, 0, 0)
        gLayout.addWidget(self.tool.createButton("Avvocato", self.reachAvvocato), 1, 0)
        gLayout.addWidget(self.tool.createButton("Cliente", self.reachCliente), 2, 0)
        gLayout.addWidget(self.tool.createButton("Amministratore", self.reachAmministratore), 3, 0)
        self.setLayout(gLayout)
        self.resize(500, 400)
        self.setWindowTitle("Gestore Studio Legale")
        self.show()

    def reachAmministratore(self):
        self.vistaAdmin = LoginAdmin()
        self.vistaAdmin.show()
        self.close()

    def reachAvvocato(self):
        self.vistaAvvocato = LoginAvvocato()
        self.vistaAvvocato.show()
        self.close()

    def reachCliente(self):
        self.vistaCliente = LoginCliente()
        self.vistaCliente.show()
        self.close()

