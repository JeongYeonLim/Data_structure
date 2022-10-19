import sys
input = sys.stdin.readline

t = int(input()) #테스트케이스 수

for i in range(0,t): #t번 
    cnt = 1
    people =[]

    n=int(input()) #사람 수 
    for i in range(n): #n번 
        p, i = map(int, input().split()) #p는 서류, i는 면접 
        people.append([p, i]) #people[]에 p, i값 추가

    people.sort() #p기준 오름차순 정렬
    max = people[0][1] #최대를 첫번째로 설정해놓음 

    for i in range(1,n): #index
        if max > people[i][1]: 
            cnt+=1 #서류는 오름차순, 면접 점수는 i-1값이 크니까 +1 
            max = people[i][1] #i+1값과 비교하기 위해 max값 현재값으로 바꿔줌


    print(cnt)

