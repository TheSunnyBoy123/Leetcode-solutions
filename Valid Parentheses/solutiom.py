class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        if len(s) == 1: return False
        for i in s:
            if i in ["(", "{", "["]:
                l.append(i)
            else:
                if len(l):
                    if i == ")":
                        if l[-1] == "(":
                            l.pop(-1)
                        else:
                            return False
                    if i == "}":
                        if l[-1] == "{":
                            l.pop(-1)
                        else:
                            return False
                    if i == "]":
                        if l[-1] == "[":
                            l.pop(-1)
                        else:
                            return False
                else:
                    return False
        if len(l):
            return False
        return True