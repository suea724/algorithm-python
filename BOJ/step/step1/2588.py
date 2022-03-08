#곱셈
num1 = int(input())
num2 = list(map(int,input()))

res1 = num1*num2[2]
res2 = num1*num2[1]
res3 = num1*num2[0]

print(res1, res2, res3, sep="\n")
print(res1 + res2*10 + res3*10**2)
