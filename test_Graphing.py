import pytest

test_range = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def speed_check(x):
		'''Determine the framerate to limit animation time'''
		T_max = len(x) - 1		
		time_constant = 8000 
		frame_interval = time_constant/T_max
		return frame_interval

def test_speed_check():
	framerate = speed_check(test_range)
	assert speed_check(framerate) == 200.0