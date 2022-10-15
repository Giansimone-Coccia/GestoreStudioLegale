from PyQt5.QtWidgets import QMessageBox

from GestoreStudioLegale.Servizi.Utilizzatore import Utilizzatore
import pickle
import os.path

class Cliente(Utilizzatore):

    def __init__(self):
        super(Cliente, self).__init__()
        self.appuntamentoCliente = []
        self.parcelle = []


    def aggiornaCliente(self, email = '', numTelefono = 0, password = '',appuntamentoCliente = None):
        if email != '':
            self.email = email
        elif numTelefono != 0:
            self.numeroTelefono = numTelefono
        elif password != '':
            self.password = password
        elif appuntamentoCliente is not None:
            self.appuntamentoCliente = appuntamentoCliente
        self.rimuoviCliente(self.Id)
        self.creaCliente(self.codiceFiscale, self.cognome, self.corsoAggiornamento, self.dataNascita, self.email,
                             self.Id, self.numeroTelefono, self.password, self.appuntamentoCliente, self.parcelle,
                             self.nome)

    def creaCliente(self, codiceFiscale, cognome, corsoAggiornamento, dataNascita, email, Id, numeroTelefono, password,
                        appuntamentoCliente, parcelle, nome):

        self.creaUtilizzatore(codiceFiscale, cognome, corsoAggiornamento, dataNascita, email, Id, numeroTelefono,
                                  password, nome)
        self.appuntamentoCliente = appuntamentoCliente
        self.parcelle = parcelle
        clienti = []
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            if os.path.getsize('GestoreStudioLegale/Dati/Clienti.pickle') == 0:
                clienti.append(self)
                with open('GestoreStudioLegale/Dati/Clienti.pickle', 'wb') as f:
                    pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
            else:
                if self.ricercaUtilizzatoreId(self.Id) is None:
                    with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                        clienti = pickle.load(f)
                        clienti.append(self)
                    with open('GestoreStudioLegale/Dati/Clienti.pickle', 'wb') as f1:
                        pickle.dump(clienti, f1, pickle.HIGHEST_PROTOCOL)


    def getDatiCliente(self):
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
                        return cliente
                return None
        else:
            return None

    def ricercaUtilizzatoreCC(self, codiceFiscale):
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                for cliente in clienti:
                    if cliente.codiceFiscale == codiceFiscale:
                        return cliente
                return None
        else:
            return None


    def ricercaUtilizzatoreId(self, Id):
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                for cliente in clienti:
                    if cliente.Id == Id:
                        return cliente
                return None
        else:
            return None


    def ricercaUtilizzatoreNomeCognome(self, nome, cognome):
        if os.path.isfile('GestoreStudioLegale/Dati/Clienti.pickle'):
            with open('GestoreStudioLegale/Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
                for cliente in clienti:
                    if cliente.nome == nome and cliente.cognome == cognome:
                        return cliente
                return None
        else:
            return None


    @staticmethod
    def rimuoviCliente(Id):
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
