def anyDuplicates(x, y):
    check = set()
    for i in range(1,y+1):
        check.add(input[x-i])
    return len(check)==y

input = open("C:/Users/mikni/source/repos/homework2.0/advent_of_code_2022/dec-6-input.txt")
# input = open("C:/Users/mikni/source/repos/homework2.0/advent_of_code_2022/dec-6-input-test.txt")

input = input.read()
lengthStartOfPacketMarker = 4
char = lengthStartOfPacketMarker
while not(anyDuplicates(char, lengthStartOfPacketMarker)):
    char+=1

print(char)