n = int(input("Enter n:"))

total = 0
primes = []

for number in range(2, n + 1):
    is_prime = True
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        total += number
        primes.append(str(number))

print(f"Sum of primes from 2 to {n} ({'+'.join(primes)}): {total}")
