from collections import defaultdict


class Solution(object):
    def dec_to_bin(self, num_in, base):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        binstr = []
        num = num_in
        while num > 0:
            remainder = hex(num % base).replace('0x', '')
            num = int(num / base)
            binstr.append(remainder)

        print(binstr)
        binstr.reverse()
        A = [str(x) for x in binstr]
        A_str = ''.join(A)
        print(A)
        return (A_str)


def main():

    S = Solution()
    num = 233
    print('Dec %d to bin = %s are ' % (num, S.dec_to_bin(num, 2)))
    print('Dec %d to oct = %s are ' % (num, S.dec_to_bin(num, 8)))
    print('Dec %d to hex = %s are ' % (num, S.dec_to_bin(num, 16)))


if __name__ == "__main__":
    main()
