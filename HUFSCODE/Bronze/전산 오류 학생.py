import sys
input = sys.stdin.readline

N = int(input())

error = []
for _ in range(N):
    date, city = input().split()
    
    year, month, day = map(int, date.split("-"))
    check = False

    if city == "Seoul":
        if year < 1954: check = True
        elif year == 1954 and month < 4: check = True
        elif year == 1954 and month == 4 and day < 20: check = True

    elif city == "Global":
        if year < 1981: check = True
        elif year == 1981 and month < 8: check = True
        elif year == 1981 and month == 8 and day < 25: check = True

    if check: error.append((date, city))

error.sort(key=lambda x: x[1], reverse=True)
error.sort(key=lambda x: x[0])
print(len(error))

for i in range(len(error)):
    print(error[i][0], error[i][1])