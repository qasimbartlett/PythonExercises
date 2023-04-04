# https://leetcode.com/problems/replace-words/
class Solution(object):
    def replaceWords(self, dictx, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        sentence_list = sentence.split()
        for dict_word in sorted(dictx, key=len):
            for i in range(len(sentence_list)):
                sentence_word = sentence_list[i]
                if sentence_word.startswith(dict_word):
                    sentence_list[i] = dict_word
        print(' '.join(sentence_list))      

def main():
    dictx = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"    
    x = Solution()
    x.replaceWords(dictx, sentence)
    x.replaceWords([], sentence)
    x.replaceWords([], '')
    x.replaceWords(dictx, '')

if __name__ == "__main__":
    main()
