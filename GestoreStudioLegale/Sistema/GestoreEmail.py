import datetime
from Servizi.Cliente import Cliente
from Servizi.Appuntamento import Appuntamento

class GestoreEmail:

    def __init__(self):
       self.Cliente = Cliente
       self.contenuto = []
       self.dataOra = datetime.datetime(year=1970, month=1, day=1, hour=00, minute=00)

    #se voglio fare la verifica sul cliente dovrei inserirlo negli attributi
    def gestoreEmail(self):

        #if ricercaUtilizzatoreId(self, Cliente.ID)

        #cliente come parametro?
    def getDatiAppuntamento(self):

        """
            if os.path.isfile('Dati\Appuntamenti.pickle'):
                with open('Dati\Appuntamenti.pickle', 'rb') as f:
                    appuntamenti = dict(pickle.load(f))
                    for appuntamento in appuntamenti.values():
                        if appuntamento.Cliente is Cliente:
                            return appuntamento
                    return None
            else:
                return None
        """
    def invioEmail(self):




