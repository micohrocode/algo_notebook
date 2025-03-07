# leetcode 448
test = [4,3,2,7,8,2,3,1]

def findDisappearedNumbers(nums):
        # get all the unique values currently there
        nums_set = set(nums)

        ret = []

        # loop through expected values
        for i in range(1,len(nums)+1):
            # if the expected value isnt there add it to the
            # missing array to be returned
            if i not in nums_set:
                ret.append(i)

        return ret

findDisappearedNumbers(test)