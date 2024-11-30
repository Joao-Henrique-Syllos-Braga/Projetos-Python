array = [1, 2, 3, 4, 5]
inverted = []

for x in range(len(array)):
    x+=1
    inverted.append(array[-x])

print(inverted)