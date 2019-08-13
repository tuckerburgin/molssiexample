import molssiexample as me
import random
import pytest

@pytest.mark.parametrize('x, answer',[(0,1), (1,2), (2,2.5), (10, 2.7182)])
def test_euler(x, answer):
	assert me.mymath.euler(x) == pytest.approx(answer, abs=0.01)

def test_euler_fail():
	with pytest.raises(ValueError):
		me.mymath.euler(-1)

def test_pi():
	random.seed(0)
	assert me.mymath.pi(10000) == pytest.approx(3.14159, abs=0.01)
