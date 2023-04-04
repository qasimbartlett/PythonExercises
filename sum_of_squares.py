import math  

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i=-1
        res = False
        all_nums = dict()
        while i < int(math.sqrt(c)):
            i += 1
            first_num = i
            all_nums[first_num**2] = first_num
            second_num = math.sqrt(c - first_num**2)
            print('FirstNum=%d secondNum=%f   c=%d' % (first_num, second_num, c))

            if second_num.is_integer():
                res = True
                print('Found it:FirstNum=%d secondNum=%d   c=%d' % (first_num, second_num, c))
                return res
        print('Result=%s' % res)
        return res
            
def main():
    S = Solution()
    S.judgeSquareSum(2147482647)


if __name__ == "__main__":
    main()