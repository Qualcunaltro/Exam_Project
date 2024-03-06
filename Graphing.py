import matplotlib.pyplot as plt
import matplotlib.animation as animation

# function to draw the static graph
def draw_graph(x, y):
	plt.plot(x, y)
	plt.xlabel('Time (a.u.)')
	plt.ylabel('Inverse function W(t)')
	plt.axhline(y = 0, color = 'black', linestyle = 'dashed')
	plt.show()

# function to draw the animated graph
def draw_animated_graph(x,y):
	fig, ax = plt.subplots()
	plt.axhline(y = 0, color = 'black', linestyle = 'dashed')
	line, = ax.plot(x, y)

	def update(num, x, y, line):
		line.set_data(x[:num], y[:num])
		return line,

	ani = animation.FuncAnimation(fig, update, len(x), interval=50, fargs=[x, y, line], blit=True)
	plt.show()
	