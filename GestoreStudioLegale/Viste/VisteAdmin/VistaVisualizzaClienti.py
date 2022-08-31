from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit, QLabel, QMessageBox

from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaVisualizzaClienti(QWidget):

    def __init__(self, parent=None):
        super(VistaVisualizzaClienti, self).__init__(parent)