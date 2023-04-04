"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def IsThisAPalindrome(num):
  num_str = str(num)
  num_str_len = int(len(num_str))
  print('length=', num_str_len, 'str', num_str)
  mid = int(num_str_len/2)
  print('mid=', mid)
  ThisIsPalindrome = True
  for i in range(0, mid):
    left = num_str[i]
    right = num_str[num_str_len-i-1]
    print (left, right)
    if left != right:
      ThisIsPalindrome = False
  return ThisIsPalindrome

def LargestPalindrome(n1, n2, n3):
  num = 1+ n1*n2*n3
  count = 1
  while count:
    num -= 1
    count += 1
    if IsThisAPalindrome(num):
      print('Num of ops=', count)
      return
