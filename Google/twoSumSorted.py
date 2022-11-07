### if the input is sorted, we use two pointers (one beggining, one end), if the sum bigger than target==> end ptr-1 if sum<target ==> beg. ptr+1
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        ### The numbers are sorted ascendingy, so use two pointers
        i = 0
        j = len(numbers)-1

        while(1):
            s = numbers[i] + numbers[j]

            if s > target:
                j = j - 1
            if s < target:
                i = i + 1    
            if s == target :
                return [i+1,j+1]    
