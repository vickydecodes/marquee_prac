vowels = 'aeiou'

s = "hello world"

c_vowels = 0
c_consonants = 0
stripped_s = s.replace(" ", '')
for char in stripped_s:
    for i in range(len(vowels)):
        if char.lower() == vowels[i]:
            c_vowels += 1
        
print(len(stripped_s) - c_vowels)
print(c_vowels)

