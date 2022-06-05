from typing import Callable

def make_division_by(n: float) -> Callable[[float], float]:
	def make_division(val: float):
		return val / n
	return make_division


division_by_3 = make_division_by(3)
assert(division_by_3(18) == 6)

division_by_5 = make_division_by(5)
assert(division_by_5(100) == 20)

division_by_18 = make_division_by(18)
assert(division_by_18(54) == 3)

assert(division_by_5(division_by_3(60)) == 4)
