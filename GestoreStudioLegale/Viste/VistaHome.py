from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel


class VistaHome(QWidget):

    #Scegli stile PyQt così non varia tra ambienti diversi
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        gLayout = QGridLayout()
        textLabel = QLabel()
        textLabel.setText("Accedi come:")
        textLabel.setGeometry(QRect(100, 1200, 350, 40))
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
        pass

    def reachCliente(self):
        pass

    def reachAmministratore(self):
        pass