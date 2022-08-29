import os.path
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView

class VistaGestioneCliente(QWidget):

    def __init__(self, parent=None):
        super(VistaGestioneCliente, self).__init__(parent)
        vertLaayout = QHBoxLayout()
        self.listaView = QListView()
        #self.

    def aggiornaVista(self):
        self.clienti = []
        self.caricaClienti()
        listaModel = QStandardItemModel(self.listaView) #definisce come è fatta una riga
        for cliente in self.clienti:
            item = QStandardItem()
            nome = f"{cliente.nome} {cliente.cognome} - {cliente.id} - {type(cliente).__name__}"
            item.setText(nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            listaModel.appendRow(item)
        self.listaView.setModel(listaModel)


    def caricaClienti(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle') as f:
                clientiLista = pickle.load(f)
                self.clienti.extend(clientiLista)

    '''
    def mostraInfo(self):
        try:
            selected = self.listaView.selectedIndexes()[0].data()
            tipo = selected.split("-")[1].strip().split(" ")[0]
            codice = int(selected.split("-")[1].strip().split(" ")[1])
            cliente = None
            if tipo == "Cliente":
                cliente = Cliente().ricercaUtilizzatoreCodice(codice)
            self.vista_cliente = VistaCliente(cliente, elimina_callback=self.update_ui)
            self.vista_cliente.show()
        except IndexError:
            print("INDEX ERROR")
            return '''

    #def show_new(self):
        #self.caricaClienti()liente = VistaInserisciCliente(callback=self.update_ui)
        #self.inserisci_cliente.show()