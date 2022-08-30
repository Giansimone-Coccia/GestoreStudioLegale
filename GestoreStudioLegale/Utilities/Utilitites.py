import os

class Tools():

    def __init__(self):
        pass

    def leggi(self):
        if os.path.isfile('GestoreStudioLegale/Dati/Credenziali.pickle'):
            with open('GestoreStudioLegale/Dati/Credenziali.pickle', 'r') as f:
                stringa1 = f.read(5)
                #stringa1 = f.readline()
                #stringa2 = f.readline()
                #self.salvaAppend(stringa2)
                return stringa1

    def salva(self, stringa):
        if os.path.isfile('GestoreStudioLegale/Dati/Credenziali.pickle'):
            with open('GestoreStudioLegale/Dati/Credenziali.pickle', 'w') as f:
                f.write(stringa)
                f.write('\n')

    def salvaAppend(self, stringa): #per richiamarlo anche poi con la password
        if os.path.isfile('GestoreStudioLegale/Dati/Credenziali.pickle'):
            with open('GestoreStudioLegale/Dati/Credenziali.pickle', 'a') as f:
                f.write(stringa)
                f.write('\n')