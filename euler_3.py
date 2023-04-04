"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def IsNumPrime(num):
  for x in range(2, num):
    if (num % x == 0):
      return False
  return True

def LargestPrime(num):
  largestPrime = 1
  for x in range(1, num+1):
    if IsNumPrime(x):
      if (num % x == 0):
        largestPrimeFactor = x
  return largestPrimeFactor