import threading
import time
import pyodbc
from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from agglocluster import cluster
import csv
server = 'boschsql.database.windows.net'
database = 'boschdb'
username = 'bosch'
password = 'Asd12345****'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
class Threading(object):

    def __init__(self, interval=1):
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()
    def run(self):
        while True:
            cursor = cnxn.cursor()
            cursor.execute("SELECT RPM, Speed, OTP FROM [dbo].[OBDstream] WHERE EXISTS(SELECT otp FROM [dbo].[otps] WHERE extraflag = 1);")
            header = map(lambda x: x[0], cursor.description)
            with open('C:/Users/CloudThat/Desktop/Clutchriding/Livedata/cl.csv', 'w+') as f:
				#f.write('\t'.join(header) + '\n')
                csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar='"', lineterminator='\n').writerows(cursor)			
            time.sleep(self.interval)
t=Threading()