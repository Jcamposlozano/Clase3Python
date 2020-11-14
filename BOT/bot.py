from threading import *

from datetime import datetime
import time

from Indicadores import *
from LeerExcel import *


class bot:

    def observadorRelog(self):
        while(True):
            time.sleep(1)
            now = datetime.now()
            hora_actual = now.strftime('%H:%M:%S')

            print(hora_actual)
            if hora_actual == '16:42:00':
                i = Indicadores()
                print(i.trm())
            if hora_actual == '16:42:30':
                l = LeerExcel()
                l.leerExcelFuncion()
                exit()

    def iniciar(self):
        t = Timer(1.0, self.observadorRelog)
        t.start()
