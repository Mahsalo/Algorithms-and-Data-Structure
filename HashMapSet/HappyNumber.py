### Happy number: sum of SQ of the digits is 1, if not it goes to an infinite loop --> unhappy
### Hashset : O(log N) time and space, Fast and Slow: (difficult) O(log N) time and O(1) space

def isHappy(N):
    st = set()
    while True:
        # get the digits of the number
        num = []
        s = 0

        while N>0:
            num.append(N%10)
            N = N//10
        print("list of nums.",num)
        for i in num:
            s = s + i**2 #sum
        print("sum",s)

        if s == 1 :
            return True
        else:
            if s in st: # if sum in the set
                return False #cyclic
            else:
                st.add(s)
                N = s


if __name__ == "__main__":

    print(isHappy(200))

    print(isHappy(1000))
