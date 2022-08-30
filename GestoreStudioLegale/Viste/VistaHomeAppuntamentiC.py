from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from GestoreStudioLegale.Viste.VistaVisualizzaAppuntamento import VistaVisualizzaAppuntamento


class VistaHomeAppuntamenti(QWidget):

    def __init__(self, parent=None):
        super(VistaHomeAppuntamenti, self).__init__(parent)
        gLayout = QGridLayout()
        gLayout.addWidget(self.createButton("Prenota Appuntamento", self.reachPrenotaAppuntamento()), 0, 0)
        gLayout.addWidget(self.createButton("Visualizza Appuntamento", self.reachVisualizzaAppuntamento()), 1, 0)
        self.setLayout(gLayout)
        self.resize(500, 400)
        self.setWindowTitle("Gestore Studio Legale")
        self.show()

    def createButton(self, nome, on_click):
        button = QPushButton(nome)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setFont(QFont('Arial', 10))
        button.clicked.connect(lambda: on_click)
        return button

    def reachPrenotaAppuntamento(self):
        pass
        # wid = QWidget()
        # self.vistaLoginAvvocato = LoginAvvocato()
        # self.vistaLoginAvvocato.setupUi(wid)
        # wid.show()

    def reachVisualizzaAppuntamento(self):
        self.vistaAppuntamento = VistaVisualizzaAppuntamento()
        self.vistaAppuntamento.show()

        # self.vistaParcelle =
        # self.vistaParcelle.show()
        # wid = QWidget()
        # self.vistaLoginCliente = LoginCliente()
        # self.vistaLoginCliente.show()
        # wid.show()
