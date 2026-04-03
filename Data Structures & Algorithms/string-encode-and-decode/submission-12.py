class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "None"
        return '|e|'.join(strs)

    def decode(self, s: str) -> List[str]:
        # print(s)
        if s == "None":
            return []
        if not s:
            return [""]
        return s.split('|e|')