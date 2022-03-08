# 오븐 시계
A, B = map(int, input().split())
C = int(input())

time = 60 * A + B + C
if time//60 >= 24:
    print(time//60-24, time%60,sep=' ')
else:
    print(time//60, time%60,sep=' ')