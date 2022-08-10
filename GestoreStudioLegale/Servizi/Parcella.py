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
            print("Aggiornato")


    def creaParcella(self, Cliente, ID, identificativo, importo, intestatario):
        self.Cliente = Cliente
        self.ID = ID
        self.importo = importo
        self.intestatario = intestatario
        self.identificativo = identificativo
        parcelle = []
        if os.path.isfile('GestoreStudioLegale/Dati/Parcelle.pickle'):
                with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'rb') as f:
                    try:
                        parcelle = pickle.load(f)
                        parcelle.append(self)
                    except EOFError as eo:
                        print("Errore")
        with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'wb') as f:
                pickle.dump(parcelle, f, pickle.HIGHEST_PROTOCOL)


    def getDatiParcellaCliente(self):
        d = {}
        d['Cliente'] = self.Cliente
        d['intestatario'] = self.intestatario
        d['identificativo'] = self.identificativo
        d['importo'] = self.importo
        d['ID'] = self.ID
        print(d)
        return d


    def ricercaParcellaCliente (self, Cliente): #Prende una stringa come parametro, cambiare in EA
        if os.path.isfile('GestoreStudioLegale/Dati/Parcelle.pickle'):
            with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'rb') as f:
                parcelle = pickle.load(f)
                listaParcelle = []
                for parcella in parcelle:
                    if parcella.Cliente is Cliente:
                        print("Trovata")
                        listaParcelle.append(parcella)
                print(listaParcelle)
                return listaParcelle
        else:
            return None


    def ricercaParcellaIntestatario (self, intestatario):
        if os.path.isfile('GestoreStudioLegale/Dati/Parcelle.pickle'):
            with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'rb') as f:
                parcelle = pickle.load(f)
                listaParcelle = []
                for parcella in parcelle:
                    if parcella.intestatario == intestatario:
                        listaParcelle.append(parcella)
                        print("Trovata")
                print(listaParcelle)
                return listaParcelle
        else:
            return None


    def ricercaParcellaIdentificativo(self, identificativo):
        if os.path.isfile('GestoreStudioLegale/Dati/Parcelle.pickle'):
            with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'rb') as f:
                parcelle = pickle.load(f)
                for parcella in parcelle:
                    if parcella.identificativo == identificativo:
                        print("Trovata")
                        return parcella
            print("Niente")
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


    def visualizzaParcella (self, ID):
        if os.path.isfile('GestoreStudioLegale/Dati/Parcelle.pickle'):
            with open('GestoreStudioLegale/Dati/Parcelle.pickle', 'rb') as f:
                parcelle = pickle.load(f)
                for parcella in parcelle:
                    if parcella.ID == ID:
                        print(parcella)
                        return parcella
                    else:
                        return None


