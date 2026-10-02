class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        matches = 0

        # get frequency map of s1 and s2 initial window 
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1

        l = 1
        n = len(s1)
        for i in range(n, len(s2)):
            if matches == 26:
                return True 

            # character to add : s[i]
            # charater to remove : s[l - i]
            
            r = ord(s2[i]) - ord('a')
            count2[r] += 1
            if count2[r] == count1[r]:
                matches += 1
            elif count2[r] == count1[r] + 1:
                matches -= 1
            
            l = ord(s2[i - n]) - ord('a')
            count2[l] -= 1
            if count2[l] == count1[l]:
                matches += 1
            elif count2[l] == count1[l] - 1:
                matches -= 1
        
        return matches == 26

            

            

            
        
        return False