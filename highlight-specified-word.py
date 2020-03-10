string = "The quick brown fox jumps over the lazy dog"
position = 4 # Highlight the word at position 4 (the fifth word)

spaces = 0
count = 0

for word in string.split():
    if count == position:
        break
    else:
        count += 1
        spaces += len(word) + 1

print(string)
print(" " * spaces, end='')
print("^")