


def generator(file_path):
    with open('1.txt', 'r') as file:
        for line in file:
            yield line.strip()

for i in generator('f.txt'):
    print(i)
print("-"*50)

with open('1.txt', 'r') as file:
    for line in file:
        print(line.strip())
def generator(a):
    b1 = -2
    q = -5
    for i in range(a):
        b1 *= q
        yield b1
        #b1*=q

a=generator(6)
for i in a:
    print(i)
