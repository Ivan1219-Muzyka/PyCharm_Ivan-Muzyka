number = int(input("Enter a number: "))

mask = 1 << 3
bit_enabled = (number & mask) !=0

result = number << 3

print("3rd bit is enabled:", bit_enabled)
print("Number *8:", result)

