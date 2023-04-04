class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        suggestions_at_every_char = list()
        # print('products=', products)
        # print('word=', searchWord)
        sorted_products_list = products
        sorted_products_list.sort()
        suggested_products = sorted_products_list
        for i in range(len(searchWord)):
            print('\n\n\nindex=', i)
            count = 0
            new_suggested_list = list()
            if len(suggested_products) == 0:
                break 

            for product in suggested_products:
                if (i < len(product)):
                    if searchWord[i] == product[i]:
                        new_suggested_list.append(product)
                        print(product)
                        count += 1
            print(new_suggested_list)
            suggested_products = new_suggested_list
            suggestions_at_every_char.append(suggested_products[0:3])
        return(suggestions_at_every_char)


def main():
    print(
    Solution().suggestedProducts(
        # ["abba"], "dabba"

        #["bags","baggage","banner","box","cloths"],
        #"bags"
        #["havana"], 
        #"tatiana"
        
        #["mobile","mouse","moneypot","monitor","mousepad"],
        #"mouse"
        ["vsmadqkolyduhygaprdqhxzjrapvvvv","gnsgdxf","utulgnjlkotgccloguvktwaxzjwplmdnhvihum","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbnei","utulgnjlkotgccloguvktwaxoaeogbsgegteviopb","utulgnjlkzqsbzvkoauvhnh","utulgnjlggueayqfanngdjnsgehwj","utulgnjlkotgvqieu","utulgnjlkotgccloguvktwaxoakxozjn","utmuklxtpgxdervbnzbgmccjccoycs","utulgnjlkotgccloguvktypqzymmtrzgpvhah","utulgnjlkotgccloguvktwaxoaeogvzqlgqwlvx","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbnoar","kmsrjmkuukyhwbpgxpejgcqpcgsgseerbp","utulgnjlkotgccloguvktwaxoaeogvv","esbxhykgbdkjwwvlgxltj","utulgnjlkotgccloguvktwaxquuohbwrgjcebwdixr","utzxzjzxioeamaxfvzurwimglzu","pxnokuo","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpu","utulgnjlkotgccloguvktwaxoapfgodyjitrins","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkf","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbnw","utulgnjlkotgccloguvktwaxoaeogvzqlgxzknnbqgr","utyuhabivmnntumqhitxrphorqopssgxdsm","utulgnjlkotgcvhrlilruzgrvkkglwfocfehzh","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbs","kmclwrvk","xlisxvedubbilwymuhbomexpcsmfvtowvadoxxu","phsqsyjqxeiljhgxycpapkqlavk","cvk","utupstizwflwvmgaiumdmowhjsr","fus","cafvusslvaawrb","utsipqaypgwwipqmeetburywagj","rutpcaapvjkoiibcmwhtyex","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbnoal","utulgnjlkotgcclzkfzwupomzeuwjklgnvvjgip","utulgnjlkotgccloguvktwaxoaeogvzqlbg","utulgnjlkotgccloguvktwaxoaeogvzqlggcrsko","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpktctm","bkkecavljaqptalivkjpmeznobypskxsklik","utulgnjlkotgccloguvktwaxoaeogvzlqrbgf","tciykqznfynxocmfdyrajrakbvlfpgox","utulgnjlkotgccloguvktwaxoafiedq","iwtmzpzmumxbmx","qdypizxv","utulgnjlkotgccloguvktwjyg","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpknuym","utulgnjlkotgcclohqajnq","utulgnjlkakihrdycmqbgofiijshoze","utulgnjlkjchoopnwlzzxxhnhsvcblddfnvwafel","utulgnjlkotgccloguvktwaxoaeogvzqlgqwetkk","utulgnjlkotgccloguvktwaxoaeorbivmjlgtyhuota","undqysjlwjlhzohtshhqznmxcdastfhlrwdbyfm","utulgnjlkotgccloguvktwunrvdo","devwgwhyprthrjdaqusrbdndgdaxcklrvhrghzpk","utulgnjlkotgccldjzkjkykyiblgfltbhhe","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbnoav","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkby","utulgnjlkotgccloguvktwaxoaeogvzqlgnx","utulgnhmuwqr","utulgnjlkotgccloguvktwaxoaeogvtsubz","utulgnjlkotgccloguvktwaxoaeogvzqlgqwu","utulgnjlkotlczqiyxkaues","utulgnjlkotgccloguvktwaxvmkkocyo","essrqlgjkrjaayzttkwlvwwdvepm","dfuyxgzpydsqinsnjkt","sk","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbntrs","utulgnjlkotgcclogugjrghwermdgbxlldpfd","uazugxdbqqjqbwduxivxtdiyvheyreslwbmyacfcfma","ynxdlrofnaaamzsmebxiwohegshbowxoyrvme","utulgnwwlgnyxovnedpemuglpmdenhxxdyanuprd","utulgnjlkotgccloguvktwaxupfrxxxwdsd","ndumnexlqqbtooreattnhibhucyldmvt","komrvcl","utulgnjskqxvzfbrbnojeuzgsgbi","utulgnjlkotgccloguvktwhrxjmorbpwmdytjch","mjzeqelitxftczpllcgcdwbrgtxmfyb","ksgeyluhppaddondhgc","utulgnjlkotgcclswgbhprbtisuztpmvosapsmzao","utulgnjlkotgf","utulgnjlkotgfwyxlsjgllacymld","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbnpqn","utulgnjlkotgccloguvktwhfni","utulgnjlkotgcclodug","utulgnjlkotgcclogcrfvumyaahcenikybwkxjppjuwv","utulgnjlkotgccloguvktwaxoaeogvzqlgpplgud","ghpgyiaavavthztpjchgjllrdhlrnfjwme","wlesdjzspxjcbfnodtsxl","ftgpsuwcqmofdpyxfcwdjbbgakbzyqvcg","wmbfnwixbtnuayoxssehabhrbvdyymkaocs","kunfcklqrjhdollzyhjg","utulgnjlkotgccloguvktwaxoaeogvp","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbnoah","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbnor","utulgnjlyciphuyhlqmglsffkkyfyvvelnurmode","dypguyuxzjbxpclvzcgbohgwtllfmevybgczcyumpwuo","utulgnjlkotgcclogugbfyitsmmflcimwpummldpw","mvsxzfklguypsrkpnmvntpchcx","utulgnjlkotgccloguvktwaxoaaflmyadalkhkz","rnjftmxry","utulgnjlkotgcclogmysnkzaxlddfhaihcfrv","utulgnjlkotgccpdfmxltawcsmoktylqhlbdnrwlm","utulgnjlkotgccloguvktwaxoaeogvzqlgqwvziee","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbjusm","utulgnjlkotgccloguoljf","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbd","utfqlnc","utulgnjlkotgccloguvktwawzhivexshqnkgvvpphf","utulgnjlkotgccloguvktwaxoaeogvzqlu","utulgnjlkotgcclorbjpaspmbuhqp","sazlasfuzoxg","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbny","utulgnjlkotgccvgqj","utulgnjlkotgccloguvktwaxoaeogvzqljhd","ecgwsubbui","utulgnjlkotgccrfjyjtaqi","pawokwnjurovmihsladrbkwxkpdduswrponatk","ezblwzrilwfcjvnasmtzso","ekqdugfmyjnbqefeorbaypcqxs","utulgnjlkotgcclobuxzogirrfdpbuxjejfofpo","kjzmhvdxtkjzrzsazmigqilixtcogtj","utulgnjlkotgccldtfgzrvqtnfjrmmylfesof","uwdjovpphryyrpyxemldhzkmmetaceoxgiseemxgar","utulgnjlkotgccloguvbekcs","cuprucyavitshrjvgtdnfqftw","ulynvxattqhevjadhbhpswozfoctauswnfj","nwluotzssluyvpf","idqnmhnkdehgvycznhjlhwyig","mzcikveabrvdtynkbhigvcmjwqtbla","hjrjiwumuhrraqrkmxkufvjwpvyvkkcylmc","utulgnjlkotgccloguvktwlqoilzjd","utulgnjlkotgccloguvktwaxoaeogpjbxgeaagfjo","jerkgaqyxtsjwawqunyriirnwarox","utibmuliyumbkxttleqwxencuyk","iswibazkfuczzbveezdiyuac","fkktqmwxidcdfahnqwqnw","exyfpfmjzgakogpnufew","utulgnjvbergkszcgibvqdwfmoujwvvgzvgvo","xzwycfgsvbjpdbqqwnkgxrheeutu","utulgajwidklidnddk","brkluarnqnxhdksiw","utulgnjlkotgccccihuhymrrtcpyhxbxrcsas","ygyepkkpttqazxjbpfk","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtgspmps","utulgnjlkotgcclogmvxxwmrmciqytq","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkkc","utulgnjlkotgccloguvktwaxoaeogfunv","zow","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkxmxml","mmfthjgvvgorgrd","jevrpakiwqxxifnajpdcdlqglnnalwifihutrz","utulgnjlkotgckuyzufsnfipwc","iykdstmvuaontqcddadldjmgw","utulgnjlkotgccljkrkeokjiesywqaxgvr","utulgnjlkotgccloguvktwaxoaeogrmyvaznzot","utulgnjlkosrhtgteokwlxrsm","utulgnjlkotgccloguvktwaxoaeogvzqzkkrcrugjd","r","qaoskkzcfiefemnf","utulgnjlkotgccloguvktwaxoaezddwpnpvnslqa","vjurawhjtlwytsogqvwdpeojopxutv","utulgnqebiiwbuueqse","utumehejudsigjacolisxegtegzo","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbnosp","utulgnjlkotgcccnislait","utulgnjlgt","utulgnjlkotgcclockykbnfigttqp","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbnofu","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtciyzjyv","utulgnjlkotgccloguvktwaxoaeogvzqlozduvyxmhyb","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbnoaf","utulgnjlkotgccloguvktwaxoaeogvzqlggl","utulukx","utulgnjlkotgccloguvktwaxoidev","utulgnjlkotgccloguvktwalaafjonuoemllze","utulgnjlkotgccloguvktrwahdfvgbshw","ukdpjsnogirtwyffy","tndxyinnemiuqguigzfuztgcrjjnpptkbjhyfo","utulgnjlkotgccloguvktwaxoib","faljccfzctjecnaicvofio","uyxnwavopzycofkcridolmylgikxpzlq","utulgnjlkotgcclsmgqb","nmpmmbldbkctubifqgpfzgaxtcbfpvjgqhizwoxkopw","u","utulgnjlkbfhqskkbhssbtxvlodvscsnsrvalzm","miluljnowlrwoikspoowsmecyoxpqzucilgcjzevyr","umnpllhttf","utulgnjlkotgcclf","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbnoao","utulgnjlkotgcclyqhmabtundhnysxelp","ljcridpvtgafadflnjguwmgksjfzihyqx","hekbxxcwzrtqsjovrwsn","utulgnjlkotgccloguvktwaxoaeogvzxbd","pfpcmpvikefvgowazugyzdozbu","cyotwihtbdsvvotpffxarybdhvtmpzedihyqtddflc","iuvn","nrdybnl","utulgnjlkotgccloguvnlvaholcs","utulgnjlkotgccloguvktwaxoaeogvzqlgltljgwiarv","aazqse","qualx","qzjzyt","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbnoaxx","utulgnjllfaoletsmqwxhucduuxhbq","fvickpphhiembucfjtv","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbnoaxg","mvgifsstqalozynscrfkinni","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbnoaxj","utulgnjlkotgccloguvktwaxoaeogvzqlwpi","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbnoaxk","utulgnjlkotgccloguvktwaxoaeogvzgjnqunjdje","utulgnjlkotgccloguvktwaxoaeogvzqlymcanevcuj","utulgnjlkotgccloguvktwaxoaeogqzshdtcab","ltguwbygbqyteuvejxluncbkrzwoeojcn","utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpf","utulgnjlkotgccloguvktwaxoaeogvzqlgqwxzycy","wouhaqsblqomgkayjgmcbulgbdgukrmoomgtwoyqq","utulgnjlkotgcclogunkjbuthlp","utulgnjlkotgccloguvktwaxoaeogiehtfoblea","utulgnjlkotgcclogugwjtnwmotwrkwloxljcnswqun"],
        "utulgnjlkotgccloguvktwaxoaeogvzqlgqwtpkbnoaxwwlwxitmrdoizupxnqtvlvvshqzmrgnzmrsjbpiugddrmljdfmgtwzlizrzkclqwgzlsjfjlggptosvbzvxbyerlbdfeoeoewriznnhajvoxeqgebucuyvkrlpyngzbgezthhkgprzuecvgcdkzdldazpzjecrxendmrxukqrbcslsmyeheiterutvmjjvntmsvsnpcmjiludnuqeabldzjzubccrbhcxtysjrcixkiyputrkdzjkojzvfgocyaxdqytdcziqjufqlhryqrmmtxjyeptwxcoazxhljkutbmbsueoalunqugrzsdpxfojrjksmoqtqqvhrmzfgwmqhyrkqnrkzxzbpwalfqxfjuldztedjpjgkjkpabcarbvrhxgwktvyxbdnqynxpbrmrsrlcyslcidtoabscnes"

))

if __name__ == "__main__":
    main()
