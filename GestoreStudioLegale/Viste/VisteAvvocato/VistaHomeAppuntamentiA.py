from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QVBoxLayout, QHBoxLayout, QScrollArea, \
    QListWidget, QScrollBar, QListWidgetItem, QLabel

from GestoreStudioLegale.Utilities.Utilities import Tools


class VistaHomeAppuntamentiA(QWidget):

    def __init__(self, parent=None):

        super(VistaHomeAppuntamentiA, self).__init__(parent)

        tool = Tools()
        outerLayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        scroll = QScrollArea()
        gridLayout = QGridLayout()


        grid = QWidget()
        grid.setLayout(gridLayout)

        outerLayout.addWidget(tool.rewindButton(self.rewind))
        outerLayout.addLayout(button_layout)
        outerLayout.addWidget(scroll)

        button_layout.addWidget(self.createButton("Inserisci", self.aggiungiAppuntamento))
        button_layout.addWidget(self.createButton("Cerca", self.cercaAppuntamento))

        scroll_bar = QScrollBar(self)
        #scroll_bar.setStyleSheet("background {color: #e4e8ff;}")
        scroll.setVerticalScrollBar(scroll_bar)
        #scroll.addScrollBarWidget(scroll_bar)
        scroll.addScrollBarWidget(grid)

        # gLayout.addWidget(self.createButton("Visualizza Appuntamenti", self.reachVisualizzaAppuntamento), 2, 0)

        self.setLayout(outerLayout)
        self.resize(1500, 1200)
        self.setWindowTitle("Gestore Studio Legale")
        self.show()


    def createButton(self, nome, on_click):
        button = QPushButton(nome)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setFont(QFont('Arial', 10))
        button.clicked.connect(on_click)
        #button.setSizePolicy(150, 50)
        return button

    def aggiungiAppuntamento(self):
        pass

    def cercaAppuntamento(self):
        pass

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeAvvocato import VistaHomeAvvocato
        self.vistaHome = VistaHomeAvvocato()
        self.vistaHome.show()
        self.close()
