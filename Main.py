import Graphing as G
import Simulation as S

def simulate(N, T):
	time, W = S.inverse_function(N, T)
	G.draw_graph(time, W)

simulate(N=4, T=40)