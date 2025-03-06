test = [1,2,3,1]

def containsDuplicate(nums):
    # create a set to quickly check number of unique entries
    if len(set(nums)) == len(nums):
        return False
    else:
        return True
    
containsDuplicate(test)