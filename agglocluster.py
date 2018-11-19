from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

class cluster:
	def clusterplot():

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
		z = np.abs(stats.zscore(df))
		print(z)