#### If words in a senetnce follows the same pattern or not
#### Find the first occurances of each element
#### O(N) in time and space


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        
        if len(pattern) != len(words):
            return False

        d = {}
        pattern_idx = {}
        word_idx = {}
        for idx, i in enumerate(pattern):
            if i not in d:
                pattern_idx[i] = idx
                d[i] = 1
            else:         
                d[i] +=1
        
        d.clear() # to free up space

        for idx, j in enumerate(words):
            if j not in d:
                word_idx[j] = idx
                d[j] =1
            else:
                d[j] +=1

        print(pattern_idx)
        print(word_idx)
        
        if list(pattern_idx.values()) == list(word_idx.values()):
            return True
        else:
            return False


            
