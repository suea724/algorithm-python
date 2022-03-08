# A+B-7
import sys

T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    str = "Case #%d:" % (i+1)
    print(str, A+B)
