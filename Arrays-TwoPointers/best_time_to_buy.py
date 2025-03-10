# leetcode 121
test = [7,1,5,3,6,4]

def maxProfit(prices):
        # two pointers
        left = 0
        right = 1
        maxProfit = 0

        while(right<len(prices)):
            if prices[left] < prices [right]:
                # check current profit at this stage
                currentProfit = prices[right] - prices[left]
                # set new max
                maxProfit = max(currentProfit, maxProfit)
            else:
                # move to the next number
                left = right

            # move the right pointer
            right += 1

        return maxProfit

maxProfit(test)