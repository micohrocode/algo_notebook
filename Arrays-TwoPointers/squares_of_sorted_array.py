# leetcode 977
test = [-4,-1,0,3,10]

def sortedSquares(nums):
        # check if empty
        if not nums:
            return nums
        
        # check if all positive
        if nums[0]>0:
            return [num**2 for num in nums]
        
        # check if all negative
        if(nums[len(nums)-1]<0):
            return [num**2 for num in reversed(nums)]

        m = 0
        # find where the negatives start
        for i, n in enumerate(nums):
            if n>=0:
                m = i
                break

        # get the negatives and positives
        # make negatives positive
        A, B = nums[m:], [-1*n for n in reversed(nums[:m])]

        def merge(A,B):
            a = b = 0
            ret = []

            # merge a and b in order
            while a < len(A) and b < len(B):
                if A[a] < B[b]:
                    ret.append(A[a])
                    a+=1
                else:
                    ret.append(B[b])
                    b+=1
            
            # dump what is left
            if a < len(A):
                ret.extend(A[a:])
            else:
                ret.extend(B[b:])
            
            # square them all
            return [n**2 for n in ret]

        return merge(A,B)

sortedSquares(test)