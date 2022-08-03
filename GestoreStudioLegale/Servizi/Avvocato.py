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


        # Vedere se può modificare tutti o solo alcuni attributi
        def aggiornaAvvocato(self, codiceFiscale='', cognome='',
                            dataNascita=datetime.datetime(year=1970, month=1, day=1), clienti = None, licenza = None,
                            email='', nome='', numTelefono=0, password='', appuntamentoCliente=None, udienza = None,
                             corsoAggiornamento = None):  # Modifica in EA
            if codiceFiscale != '':
                self.codiceFiscale = codiceFiscale
            elif cognome != '':
                self.cognome = cognome
            elif corsoAggiornamento != None:
                self.corsoAggiornamento = corsoAggiornamento
            elif dataNascita != datetime.datetime(year=1970, month=1, day=1):
                self.dataNascita = dataNascita
            elif email != '':
                self.email = email
            # elif Id != '':
            # self.Id = Id
            elif nome != '':
                self.nome = nome
            elif numTelefono != 0:
                self.numeroTelefono = numTelefono
            elif password != '':
                self.password = password
            elif udienza is not None:
                self.udienza = udienza
            # elif parcelle is not None:
            # self.parcelle = parcelle
            elif appuntamentoCliente is not None:
                self.appuntamentoCliente = appuntamentoCliente
            elif clienti is not None:
                self.clienti = clienti
            elif licenza is not None:
                self.licenza = licenza
            return self


    def creaAvvocato(self, codiceFiscale, cognome, corsoAggiornamento, dataNascita, email, Id, numeroTelefono, password, #modifica ea
                         udienza, clienti, licenza, appuntamentoAvvocato):
        self.creaUtilizzatore(codiceFiscale = codiceFiscale, cognome = cognome, corsoAggiornamento = corsoAggiornamento,
                              dataNascita = dataNascita, email = email, Id = Id, numeroTelefono = numeroTelefono,
                              password = password, udienza = udienza)
        self.clienti = clienti
        self.licenza = licenza
        self.appuntamentiAvvocato = appuntamentoAvvocato


    def getDatiAvvocato(self, avvocati):
        d = self.getInfoUtilizzatore()
        d['udienza'] = self.udienza
        d['clienti'] = self.clienti
        d['licenza'] = self.licenza
        return d


    def ricercaUtilizzatoreId(self, id):
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                avvocati = dict(pickle.load(f))
                for avvocato in avvocati.values():
                    if avvocato.Id == id:
                        return avvocato
                return None
        else:
            return None


    def ricercaUtilizzatoreEmail(self, email):
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                avvocati = dict(pickle.load(f))
                for avvocato in avvocati.values():
                    if avvocato.email == email:
                        return avvocato
                return None
        else:
            return None


    def ricercaUtilizzatoreNomeCognome(self, nome, cognome):
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                avvocati = dict(pickle.load(f))
                for avvocato in avvocati.values():
                    if avvocato.nome == nome and avvocato.cognome == cognome:
                        return avvocato
                return None
        else:
            return None


    def rimuoviAvvocato(self, Id):      #Effettuo una ricerca tramite Id
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocato.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocato.pickle', 'wb+') as f:
                avvocati = dict(pickle.load(f))
                if self.ricercaUtilizzatoreId(Id):
                    del avvocati[self.Id]
                    pickle.dump(avvocati, f, pickle.HIGHEST_PROTOCOL)
            self.rimuoviUtilizzatore()
            self.licenza = None
            #self.udienza = None #Vedere se aggiungere la lista delle udienze
            self.clienti = None
            self.appuntamentiAvvocato = None
            del self


    def visualizzaAvvocato(self, Id): #Ricerca tramite Id, quindi modifica in EA
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                avvocati = dict(pickle.load(f))
                for avvocato in avvocati.values():
                    if avvocato.Id == Id:
                        return avvocato
                    else:
                        return None