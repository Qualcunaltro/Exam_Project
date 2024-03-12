import pytest

test_range = (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1)
test_time_constant = 8000

def speed_check(x, time_constant):
		'''Determine the framerate to limit animation time'''
		T_max = len(x) - 1
		frame_interval = time_constant/T_max
		return frame_interval

def test_speed_check():
	'''Check if the function work as we expect'''
	assert speed_check(test_range, test_time_constant) == 800.0