arr = [1, 2, 4, 5]

n = 5

expected_sum = 0 
actual_sum = 0

for i in range(n + 1):
    expected_sum += i

for i in arr:
    actual_sum += i

missing = expected_sum - actual_sum

print("Missing number:", missing)