# ID 51324808

with open('input.txt') as reader:
    k = int(reader.readline())
    pole = [[]]

    for i in range(4):
        pole[i] = [str(item) for item in reader.readline().strip('\n')]
        if i < 3:
            pole.append([])


schet = 0
a = 0

for i in range(len(pole)):
    for j in range(len(pole[i])):
        if pole[i][j].isnumeric():
            pole[i][j] = int(pole[i][j])

for t in range(10):
    for i in range(len(pole)):
        if pole[i].count(t) > 0:
            a += pole[i].count(t)
    if 0 < a <= 2 * k:
        schet += 1
    a = 0

print(schet)
