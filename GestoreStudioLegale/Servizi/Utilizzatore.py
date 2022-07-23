import datetime
from abc import abstractmethod

class Utilizzatore:

    def __init__(self):
        self.codiceFiscale = codiceFiscale
        self.cognome = cognome
        self.corsoAggiornamento = corsoAggiornamento
        self.dataNascita = datetime.datetime(year=1970, month=1, day=1)
        self.email = email
        self.Id = Id
        self.nome = nome
        self.numeroTelefono = numeroTelefono
        self.password = password
        self.udienza = udienza

    def creaUtilizzatore(self, codiceFiscale, cognome, corsoAggiornamento, dataNascita, email, Id, numeroTelefono, password,
                         udienza,):
        self.codiceFiscale = codiceFiscale
        self.cognome = cognome
        self.corsoAggiornamento = corsoAggiornamento
        self.dataNascita = dataNascita
        self.email = email
        self.Id = Id
        self.nome = nome
        self.numeroTelefono = numeroTelefono
        self.password = password
        self.udienza = udienza

    def getInfoUtilizzatore(self):
        return {
            'nome' : self.nome,
            'cognome': self.cognome,
            'codice fiscale': self.codiceFiscale,
            'data nascita': self.dataNascita,
            'email': self.email,
            'id': self.id,
            'numero telefono': self.numeroTelefono,
            'password': self.password,
            'udienza': self.udienza,
            'corso aggiornamento': self.corsoAggiornamento
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
        self.udienza = None
        self.corsoAggiornamento = None

