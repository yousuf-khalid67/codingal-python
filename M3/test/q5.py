words = ["apple", "banana", "orange", "kiwi", "egg", "ice"]
vowels = "aeiouAEIOU"

result = [word.upper() for word in words if word[0] in vowels]

# Test
print(result) # ['APPLE', 'ORANGE', 'EGG', 'ICE']