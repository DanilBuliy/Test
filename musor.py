m = {1,True,1.0}

print(len(m))


my_tuple = (range(11))
print(tuple(my_tuple))

string1 = " "
def convert(n):
    #res = [i for i in range(n+1)]efef,
    return "".join(map(str,range(n+1)))

print(convert(10))

def merge(l1=[],l2=[]):
    d = {i:y for i in l1 for y in l2}
    return dict(sorted(d.items()))

print(merge([1,2,3,0],["efef","fgrg"]))

import random

n = [random.randint(1, 5) for _ in range(5)]
m = [random.randint(1, 5) for _ in range(5)]

for i in n:
    for y in m:
        print(y, end=" ")
    print(i)

first_element = n[0]
print("First element of the matrix:", first_element)

