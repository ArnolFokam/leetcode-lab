class Solution:
    """Module containing the solution
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        ms1, ms2 = [0] * 26, [0] * 26
        
        for i in range(len(s1)):
            ms1[ord(s1[i]) - ord('a')] += 1
            ms2[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26):
            matches += (1 if ms1[i] == ms2[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            
            if matches == 26: return True

            index = ord(s2[r]) - ord('a')
            ms2[index] += 1

            if ms1[index] == ms2[index]:
                matches += 1
            elif ms1[index] + 1 == ms2[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            ms2[index] -= 1

            if ms1[index] == ms2[index]:
                matches += 1
            elif ms1[index] - 1 == ms2[index]:
                matches -= 1

            l += 1

        return matches == 26