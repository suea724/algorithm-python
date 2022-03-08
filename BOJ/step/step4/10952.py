# A+B-5
import sys
A, B = 1, 1

while (A and B) != 0:
    A, B = map(int, sys.stdin.readline().rstrip().split())
    if A == 0 and B == 0:
        break
    print(A + B)

