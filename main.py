import pickle
import sys

from PyQt5.QtWidgets import QApplication

from GestoreStudioLegale.Gestione.Backup import Backup
from GestoreStudioLegale.Sistema.GestoreEmail import GestoreEmail
from GestoreStudioLegale.Viste.VistaHome import VistaHome


backup = Backup()
email = GestoreEmail()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    vista_home = VistaHome()
    vista_home.show()
    backup.eseguiBackup()
    email.invioEmail()
    sys.exit(app.exec())