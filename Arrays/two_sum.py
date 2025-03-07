# leetcode 1
test = [2,7,11,15]
test_target = 9

def twoSum(nums, target):
        # hashmap/dictionary to keep track of past items
        hold = {}

        for i, v in enumerate(nums):
            # check if the difference has already been found
            if target - v in hold:
                return i, hold[target-v]
            else:
                # add the item to the hashmap
                hold[v] = i

twoSum(test,test_target)