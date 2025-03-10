# leetcode 200
test = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

def numIslands(grid):
        # if no grid there are no islands
        if not grid:
            return 0

        def bfs(r,c):

            q = deque()
            # mark the 1 as visited
            visit.add((r,c))
            # add it to the queue
            q.append((r,c))

            while q:
                # remove the oldest item
                row, col = q.popleft()
                # directions to check for a one
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    # get item to check
                    r,c = row+dr, col+dc

                    # if its a one that has not been visited
                    # add it to the queue and mark it as visited
                    if (r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))

        # number to return
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        for r in range(rows):
            for c in range(cols):
                # find a one that hasnt been visited yet
                if grid[r][c] == '1' and (r,c) not in visit:
                    # search for all connecting ones
                    bfs(r,c)
                    # increment the answer
                    count+=1

        return count

numIslands(test)