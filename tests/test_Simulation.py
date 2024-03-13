import pytest
import math

exp_time = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1]

def time_set_generation(T):
	'''Generate a list with a range (0, T) and 0.1 step.'''
	time_set = []
	t_element = 0
	t_resolution = 0.1
	while t_element < T+t_resolution:
		time_set.append(t_element)
		t_element += t_resolution
	return(time_set)

def inverse_function(N, T, approximation):
	'''Generate two list of data, time and values of W(t), to represent the inverse function.'''
	W_set = []
	time_set = time_set_generation(T)
	# Apply the inverse function formula to fill the W_set.
	n_tot = range(1, approximation+1, 1)
	for t in time_set:
		S = 0
		for n in n_tot:
			S += ((N**n)/math.factorial(n))*((math.sin(math.sqrt(n)*t/2))**2)
		value = -1+(2*(math.e**(-N)))*S
		W_set.append(value)
	return(time_set, W_set)

def test_time_set_generation():
	'''Check that the time set generated by the function (mady of floats) 
	is close enough to the true decimal values.'''
	test_time = time_set_generation(test_T)
	i = 0
	for t in test_time:
		assert math.isclose(t, exp_time[i], abs_tol=0.00001) == True
		i += 1



