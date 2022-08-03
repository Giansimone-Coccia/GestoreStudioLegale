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

   # def aggiornaParcella(self):

    def creaParcella(self, Cliente, ID, importo, intestatario ):
        self.Cliente = Cliente
        self.ID = ID
        self.importo = importo
        self.intestatario = intestatario
        if os.path.isfile('Dati\Parcelle.pickle'):
            with open('Dati\Parcelle.pickle', 'rb') as f:
                parcelle = pickle.load(f)
                parcelle[ID] = self
            with open('Dati\Parcelle.pickle', 'wb') as f:
                pickle.dump(parcelle, f, pickle.HIGHEST_PROTOCOL)

    def getDatiParcellaCliente(self):
        return{
            'Cliente': self.Cliente,
            'intestatario': self.intestatario,
            'importo': self.importo,
            'ID': self.ID,
        }

    def ricercaParcellaCliente (self, Cliente): #Prende una stringa come parametro, cambiare in EA
        if os.path.isfile('Dati\Parcelle.pickle'):
            with open('Dati\Parcelle.pickle', 'rb') as f:
                parcelle = dict(pickle.load(f))
                for parcella in parcelle.values():
                    if parcella.Cliente is Cliente:
                        listaParcelle = [parcella]
                return listaParcelle
            return None
        else:
            return None

    def ricercaParcellaIntestatario (self, intestatario):
        if os.path.isfile('Dati\Parcelle.pickle'):
            with open('Dati\Parcelle.pickle', 'rb') as f:
                parcelle = dict(pickle.load(f))
                for parcella in parcelle.values():
                    if parcella.intestatario == intestatario:
                        listaParcelle = [parcella]
                return listaParcelle
            return None
        else:
            return None

    def ricercaParcellaIdentificativo(self, identificativo):
        if os.path.isfile('Dati\Parcelle.pickle'):
            with open('Dati\Parcelle.pickle', 'rb') as f:
                parcelle = dict(pickle.load(f))
                for parcella in parcelle.values():
                    if parcella.identificativo == identificativo:
                        listaParcelle = [parcella]
                return listaParcelle
            return None
        else:
            return None

    def rimuoviParcella (self, ID):
        if os.path.isfile('Dati\Parcelle.pickle'):
            with open('Dati\Parcelle.pickle', 'wb+') as f:
                parcelle = dict(pickle.load(f))
                if self.ricercaParcellaID(ID):
                    del parcelle[self.ID]
                    pickle.dump(parcelle, f, pickle.HIGHEST_PROTOCOL)


    def visualizzaParcella (self, ID):
        if os.path.isfile('Dati\Parcelle.pickle'):
            with open('Dati\Parcelle.pickle', 'rb') as f:
                parcelle = dict(pickle.load(f))
                for parcella in parcelle.values():
                    if parcella.ID == ID:
                        return parcella
                    else:
                        return None


