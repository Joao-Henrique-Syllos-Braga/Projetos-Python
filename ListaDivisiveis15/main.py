numbers = [5, 10, 15, 20, 25, 30]
menor_nao_divisivel_por_5 = [x for x in numbers if x < 20 and x % 5 != 0]
print(menor_nao_divisivel_por_5)
