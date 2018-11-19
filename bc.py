# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 11:52:14 2018

@author: CloudThat
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import savefig
from sklearn.ensemble import IsolationForest
#import datafetch.fetch
#
#Cd=pd.read_csv('C:/Users/CloudThat/Desktop/merged/OBDdata_clean_140.csv')
#d=Cd.iloc[:, [1,0]].values
#test = pd.read_csv('C:/Users/CloudThat/Desktop/Clutchriding/CSV/raw.csv')
#file = open("C:/Users/CloudThat/Desktop/myCSV Files/rawtxtday030918hometowork.csv")
#numline = len(file.readlines())
#r=0
#f=
#for i in range(r, f)

# Generating training data
y=0
t=3600
for i in range(y, t):
	X_train = pd.read_csv('C:/Users/CloudThat/Desktop/myCSV Files/rawtxtday030918hometowork.csv')
	X_train = X_train.iloc[[y,t], [2,0]].values
	clf = IsolationForest(max_samples=100)
	clf.fit(X_train)
	clf = IsolationForest(max_samples=100)
	clf.fit(X_train)
	y_pred_train = clf.predict(X_train)
	c=list(y_pred_train).count(-1)
	print(c)
	file = open("C:/Users/CloudThat/Desktop/myCSV Files/rawtxtday030918hometowork.csv")
	numline = len(file.readlines())
	print (numline)
	train=(c/numline)
	print(train)
	y=y+3600
	t=t+3600
	train =
	if(train>0.11):
		print("Yes")
		a="yes"
	else:
		print("No")
		a="no"

