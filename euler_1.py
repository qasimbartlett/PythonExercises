"""
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
def FindAllMultiples(max_val, multiples_of):
  # i = list(range(0, max_val, multiples_of))
  all_multiples = []
  i = multiples_of
  while i < max_val:
    # print(i)
    if int(i%multiples_of) == 0:
      all_multiples.append(i)
      # print(i)
    i += 1
  print(all_multiples)




