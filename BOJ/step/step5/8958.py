# OX 퀴즈
N = int(input())
o_list = []

for i in range(N):
    # score 출력하고 다음 반복 시 초기화해서 값 누적 방지
    score = 0
    res = list(map(str, input()))

    for j in res:
        # 'O'가 들어올 경우 o_list에 append
        if j == 'O':
            o_list.append(j)
            score += len(o_list)

        # 'X'가 들어올 경우 o_list 비움
        elif j == 'X':
            o_list.clear()

    print(score)
    # 데이터 누적 방지를 위해 o_list clear
    o_list.clear()

