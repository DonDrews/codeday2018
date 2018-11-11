import re

file = open('test.txt', 'r')
bannedFile = open('joshs_thot_police.txt')

lines = []

banned = []

for line in bannedFile:
    banned.append(line)

#replace all special chars with spaces
for line in file:
    line = re.sub('[^A-Za-z0-9]', ' ', line)
    lines.append(line)

words = []
for l in lines:
    ws = l.split(' ')
    if ws != "":
        found = False
        for b in banned:
            if ws == b:
                found = True
        if not found:
            words.append(ws)

for w in words:
    print(w)
