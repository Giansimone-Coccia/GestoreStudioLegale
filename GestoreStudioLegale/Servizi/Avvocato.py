from PyQt5.QtWidgets import QMessageBox

from GestoreStudioLegale.Servizi.Utilizzatore import Utilizzatore
import pickle
import os.path

class Avvocato(Utilizzatore):

    def __init__(self):
        super(Avvocato, self).__init__()
        self.appuntamentiAvvocato = []
        self.clienti = []


    def aggiornaAvvocato(self, clienti = None, email='', numTelefono=0, password='', appuntamentoAvvocato=None,
                             corsoAggiornamento = None):
        if corsoAggiornamento != None:
            self.corsoAggiornamento = corsoAggiornamento
        elif email != '':
            self.email = email
        elif numTelefono != 0:
            self.numeroTelefono = numTelefono
        elif password != '':
            self.password = password
        elif appuntamentoAvvocato is not None:
            self.appuntamentoAvvocato = appuntamentoAvvocato
        elif clienti is not None:
            self.clienti = clienti
        self.rimuoviAvvocato(self.Id)
        self.creaAvvocato(self.codiceFiscale, self.cognome, self.nome, self.corsoAggiornamento, self.dataNascita, self.email,
                             self.Id, self.numeroTelefono, self.password, self.clienti, self.appuntamentiAvvocato)


    def creaAvvocato(self, codiceFiscale, cognome, nome, corsoAggiornamento, dataNascita, email, Id, numeroTelefono, password, #modifica ea
                          clienti,  appuntamentoAvvocato):
        self.creaUtilizzatore(codiceFiscale = codiceFiscale, cognome = cognome, nome = nome, corsoAggiornamento = corsoAggiornamento,
                              dataNascita = dataNascita, email = email, Id = Id, numeroTelefono = numeroTelefono,
                              password = password)
        self.clienti = clienti
        self.appuntamentiAvvocato = appuntamentoAvvocato
        avvocati = []
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            if os.path.getsize('GestoreStudioLegale/Dati/Avvocati.pickle') == 0:
                avvocati.append(self)
                with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'wb') as f1:
                    pickle.dump(avvocati, f1, pickle.HIGHEST_PROTOCOL)
            else:
                if self.ricercaUtilizzatoreId(self.Id) is None:
                    with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                        avvocati = pickle.load(f)
                        avvocati.append(self)
                    with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'wb') as f1:
                        pickle.dump(avvocati, f1, pickle.HIGHEST_PROTOCOL)


    def getDatiAvvocato(self):
        d = self.getInfoUtilizzatore()
        d['clienti'] = self.clienti
        return d


    def ricercaUtilizzatoreId(self, Id):
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                avvocati = pickle.load(f)
                for avvocato in avvocati:
                    if avvocato.Id == Id:
                        return avvocato
                return None
        else:
            return None


    def ricercaUtilizzatoreEmail(self, email):
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                avvocati = pickle.load(f)
                for avvocato in avvocati:
                    if avvocato.email == email:
                        return avvocato
                return None
        else:
            return None


    def ricercaUtilizzatoreNomeCognome(self, nome, cognome):
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                avvocati = pickle.load(f)
                for avvocato in avvocati:
                    if avvocato.nome == nome and avvocato.cognome == cognome:
                        return avvocato
                return None
        else:
            return None

    def ricercaUtilizzatoreCC(self, codiceFiscale):
        if os.path.isfile('GestoreStudioLegale/Dati/Avvocati.pickle'):
            with open('GestoreStudioLegale/Dati/Avvocati.pickle', 'rb') as f:
                avvocati = pickle.load(f)
                for avvocato in avvocati:
                    if avvocato.codiceFiscale == codiceFiscale:
                        return avvocato
                return None
        else:
            return None

    @staticmethod
    def rimuoviAvvocato(Id):
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
