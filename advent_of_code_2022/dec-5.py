def move_crates(x, y, z):
    for i in range(int(x)):
        loading_dock[int(z)-1].append(loading_dock[int(y)-1].pop(-1))

def move_crates2(x,y,z):
    addToZ = []
    for i in range(int(x)):
        addToZ.append(loading_dock[int(y)-1].pop(-1))
    addToZ.reverse()
    loading_dock[int(z)-1] += addToZ


# steps = open("C:/Users/mikni/source/repos/homework2.0/advent_of_code_2022/dec-5-input.txt")
# starting_dock = open("C:/Users/mikni/source/repos/homework2.0/advent_of_code_2022/dec-5-starting-dock.txt")
steps = open("C:/Users/mikni/source/repos/homework2.0/advent_of_code_2022/dec-5-input-test.txt")
starting_dock = open("C:/Users/mikni/source/repos/homework2.0/advent_of_code_2022/dec-5-starting-dock-test.txt")

loading_dock = []
first_dock = starting_dock.readlines()

for i in range(len(first_dock[0])//4):
    loading_dock.append([])

for i in first_dock:
    k=1
    l = 0
    while k<len(i):
        loading_dock[l].append(i[k])
        k+=4
        l+=1

o=0 
for m in loading_dock:
    while m[0] == ' ':
        del m[0]
    m.reverse()
    loading_dock[o] = m
    o+=1

print(loading_dock)

for i in steps:
    move_crates2(i[5:].split(" from ")[0], i[5:].split(" from ")[1].split(" to ")[0], i[5:].split(" from ")[1].split(" to ")[1][0])

print(loading_dock)
for i in loading_dock:
    print(i[-1])