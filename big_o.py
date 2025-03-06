# O(n), only looped over once
numbers = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numbers)):
    print(numbers[i])

# O(n^2), n*n
for i in range(len(numbers)):
    for j in range(len(numbers)):
        print(numbers[i]*numbers[j])
    print("---------------------------")

# O(1)
def recur(n):
    if n == 1:
        return
    recur(n-1)

# O(2^(n-1))
def recur2(n):
    if n == 1:
        return
    recur2(n-1)
    recur2(n-1)

# input size, required time complexity
# n ≤ 10 O(n!)
# n ≤ 20 O(2^n)
# n ≤ 500 O(n^3)
# n ≤ 5000 O(n^2)
# n ≤ 106 O(n log n) or O(n)
# n is large O(1) or O(log n)

# Max subarray algo
numbers = [-1,2,4,-3,5,2,-5,2]

# O(n^3), three loops
best = 0
for i in range(len(numbers)):
    for j in range(len(numbers)):
        check = 0
        for k in range(i,j):
            check += numbers[k]
        best = max(best,check)

print("Best: ",best)

# O(n^2)
best2 = 0
for i in range(len(numbers)):
    check = 0
    # remove a loop and calculate it in the second loop
    for j in range(i,len(numbers)):
        check += numbers[j]
        best2 = max(best2,check)

print("Best2: ",best2)

# O(n), linear time, as the number of inputs grow time grows
best3 = 0
check3 = 0

for i in range(len(numbers)):
    check3 = max(numbers[i],check3+numbers[i])
    best3 = max(best,check3)

print("Best3: ",best3)

# Constant, Logarithmic, Linear, Linearithmic, Quadratic, Exponential, Factorial
# Fastest to slowest