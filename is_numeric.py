s = '123456'
numeric = True

for char in s:
    if not char.isnumeric():
        numeric = False
        break
    
print(numeric)