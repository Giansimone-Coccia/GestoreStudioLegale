from GestoreStudioLegale.Servizi.Utilizzatore import Utilizzatore
import pickle
import os.path
import datetime

class Cliente(Utilizzatore):

    def __init__(self):
        super(Cliente, self).__init__()
        self.appuntamentoCliente = []
        self.parcelle = []


    #Vedere se può modificare tutti o solo alcuni attributi
    def aggiornaCliente(self, codiceFiscale = '', cognome = '', dataNascita = datetime.datetime(year=1970, month=1, day=1),
                        email = '', nome = '', numTelefono = 0, password = '',appuntamentoCliente = None): #Modifica in EA
        if codiceFiscale != '':
            self.codiceFiscale = codiceFiscale
        elif cognome != '':
            self.cognome = cognome
        #elif corsoAggiornamento != None:
            #self.corsoAggiornamento = corsoAggiornamento
        elif dataNascita != datetime.datetime(year=1970, month=1, day=1):
            self.dataNascita = dataNascita
        elif email != '':
            self.email = email
        #elif Id != '':
            #self.Id = Id
        elif nome != '':
            self.nome = nome
        elif numTelefono != 0:
            self.numeroTelefono = numTelefono
        elif password != '':
            self.password = password
        #elif udienza is not None:
            #self.udienza = udienza
        #elif parcelle is not None:
            #self.parcelle = parcelle
        elif appuntamentoCliente is not None:
            self.appuntamentoCliente = appuntamentoCliente
        #self.aggiungiCliente(codiceFiscale, cognome,)
        #self.rimuoviCliente()
        return self


    def aggiungiCliente(self, codiceFiscale, cognome, corsoAggiornamento, dataNascita, email, Id, numeroTelefono, password,
                        appuntamentoCliente, parcelle, nome, udienza):
        self.creaUtilizzatore(codiceFiscale, cognome, corsoAggiornamento, dataNascita, email, Id, numeroTelefono,
                                  password, udienza, nome) #Messi in ordine, così non utilizzo l'='
        self.appuntamentoCliente = appuntamentoCliente
        self.parcelle = parcelle
        #clienti = {}
        clienti = []
        #try:
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
                with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                    try:
                        clienti = pickle.load(f)
                        #clienti['Id'] = self
                        clienti.append(self)
                    except EOFError as er:
                        print("Errore")
        #except Exception as e:
        #print("Errore durane l'acquisizione del file")
        with open('GestoreStudioLegale/Dati/Clienti.pickle', 'wb') as f:
            pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)


    def getDatiCliente(self, clienti): #Provare lettura da file
        d = self.getInfoUtilizzatore()
        d['appuntamentoCliente'] = self.appuntamentoCliente
        d['parcelle'] = self.parcelle
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
                        print("Trovato")
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
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                #print("ciao")
                try:
                    clienti = pickle.load(f)
                    #print("ciao")
                except EOFError as e:
                    clienti =dict()
                    for cliente in clienti.values():
                        if cliente.Id == Id:
                            print("Visualizzato")
                            return cliente
                        else:
                            return None

