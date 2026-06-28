s = "swiss"

chars = {}


for char in s:
    chars[char] = chars.get(char, 0) + 1
    
    
for char in s:
    if chars[char] == 1:
        print(char)
        break