from collections import defaultdict


class Solution(object):
    def anagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        # create s_dict
        for i in range(len(s)):
            s_dict[s[i]] += 1
        # Create t_dict
        for i in range(len(t)):
            t_dict[t[i]] += 1

        print(s_dict)
        print(t_dict)

        s_matches = True
        for s_key in s_dict.keys():
            if s_dict[s_key] != t_dict.get(s_key, -1):
                print('1. Mismatch:', s_key, ' Missing in ', t)
                s_matches = False

        t_matches = True
        for t_key in t_dict.keys():
            if t_dict[t_key] != s_dict.get(t_key, -1):
                print('2. Mismatch:', t_key, ' Missing in ', s)
                t_matches = False

        if s_matches and t_matches:
            return True
        else:
            return False


def main():
    # Adding a comment using gitpod
    s = '12341234'
    t = '11223344k'
    S = Solution()

    print('anagram = %s, %s are anagrams' % (s, t), S.anagram(s, t))


if __name__ == "__main__":
    main()
