array = [1, 2, 2, 3, 4, 4, 5]
unique_array = []

for item in array:
    if item not in unique_array:
        unique_array.append(item)

print(unique_array)
