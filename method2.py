import numpy as np
import random
import matplotlib.pyplot as plt


def main():
	dataset = read("datasets/optdigits/optdigits_training.txt")
	fltrDtst = np.array(get2Classes(dataset))
	fltrDtst = fltrDtst[np.argsort(fltrDtst[:,-1])]
	splitDataset = splitInClasses(fltrDtst)
	binDataset = transformArrayToBinary(splitDataset)
	attractors = generateAttractors(binDataset)
	#showAttractors(attractors)
	#print(attractors)


def generateAttractors(dataset):
	attractors = {}
	keys = list(dataset.keys())
	for key in range(len(keys)):
		attractors[keys[key]] = {}
	for col in range(len(dataset[keys[0]][0])):
		maxDistance = -1000
		for i in range(len(keys)):
			key1 = keys[i]
			for j in range(i+1,len(keys)):
				key2 = keys[j]
				for row in dataset[key1]:
					for row2 in dataset[key2]:
						dist = euclDistance(row[col],row2[col])
						if maxDistance < dist:
							maxDistance = dist
							attractors[key1][col] = row[col]
							attractors[key2][col] = row2[col]
		print(maxDistance)
	return attractors

def showNumbers(dataset):
	for key in dataset:
		for row in dataset[key]:
			number = np.array(row)
			number = number.reshape((8, 8))
			plt.matshow(number,cmap=plt.cm.Blues)
	plt.show()


def showAttractors(attractors):
	for key in attractors:
		number = []
		for col in attractors[key]:
			number.append(binArrayToInt(attractors[key][col]))
		number = np.array(number)
		number = number.reshape((8, 8))
		plt.matshow(number,cmap=plt.cm.Blues)
	plt.show()
				

def binArrayToInt(bitlist):
	out = 0
	for bit in bitlist:
		out = (out << 1) | bit
	return out


def hamDistance(b1,b2):
	count = 0
	for i in range(len(b1)):
		count += b1[i] ^ b2[i]
	return count

def euclDistance(b1,b2):
	n1 = binArrayToInt(b1)
	n2 = binArrayToInt(b2)
	return abs(n1-n2)

def splitInClasses(dataset):
	splitDataset = {}
	noClass = -1
	for row in dataset:
		if row[-1] != noClass:
			noClass = row[-1]
			if noClass not in splitDataset:
				splitDataset[noClass] = []
		else:
			if noClass in splitDataset:
				splitDataset[noClass].append(row[:-1])

	return splitDataset

def transformArrayToBinary(dataset):
	binDataset = {}
	for key in dataset:
		binDataset[key] = []
		for row in dataset[key]:
			binNums = []
			for col in row:
				binNums.append(list(map(int,"{0:0>5b}".format(col))))
			binDataset[key].append(binNums)
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

main()
#theplot()