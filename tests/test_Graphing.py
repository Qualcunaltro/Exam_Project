import pytest
import math
import csv
import itertools
from decimal import getcontext, Decimal

test_range = (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1)
test_function = (-1,
	-0.95062611960097898045063402605592273175716400146484375,
	-0.8078600400715509888271981253637932240962982177734375,
	-0.587141801018192577288346001296304166316986083984375,
	-0.3121941651050128552213891452993266284465789794921875,
	-0.01226999014777041541179869454936124384403228759765625,
	0.28121047704031010283642899594269692897796630859375,
	0.53821964703788882644630575668998062610626220703125,
	0.733448895723868066198747328598983585834503173828125,
	0.8490069926234136143960995468660257756710052490234375,
	0.8761829488924457454146477175527252256870269775390625)
test_time_constant = 8000

def speed_check(x, time_constant):
		'''
		Determine the framerate to limit animation time.
		Input: the time data set, a positive integer time constant.
		Output: set the time interval for FuncAnimation, the time in ms between frames.
		'''
		T_max = len(x) - 1
		frame_interval = time_constant/T_max
		return frame_interval

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
			

def test_speed_check():
	'''Check if the function work as we expect, i.e. divide correctly the interval between frames.'''
	assert speed_check(test_range, test_time_constant) == 800.0

def test_decimal():
	'''Check if the approximation to decimal is close enough to the true raw values.'''
	getcontext().prec = 4
	for v_raw in test_function:
		v_rounded = round(v_raw, 3)
		assert math.isclose(v_raw, v_rounded, abs_tol=0.001) == True
