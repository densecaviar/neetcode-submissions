class Solution:

    def encode(self, strs: List[str]) -> str:
        
        if strs == []:
            return "/e"
        else:
            string="/s".join(strs)   
            return string.encode().hex()
        #now we have made a single string with all the letters.
        # we can encode and decode them in the next function.
        
    def decode(self, s: str) -> List[str]:
        if s=="/e":
            return []
        # first we decode hex to bytes and then to utf-8
        else:
            hextostr=bytes.fromhex(s).decode()
        # then we just split the string according to our separator
            real = hextostr.split('/s')
            return real