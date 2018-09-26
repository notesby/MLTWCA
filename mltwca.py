import numpy as np
import random


def main():
	dataset = generateDataset(10,10)
	dist = getDistanceMatrix(dataset)
	print(dataset)
	print(dist)


def getDistanceMatrix(dataset):
	dist = np.zeros(shape=(len(dataset),len(dataset)))
	for row in range(0,len(dataset)):
		for pattern in range(row,len(dataset)):
			count = 0
			for x in range(0,len(dataset[pattern])):
				if ( int(dataset[row][x]) ^ int(dataset[pattern][x])):
					count += 1
			dist[row][pattern] = count
	return dist

def generateDataset(rows,columns):
	dataset = np.zeros(shape=(rows,columns))
	for i in range(0,rows):
		for j in range(0,columns):
			dataset[i][j] = int(random.randint(0,100)%2)
	return dataset

main()