class Solution:
    def lengthOfLongestSubstring(self, st: str) -> int:
        s = 0
        e = 0
        max_sm = 0
        d = dict()            
        if len(set(st)) == len(st):
            return len(st)
        
        while e < len(st):
            if st[e] not in d:
                d[st[e]] = e
                e += 1
            else:
                l = e - s
                if l > max_sm:
                    max_sm = l
                
                idx = d[st[e]]

                while s <= idx:
                    del d[st[s]]
                    s += 1
                d[st[e]] = e
                e += 1

        # Capture the length of the final remaining window at the end
        max_sm = max(max_sm, e - s)

        return max_sm
