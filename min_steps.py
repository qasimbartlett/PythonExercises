class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        for x in s.split():
            print(x)

def main():
    s = 'bab'
    t = 'aba'
    S = Solution()
    
    print('min steps = ', S.minSteps(s, t))



if __name__ == "__main__":
    main()

