import numpy as np
import random


def main():
	k= 9
	if k<= 0:
		print("Error: k must be greater than 0")
		return -1

	dataset = generateDataset(10,10)
	dist = getDistanceMatrix(dataset)
	#print(dataset)
	#print(dist)
	sumatory = getSumatory(dist)
	#print(sumatory)
	if k == 1:
		first = getFirstAttractor(sumatory)
		return first
	elif k == 2:
		first = getFirstAttractor(sumatory)
		second = getSecondAttractor(first,dist)
		return [first,second]
	else:
		first = getFirstAttractor(sumatory)
		second = getSecondAttractor(first,dist)
		attractors = getOtherAttractors(first,second,k,dist)
		#print(attractors)
		return attractors


def getPartitions(attractors,dataset):
	pass



def getDistanceMatrix(dataset):
	dist = np.zeros(shape=(len(dataset),len(dataset)))
	for row in range(0,len(dataset)):
		for pattern in range(row,len(dataset)):
			dist[row][pattern] = getEuclDistance(dataset[row],dataset[pattern])
	return dist

def getHamDistance(p1,p2):
	dist = 0
	for i in range(len(p1)):
		dist += p1[i] ^ p2[i]
	return dist

def getEuclDistance(p1,p2):
	dist = 0
	for i in range(len(p1)):
		dist += pow(p1[i]-p2[i],2)
	dist = pow(dist,1/2)
	#print(p1,p2,dist)
	return dist

def getSumatory(dist):
	sumatory = np.zeros(shape=len(dist))
	for i in range(0,len(dist)):
		for j in range(0,len(dist)):
			if (i <= j):
				sumatory[i] += dist[i][j]
			else:
				sumatory[i] += dist[j][i]
	return sumatory

def getFirstAttractor(sumatory):
	return getMax(sumatory)

def getSecondAttractor(firstIndex,dist):
	maxIndex = 0
	for j in range(0,len(dist)):
		maxValue = 0
		if maxIndex < firstIndex:
			maxValue = dist[maxIndex][firstIndex]
		else:
			maxValue = dist[firstIndex][maxIndex]

		if (j <= firstIndex):
			if maxValue < dist[j][firstIndex]:
				maxIndex = j
		else:
			if maxValue < dist[firstIndex][j]:
				maxIndex = j
	return maxIndex

def getOtherAttractors(first,second,k,dist):
	attractors = [first,second]
	sumatory = np.zeros(shape=(len(dist)))
	sumDistances(first,dist,sumatory)
	sumDistances(second,dist,sumatory)
	for i in range(0,k-2):
		maxIndex = getMax(sumatory)
		attractors.append(maxIndex)
		sumDistances(maxIndex,dist,sumatory)
	return attractors


def sumDistances(index,dist,store):
	for j in range(0,len(dist)):
		if (j <= index):
			store[j] += dist[j][index]
			dist[j][index] = 0
		else:
			store[j] += dist[index][j]
			dist[index][j] = 0



def getMax(arr):
	maxIndex = 0
	for i in range(0,len(arr)):
		if arr[maxIndex] < arr[i]:
			maxIndex = i
	return maxIndex

def generateDataset(rows,columns):
	dataset = np.zeros(shape=(rows,columns))
	for i in range(0,rows):
		for j in range(0,columns):
			dataset[i][j] = int(random.randint(0,100)%2)
	return dataset

main()