"""
https://leetcode.com/problems/two-sum/
"""

def two_sum_n2(nums, target):
  for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
      print(i,j,nums[i], nums[j])
      if nums[i]+nums[j] == target:
          print(i,j)
          return(i,j)


def two_sum_n(nums, target):
  # euler_5.DivisibleBy([2,5,5,11], 10)
  # euler_5.DivisibleBy([1,3,4,2], 6)
  nums_dict = dict()
  for i in range(0, len(nums)):
    nums_dict[nums[i]] = []
  for i in range(0, len(nums)):
    nums_dict[nums[i]].append(i)
  print(nums, target)
  print(nums_dict)
  # Now find if the complement exists in the dictionary
  for i in range(0, len(nums)):
    # print('index', i)
    # print('nm_dict', nums_dict[nums[i]])
    val1 = nums[i]
    val2 = target - val1
    print('index=', i, 'val1=', val1, 'val2=', val2)
    
    if val2 in nums_dict.keys():
      val2_index = nums_dict[val2].pop()
      print('val2 index=', val2_index)
      if (val2_index):
        if i != val2_index:
          print('answer=', i, val2_index)
          return (i,val2_index)
      
