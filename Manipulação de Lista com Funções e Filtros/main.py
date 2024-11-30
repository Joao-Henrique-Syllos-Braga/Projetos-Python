numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mais10 (x):
    return x+10

def maior15(x):
    return x > 15
        
def dobrar(x):
    return x*2

soma = list(map(mais10, numbers))
print(soma)
maior = list(filter(maior15, soma))
print(maior)
dobrar = list(map(dobrar, maior))
print(dobrar)

print(dobrar)