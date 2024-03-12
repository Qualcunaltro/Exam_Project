import pytest

N_e = 10
T_x = 50
anime = False
approx = 20
time_const = 8000

def setup():
	'''Return the parameters'''
	return(N_e, T_x, approx, time_const, anime)

def test_setup():
	'''Check if the parameters are correctly returned'''
	assert setup() == (10, 50, 20, 8000, False)