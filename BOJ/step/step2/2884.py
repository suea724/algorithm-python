# 알람 시계
H, M = map(int,input().split())

if M >= 45:
    print(H, M-45, sep=' ')
elif H == 0 and M < 45:
    print(23, M+15, sep=' ')
elif M < 45 :
    print(H-1, M+15, sep=' ')
