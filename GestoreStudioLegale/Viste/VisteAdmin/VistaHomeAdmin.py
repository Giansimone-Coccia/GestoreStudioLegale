from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy


class VistaHomeAdmin(QWidget):

    def __init__(self, parent=None):
        super(VistaHomeAdmin, self).__init__(parent)
        gLayout = QGridLayout()
        gLayout.addWidget(self.createButton("Modifica Password", self.reachModificaPassword), 0, 0)
        gLayout.addWidget(self.createButton("Avvocati", self.reachAvvocati), 1, 0)
        gLayout.addWidget(self.createButton("Clienti", self.reachClienti), 2, 0, 1, 2)
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

    def reachModificaPassword(self):
        self.vistaModPaasword = VistaModificaPassword()
        self.vistaModPaasword.show()
        self.close()

    def reachAvvocati(self):
        self.vistaVisualizzaA = VistaVisualizzaAvvocati()
        self.vistaVisualizzaA.show()
        self.close()

    def reachClienti(self):
        self.vistaVisualizzaC = VistaVisualizzaClienti()
        self.vistaVisualizzaC.show()
        self.close()