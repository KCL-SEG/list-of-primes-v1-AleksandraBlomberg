"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    counter= 1
    char = ""
    frequencies = {}
    for x in range(0,len(items)):
        char = items[x]
        if char in frequencies:
            count= frequencies.get(char)+1
            frequencies[char]= count
        else:
            frequencies[char]= 1
    return frequencies
