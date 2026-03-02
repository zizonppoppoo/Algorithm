T = int(input())
triangle = [1,1,1,2,2,3,4,5,7,9,12]

for i in range(T):
    n = int(input())
    if n <= len(triangle):
        print(triangle[n-1])
    else:
        index = len(triangle) - 1
        while len(triangle) < n:
            triangle.append(triangle[index]+triangle[index-4])
            index += 1
        print(triangle[n-1])