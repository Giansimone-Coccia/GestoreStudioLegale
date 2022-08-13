from GestoreStudioLegale.Servizi.Utilizzatore import Utilizzatore
import pickle
import os.path
import datetime

class Avvocato(Utilizzatore):

    def __init__(self):
        super(Avvocato, self).__init__()
        self.appuntamentiAvvocato = []
        self.clienti = []
        self.licenza = []


    def aggiornaAvvocato(self, clienti = None, email='', numTelefono=0, password='', appuntamentoAvvocato=None,
                            udienza = None, corsoAggiornamento = None):  # Modifica in EA
        if corsoAggiornamento != None:
            self.corsoAggiornamento = corsoAggiornamento
        elif email != '':
            self.email = email
        elif numTelefono != 0:
            self.numeroTelefono = numTelefono
        elif password != '':
            self.password = password
        elif udienza is not None:
            self.udienza = udienza
        elif appuntamentoAvvocato is not None:
            self.appuntamentoAvvocato = appuntamentoAvvocato
        elif clienti is not None:
            self.clienti = clienti
        self.rimuoviAvvocato(self.Id)
        self.creaAvvocato(self.codiceFiscale, self.cognome, self.nome, self.corsoAggiornamento, self.dataNascita, self.email,
                             self.Id, self.numeroTelefono, self.password, self.udienza, self.clienti, self.licenza,
                              self.appuntamentiAvvocato)
        print("Aggiornato")


    def creaAvvocato(self, codiceFiscale, cognome, nome, corsoAggiornamento, dataNascita, email, Id, numeroTelefono, password, #modifica ea
                         udienza, clienti, licenza, appuntamentoAvvocato):
        self.creaUtilizzatore(codiceFiscale = codiceFiscale, cognome = cognome, nome = nome, corsoAggiornamento = corsoAggiornamento,
                              dataNascita = dataNascita, email = email, Id = Id, numeroTelefono = numeroTelefono,
                              password = password, udienza = udienza)
        self.clienti = clienti
        self.licenza = licenza
        self.appuntamentiAvvocato = appuntamentoAvvocato
        avvocati = []
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            #if os.stat('GestoreStudioLegale/Dati/Avvocati.pickle').st_size != 0:
            if os.path.getsize('GestoreStudioLegale/Dati/Avvocati.pickle') == 0:
                avvocati.append(self)
                with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'wb') as f1:
                    pickle.dump(avvocati, f1, pickle.HIGHEST_PROTOCOL)
                #raise EOFError
            else:
                if self.ricercaUtilizzatoreId(self.Id) is None:
                    with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                    #try:
                        avvocati = pickle.load(f)
                        avvocati.append(self)
                    #except EOFError as er:
                    #   print("Errore")
                    with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'wb') as f1:
                        pickle.dump(avvocati, f1, pickle.HIGHEST_PROTOCOL)


    def getDatiAvvocato(self):
        d = self.getInfoUtilizzatore()
        d['udienza'] = self.udienza
        d['clienti'] = self.clienti
        d['licenza'] = self.licenza
        print(d)
        return d


    def ricercaUtilizzatoreId(self, Id):
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                avvocati = pickle.load(f)
                for avvocato in avvocati:
                    if avvocato.Id == Id:
                        print("Trovato")
                        return avvocato
                print("Avvocato non trovato")
                return None
        else:
            return None


    def ricercaUtilizzatoreEmail(self, email):
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                avvocati = pickle.load(f)
                for avvocato in avvocati:
                    if avvocato.email == email:
                        print("Ok avvocato")
                        return avvocato
                print("Nessun avvocato trovato")
                return None
        else:
            return None


    def ricercaUtilizzatoreNomeCognome(self, nome, cognome):
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                avvocati = pickle.load(f)
                for avvocato in avvocati:
                    if avvocato.nome == nome and avvocato.cognome == cognome:
                        print("Trovato")
                        return avvocato
                print("Avvocato non trovato")
                return None
        else:
            return None


    @staticmethod
    def rimuoviAvvocato(Id):      #Effettuo una ricerca tramite Id
        try:
            avvocati = []
            if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
                with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                    avvocati = pickle.load(f)
            for avvocato in avvocati:
                if avvocato.Id == Id:
                    avvocati.remove(avvocato)
                else:
                    print("Avvocato non trovato")
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'wb') as f1:
                pickle.dump(avvocati, f1, pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            print("Finito")