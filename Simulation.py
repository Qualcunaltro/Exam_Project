import math

'''Define and apply the Jaynes-Cummings inverse function formula 
with zero detuning to generate a data set, starting from
average number of photons and the time window.'''

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



