output = []
paklijst = open("C:/Users/mikni/source/repos/homework2.0/advent_of_code/dec-1-input.txt")
# paklijst = open("C:/Users/mikni/source/repos/homework2.0/advent_of_code/dec-1-input-test.txt")
y = 0
for item in paklijst:
    if item[:-1]=="":
        output.append(y)
        y = 0
    else:
        y += int(item[:-1])

print(output)

# part_2
big = 0
bigger = 0
biggest = 0
for elf in output:
    if elf > biggest:
        big = bigger
        bigger = biggest
        biggest = elf
    elif elf > bigger:
        big = bigger
        bigger = elf
    elif elf > big:
        big = elf

print(big, bigger, biggest)
print(big+bigger+biggest)
