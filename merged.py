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

from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import matplotlib.pyplot as plt
Cd=pd.read_csv('C:/Users/CloudThat/Desktop/Clutchriding/Livedata/cl.csv')
d=Cd.iloc[:, [1,0]].values
Cd.fillna(Cd.mean())
fig, ax = plt.subplots(figsize=(3,2))
Hclustering = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
Hclustering.fit(d)
plt.scatter(d[:, 0], d[:, 1])
ax.set_xlabel('Speed')
ax.set_ylabel('RPM')
plt.show()


df = pd.DataFrame(Cd)
import seaborn as sns
sns.boxplot(x=df)

from scipy import stats
import numpy as np
z = np.abs(stats.zscore(df))
print(z)

threshold = 5
print(np.where(z > 5))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import savefig
from sklearn.ensemble import IsolationForest

X_train = pd.read_csv('C:/Users/CloudThat/Desktop/merged/OBDdata_clean_140.csv')
X_train = X_train.iloc[:, [1,0]].values

X_test = pd.read_csv('C:/Users/CloudThat/Desktop/Clutchriding/CSV/raw.csv')
X_test = X_test.iloc[:, [0,3]].values

clf = IsolationForest(max_samples=100)
clf.fit(X_train)

y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)

print(list(y_pred_test).count(-1))
file = open("C:/Users/CloudThat/Desktop/Clutchriding/Livedata/cl.csv")
numline = len(file.readlines())
print (numline)
test=(list(y_pred_test).count(-1))/numline
print(test)

clf = IsolationForest(max_samples=100)
clf.fit(X_test)

print(list(y_pred_train).count(-1))
file = open("C:/Users/CloudThat/Desktop/merged/OBDdata_clean_140.csv")
numline = len(file.readlines())
print (numline)
train=(list(y_pred_train).count(-1))/numline
print(train)

if(test>0.11):
    print("Clutch Riding : Yes")