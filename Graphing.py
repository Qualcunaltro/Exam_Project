import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv
import itertools
from decimal import getcontext, Decimal
from datetime import datetime

'''Create the graphic representation of the data, given a dataset.'''

def draw_graph(x, y, saving):
	'''
	Draw the static graph from two data set (time and function) and saves the data in a .csv file.
	Input: time data set, the function data set and the boolean check for saving the data.
	Output: a graph and, optionally, a .csv file.
	Note: to save the graph as an image, use the matplotlib interface during the graph visualization.
	'''
	plt.plot(x, y)
	plt.xlabel('Time (a.u.)')
	plt.ylabel('Inverse function W(t)')
	plt.axhline(y = 0, color = 'black', linestyle = 'dashed')
	if saving == True:
		plt.show()
		write_csv(x, y)
	else:
		plt.show()

def draw_animated_graph(x,y, time_constant, saving):
	'''Draw the animated graph from two data set (time and function) and saves the data in a .csv file.
	Input: time data set, the function data set and the boolean check for saving the data.
	Output: a graph and, optionally, a .csv file.
	Note: to save the graph as an image, use the matplotlib interface during the graph visualization.'''
	fig, ax = plt.subplots()
	plt.axhline(y = 0, color = 'black', linestyle = 'dashed')
	line, = ax.plot(x, y)

	def update(num, x, y, line):
		'''Update to next frame with next data pair.'''
		line.set_data(x[:num], y[:num])
		return line,

	def speed_check(x, time_constant):
		'''
		Determine the framerate to limit animation time.
		Input: the time data set, a positive integer time constant.
		Output: set the time interval for FuncAnimation, the time (in ms) between frames.
		'''
		T_max = len(x) - 1
		frame_interval = time_constant/T_max
		return frame_interval

	ani = animation.FuncAnimation(
		fig, update, len(x), interval=speed_check(x, time_constant), 
		fargs=[x, y, line], blit=True)
	if saving == True:
		plt.show()
		write_csv(x, y)
	else:
		plt.show()

def write_csv(time, function):
	'''
	Write a .cvs file containing the input data sets time & function.
	Input: the time data set and the function data set.
	Output: the .csv file tabling the data, rounded to the decimal place for readability.
	'''
	current_time = datetime.now().strftime("%H-%M-%S")
	file_name = 'Jaynes-Cummings inverse function ' + current_time + '.csv'
	getcontext().prec = 4
	with open(file_name, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['Time (a.u.)', ' Inverse Function W(t)'])
		for (t, f) in zip(time, function):
			tdec, fdec = Decimal(t), Decimal(f)
			writer.writerow([round(tdec, 1), round(fdec, 3)])
				