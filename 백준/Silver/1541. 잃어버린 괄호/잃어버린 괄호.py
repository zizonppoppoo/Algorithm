import re
s = input()
tokens = re.split(r'([-+])', s)

check = False
result = int(tokens[0])

for i in range(1,len(tokens),2):
    if check == True:
        result -= int(tokens[i+1])
    else:
        if tokens[i] == '+':
            result += int(tokens[i+1])
        elif tokens[i] == '-':
            check = True
            result -= int(tokens[i+1])

print(result)