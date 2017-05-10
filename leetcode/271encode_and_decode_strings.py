class Codec:
    def encode(self, strs):
        res = ""
        for _str in strs:
            res += str(len(_str)) + " " +  _str
        return res

    def decode(self, s):
        res = []
        lenStartIdx = 0
        
        while lenStartIdx < len(s):
            lenEndIdx = lenStartIdx + 1
            
            while s[lenEndIdx] != " ":
                lenEndIdx += 1
                
            strStartIdx = lenEndIdx + 1
            l = int(s[lenStartIdx:lenEndIdx])
            
            res.append(s[strStartIdx:strStartIdx+l])
            lenStartIdx = strStartIdx + l
            
        return res

if __name__ == "__main__":
    codec = Codec()
    strs = codec.encode(["hello", "world", "m45345", "  ~$* "])
    strs2 = codec.encode(["63/Rc","h","BmI3FS~J9#vmk","7uBZ?7*/","24h+X","O "])
    print strs2
    print codec.decode(strs2)
