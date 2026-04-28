import sys

# read shift key
shift = int(sys.argv[1])

text = sys.stdin.read().upper()

result = ""

for ch in text:
    if 'A' <= ch <= 'Z':
        new_char = chr(((ord(ch) - ord('A') + shift) % 26) + ord('A'))
        result += new_char

# print in blocks of 5 letters, 10 blocks per line
count = 0
for i in range(0, len(result), 5):
    print(result[i:i+5], end=" ")
    count += 1
    if count == 10:
        print()
        count = 0
