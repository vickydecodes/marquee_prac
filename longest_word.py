s = 'I love competetive programming'

arr = s.split(' ')

longest = 0
word_length = 0

idx = 0

for i in range(len(arr)):
    for char in arr[i]:
        word_length += 1
        
    if word_length > longest:
        longest = word_length
        idx = i
    
    word_length = 0
        
        
print(arr[idx])
        
