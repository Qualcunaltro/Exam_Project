import math

'''Define and apply the Jaynes-Cummings inverse function formula 
with zero detuning to generate a data set, starting from
average number of photons and the time window.'''

def inverse_function(N, T, approximation):
	'''Generate two list of data, time and values of W(t), to represent the inverse function.'''
	
	# Time data for the x-axis.
	time_set = []
	# Function data for the y-axis.
	W_set = []
	# Fill the time_set with a range (0, T) with 0.1 step.
	t_element = 0
	t_resolution = 0.1
	while t_element < T+t_resolution:
		time_set.append(t_element)
		t_element += t_resolution
	# Apply the inverse function formula to fill the W_set.
	n_tot = range(1, approximation+1, 1)
	for t in time_set:
		S = 0
		for n in n_tot:
			S += ((N**n)/math.factorial(n))*((math.sin(math.sqrt(n)*t/2))**2)
		value = -1+(2*(math.e**(-N)))*S
		W_set.append(value)
	return(time_set, W_set)

