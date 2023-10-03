"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

import math

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError
    else:
        count = 0
        num = 2
        while count < number_of_primes:
            if (isPrime(num)):
                list.append(num)
                count += 1
            num += 1

    return list


def isPrime(num):
    upper_check = math.floor(math.sqrt(num))
    for i in range(2, upper_check + 1):
        if (num % i == 0):
            return False
    return True

    