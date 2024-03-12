import pytest
import math

test_N, test_T, test_approx = 4, 1, 20
exp_time = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1]

def inverse_function(N, T, approximation):
	'''Generate two list of data, time and values of W(t), to represent the inverse function.'''
	
	# time data for the x-axis
	time_set = []
	# function data for the y-axis
	W_set = []

	t_element = 0
	t_resolution = 0.1
	while t_element < T+t_resolution:
		time_set.append(t_element)
		t_element += t_resolution

	n_tot = range(1, approximation+1, 1)
	for t in time_set:
		S = 0
		for n in n_tot:
			S += ((N**n)/math.factorial(n))*((math.sin(math.sqrt(n)*t/2))**2)
		value = -1+(2*(math.e**(-N)))*S
		W_set.append(value)
	return(time_set, W_set)

def test_inverse_function_time():
	''''''
	test_time, not_tested_W = inverse_function(test_N, test_T, test_approx)
	i = 0
	for t in test_time:
		assert math.isclose(t, exp_time[i], abs_tol=0.00001) == True
		i += 1