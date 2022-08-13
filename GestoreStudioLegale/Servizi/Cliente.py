from GestoreStudioLegale.Servizi.Utilizzatore import Utilizzatore
import pickle
import os.path
import datetime

class Cliente(Utilizzatore):

    def __init__(self):
        super(Cliente, self).__init__()
        self.appuntamentoCliente = []
        self.parcelle = []


    #Da vedere in seguito
    def aggiornaCliente(self, email = '', numTelefono = 0, password = '',appuntamentoCliente = None): #Modifica in EA
        if email != '':
            self.email = email
        elif numTelefono != 0:
            self.numeroTelefono = numTelefono
        elif password != '':
            self.password = password
        elif appuntamentoCliente is not None:
            self.appuntamentoCliente = appuntamentoCliente
        self.rimuoviCliente(self.Id)
        self.aggiungiCliente(self.codiceFiscale, self.cognome, self.corsoAggiornamento, self.dataNascita, self.email,
                             self.Id, self.numeroTelefono, self.password, self.appuntamentoCliente, self.parcelle,
                             self.nome, self.udienza)
        print("Aggiornato")


    def creaCliente(self, codiceFiscale, cognome, corsoAggiornamento, dataNascita, email, Id, numeroTelefono, password,
                        appuntamentoCliente, parcelle, nome, udienza):
        self.creaUtilizzatore(codiceFiscale, cognome, corsoAggiornamento, dataNascita, email, Id, numeroTelefono,
                                  password, udienza, nome) #Messi in ordine, così non utilizzo l'='
        self.appuntamentoCliente = appuntamentoCliente
        self.parcelle = parcelle
        clienti = []
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            if os.path.getsize('GestoreStudioLegale/Dati/Clienti.pickle') == 0:
                clienti.append(self)
                with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f1:
                    pickle.dump(clienti, f1, pickle.HIGHEST_PROTOCOL)
                with open('GestoreStudioLegale/Dati/Clienti.pickle', 'wb') as f:
                    pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
            else:
                if self.ricercaUtilizzatoreId(self.ID) is None:
                    with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                    #try:
                        clienti = pickle.load(f)
                        clienti.append(self)
                    #except EOFError as er:
                    #   print("Errore")
                    with open('GestoreStudioLegale/Dati/Clienti.pickle', 'wb') as f1:
                        pickle.dump(clienti, f1, pickle.HIGHEST_PROTOCOL)


    def getDatiCliente(self):
        d = self.getInfoUtilizzatore()
        d['appuntamentoCliente'] = self.appuntamentoCliente
        d['parcelle'] = self.parcelle
        print(d)
        return d


    def ricercaUtilizzatoreEmail(self, email):
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                for cliente in clienti:
                    if cliente.email == email:
                        print("Ok cliente")
                        return cliente
                print("Nessun cliente trovato")
                return None
        else:
            return None


    def ricercaUtilizzatoreId(self, Id):
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                for cliente in clienti:
                    if cliente.Id == Id:
                        #print("Trovato")
                        return cliente
                print("Cliente non trovato")
                return None
        else:
            return None


    def ricercaUtilizzatoreNomeCognome(self, nome, cognome):
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                for cliente in clienti:
                    if cliente.nome == nome and cliente.cognome == cognome:
                        print("Trovato")
                        return cliente
                print("Cliente non trovato")
                return None
        else:
            return None


    @staticmethod
    def rimuoviCliente(Id):   #Anche quì suppongo una ricerca per Id oppure passo direttamente l'oggetto, da vedere
        try:
            clienti = []
            if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
                with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                    clienti = pickle.load(f)
            for cliente in clienti:
                if cliente.Id == Id:
                    clienti.remove(cliente)
                else:
                    print("Cliente non trovato")
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'wb') as f1:
                pickle.dump(clienti, f1, pickle.HIGHEST_PROTOCOL)
        except Exception as e:
                print("Finito")


    def visualizzaCliente(self, Id): #Stessa cosa del metodo precedente
        if self.ricercaUtilizzatoreId(Id):
            print(self.ricercaUtilizzatoreId(Id))
