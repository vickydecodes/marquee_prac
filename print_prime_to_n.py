n = 18

def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(1, n + 1):
    if check_prime(i):
        print(i, end=' ')
        
