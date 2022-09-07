from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QVBoxLayout

from GestoreStudioLegale.Utilities.Utilities import Tools
#from GestoreStudioLegale.Viste.VisteCliente.VistaHomeCliente import VistaHomeCliente
from GestoreStudioLegale.Viste.VisteCliente.VistaVisualizzaAppuntamento import VistaVisualizzaAppuntamento


class VistaHomeAppuntamentiC (QWidget):

    def __init__(self, parent=None):
        super(VistaHomeAppuntamentiC, self).__init__(parent)

        tool=Tools()
        gLayout = QGridLayout()
        gLayout.addWidget(tool.rewindButton(self.rewind), 0, 0)
        gLayout.addWidget(self.createButton("Prenota Appuntamento", self.reachPrenotaAppuntamento), 1, 0)
        gLayout.addWidget(self.createButton("Visualizza Appuntamento", self.reachVisualizzaAppuntamento), 2, 0)
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

    def reachPrenotaAppuntamento(self):
        pass

    def reachVisualizzaAppuntamento(self):
        self.vistaAppuntamento = VistaVisualizzaAppuntamento()
        self.vistaAppuntamento.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteCliente.VistaHomeCliente import VistaHomeCliente
        self.vistaHome = VistaHomeCliente()
        self.vistaHome.show()
        self.close()


