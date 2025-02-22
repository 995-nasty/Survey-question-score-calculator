N = int(input("문항수를 입력하세요: "))
sum = 0

for i in range(N):
    for j in range(1):
        a = int(input("%d번: " %(i+1)))
        sum = sum+a

print("총 점수: %d" %sum)    
    