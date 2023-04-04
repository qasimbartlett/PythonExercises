"""
https://leetcode.com/problems/letter-tile-possibilities/
You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.
"""
class Solution(object):
    def swap(self, i, j, tiles):
        # print('i=%d=, j=%d= tiles=%s' % (i, j, tiles))
        i_val = tiles[i]
        j_val = tiles[j]
        tiles[i] = j_val
        tiles[j] = i_val
        return tiles

    def numTilePossibilities2(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        # print('Idrees tiles=%s' % tiles)
        if len(tiles) <= 1:
            tiles.append('')
            # print('Idrees hit end; returning tiles=%s' % tiles)
            return tiles
        
        combos = []
        for i in range(len(tiles)):
            # swap
            combos.append('')
            tiles = self.swap(0, i, tiles)
            sub_combos= self.numTilePossibilities2(tiles[1:])
            # undo swap
            tiles = self.swap(i, 0, tiles)
            for j in sub_combos:
                combos.append('%s%s' % (tiles[i], j))
        # return(list(set(combos)))
        return combos
    
        # first = tiles[0]
        #combos = self.numTilePossibilities(tiles[1:])
        #for i in combos:
        #    all_combos.append("%s%s" % (first, i))
        ##    all_combos.append("%s%s" % (i, first))
        #    all_combos.append("%s" % (i))
        #return list(set(all_combos))

    def numTilePossibilities(self, tiles):
        combos = self.numTilePossibilities2(tiles)
        return len(combos) - 1

        
def main():
    S1 = Solution()
    all_combos_size = S1.numTilePossibilities(list('AAABBC'))
    # print(all_combos, 'and its length is ', len(all_combos))
    print('all_combos_size=%d' % all_combos_size)


if __name__ == "__main__":
    main()
