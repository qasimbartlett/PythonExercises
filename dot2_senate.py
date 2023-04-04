# https://leetcode.com/problems/dota2-senate/
import collections

class Solution(object):
    def voting_round(self, senate):
        print('in voting round')
        for i in range(len(senate)):
            senator = senate[i]
            print('i=%d; senator=%s=' % (i, senator))
            senator_to_right = senate[(i+1) % len(senate)]
            print('senator to right=%s' % senator_to_right)
            if senator == ' ' or senator_to_right == ' ':
                pass
            elif senator_to_right != senator:
                # ban senator to right
                print('before banning senator; senate=%s='%senate)
                senate_list = list(senate)
                senate_list[(i+1) % len(senate)] = ' '
                senate = ''.join(senate_list)
                print('After  banning senator; senate=%s='%senate)
        return senate.replace(' ', '')

    def victory(self, senate):
        senate_at_start = senate
        senate_at_end = self.voting_round(senate)
        print('senate before=%s=' % senate_at_start)
        print('senate after =%s=' % senate_at_end)
    
    
        # Detect victory
        count_sentors_R = senate.count('R')
        count_sentors_D = senate.count('D')
        if count_sentors_D == 0 and count_sentors_R == 0:
            return 'Z'
        elif count_sentors_D == 0 and count_sentors_R > 0:
            return 'R'
        elif count_sentors_D > 0 and count_sentors_R == 0:
            return 'D'
    
        # Detect a deadlock
        if senate_at_end == senate_at_start:
            return 'X'
    
        return senate_at_end
        

    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        while senate not in ['R', 'D', 'X', 'Z']:
            senate =  self.victory(senate)
        
        if senate == 'R':
            return('Radiant ')
        if senate == 'D':
            return('Dire ')


def main():
    x = Solution()
    print(x.predictPartyVictory('DDRRR'))

if __name__ == "__main__":
    main()
