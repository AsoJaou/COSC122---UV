from fractions122 import Fraction, ReducedFraction
r = ReducedFraction(12, 24)
print('repr:', repr(r))
print('str:', r)
print('numerator is an int:', isinstance(r.numerator, int))
print('denominator is an int:', isinstance(r.denominator, int))