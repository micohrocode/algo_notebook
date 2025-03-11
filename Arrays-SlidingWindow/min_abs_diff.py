# leetcode 1200
test = [4,2,1,3]

def minimumAbsDifference(arr):
        # sort the array to get the right order
        arr.sort()

        # get the min difference between any two elements
        min_diff = float('inf')
        for i in range(1,len(arr)):
            min_diff = min(min_diff, arr[i]-arr[i-1])

        # check which pairs match that difference
        result = []
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                result.append([arr[i-1],arr[i]])

        return result 

minimumAbsDifference(test)