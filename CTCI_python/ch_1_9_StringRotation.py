import numpy as np

s1 = str(input())
s2 = str(input())

def IsSubstring(s1,s2):#determine whether s2 is a substring of s1
    l1 = len(s1)
    l2 = len(s2)
    
    for i in range(l1):

        if i != l1-l2+1:
            if s1[i:i+l2] == s2:
                return True
        else:
            break
    return False    

newString = 2*s1 ##s1+s1
result = IsSubstring(newString,s2)
if result == True:
    print("{s2} is the rotated version of {s1}".format(s1=s1,s2=s2))
else:
    print("{s2} is NOT a rotated version of {s1}".format(s1=s1,s2=s2))
         
    