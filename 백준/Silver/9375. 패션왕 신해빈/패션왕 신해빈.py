import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    result = 1
    n = int(input())
    count_list = []
    type_list = []

    for j in range(n):
        name, type = input().split()
        if type in type_list:
            count_list[type_list.index(type)] += 1
        else:
            type_list.append(type)
            count_list.append(1)

    for k in count_list:
        result *= (k + 1)
    print(result - 1)