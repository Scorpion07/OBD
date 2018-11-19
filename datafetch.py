import pyodbc
import csv
class fetch:

	server = 'boschsql.database.windows.net'
	database = 'boschdb'
	username = 'bosch'
	password = 'Asd12345****'
	driver= '{ODBC Driver 13 for SQL Server}'
	cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	cursor = cnxn.cursor()
	cursor.execute("SELECT RPM, Speed FROM [dbo].[OBDstream] WHERE OTP = '456' AND Speed <> '0';")
	header = map(lambda x: x[0], cursor.description)
	with open('C:/Users/CloudThat/Desktop/Clutchriding/Livedata/cl.csv', 'w+') as f:
		#f.write('\t'.join(header) + '\n')
		csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar='"', lineterminator='\n').writerows(cursor)
