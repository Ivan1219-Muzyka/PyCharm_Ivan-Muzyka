text = input("Enter a word (lowercase Latin letters): ")
shift = 3

result = ""
for ch in text:
    # cyclic shift: z -> c
    new_code = (ord(ch) - ord('a') + shift) % 26 + ord('a')
    result += chr(new_code)

print(f'Encrypted text: "{result}"')
