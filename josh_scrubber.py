polished_words = []

file = open('banned_words_for_bad_people.txt')
for line in file:
    trimmed = line.rstrip().split(" ")[0]
    trimmed = trimmed.split("\t")[0]
    found = False
    for word in polished_words:
        if trimmed == word:
            found = True
    if not found:
        polished_words.append(trimmed)

for finalword in polished_words:
    print(finalword)