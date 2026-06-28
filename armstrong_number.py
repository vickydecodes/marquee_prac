import math
n = 153

st = str(n)

length = len(st)

sum = 0

for num in st:
    sum += math.pow(int(num), length)
    
if sum == n:
    print('armstrong')
else: 
    print('not armstrong')
    
    
### raj karan approach

num = int(input("Enter a number: "))

temp = num
digits=len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** digits
    temp = temp // 10

if sum == num:
    print("Armstrong")
else:
    print("Not Armstrong")
