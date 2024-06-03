def numero_par_impar():
    numero_inserido = int(input('Insira um número: '))

    if numero_inserido % 2 == 0:
        print("O número é par")
    else:
        print("O número é impar")

def idade():
    idade = int(input('Digite sua idade: '))

    if idade >= 18:
        print('Você é um adulto')
    elif idade <= 17 and idade >= 13:
        print('Você é um adolescente')
    else:
        print('Você é uma criança')

def login():
    login = input('Digite seu login: ')
    senha = int(input('Digite sua senha: '))

    login_correto = 'login'
    senha_correto = 123456

    if login == login_correto and senha == senha_correto:
        print('Você logou')
    elif login == login_correto and senha != senha_correto:
        print('Sua senha está incorreta')
    else:
        print('Login ou senha incorreto')

def coordenadas():
    x = int(input('Digite a coordenada x: '))
    y = int(input('Digite a coordenada y: '))

    if x > 0 and y > 0:
        print('Você está no primeiro quadrante')
    elif x < 0 and y > 0:
        print('Você está no segundo quadrante')
    elif x < 0 and y < 0:
        print('Você está no terceiro quadrante')
    elif x > 0 and y < 0:
        print('Você está no quarto quadrante')
    else: 
        print('Você está no eixo/origem')

def listas():

    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nomes = ['Gabriel', 'Maria Julia', 'Gabriela']
    anos = [1992, 2024]

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
    for numero in numeros:
        print() #numero

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
    soma_impares = 0
    for i in range(1, 11, 2):
        soma_impares += i
        print() #soma_impares

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
    for c in range(10, 0, -1):
        print () #c

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
    numero_solicitado = int(input('Digite um número para sua tabuada: '))

    for n in range(1, 11):
        resultado = numero_solicitado * n
        print() #f'{numero_solicitado} x {n} = {resultado}'

#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
    soma = 0
    try:
        for numero in numeros:
            soma += numero
        print() #soma
    except Exception as e:
        print() #f'Ocorreu um erro: {e}'

#7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
    media = 0
    try:
        for valor in numeros:
            media += valor
            media_total = media / len(numeros)
            print(media)
    except Exception as e:
        print() #f'Ocorreu um erro: {e}'