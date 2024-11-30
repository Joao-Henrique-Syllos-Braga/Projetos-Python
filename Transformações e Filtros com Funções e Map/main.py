
numbers = [12, 15, 24, 35, 40, 53, 60, 72, 81, 90]

def dividir3(x):
    return x / 3
dividido = list(map(dividir3, numbers))

def filtrar(x):
    return x % 3 == 0
fitrado = list(filter(filtrar, dividido))

def dubtrair(x):
    return x - 5
subtraido = list(map(dubtrair, fitrado))

print(subtraido)