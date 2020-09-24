# incomplete
# total no. of palindrome substrings
def isPalindrome(s):
    n = len(s)
    for i in range(n):
        if s[i] != s[n-1-i]:
            return False
    return True


def isvalid(i):
    a = len(ans)
    if a <= l//2+1:
        return True
    if l % 2:
        pass
    else:
        pass


def solve():
    global l, ans, total
    if len(ans) == l:
        total += 1
    else:
        for i in s:
            if isvalid(i):
                ans.append(i)
                solve()
                ans.pop()


s = input()
total = len(set(s))
for i in range(2, len(s)+1):
    ans = []
    l = i
print(total)
