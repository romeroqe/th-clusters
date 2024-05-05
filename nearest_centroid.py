#################################################################################
# Implementation of the Euclidean distance from a list of centroids and profiles
# - Emmanuel Romero (https://github.com/romeroqe)
# 
# This file contains code used to develop the methodology 
# of a publication that is currently under review.
#

import math, operator

###############################
# Calculate Euclidean distance 
###############################
def distance(X, y, N):
	distance = 0
	for x in range(N):
		# Euclidean distance
		distance += (X[x] - y[x])**2
	return math.sqrt(distance)

###############################
# Get nearest centroid 
###############################
def getNearestCentroid(Xi, centroids):
	N = len(Xi)
	labels = list(range(len(centroids)))
	distances = []
	for key in labels:
		distances.append((key, distance(Xi, centroids[key], N)))
	distances.sort(key=operator.itemgetter(1))
	return distances[0][0]

###############################
# Iterate profiles
###############################
def NearestCentroid(X, centroids):
	#############################################################
	# parameters:
	# 	X: 2-D list, shape: [num_profiles, 1451 (depth)]
	# 	centroids: 2-D list, shape: [num_clusters, 1451 (depth)]

	predictions = []
	for i in range(len(X)):
		predictions.append(getNearestCentroid(X[i], centroids))
		print(f"{i}/{len(X)}", end="\r")
	print(f"{i}/{len(X)}")
	return predictions
