word = input()
first = next(i for i, c in enumerate(word) if c.isupper())
second = next(i for i, c in enumerate(word) if c.isdigit())
second += 1
step = second - first
result = []
while True:
    result.append(word[first])
    if word[first] == '.':
        break
    first += step
print(''.join(result))
