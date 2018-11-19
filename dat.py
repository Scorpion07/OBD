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
	cursor.execute("SELECT STARTH, STARTM, ENDH, ENDM FROM [dbo].[otps] WHERE EXISTS(SELECT OTP FROM [dbo].[OBDStream] WHERE otp = OTP AND extraflag = 1);")
	d1=cursor.fetchone()
	print(d1)
	sh=float(d1[0])
	sm=float(d1[1])
	eh=float(d1[2])
	em=float(d1[3])
	tt=(eh+(em/60))-(sh+(sm/60))
	print(tt)
	