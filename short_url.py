import string

# Assume tihis is machine #65

class Codec:
    def __init__(self):
        self._machineNumber = 786
        self._NumCharsForMacineNumber = 3
        self._NumCharsForIndex = 3
        self._insertPosition = 0 
        self._holePosition = 0
        self._MAX_NUM_URLS = 1000
        self._Characters = string.ascii_lowercase[:26] + string.ascii_uppercase[:26] + '0123456789'
        # List of tuples; each tuple is longurl, shorturl
        self._ListOfUrls = [('', '')] * self._MAX_NUM_URLS
        print('==%s===',self.decToEncoding(786))
        self.encode('abba')
        self.encode('dabba')
        self.encode('jabba')
        self.encode('abba')
        self.decode('amQa#ac')

    def decToEncoding(self, num):
        base = len(self._Characters)
        remaining = num        
        ret_str = ''

        if remaining == 0:
            return self._Characters[0]
    
        while remaining > 0:
            ret_str = self._Characters[remaining % base] + ret_str
            remaining = int (remaining / base)
        
        return ret_str
    
    def urlAlreadyExists(self, longUrl):
        for i in range(self._MAX_NUM_URLS):
            if longUrl == self._ListOfUrls[i][0]:
                return self._ListOfUrls[i][1]
        return ''
            
    def nextHole(self):
        for i in range(self._MAX_NUM_URLS):
            if self._ListOfUrls[i][1] == '':
                return i
        return -1       

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        short_url = self.urlAlreadyExists(longUrl)
        if self.urlAlreadyExists(longUrl):
            return short_url
          
        if self._insertPosition == self._holePosition:
            short_url = self._InsertUrl(self._insertPosition, longUrl)
            self._insertPosition += 1
            self._holePosition += 1
        else:
            if self._holePosition >= 0:
                short_url = self._InsertUrl(self._holePosition, longUrl)
                # Send the short url to the caller, then update the posiions
                self._holePosition = self.nextHole()
        return short_url

    def _InsertUrl(self, insert_at, longUrl):
        # 1st 3 characters for machine number
        prefix = (self._Characters[0]*self._NumCharsForMacineNumber + \
        self.decToEncoding(self._machineNumber))[-self._NumCharsForMacineNumber:]
        print('Idrees prefix=%s=' % prefix)
    
        index_str = (self._Characters[0]*self._NumCharsForIndex + self.decToEncoding(insert_at))[-self._NumCharsForIndex:]
        print('Idrees insert_at=%d= index_str=%s=' % (insert_at, index_str))
        short_url = prefix + index_str
        print('Idrees short_url=%s=\n\n' % short_url)
        # then random 3 characters
        self._ListOfUrls[insert_at] = (longUrl, short_url)
        return short_url
     

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        index_str = shortUrl[self._NumCharsForMacineNumber:]
        base = len(self._Characters)
        len_url = len(index_str)
        num = 0
        print('idfrees index_str=%s= base=%d= len_url=%d=' % (index_str, base, len_url))


        for i in range(len_url-1, -1, -1):
            if index_str[i] not in self._Characters:
                print('Idrees an unspoorted character seen in short Url')
                return 'No Long Url'
            num = num + self._Characters.index(index_str[i]) * pow(base, len_url - i - 1)
            print('num=%d' % num)
        
        print('short_url=%s, index=%d' % (shortUrl, num, ))

        return self._ListOfUrls[num][0]
        
def main():
    Codec()


if __name__ == "__main__":
    main()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
