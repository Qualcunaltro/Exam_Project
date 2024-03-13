import Graphing as G
import Simulation as S
from Config import setup

'''Execute the program, drawing graphs from user inputs.'''

def simulate_static(N, T, approximation, saving):
	'''
	Apply the J-C inverse function formula and draw its static graph by calling the respective functions from the modules.
	Input: positive integers N & approximation, positive float T (rounded to 0.1) and boolean saving
	Output: graph and, optionally, data in .csv file.
	'''
	time, W = S.inverse_function(N, T, approximation)
	G.draw_graph(time, W, saving)
	
def simulate_animated(N, T, approximation, time_constant, saving):
	'''
	Apply the J-C inverse function formula and draw its animated graph by calling the respective functions from the modules.
	Input: positive integers N, approximation and time_constant, positive float T (rounded to 0.1) and boolean saving
	Output: graph and, optionally, data in .csv file.
	'''
	time, W = S.inverse_function(N, T, approximation)
	G.draw_animated_graph(time, W, time_constant, saving)
		
def start_program(N, T, approximation, time_constant, anim_check, saving):
	'''
	The program main executable.
	Check if the graph to generate must be animated or static, then call the proper function.
	'''
	
	if anim_check == True:
		simulate_animated(N, T, approximation, time_constant, saving)
	else:
		simulate_static(N, T, approximation, saving)
		
if __name__ == '__main__':
	p1, p2, p3, p4, p5, p6 = setup()
	start_program(p1, p2, p3, p4, p5, p6)
