import Graphing as G
import Simulation as S

'''Execute the program, drawing graphs from user inputs.'''

def simulate_static(N, T):
	'''Apply the J-C inverse function formula and draw its static graph'''
	time, W = S.inverse_function(N, T)
	G.draw_graph(time, W)

def simulate_animated(N, T):
	'''Apply the J-C inverse function formula and draw its animated graph'''
	time, W = S.inverse_function(N, T)
	G.draw_animated_graph(time, W)
	
def start_program():
	'''Welcome the user and ask for inputs N and T'''

	starting_prompt = "\nWelcome to the Jaynes-Cunning model simulation."
	starting_prompt += "\nTo exit at any time, type 'q' and press Enter."
	starting_prompt += "\nTo generate a inverse function graph for your model," 
	starting_prompt += "\ninput the average number of photons in the system"
	starting_prompt += "\nand the lenght of time to be considered."

	Looping = True
	while Looping == True:
		print(starting_prompt)
		N_input = input("Insert average number of photons: ")
		if N_input == 'q':
			break
		elif N_input.isdigit() == False:
			print("ERROR: number of photons must be an integer")
		else:
			N = int(N_input)
			T_input = input("Insert lengh of time: ")
			if T_input == 'q':
				break
			else:
				T = float(T_input)
			
			anim_check = input("Do you want an animated graph? ")
			if anim_check == 'yes' or anim_check == 'Yes' or anim_check == 'y' or anim_check == 'Y':
				simulate_animated(N, T)
			elif anim_check == 'q':
				break
			else:
				simulate_static(N, T)
	
start_program()