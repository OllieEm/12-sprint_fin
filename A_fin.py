# ID 51324729

with open('input.txt') as reader:
    a = int(reader.readline())
    spisok_A = [int(item) for item in reader.readline().split(' ')]


spisok_B = [0 for i in range(a)]

bliz1 = spisok_A.index(0)
for b1 in range(bliz1, a):
    if spisok_A[b1] != 0:
        spisok_B[b1] = spisok_B[b1 - 1] + 1
    else:
        spisok_B[b1] = 0

bliz2 = a - 1 - spisok_A[::-1].index(0)
for b2 in range(bliz2, bliz1, -1):
    if spisok_A[b2] != 0:
        spisok_B[b2] = min(spisok_B[b2], spisok_B[b2 + 1] + 1)
    else:
        spisok_B[b2] = 0

for b3 in range(bliz1, -1, -1):
    if spisok_A[b3] != 0:
        spisok_B[b3] = spisok_B[b3 + 1] + 1

print(' '.join(map(str, spisok_B)))
