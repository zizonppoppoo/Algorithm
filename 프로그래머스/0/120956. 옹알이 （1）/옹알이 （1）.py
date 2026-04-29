def solution(babbling):
    answer = 0
    for word in babbling:
        idx = 0
        check = True

        while idx < len(word):
            if idx + 2 < len(word):
                if word[idx:idx+3] == "aya" or word[idx:idx+3] == "woo":
                    idx += 3

                elif word[idx:idx+2] == "ye" or word[idx:idx+2] == "ma":
                    idx += 2
                
                else:
                    check = False
                    break

            elif idx + 1 < len(word):
                if word[idx:idx+2] == "ye" or word[idx:idx+2] == "ma":
                    idx += 2

                else:
                    check = False
                    break
            
            else:
                check = False
                break
        
        if check: answer += 1
    
    return answer