s = "I am good"

arr1 = s.split(' ')

arr2 = []

for i in range(len(arr1) - 1, -1, -1):
    arr2.append(arr1[i])
    
    
print(arr2)