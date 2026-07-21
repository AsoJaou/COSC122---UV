from fractions122 import Fraction, ReducedFraction
f = Fraction(1, 6)
r = ReducedFraction(2, 6)

# the add should return a Fraction
print('{} + {} = {}'.format(repr(f), repr(r), repr(f + r)))

# the add should return a ReducedFraction
print('{} + {} = {}'.format(repr(r), repr(f), repr(r + f)))

# the multiplication should return a Fraction
print('{} * {} = {}'.format(repr(f), repr(r), repr(f * r)))

# the multiplication should return a ReducedFraction
print('{} * {} = {}'.format(repr(r), repr(f), repr(r * f)))