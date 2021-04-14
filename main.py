counter = {'a': 0, 'o': 0, 'u': 0, 'i': 0, 'e': 0, 'y': 0}
letters = ['a', 'o', 'u', 'i', 'e', 'y']
text = input()
for letter in text:
    if letter.lower() in letters:
        for key in counter:
            if key == letter:
                counter[key] += 1
print(counter)
