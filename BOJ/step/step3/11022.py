#A+B-8
import sys

T = int(input())
for i in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print("Case #{}: {} + {} = {}".format(i+1, A, B, (A+B)))

