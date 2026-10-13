number = int(input("Enter a three-digit number: "))

hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10

sum_squares = hundreds**2 + tens**2 + ones**2

print(f"Sum of squares of digits:{sum_squares}")


