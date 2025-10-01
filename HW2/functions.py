def char_frequency(text):
    freq = {}
    for char in text:
        if char != " ":
            freq[char] = freq.get(char, 0) + 1
    return freq

user_input = input("Enter string: ")

parts = user_input.split(",")

for part in parts:
    part = part.strip() 
    result = char_frequency(part)
    
    for key, value in result.items():
        print(f"{key}={value}", end=" ")
    print() 
