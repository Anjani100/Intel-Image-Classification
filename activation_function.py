import numpy as np

def sigmoid(Z):
	
	A = 1 / (1 + np.exp(-Z))
	cache = Z

	return A, cache

def relu(Z):

	A = np.maximum(0, Z)
	cache = Z

	return A, cache

def sigmoid_backward(dA, cache):

	Z = cache
	s = 1 / (1 + np.exp(-Z))

	dZ = dA * s * (1 - s)

	return dZ

def relu_backward(dA, cache):

	Z = cache
	dZ = np.array(dA, copy = True)  ## Converting dZ to a correct object

	dZ[ Z <= 0 ] = 0

	return dZ