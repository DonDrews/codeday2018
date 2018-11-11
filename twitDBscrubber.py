polished_words = []

file = open('twitDB.csv', 'r')
fp = open('twitDB(-B).txt', 'w')
for line in file:
    trimmed = line.rstrip().split(("b"))[1]
    trimmed = trimmed.split("\t")[0]
    found = False
    for word in polished_words:
        if trimmed == word:
            found = True
    if not found:
        polished_words.append(trimmed)

for finalword in polished_words:
    print(finalword)
    fp.write(str(finalword))
    fp.write("\n")

file.close()
fp.close()
