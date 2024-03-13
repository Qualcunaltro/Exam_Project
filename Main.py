import Graphing as G
import Simulation as S
from Config import setup

'''Execute the program, drawing graphs from user inputs.'''

def simulate_static(N, T, approximation, saving):
	'''
	Apply the J-C inverse function formula and draw its static graph by calling the respective functions from the modules.
	Input: positive real values N & approximation, T and boolean saving
	Output: graph and, optionally, data in .csv file.
	'''
	time, W = S.inverse_function(N, T, approximation)
	G.draw_graph(time, W, saving)
	
def simulate_animated(N, T, approximation, time_constant, saving):
	'''
	Apply the J-C inverse function formula and draw its animated graph by calling the respective functions from the modules.
	Input: positive real numbers N, approximation T and time_constant, plus the boolean saving.
	Output: graph and, optionally, data in .csv file.
	'''
	time, W = S.inverse_function(N, T, approximation)
	G.draw_animated_graph(time, W, time_constant, saving)
		
def start_program(N, T, approximation, time_constant, anim_check, saving):
	'''
	The program main executable.
	Check if the graph to generate must be animated or static through the variable saving, then call the proper function.
	'''
	
	if anim_check == True:
		simulate_animated(N, T, approximation, time_constant, saving)
	else:
		simulate_static(N, T, approximation, saving)
		
if __name__ == '__main__':
	p1, p2, p3, p4, p5, p6 = setup()
	start_program(p1, p2, p3, p4, p5, p6)
