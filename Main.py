import Graphing as G
import Simulation as S

def simulate(N, T):
	time, W = S.inverse_function(N, T)
	G.draw_graph(time, W)

def start_program():
	'''Welcome the user and ask for inputs'''

	starting_prompt = "\nWelcome to the Jaynes-Cunning model simulation."
	starting_prompt += "\nTo exit at any time, type 'q' and press Enter."
	starting_prompt += "\nTo generate a inverse function graph for your model," 
	starting_prompt += "\ninput the average number of photons in the system and the lenght of time to be considered."
	
	Looping = True
	while Looping == True:
		print(starting_prompt)
		N_input = input("Insert average number of photons:")
		if N_input == 'q':
			break
		else:
			N = int(N_input)
		T_input = input("Insert lengh of time:")
		if T_input == 'q':
			break
		else:
			T = int(T_input)
		simulate(N, T)
		

start_program()