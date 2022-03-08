# 평균
N = int(input())
s_list = list(map(int, input().split()))
sum = 0

for i in s_list:
    sum += i/max(s_list)*100

print(sum/len(s_list))