import math

# define and apply the Jaynes-Cummings inverse function formula with zero detuning

def inverse_function(N, T):
	# time data for the x-axis
	time_set = []
	# function data for the y-axis
	W_set = []
	t_element = 0
	t_max = T + 0.1
	while t_element < t_max:
		time_set.append(t_element)
		t_element += 0.1
	# summation approximated to the first 20 terms
	n_tot = range(1, 21, 1)
	for t in time_set:
		S = 0
		for n in n_tot:
			S += ((N**n)/math.factorial(n))*((math.sin(math.sqrt(n)*t/2))**2)
		value = -1+(2*(math.e**(-N)))*S
		W_set.append(value)
	return(time_set, W_set)

