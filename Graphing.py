import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv
import itertools
from datetime import datetime

'''Create the graphic representation of the data, given a dataset.'''

def draw_graph(x, y, saving):
	'''Draw the static graph'''
	plt.plot(x, y)
	plt.xlabel('Time (a.u.)')
	plt.ylabel('Inverse function W(t)')
	plt.axhline(y = 0, color = 'black', linestyle = 'dashed')
	plt.show()
	if saving == True:
		write_csv(x, y)
	else:
		plt.show()

def draw_animated_graph(x,y, time_constant):
	'''Draw the animated graph.'''
	fig, ax = plt.subplots()
	plt.axhline(y = 0, color = 'black', linestyle = 'dashed')
	line, = ax.plot(x, y)

	def update(num, x, y, line):
		'''Update to next frame with next data pair.'''
		line.set_data(x[:num], y[:num])
		return line,

	def speed_check(x, time_constant):
		'''Determine the framerate to limit animation time.'''
		T_max = len(x) - 1
		frame_interval = time_constant/T_max
		return frame_interval

	ani = animation.FuncAnimation(
		fig, update, len(x), interval=speed_check(x, time_constant), 
		fargs=[x, y, line], blit=True)
	plt.show()

def write_csv(time, function):
	'''Generate .cvs file containing the input datasets time & function.'''
	current_time = datetime.now().strftime("%H-%M-%S")
	file_name = 'Jaynes-Cummings inverse function ' + current_time + '.csv'
	with open(file_name, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['Time (a.u.)', ' Inverse Function W(t)'])
		for (t, f) in zip(time, function):
			writer.writerow([t, f])


	