import Graphing as G
import Simulation as S
from Config import setup

'''Execute the program, drawing graphs from user inputs.'''

def simulate_static(N, T, approximation, saving):
	'''Apply the J-C inverse function formula and draw its static graph.'''
	time, W = S.inverse_function(N, T, approximation)
	G.draw_graph(time, W, saving)

def simulate_animated(N, T, approximation, time_constant):
	'''Apply the J-C inverse function formula and draw its animated graph.'''
	time, W = S.inverse_function(N, T, approximation)
	G.draw_animated_graph(time, W, time_constant)
	
def start_program(N, T, approximation, time_constant, anim_check, saving):
	'''The program main executable.'''
	
	if anim_check == True:
		simulate_animated(N, T, approximation, time_constant)
	else:
		simulate_static(N, T, approximation, saving)
		
if __name__ == '__main__':
	p1, p2, p3, p4, p5, p6 = setup()
	start_program(p1, p2, p3, p4, p5, p6)
