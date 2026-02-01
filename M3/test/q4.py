import math

def is_prime(n):
    if n <= 1:
        return False
    # Check up to square root of n for efficiency
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Test
print(is_prime(11)) # True
print(is_prime(4))  # False