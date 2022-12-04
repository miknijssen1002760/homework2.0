def kiesbonus(x):
    if x == 'X':
        return 1
    if x == 'Y':
        return 2
    if x == 'Z':
        return 3

def win_or_not(a, b):
    if a=='A' and b=="X":
        return 3
    if a=='A' and b=="Y":
        return 6
    if a=='A' and b=="Z":
        return 0
    if a=='B' and b=="X":
        return 0
    if a=='B' and b=="Y":
        return 3
    if a=='B' and b=="Z":
        return 6
    if a=='C' and b=="X":
        return 6
    if a=='C' and b=="Y":
        return 0
    if a=='C' and b=="Z":
        return 3

def what_to_pick(a, b):
    if a=='A' and b=="X":
        return 'Z'
    if a=='A' and b=="Y":
        return 'X'
    if a=='A' and b=="Z":
        return 'Y'
    if a=='B' and b=="X":
        return 'X'
    if a=='B' and b=="Y":
        return 'Y'
    if a=='B' and b=="Z":
        return 'Z'
    if a=='C' and b=="X":
        return 'Y'
    if a=='C' and b=="Y":
        return 'Z'
    if a=='C' and b=="Z":
        return 'X'

def winbonus(x):
    if x == 'X':
        return 0
    if x == 'Y':
        return 3
    if x == 'Z':
        return 6
# part 1
spiekbrief = open("C:/Users/mikni/source/repos/homework2.0/advent_of_code/dec-2-input.txt")
# spiekbrief = open("C:/Users/mikni/source/repos/homework2.0/advent_of_code/dec-2-input-test.txt")
# output = 0

# for antwoord in spiekbrief:
#     output += kiesbonus(antwoord[2])
#     output += win_or_not(antwoord[0], antwoord[2])

# print(output)

# part 2
output = 0

for antwoord in spiekbrief:
    output += kiesbonus(what_to_pick(antwoord[0], antwoord[2]))
    output += winbonus(antwoord[2])

print(output)