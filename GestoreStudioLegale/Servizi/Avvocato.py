from Servizi.Utilizzatore import Utilizzatore
import pickle
import os.path

class Avvocato(Utilizzatore.Utilizzatore):

    def __init__(self):
        super(Avvocato, self).__init__()
        self.appuntamentiAvvocato = []
        self.clienti = []
        self.licenza = []

    def aggiornaAvvocato(self): #Chiedi per questa

    def aggiungiAvvocato(self, codiceFiscale, cognome, corsoAggiornamento, dataNascita, email, Id, numeroTelefono, password,
                         udienza, clienti, licenza):
        self.creaUtilizzatore(codiceFiscale = codiceFiscale, cognome = cognome, corsoAggiornamento = corsoAggiornamento,
                              dataNascita = dataNascita, email = email, Id = Id, numeroTelefono = numeroTelefono,
                              password = password, udienza = udienza)
        self.clienti = clienti
        self.licenza = licenza
        avvocati = {}
        if os.path.isfile('Dati\Avvocati.pickle'):
            with open('Dati\Avvocati.pickle', 'rb') as f:
                avvocati = pickle.load(f)
        avvocati[Id] = self
        with open('Dati\Avvocati.pickle', 'wb') as f:
            pickle.dump(avvocati, f, pickle.HIGHEST_PROTOCOL)

    def getDatiAvvocato(self, avvocati):
        d = self.getInfoUtilizzatore()
        d['udienza'] = self.udienza
        d['clienti'] = self.clienti
        d['licenza'] = self.licenza
        return d

    def ricercaUtilizzatoreId(self, id):
        if os.path.isfile('Dati\Avvocati.pickle'):
            with open('Dati\Avvocati.pickle', 'rb') as f:
                avvocati = dict(pickle.load(f))
                for avvocato in avvocati.values():
                    if avvocato.Id == Id:
                        return avvocato
                return None
        else:
            return None

    def ricercaUtilizzatoreEmail(self, email):
        if os.path.isfile('Dati\Avvocati.pickle'):
            with open('Dati\Avvocati.pickle', 'rb') as f:
                avvocati = dict(pickle.load(f))
                for avvocato in avvocati.values():
                    if avvocato.email == email:
                        return avvocato
                return None
        else:
            return None

    def ricercaUtilizzatoreNomeCognome(self, nome, cognome):
        if os.path.isfile('Dati\Avvocati.pickle'):
            with open('Dati\Avvocati.pickle', 'rb') as f:
                avvocati = dict(pickle.load(f))
                for avvocato in avvocati.values():
                    if avvocato.nome == nome and avvocato.cognome == cognome:
                        return avvocato
                return None
        else:
            return None

    def rimuoviAvvocato(self, Id):      #Effettuo una ricerca tramite Id
        if os.path.isfile('Dati\Avvocato.pickle'):
            with open('Dati\Avvocato.pickle', 'wb+') as f:
                avvocati = dict(pickle.load(f))
                if self.ricercaUtilizzatoreId(Id):
                    del avvocati[self.Id]
                    pickle.dump(avvocati, f, pickle.HIGHEST_PROTOCOL)
            self.rimuoviUtilizzatore()
            self.licenza = None
            self.udienza = None
            self.clienti = None
            del self

    def visualizzaAvvocato(self, Id): #Ricerca tramite Id, quindi modifica in EA
        if os.path.isfile('Dati\Avvocati.pickle'):
            with open('Dati\Avvocati.pickle', 'rb') as f:
                avvocati = dict(pickle.load(f))
                for avvocato in avvocati.values():
                    if avvocato.Id == Id:
                        return avvocato
                    else:
                        return None