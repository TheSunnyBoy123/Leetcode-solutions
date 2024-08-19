class Solution:
    def encode(self, strs: List[str]) -> str:
        ret = ""
        for word in strs:
            ret += word + "\n"
        return ret
    def decode(self, s: str) -> List[str]:
        return s.split("\n")[:-1]