'''Set the parameters for the simulation.'''

# Average number of photons in the system (must be a natural number).
N_e = 10
# Time interval to be considered in the data set.
T_x = 50
# Determine if the graph should be animated (True) or static (False).
anime = False
# Save the generated data [t, W(t)] as a csv (True) or no (False).
save = True
# Set how many terms to consider for the all summations.
approx = 20
# Set the duration of animated graphs (the higher, the longer the animation).
time_const = 8000

def setup():
	'''Return the parameters for Main's use.'''
	return(N_e, T_x, approx, time_const, anime, save)