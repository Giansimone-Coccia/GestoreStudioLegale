from Servizi.Utilizzatore import Utilizzatore
import pickle
import os.path

class Cliente(Utilizzatore):

    def __init__(self):
        super(Cliente, self).__init__()
        self.appuntamentoCliente = []
        self.parcelle = []

    def aggiornaCliente(self): #Chiedi per questa

    def aggiungiCliente(self, codiceFiscale, cognome, corsoAggiornamento, dataNascita, email, Id, numeroTelefono, password,
                        appuntamentoCliente, parcelle):
        self.aggiungiUtilizzatore(codiceFiscale, cognome, corsoAggiornamento, dataNascita, email, Id, numeroTelefono,
                                  password) #Messi in ordine, così non utilizzo l'='
        self.appuntamentoCliente = appuntamentoCliente
        self.parcelle = parcelle
        clienti = {}
        if os.path.isfile('Dati\Clienti.pickle'):
            with open('Dati\Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
        clienti[Id] = self
        with open('Dati\Clienti.pickle', 'wb') as f:
            pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

    def getDatiCliente(self, clienti):
        d = self.getInfoUtilizzatore()
        d['appuntamentoCliente'] = self.appuntamentoCliente
        d['parcelle'] = self.parcelle
        return d

    def ricercaUtilizzatoreEmail(self, email):
        if os.path.isfile('Dati\Clienti.pickle'):
            with open('Dati\Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                for cliente in clienti.values():
                    if cliente.email == email:
                        return cliente
                return None
        else:
            return None

    def ricercaUtilizzatoreId(self, Id):
        if os.path.isfile('Dati\Clienti.pickle'):
            with open('Dati\Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                for cliente in clienti.values():
                    if cliente.Id == Id:
                        return cliente
                return None
        else:
            return None

    def ricercaUtilizzatoreNomeCognome(self, nome, cognome):
        if os.path.isfile('Dati\Clienti.pickle'):
            with open('Dati\Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                for cliente in clienti.values():
                    if cliente.nome == nome and cliente.cognome == cognome:
                        return cliente
                return None
        else:
            return None

    def rimuoviCliente(self, Id):   #Anche quì suppongo una ricerca per Id
        if os.path.isfile('Dati\Clienti.pickle'):
            with open('Dati\Clienti.pickle', 'wb+') as f:
                clienti = dict(pickle.load(f))
                if self.ricercaUtilizzatoreId(Id):
                    del clienti[self.Id]
                    pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
            self.rimuoviUtilizzatore()
            self.appuntamentoCliente = None
            self.parcelle = None
            del self

    def visualizzaCliente(self, Id):
        if os.path.isfile('Dati\Clienti.pickle'):
            with open('Dati\Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                for cliente in clienti.values():
                    if cliente.Id == Id:
                        return cliente
                    else:
                        return None

