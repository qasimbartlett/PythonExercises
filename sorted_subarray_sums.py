# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/
class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        sumList = list()

        for start in range(len(nums)):
            end = start+1
            sum = nums[start]
            sumList.append(sum)
            # print(sum)
            while end < len(nums):
                sum += nums[end]
                end += 1
                sumList.append(sum)
                # print (sum)
        sumList.sort()
        print(sumList)

        finalSum=0
        start = left-1
        while (start < right):
            finalSum += sumList[start]
            start += 1
        print(finalSum % (pow(10, 9)+7))

def main():
    S = Solution()
    # [1,2,3,4], n = 4, left = 1, right = 5
    S.rangeSum( [1,2,3,4], 4, 1, 5)


if __name__ == "__main__":
    main()