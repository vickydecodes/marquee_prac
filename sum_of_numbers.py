n = 9875

st = str(n)
sum = 0
sum2 = 0

for num in st:
    sum += int(num)
    
while n > 0:
    sum2 += n % 10
    n = n // 10
    
print(sum)
print(sum2)