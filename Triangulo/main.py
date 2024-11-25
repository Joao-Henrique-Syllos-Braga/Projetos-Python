def triangule(lines, char):
    result = ""
    for x in range(1, lines + 1):  
        result += " " * (lines - x) + char * x + "\n"
    return result

# Exemplo de uso

lines = int(input("Digite o numero de linhas: "))
char = input("Digite o caractere: ")
print(triangule(lines, char))
