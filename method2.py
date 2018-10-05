import numpy as np
import random
import matplotlib.pyplot as plt


def main():
	dataset = read("datasets/optdigits/optdigits_training.txt")
	fltrDtst = np.array(get2Classes(dataset))
	fltrDtst=fltrDtst[np.argsort(fltrDtst[:,-1])]
	x_training = fltrDtst[:,:-1]
	y_training = fltrDtst[:,-1]
	print(x_training)
	print(y_training)
	binDataset = transformArrayToBinary(x_training)
	print(binDataset)

def theplot():
	plt.matshow([[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]],cmap=plt.cm.Blues)
	plt.show()

def transformArrayToBinary(dataset):
	binDataset = []
	for row in dataset:
		binNums = []
		for col in row:
			binNums.append(list(map(int,"{0:0>5b}".format(col))))
		binDataset.append(binNums)
	return binDataset

def get2Classes(dataset):
	fltrDtst = []
	for row in dataset:
		if row[-1] == 5 or row[-1] == 6:
			fltrDtst.append(row)
	return fltrDtst


def read(path):
	file = open(path,'r')
	reader = file.readlines()
	dataset = []
	for line in reader:
		txt = line.replace('\n','')
		strLst = txt.split(",")
		intLst = list(map(int,strLst))
		dataset.append(intLst)
	return dataset

#main()
theplot()