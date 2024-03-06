import matplotlib.pyplot as plt

# function to draw the graph
def draw_graph(x, y):
	plt.plot(x, y)
	plt.xlabel('Time (a.u.)')
	plt.ylabel('Inverse function W(t)')
	plt.show()