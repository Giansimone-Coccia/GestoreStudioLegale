import datetime
from abc import abstractmethod

class Utilizzatore:

    def __init__(self):
        self.codiceFiscale = ''
        self.cognome = ''
        self.corsoAggiornamento = None
        self.dataNascita = datetime.datetime(year=1970, month=1, day=1)
        self.email = ''
        self.Id = ''
        self.nome = ''
        self.numeroTelefono = 0
        self.password = ''


    def creaUtilizzatore(self, codiceFiscale, cognome, corsoAggiornamento, dataNascita, email, Id, numeroTelefono, password,
                          nome):
        self.codiceFiscale = codiceFiscale
        self.cognome = cognome
        self.corsoAggiornamento = corsoAggiornamento
        self.dataNascita = dataNascita
        self.email = email
        self.Id = Id
        self.nome = nome
        self.numeroTelefono = numeroTelefono
        self.password = password

    def getInfoUtilizzatore(self):
        return {
            'Nome' : self.nome,
            'Cognome': self.cognome,
            'Codice fiscale': self.codiceFiscale,
            'Data nascita': self.dataNascita,
            'Email': self.email,
            'Id': self.Id,
            'Numero telefono': self.numeroTelefono,
            'Password': self.password,
            'Corso aggiornamento': self.corsoAggiornamento
        }

    @abstractmethod
    def ricercaUtilizzatoreEmail(self, email):
        pass

    @abstractmethod
    def ricercaUtilizzatoreId(self, id):
        pass

    @abstractmethod
    def ricercaUtilizzatoreNomeCognome(self, nome, cognome):
        pass

    def rimuoviUtilizzatore(self):
        self.codiceFiscale = ''
        self.cognome = ''
        self.nome = ''
        self.dataNascita = datetime.datetime(year=1970, month=1, day=1)
        self.email = ''
        self.id = ''
        self.numeroTelefono = ''
        self.password = ''
        self.corsoAggiornamento = None

