import random
list1=[0,0,0,0,0,0]
for i in range(6):
    x = random.randint(0,49)
    list1[i]=x
print('Lucky Lotto Number')
for i in range(6):
    print(list1[i])
print('Good Lucky')