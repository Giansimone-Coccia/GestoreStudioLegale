from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QScrollArea, QLabel, QMainWindow

from GestoreStudioLegale.Utilities.Utilities import Tools
from GestoreStudioLegale.Viste.VisteAvvocato.VistaAggiornaAppuntamentoA import VistaAggiornaAppuntamentoA
from GestoreStudioLegale.Viste.VisteAvvocato.VistaEliminaAppuntamentoA import VistaEliminaAppuntamentoA

class AppuntamentoRicercatoA(QMainWindow):

    def __init__(self, parent = None):
        super(AppuntamentoRicercatoA, self).__init__(parent)

    def initUI(self, appuntamento):
        tool = Tools()
        self.appuntamentoTrovato = appuntamento
        self.cWidget = QWidget()
        self.outerLayout = QVBoxLayout()
        self.scroll = QScrollArea()
        self.widget = QWidget()

        self.grid = QGridLayout()


        self.outerLayout.addWidget(tool.rewindButton(self.rewind), 1)
        self.outerLayout.addWidget(self.scroll, 9)
        self.cWidget.setLayout(self.outerLayout)

        self.widget.setLayout(self.grid)

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)


        self.setCentralWidget(self.cWidget)
        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Appuntamenti')
        self.getDatiAp()


    def rimuoviAppuntamento(self, id):
        self.subWindow = VistaEliminaAppuntamentoA()
        self.subWindow.setData(id)
        self.subWindow.show()
        self.close()

    def rewind(self):
        from GestoreStudioLegale.Viste.VisteAvvocato.VistaHomeAppuntamentiA import VistaHomeAppuntamentiA
        self.vistaAvvocatoR = VistaHomeAppuntamentiA()
        self.vistaAvvocatoR.show()
        self.close()

    def getDatiAp(self):
        tool = Tools()
        i = 0
        label = QLabel()
        self.vistaAggiorna = VistaAggiornaAppuntamentoA()
        self.vistaAggiorna.appuntamento =self.appuntamentoTrovato
        datIn = self.appuntamentoTrovato.getDatiAppuntamento()['Data e Ora Inizio'].strftime("%m/%d/%Y, %H:%M:%S")
        datFin = self.appuntamentoTrovato.getDatiAppuntamento()['Data e Ora Fine'].strftime("%m/%d/%Y, %H:%M:%S")

        label.setText(
            'Appuntamento: ' + '\n' + 'TIPO PROCEDIMENTO: ' + f"{self.appuntamentoTrovato.getDatiAppuntamento()['Tipo Procedimento']}" + '\n' + 'ID: ' + f"{self.appuntamentoTrovato.getDatiAppuntamento()['ID']}" + '\n' + 'DATA E ORA INIZIO: ' + f"{datIn}" + '\n' + 'DATA E ORA FINE' + f"{datFin}")
        label.setGeometry(QRect(0, 0, 350, 20))
        label.setFont(QFont('Arial', 10))
        label.setStyleSheet("border: 1px solid black;")
        self.grid.addWidget(label, i, 1, 1, 2)
        i += 1
        self.grid.addWidget(tool.createButton("Modifica",lambda: self.vistaAggiorna.show(),method2=self.close), i, 1)
        self.grid.addWidget(
            tool.createButton("Elimina", lambda: self.rimuoviAppuntamento(self.appuntamentoTrovato.getDatiAppuntamento()['ID']),method2=self.close), i, 2)