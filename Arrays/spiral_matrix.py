# leetcode 54
test = [[1,2,3],[4,5,6],[7,8,9]]

def spiralOrder(matrix):
        ret = []
        while matrix:
            #  take in the first row
            ret+=(matrix.pop(0))

            # append the last element of each remaining row
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())

            # take in the remainder of the last row
            # in reverse
            if matrix:
                ret+=(matrix.pop()[::-1])
            
            # take first element of remaining rows
            # in reverse
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))

        return ret

spiralOrder(test)