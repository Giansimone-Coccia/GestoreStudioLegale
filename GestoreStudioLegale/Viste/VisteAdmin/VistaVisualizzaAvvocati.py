from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLineEdit, QLabel, QMessageBox

from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaVisualizzaAvvocati(QWidget):

    def __init__(self, parent=None):
        super(VistaVisualizzaAvvocati, self).__init__(parent)
