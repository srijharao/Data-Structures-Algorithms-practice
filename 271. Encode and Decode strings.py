class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        for string in strs:
            for c in string:
                res.append(str(ord(c)))
                res.append('#')
            res.append(' ')
        result = ''.join(res)
        return result
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        string = s.split(' ')
        for word in string:
            temp = []
            for c in word.split('#'):
                if c:
                    temp.append(chr(int(c)))
            res.append(''.join(temp))
        res.pop()
        return res


        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
