"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    List = []
    number = 2
    while len(List)<number_of_primes:
        count=2
        flag = True
        while flag:
            if count == number:
                List.append(number)
                flag = False
            if number % count != 0:
                count= count+1
            else:
                number= number+1
                count = 2
    return List
