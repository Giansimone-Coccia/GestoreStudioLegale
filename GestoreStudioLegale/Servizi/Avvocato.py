from Servizi.Utilizzatore import Utilizzatore

class Avvocato(Utilizzatore):

    def __init__(self):
        super(Avvocato, self).__init__()
        self.appuntamentiAvvocato = None
        self.clienti = None
        self.licenza = None

    def aggiornaAvvocato(self):

    def aggiungiAvvocato(self, nome, cognome, email, codiceFiscale, dataNascita, id, ):
