# x보다 작은 수
import sys

N, X = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))

for i in N:
    if X > i:
        print(i, end=" ")

