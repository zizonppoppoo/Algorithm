# 문제 : https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-beautiful-number/description
# 아이디어 : 수가 몇번 반복했는지를 함수의 state로 넣어서 current_num과 같아지면 초기화 하는 방식으로 진행

n = int(input())
count = 0
def beautiful(state, current_num, current_len):
    global count
    if state == current_num: state = 0

    if current_len == n: # 구하는 수가 N자리가 되었을 때 판정
        if state == 0:
            count += 1
            return
        else: return

    if state == 0:
        beautiful(0, 1, current_len + 1)
        for i in range(2,5):
            beautiful(1, i, current_len + 1)

    else: beautiful(state + 1, current_num, current_len + 1)

beautiful(0, 0, 0)
print(count)