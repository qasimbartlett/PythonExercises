"""
https://leetcode.com/problems/partition-labels/
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
"""
class Solution(object):
        
    def findLastEntry(self, character, in_string):
        # print('character=%s= in_str=%s' % (character, in_string))
        ret = -1
        for i in range(len(in_string)-1, 0, -1):
            if character == in_string[i]:
                return i
        return ret

    def partitionLabels2(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        position_2 = -1
        res = list()

        print('\n\nS=%s=' % S)
        if len(S) <=1 :
            res.append(S)
            return res
        
        position_2 = -1
        position_1 = 0
        for position_1 in range(len(S)-1):
            character = S[position_1]
            position_2 = self.findLastEntry(character, S)
            print('character=%s= str=%s= pos1=%d= pos2=%d' % (character, S, position_1, position_2))
            # Found another instace of character
            if position_2 != -1:
                break  
                  
        if position_2 != -1:
            res.append(S[0:position_1])
            
            # check if any character between post1-post2 has a dup putside
            res_2 = list()
            for i in range(position_1, position_2+1):
                res_2.append(self.findLastEntry(S[i], S))
            position_2 = max(res_2)
            res.append(S[position_1:position_2+1])

            remaining = S[position_2+1:]
            print('res=%s, remai=%s=' % (res, remaining))
        else:
            res.append(S)
            remaining = ''
        print('3: res=%s=' % res)
        res = list(set(res)) + self.partitionLabels2(remaining)
        print('--- S=%s res=%s---' % (S, res))
        return res

    def partitionLabels(self, S):
        res = self.partitionLabels2(S)
        print('===res=%s=' % res)
        res2 = list()
        for pattern in res:
            len_pat = len(pattern)
            # print('1. Ifrees i=%s= =%d=' % (pattern, len_pat))
            if len_pat > 0:
                print('2. Ifrees i=%s= =%d=' % (pattern, len_pat))
                res2.append(len_pat)
                # print('Ifrees i=%s= =%d=' % (pattern, len(pattern)))
                # res2.append(len_pat)

            # res.append(len(i))
        print('res2=%s=' % res2)
        return res2


def main():
    S = Solution()
    test = 'dccccbaabe'
    print('Partitions are %s ' % S.partitionLabels(test))


if __name__ == "__main__":
    main()
