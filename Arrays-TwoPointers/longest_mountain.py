# leetcode 845
test = [2,1,4,7,3,2,5]

def longestMountain(self, arr):
        # max mountain size
        ret = 0

        for i in range(1,len(arr)-1):
            
            # check for min size mountain
            if arr[i-1] < arr[i] > arr[i+1]:

                l=r=i

                # keep moving left while mountain
                # is possible
                while l>0 and arr[l] > arr[l-1]:
                    l-=1
                
                # keep moving right while mountain
                # is possible
                while r+1<len(arr) and arr[r] > arr[r+1]:
                    r+=1
                
                # check for new max mountain
                ret = max(ret, r-l+1)

        return ret

longestMountain(test)