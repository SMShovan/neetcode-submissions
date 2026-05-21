class Solution:

    def encode(self, strs: List[str]) -> str:

        encode = ''

        for s in strs:
            encode+= str(len(s)) + '/.' + s
        return encode

    def decode(self, s: str) -> List[str]:
        
        decode = []

        i = 0

        while (i < len(s)):
            delim = s.find('/.', i)
            length = int(s[i:delim])
            str_ = s[delim + 2: delim + 2 + length]
            decode.append(str_)
            i = delim + 2 + length
        return decode        