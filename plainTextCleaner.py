import re

file = open('test.txt', 'r')
bannedFile = open('joshs_thot_police.txt')

lines = []

banned = []

for line in bannedFile:
    banned.append(line)

#replace all special chars with spaces
for line in file:
    line = re.sub('[^A-Za-z0-9@]', ' ', line)
    lines.append(line)

words = []
for l in lines:
    wordList = l.split(' ')
    for ws in wordList:
        if ws != "" and not '@' in ws:
            found = False
            for b in banned:
                if ws.lower().rstrip() == b.lower().rstrip():
                    found = True
            if not found:
                words.append(ws.lower())

output = open('mapme.txt', 'w')

for w in words:
    output.write(w)
    output.write('\n')

output.close()