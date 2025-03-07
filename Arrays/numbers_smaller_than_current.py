# leetcode 1365
test = [8,1,2,2,3]

def smallerNumbersThanCurrent(self, nums):
        # sorted numbers
        temp = sorted((nums))

        # hashmap/dict to store where the first is found
        d = {}

        for i, v in enumerate(temp):
            # find the first index of each in the sorted list
            if v not in d:
                d[v]=i

        ret = []

        for i in nums:
            # add how many numbers are smaller than it to the list
            # but in the right original order
            ret.append(d[i])

        return ret      

smallerNumbersThanCurrent(test)  