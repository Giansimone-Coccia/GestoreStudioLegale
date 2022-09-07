from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit, QLabel, QMessageBox

from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaEliminaCliente(QWidget):

    def __init__(self,id):
        super(VistaEliminaCliente, self).__init__()

        tool = Tools()
        gLayout = QGridLayout()
        gLayout.addWidget(tool.rewindButton(self.rewind), 0, 0)
        gLayout.addWidget(self.createButton("Sì", self.eliminaCliente(id)), 1, 0)
        gLayout.addWidget(self.createButton("No", self.rewind), 1, 1)
        self.setLayout(gLayout)
        self.resize(500, 400)
        self.setWindowTitle("Gestore Studio Legale")
        self.show()

    def eliminaCliente(self,id):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaClienti import VistaVisualizzaClienti
        Cliente.rimuoviCliente(id)
        self.vistaHome = VistaVisualizzaClienti()
        self.vistaHome.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAdmin.VistaVisualizzaClienti import VistaVisualizzaClienti
        self.vistaHome = VistaVisualizzaClienti()
        self.vistaHome.show()
        self.close()