# Write a function that takes a positive integer n, sums all the cubed values from 1 to n, and returns that sum.

# Assume that the input n will always be a positive integer.

# Examples: (Input --> output)

# 2 --> 9 (sum of the cubes of 1 and 2 is 1 + 8)
# 3 --> 36 (sum of the cubes of 1, 2, and 3 is 1 + 8 + 27) >> 
#  (1*1*1) + (2*2*2) + (3*3*3) >> (n) + (n - 1)


def sum_cubes(n):
    ans = 0
    while n > 0:
        ans += n*n*n
        n -= 1
    return ans

print(sum_cubes(3))



# def sum_cubes(n):
#     return sum(i**3 for i in range(0,n+1))


