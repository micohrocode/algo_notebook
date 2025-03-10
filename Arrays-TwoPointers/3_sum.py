# leetcode 15
test = [-1,0,1,2,-1,-4]

def threeSum(nums):
        # set of all combinations
        triplets = set()

        # sort the list
        nums.sort()

        for i, v in enumerate(nums):

            # check if value is a duplicate
            if (i>0) and (v == nums[i-1]):
                continue
            
            # your two pointers
            left = i + 1
            right = len(nums)-1

            while left<right:
                # check current value
                curr = v + nums[left] + nums[right]

                
                if curr > 0:
                    # if less than target you need a bigger number
                    right-=1
                elif curr < 0:
                    # if greater than target you need a smaller number
                    left+=1
                else:
                    # if equal to target, add and move to check more combos
                    triplets.add((v,nums[left],nums[right]))
                    left+=1
                    right-=1
        
        output = list(triplets)
        return output

threeSum(test)