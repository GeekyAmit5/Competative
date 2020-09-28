def solve(x, y):
    if (x, y) == (8, 8):
        return 0
    if x == 8 or y == 8:
        return 1
    return solve(x+1, y) + solve(x, y+1)

# def fact(x):
#     if x <= 1:
#         return 1
#     return x*fact(x-1)
# ans = fact(16) // fact(8)**2


ans = solve(1, 1)
print(ans)
