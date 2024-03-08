import matplotlib.pyplot as plt
import matplotlib.animation as animation

'''Create the graphic representation of the data, given a dataset'''

def draw_graph(x, y):
	'''Draw the static graph'''
	plt.plot(x, y)
	plt.xlabel('Time (a.u.)')
	plt.ylabel('Inverse function W(t)')
	plt.axhline(y = 0, color = 'black', linestyle = 'dashed')
	plt.show()

def draw_animated_graph(x,y):
	'''Draw the animated graph'''
	fig, ax = plt.subplots()
	plt.axhline(y = 0, color = 'black', linestyle = 'dashed')
	line, = ax.plot(x, y)

	def update(num, x, y, line):
		'''Update to next frame with next data pair'''
		line.set_data(x[:num], y[:num])
		return line,

	def speed_check(x):
		'''Determine the framerate to limit animation time'''
		T_max = len(x)
		time_constant = 8000 #configurable?
		frame_interval = time_constant/T_max
		return frame_interval

	ani = animation.FuncAnimation(
		fig, update, len(x), interval=speed_check(x), 
		fargs=[x, y, line], blit=True)
	plt.show()
	