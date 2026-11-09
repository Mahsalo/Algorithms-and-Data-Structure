#### every paranthesis or brackety that is opened must be closed in the same order
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: # must have even number of elements
            return False

        open_close = {"(":")", "{":"}", "[":"]"}
        stck = []

        for i in s:
            if i in open_close.values():
                # Check if stack is empty before popping to prevent IndexError
                if not stck:
                    return False
                last = stck.pop()
                if open_close[last] != i:
                    return False
            else:
                stck.append(i)

        # If stack is empty, it's valid (True); otherwise invalid (False)
        return not stck
