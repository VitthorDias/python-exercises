nome = str(input("Digite o seu nome completo: ")).strip()
print('#'*100)
print(f'Maiscula: {nome.upper()}')
print('#'*100)
print(f'Minuscula: {nome.lower()}')
print('#'*100)
print(f'Total de letras sem espaço: {len(nome) - nome.count(" ")}')
print('#'*100)
print(f'Total de letras da primeira palavra: {nome.find(" ")}')
