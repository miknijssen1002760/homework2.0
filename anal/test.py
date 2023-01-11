from itertools import permutations
import random
import math

def sim(num_of_experiments = 1_000_000):
    input = 'ANALYSIS'
    output = 0
    result = []
    for _ in range(num_of_experiments):
        l = list(input)
        random.shuffle(l)
        result.append(''.join(l))
    for i in result:
        if len(i.split('SIS'))>1:
            output +=1
    print(output)
    output /= len(result)
    return output

def theory():
    output = (math.factorial(6)/2)/(math.factorial(7)*2)
    return output

def itertools():
    count = 0
    Perms = list(permutations(["a","n","a","l","y","s","i","s"]))
    for i in range(len(Perms)):
            word = "".join(Perms[i])
            if "sis" in word:
                count += 1
    return count/len(Perms)

# print(sim())
# print(itertools())
# print(theory())
