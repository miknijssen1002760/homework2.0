def chat_to_int(a):
    x = ord(a)
    if x>96:
        return x-96
    else:
        return x-64+26

paklijst = open("C:/Users/mikni/source/repos/homework2.0/advent_of_code_2022/dec-3-input.txt")
# paklijst = open("C:/Users/mikni/source/repos/homework2.0/advent_of_code_2022/dec-3-input-test.txt")

""" part 1 """

# fouten = []
# prioretys = []
# output = 0

# for backpack in paklijst:
#     vak_1 = set()
#     vak_2 = set()
#     x = 0
#     for i in backpack[:-1]:
#         if x<(len(backpack)//2):
#             vak_1.add(i)
#         else:
#             vak_2.add(i)
#         x+=1
#     print(vak_1, vak_2)
#     tmp = vak_1.intersection(vak_2)
#     fouten.append(tmp.pop())
#     print(fouten)

# for char in fouten:
#     prioretys.append(chat_to_int(char))


# print(prioretys)

# for i in prioretys:
#     output += i

# print(output)

""" part 2 """
output = 0
bages = []
prioretys = []
x = 0
bag_1 = set()
bag_2 = set()
bag_3 = set()

for backpack in paklijst:
    x+=1
    if x == 1:
        for i in backpack[:-1]:
           bag_1.add(i) 
    elif x == 2:
        for i in backpack[:-1]:
            bag_2.add(i)
    elif x == 3:
        for i in backpack[:-1]:
            bag_3.add(i)
        x=0
        tmp = bag_1.intersection(bag_2)
        tmp = tmp.intersection(bag_3)
        bages.append(tmp.pop())
        bag_1 = set()
        bag_2 = set()
        bag_3 = set()



for char in bages:
    prioretys.append(chat_to_int(char))


for i in prioretys:
    output += i

print(output)