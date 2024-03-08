import math

'''Define and apply the Jaynes-Cummings inverse function formula 
with zero detuning to generate a data set, starting from
average number of photons and time window.'''

def inverse_function(N, T):
	'''Generate two list of data, time and values of W(t), to represent the inverse function.'''
	
	# time data for the x-axis
	time_set = []
	# function data for the y-axis
	W_set = []

	t_element = 0
	t_resolution = 0.1 #configurable?
	t_max = T + t_resolution
	while t_element < t_max:
		time_set.append(t_element)
		t_element += t_resolution

	# summation approximated to the first 20 terms
	approximation = 20 #configurable?
	n_tot = range(1, approximation+1, 1)
	for t in time_set:
		S = 0
		for n in n_tot:
			S += ((N**n)/math.factorial(n))*((math.sin(math.sqrt(n)*t/2))**2)
		value = -1+(2*(math.e**(-N)))*S
		W_set.append(value)
	return(time_set, W_set)

