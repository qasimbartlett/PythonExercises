
class Words:
    # Assumptions
    # words in s1, s2 are unique
    # words dont start with another word: eg: abba,   abbadabba
    def FindSpacesInSentence(self, s1, s2):
        return True
        #spaces_index_list = []
        #new_s1 = ' ' + s1 + ' '
        #for word in new_s1.split():
        #    space_index = new_s1.find(' ' + word + ' ')
        #    spaces_index_list.append(space_index)
        #    # print(word, space_index)
        #spaces_index_list.append(len(new_s1))
        # 4 words in sequence
        #width=2
        #for i in range(len(spaces_index_list) - width):
        #    start = spaces_index_list[i]
        #    end = spaces_index_list[i+width]
        #    sub_str = s1[start:end]
        #    sub_str_set = set(sub_str)
            # print(i, sub_str)
            #print(sub_str.split())
            # if (set(s2) == sub_str_set):
            #    print('This is the shortest')


    def SubStrExists (self, s1, s2):
        s2_dict = {}

        word_count = 0
        ind = 0
        # Create an empty dict of lists and append to it
        for word in s2.split():
            word_count += 1
            if word_count > 1:
                word = ' ' + word
            ind = s2.index(word, ind)
            s2_dict.setdefault(word, []).append(ind)

        print(s2_dict)

        word_count = 0
        all_indces = []
        for word in s1.split():
            word_count += 1
            if word_count > 1:
                word = ' ' + word
            print(word)
            print(s2_dict[word])
        # print(all_indces)
        return True


def main():
    S1 = 'a cat orange catrina abba      bobcat'
    S2 = 'I have a cat a dog and an orange'
    #     012345678901234567890123456789012345'
    print(Words().FindSpacesInSentence(S1, S2))
    # print('Maze: path exists ', Words().SubStrExists(S1, S2))


if __name__ == "__main__":
    main()
