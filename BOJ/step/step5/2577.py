# 숫자의 개수
A = int(input())
B = int(input())
C = int(input())

dig_list = list(map(int, str(A*B*C)))
for i in range(0, 10):
    print(dig_list.count(i))

