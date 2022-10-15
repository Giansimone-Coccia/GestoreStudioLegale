from PyQt5.QtWidgets import QMessageBox

from GestoreStudioLegale.Servizi.Cliente import Cliente
import pickle
import os.path

class Parcella():

    def __init__(self):
       self.Cliente = Cliente
       self.ID = ''
       self.identificativo = 0
       self.importo = 0
       self.intestatario = ''


    def aggiornaParcella(self, Cliente = None, identificativo = 0, importo = 0, intestatario = ''):
            if Cliente != None:
                self.Cliente = Cliente
            elif identificativo != 0:
                self.identificativo = identificativo
            elif importo != 0:
                self.importo = importo
            elif intestatario != '':
                self.intestatario = intestatario

            self.rimuoviParcella(self.ID)
            self.creaParcella( self.Cliente, self.ID, self.importo,
                             self.intestatario, self.identificativo)


    def creaParcella(self, Cliente, ID, identificativo, importo, intestatario):
        self.Cliente = Cliente
        self.ID = ID
        self.importo = importo
        self.intestatario = intestatario
        self.identificativo = identificativo

        parcelle = []

        if os.path.isfile('GestoreStudioLegale/Dati/Parcelle.pickle'):

            if os.path.getsize('GestoreStudioLegale/Dati/Parcelle.pickle') == 0:
                parcelle.append(self)
                with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'wb') as f1:
                    pickle.dump(parcelle, f1, pickle.HIGHEST_PROTOCOL)
            else:
                if self.ricercaParcellaIdentificativo(self.identificativo) is None:
                    with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'rb') as f:
                        parcelle = pickle.load(f)
                        parcelle.append(self)
                    with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'wb') as f1:
                        pickle.dump(parcelle, f1, pickle.HIGHEST_PROTOCOL)


    def getDatiParcellaCliente(self):
        d = {}
        d['Cliente'] = self.Cliente
        d['intestatario'] = self.intestatario
        d['identificativo'] = self.identificativo
        d['importo'] = self.importo
        d['ID'] = self.ID
        return d


    def ricercaParcellaCliente (self, Cliente):
        listaParcelle = []
        if os.path.isfile('GestoreStudioLegale/Dati/Parcelle.pickle'):
            with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'rb') as f:
                parcelle = pickle.load(f)
                for parcella in parcelle:
                    if parcella.Cliente.Id == Cliente.Id:
                        listaParcelle.append(parcella)
                return listaParcelle
        else:
            return None


    def ricercaParcellaIntestatario (self, intestatario):
        listaParcelle = []
        if os.path.isfile('GestoreStudioLegale/Dati/Parcelle.pickle'):
            with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'rb') as f:
                parcelle = pickle.load(f)
                for parcella in parcelle:
                    if parcella.intestatario == intestatario:
                        listaParcelle.append(parcella)
                return listaParcelle
        else:
            return None


    def ricercaParcellaIdentificativo(self, identificativo):
        if os.path.isfile('GestoreStudioLegale/Dati/Parcelle.pickle'):
            with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'rb') as f:
                parcelle = pickle.load(f)
                for parcella in parcelle:
                    if parcella.identificativo == identificativo:
                        return parcella
            return None
        else:
            return None


    @staticmethod
    def rimuoviParcella (ID):
        try:
            parcelle = []
            if os.path.isfile('GestoreStudioLegale/Dati/Parcelle.pickle'):
                with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'rb') as f:
                    parcelle = pickle.load(f)
            for parcella in parcelle:
                if parcella.ID == ID:
                    parcelle.remove(parcella)
                else:
                    print("Parcella non trovata")
            with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'wb') as f1:
                pickle.dump(parcelle, f1, pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            print("Finito")
