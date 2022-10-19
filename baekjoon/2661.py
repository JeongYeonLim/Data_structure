def check(num):
    for i in range(1, (num//2) + 1):
        if num[-i:] == num[(-2)*i:-i]:
            return False

    if num == n:
        for i in range(n):
            print(s[i], end = '')
            return 0

    for i in range(1,4):
        s. append(i)
        if check(num+1)==0:
            return 0
        s.pop()
    


n = int(input())
s = []
check(0)
