class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumbers = { "I": 1 , "V": 5, "X": 10, "L":50,"C":100, "D":500, "M": 1000 }
        res = 0
        
        for i in range(len(s)):
            if i+1 < len(s) and romanNumbers [s[i]] < romanNumbers [s[i + 1]]:
                res -= romanNumbers [s[i]]
            else:
                res += romanNumbers [s[i]]
        return res
                