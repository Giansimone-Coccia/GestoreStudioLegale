from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel


class VistaVisualizzaAppuntamento(QWidget):

    def __init__(self, parent=None):
        super(VistaVisualizzaAppuntamento, self).__init__(parent)

        textLabel = QLabel()
        gLayout = QGridLayout()
        gLayout.addWidget(textLabel.setText("Avvocato"), 1, 0)
        gLayout.addWidget(textLabel.setText("Data e Ora Inizio"), 1, 1)
        gLayout.addWidget(textLabel.setText("Data e Ora Fine"), 1, 2)
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
        pass
        # self.vistaParcelle =
        # self.vistaParcelle.show()
        # wid = QWidget()
        # self.vistaLoginCliente = LoginCliente()
        # self.vistaLoginCliente.show()
        # wid.show()
