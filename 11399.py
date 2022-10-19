n=int(input()) #ATM앞 사람의 수 입력
array=list(map(int,input().split())) #사람당 걸리는 시간 입력
array.sort() #sort를 이용해 오름차순 정리

result = 0

#array[i]에 array[i]까지 걸리는 총 시간 대입
for i in range(1,n):
    array[i] += array[i-1]

result = sum(array) #사람당 걸리는 시간의 합

print(result)