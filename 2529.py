n = int(input())
sign = input().split()
visited = [False]*10
max_ans = ""
min_ans = ""


def check(i,j,k): 
    if k=="<":
        return i<j
    elif k==">":
        return i>j
    return True


def solve(idx,s):
    global max_ans, min_ans

    if idx>n:
        if len(min_ans)==0:
            min_ans = s
        else:
            max_ans = s
        return
    
    for i in range(10):
        if visited[i] == False:
            if(idx==0 or check(s[-1],str(i),sign[idx-1])):
               visited[i] = True
               solve(idx+1, s+str(i))
               visited[i] = False
    

solve(0, "")
print(max_ans)
print(min_ans)
