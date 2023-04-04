from collections import defaultdict


class Solution(object):
    def palindrome(self, s):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        palin = True
        for i in range(int(len(s)/2)):
            if s[i] != s[len(s)-1-i]:
                palin = False

        return (palin)
            


def main():
    s = 'AbA'
    S = Solution()

    print('palindrome = %s is a palindrome' % s, S.palindrome(s))


if __name__ == "__main__":
    main()
