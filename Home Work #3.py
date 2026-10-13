import math
a = 3.0
b = 4.0
expected_c = 5.0

c= math.sqrt(a**2 + b**2)
perimeter = a + b + c
matches = math.isclose(c, expected_c, abs_tol=1e-6)

print(f"Hypotenuse: {c}")
print(f"Perimeter: {perimeter}")
print(f"Manches: {matches}")
