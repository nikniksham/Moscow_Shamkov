coords = []
for elem in input().split(', '):
    a, b = elem.split(';')[0][1:], elem.split(';')[1][:-1]
    if ',' in a:
        a = a[:a.find(',')]
    if ',' in b:
        b = b[:b.find(',')]
    coords.append([int(a), int(b)])