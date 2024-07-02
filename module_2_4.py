numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
def is_prime(n: object) -> object:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(len(numbers)):
    if is_prime(numbers[i]) and numbers[i] != 1:
        primes.append(numbers[i])
    elif not is_prime(numbers[i]) and numbers[i] != 1:
        not_primes.append(numbers[i])

print(numbers)
print(primes)
print(not_primes)