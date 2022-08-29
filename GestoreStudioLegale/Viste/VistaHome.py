from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel

from GestoreStudioLegale.Viste.LoginAdmin import LoginAdmin
from GestoreStudioLegale.Viste.LoginAvvocato import LoginAvvocato
from GestoreStudioLegale.Viste.LoginCliente import LoginCliente


class VistaHome(QWidget):

    #Scegli stile PyQt così non varia tra ambienti diversi
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        gLayout = QGridLayout()
        textLabel = QLabel()
        textLabel.setText("Accedi come:")
        textLabel.setGeometry(QRect(100, 120, 350, 40))
        textLabel.setFont(QFont('Arial', 12))
        gLayout.addWidget(textLabel, 0, 0)
        gLayout.addWidget(self.createButton("Avvocato", self.reachAvvocato), 1, 0)
        gLayout.addWidget(self.createButton("Cliente", self.reachCliente), 2, 0)
        gLayout.addWidget(self.createButton("Amministratore", self.reachAmministratore), 3, 0)
        self.setLayout(gLayout)
        self.resize(500, 400)
        self.setWindowTitle("Gestore Studio Legale")
        self.show()

    def createButton(self, nome, on_click):
        button = QPushButton(nome)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setFont(QFont('Arial', 10))
        button.clicked.connect(on_click)
        return button

    def reachAvvocato(self):
        wid = QWidget()
        self.vistaLoginAvvocato = LoginAvvocato()
        self.vistaLoginAvvocato.setupUi(wid)
        # self.vistaLoginCliente.retranslateUi(wid)
        wid.show()

    def reachCliente(self):
        wid = QWidget()
        self.vistaLoginCliente = LoginCliente()
        self.vistaLoginCliente.setupUi(wid)
        #self.vistaLoginCliente.retranslateUi(wid)
        wid.show()

    def reachAmministratore(self):
        wid = QWidget()
        self.vistaLoginAdmin = LoginAdmin()
        self.vistaLoginAdmin.setupUi(wid)
        # self.vistaLoginCliente.retranslateUi(wid)
        wid.show()