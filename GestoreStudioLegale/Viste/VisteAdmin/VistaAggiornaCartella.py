from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit, QLabel, QMessageBox
from PyQt5 import QtCore as qtc

from GestoreStudioLegale.Servizi.Cliente import Cliente
from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaAggiornaCliente(QWidget):
    cliente = Cliente()
    def __init__(self,parent = None):

        super(VistaAggiornaCliente, self).__init__(parent)
        print("shit")
        print(self.cliente)

    def setData(self, cliente):
        self.cliente = cliente