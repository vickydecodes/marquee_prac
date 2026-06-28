s = "aabbbc"


chars = {}


for char in s:
    chars[char] = chars.get(char, 0) + 1
    
    
print(chars)