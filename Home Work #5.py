numbers = [12, 45, 2, 89, 34, 6, 90, 23]
minimum = numbers[0]
maximum = numbers[0]
for n in numbers:
    if n < minimum:
        minimum = n
    if n > maximum:
        maximum = n
print(f"Minimum: {minimum}, Maximum: {maximum}, Difference: {maximum - minimum}")
