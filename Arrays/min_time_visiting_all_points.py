# leetcode 1266
test = [[1,1],[3,4],[-1,0]]

def minTimeToVisitAllPoints(points):
        answer = 0
        # get the last point
        x1, y1 = points.pop()
        while points:
            # get the next point from the end
            x2, y2 = points.pop()
            # check the number of moves needed to reach the 
            # nex point
            answer += max(abs(x1-x2), abs(y1-y2))
            # move to the next point
            x1, y1 = x2, y2
        return answer

minTimeToVisitAllPoints(test)