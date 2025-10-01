def char_frequency(text):
    freq = {}
    for char in text:
        if char != " ":   # ignore spaces
            freq[char] = freq.get(char, 0) + 1
    return freq

# Main program
user_input = input("Enter string: ")

# Split by comma
parts = user_input.split(",")

for part in parts:
    part = part.strip()  # remove extra spaces
    result = char_frequency(part)
    
    # Print output for this part
    for key, value in result.items():
        print(f"{key}={value}", end=" ")
    print()  # new line for next word
