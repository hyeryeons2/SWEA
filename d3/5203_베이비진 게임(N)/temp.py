# tc 8개 맞는 코드..

import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())

for t in range(1, TC + 1):
    card = list(map(int, input().split()))

    ## p1
    p1 = card[::2]
    p11 = []
    for i in range(6):
        p11.append((p1[i], i))  # 카드번호, idx(뽑는순서)
    p111 = sorted(p11)

    d1 = []
    # run 판별
    for _ in range(4):
        if 2 * p111[_ + 1][0] == p111[_][0] + p111[_ + 2][0]:
            d1.append(max(p111[_ + 2][1], p111[_ + 1][1], p111[_][1]))
            break

    # triple 판별
    for _ in range(6):
        if p111.count(p111[_][0]) >= 3:
            temp = []
            temp.append(_)
            d1.append(sorted(temp)[2])
            break
    if not d1:
        d1 += [0]

    ## p2
    p2 = card[1::2]
    p22 = []
    for i in range(6):
        p22.append((p2[i], i))
    p222 = sorted(p22)

    d2 = []
    # run 판별
    for _ in range(4):
        if 2 * p222[_ + 1][0] == p222[_][0] + p222[_ + 2][0]:
            d2.append(max(p222[_ + 2][1], p222[_ + 1][1], p222[_][1]))
            break

    # triple 판별
    for _ in range(6):
        if p222.count(p222[_][0]) >= 3:
            temp = []
            temp.append(_)
            d2.append(sorted(temp)[2])
            break
    if not d2:
        d2 += [0]

    if 0 in d1 and 0 in d2:
        print('#{} 0'.format(t))
    elif 0 in d1 and 0 not in d2:
        print('#{} 2'.format(t))
    elif 0 not in d1 and 0 in d2:
        print('#{} 1'.format(t))
    else:
        if min(d1) < min(d2):
            print('#{} 1'.format(t))
        elif min(d1) > min(d2):
            print('#{} 2'.format(t))
        else:
            print('#{} 0'.format(t))