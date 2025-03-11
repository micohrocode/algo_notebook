# leetcoce 219
test = [1,2,3,1]

def containsNearbyDuplicate(nums, k):
        # the sliding window
        seen = set()

        for i,num in enumerate(nums):
            # check for duplicate
            if num in seen:
                return True
            
            seen.add(num)

            # move window over
            if len(seen) > k:
                seen.remove(nums[i-k])
        return False

containsNearbyDuplicate(test,3)