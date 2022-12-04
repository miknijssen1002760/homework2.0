def maakSet(x, y):
    output = set()
    x=int(x)
    y=int(y)
    while y>=x:
        output.add(x)
        x+=1
    return output

def subset(x, y):
    if x.issubset(y):
        return True
    if y.issubset(x):
        return True
    return False

def overlap(x, y):
    if x.intersection(y)!=set():
        return True
    return False
assignment = open("C:/Users/mikni/source/repos/homework2.0/advent_of_code_2022/dec-4-input.txt")
# assignment = open("C:/Users/mikni/source/repos/homework2.0/advent_of_code_2022/dec-4-input-test.txt")
### part 1 ###
# output = 0

# for id in assignment:
#     elf_1 = id.split(",")[0]
#     elf_2 = id.split(",")[1]
#     vakken_elf_1 = maakSet(elf_1.split("-")[0], elf_1.split("-")[1])
#     vakken_elf_2 = maakSet(elf_2.split("-")[0], elf_2.split("-")[1])
#     if subset(vakken_elf_1, vakken_elf_2):
#         output+=1
# print(output)
### part 2 ###
output = 0

for id in assignment:
    elf_1 = id.split(",")[0]
    elf_2 = id.split(",")[1]
    vakken_elf_1 = maakSet(elf_1.split("-")[0], elf_1.split("-")[1])
    vakken_elf_2 = maakSet(elf_2.split("-")[0], elf_2.split("-")[1])
    if overlap(vakken_elf_1, vakken_elf_2):
        output+=1
print(output)