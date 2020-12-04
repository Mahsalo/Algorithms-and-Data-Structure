class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        sorted_ind = sorted((e,i) for i , e in enumerate(indexes))
        indexes = []
        indind=[] #index of indexes after sorting
        SRC = []
        T = []
        
        for j in range (len(sorted_ind)):
            x = sorted_ind[j]        
            indexes.append(x[0])
            indind.append(x[1])
        for k in range (len(indind)):
            SRC.append(sources[indind[k]])
            T.append(targets[indind[k]])
            
        sources = SRC
        targets = T

        new_ind = 0
        n = 0
        for i in range(len(sources)):

            sr = sources[i]            
            ind = indexes[i]
            if new_ind >=1:
                I = ind + n
               
            else:
                I = ind

            if S[I:I+len(sr)] == sr:
                
                rep = targets[i]
                ending = S[I+len(sr):len(S)]
                starting = S[0:I]
                res = starting+rep+ending
                new_ind = 1
                n += len(rep)-len(sr)           
                S = res
               
                
      
        return S   
                
                    
                
                    
        