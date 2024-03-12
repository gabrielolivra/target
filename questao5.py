texto = input()
resultado = ''
for i in range(len(texto) - 1, -1, -1):
    resultado += texto[i]
print(resultado)
