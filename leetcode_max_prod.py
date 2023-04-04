"""
https://leetcode.com/problems/maximum-product-subarray/
152. Maximum Product Subarray
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

def ListProd(somelist):
  ret = 1
  for i in somelist:
    ret *= i
  return ret

def XMaxProd(somelist):
  max_prod = -99999999999
  max_prod_list = []
  for sizee in range(1, len(somelist)+1):
    for position in range(0, len(somelist)):
      temp_max_prod_list = somelist[position:position+sizee]
      prod = ListProd(temp_max_prod_list)
      print('Idrees; size=', sizee, ' positon=', position, 'prod=', prod, ' List=', temp_max_prod_list)
      if prod > max_prod:
        max_prod = prod
        max_prod_list = temp_max_prod_list
  print('--Max prod list=', max_prod_list)
  return temp_max_prod_list

class Solution(object):
  # returns 0 if the #of -ve #s is even
  def NumberOfNegativesEven(self, nums):
    num_negatives = 0
    for i in range(len(nums)):
      if int(nums[i]) < 0:
        num_negatives += 1
    print('NumberOfNegativesEven: Nums=', nums, '# of negs=', num_negatives)
    return num_negatives % 2
      
  def First_n_Last_NegativeNum(self, nums):
    first=0
    last=0
    for i in range(len(nums)):
      if int(nums[i]) < 0:
        first = i
        break
    for i in range(len(nums)-1,-1,-1):
      if int(nums[i]) < 0:
        last = i
        break
    print('First_n_Last_NegativeNum nums=', nums, 'first, last', first, last)
    return (first, last)

  # Multiply all elements in the list and return
  def Mult(self, nums):
    if nums:
      ret = 1
    else:
      # Returns None if list is empty
      return
      
    for i in nums:
      ret *= int(i)

    print('in Mult: Nums=', nums, 'res=', ret)
    return ret

  
  def MaxSubProducts(self, nums_str):
    print('\n\n')
    nums = nums_str.split()
    possible_products = []
    # If there is 1 entry; 
    if (len(nums)==1):
        possible_products.append(self.Mult(nums))
        return possible_products
  
    if self.NumberOfNegativesEven(nums) == 0:
      possible_products.append(self.Mult(nums))
    else:
      (first, last) = self.First_n_Last_NegativeNum(nums)
      possible_products.append(self.Mult(nums[0:first]))
      possible_products.append(self.Mult(nums[first+1:]))
      possible_products.append(self.Mult(nums[0:last]))
      possible_products.append(self.Mult(nums[last+1:]))
    print('possible_products=', possible_products)
    # This list can potentially have a None entry
    possible_products = [x for x in possible_products if x is not None]
    print('possible_products=', possible_products)
    return possible_products
  
  def maxProduct(self, nums):
    allProds = []
    nums_str_t = ' '.join(str(i) for i in nums)
    print('Nums=', nums)
 
    if '0' in nums_str_t:
      allProds.append(0)
      num_str = nums_str_t.split('0')
    else:
      num_str = nums_str_t.split('0')
  
    for i in num_str:
      print('y=', num_str)
      allProds += self.MaxSubProducts(i)
    print('allProds=', allProds)
    print('Max=', max(allProds))
    return max(allProds)  


def run():
  s = Solution()
  res = s.maxProduct([1,-5,6,-5,2,-4,-5,0,3,2,-4,0,-5,-3,-1,-4,-1,4,1,-1,-3,-1,1,3,-4,-6,-2,5,1,-5,0,-1,-5,0,1,2,6,1,2,-6,5,5,0,1,0,1,1,-1,-1,3,1,0,4,-3,0,4,-4,-1,6,5,5,6,-6,1,1,3,4,3,-1,-3,0,-5,-4,1,5,-2,3,-1,2,1,1,6,0,5,-5,6,-6,3,0,4,-1,3,6,0,-2,0,-1,6,4,1,-5,1,0,1,-1,-1,3,5,5,4,2,5,0,-1,5,2,2,-3,-1,-1,0,-6,-2,-5,1,-2,2,0,0,2,-3,-2,-4,1,1,-4,-3,-1,0,0,1,-3,-2,3,-4,5,2,-1,4,1,5,6,0,1,1,-2,-1,0,-1,-5,5,6,6,-1,-1,0,-4,2,1,3,-5,6,-5,-1,-1,-3,-1,-4,-2,-1,-1,1,-3,-4,0,1,-3,4,3,2,-2,6,-3,-6,-6,-2,-5,1,2,0,-1,0,0,-2,3,-4,2,4,3,-1,3,1,0,2,1,-1,0,5,-1,-3,-6,-5,0,6,6,-6,-5,4,-2,-1,0,4,6,-3,1,-1,0,1,-5,5,-3,-3,-3,-1,-1,4,0,-2,-4,3,5,5,-1,-1,-5,-2,-4,-4,6,0,-3,-1,-5,-3,-1,6,1,-5,-1,0,1,-4,-5,0,0,0,-3,-5,-1,-4,-1,5,5,-4,4,-1,6,-1,1,-1,2,-2,-3,0,1,0,0,-3,0,2,5,-6,-3,-3,3,-4,-2,-6,-1,1,4,4,0,-6,-5,-6,-3,5,-3,1,-4,6,-2,0,-4,-1,0,-1,0,6,-6,0,5,0,1,-3,6,1,-1,1,0,-1,1,-1,-6,-3,4,-1,-4,6,4,-1,-3,2,-6,5,0,4,-2,1,0,4,-2,2,0,0,5,5,-3,4,3,-5,2,2,6,-1,-2,1,-3,1,-1,6,-4,0,0,0,2,-5,-4,2,6,-3,-6,-1,-6,0,0,2,-1,6,-4,-5,-1,0,-3,-3,-1,0,-4,3,1,5,0,2,5,0,4,-5,-1,3,1,-1,-1,1,1,-2,3,5,4,6,2,6,-6,5,2,-3,0,-1,-1,3,1,1,1,-2,-5,3,-1,3,0,-1,3,1,1,-2,6,3,-6,5,-5,-5,0,-2,-3,-3,-4,6,-1,-6,6,-3,-5,1,-1,0,0,1,4,-5])
  res = s.maxProduct([2,3,-2,4])
  res = s.maxProduct([-2,0,-1])
  res = s.maxProduct([2])
  res = s.maxProduct([0,2])