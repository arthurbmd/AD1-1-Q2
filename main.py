while True: # Tratamento de erro para números abaixo de 1
    qtd = int(input('Digite a quantidade de números: '))
    if qtd >=0:
        break
    else:
        print('Digite um número inteiro maior que 0')

for i in range(qtd):
    numero = int(input('Digite o número: '))

    if i == 0: # Teste para o primeiro número digitado
        menor = numero
        maior = numero
        soma = 0

    soma += numero
    
    # Teste dos maiores e menores números digitados
    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

# Tratamento da saída 
media = soma / qtd
print(f'Soma: {soma}')
print(f'Média: {media:.2f}')
print(f'Menor: {menor}')
print(f'Maior: {maior}')