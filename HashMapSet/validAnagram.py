#### We could also use Counter to find the frequency map quickly but I used the following approach with the same time and space complexity O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d_s = dict()


        for i in s:
            if i not in d_s:
                d_s[i] = 1
            else:
                d_s[i] +=1
        print(d_s)
        for j in t:
            if j in d_s:
                d_s[j] -=1
            else:
                return False
        for i,j in d_s.items():

            if j!=0:
                return False
        return True
