arr = [3,7,1,9,4]

largest = 0
second_largest = 0

for i in arr:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print("Largest:", largest)
print("Second Largest:", second_largest)