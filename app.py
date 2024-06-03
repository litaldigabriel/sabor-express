import os

#Dicionário
restaurantes = [{'nome':'Yoki', 'categoria':'Comida Japonesa', 'ativo':False},
                {'nome':'Comidaria', 'categoria':'Hamburgueria', 'ativo':True},
                {'nome':'Don Raffaelo', 'categoria':'Pizzaria', 'ativo':False}]

def exibir_nome_programa():
    '''Função para exibir o nome do programa em forma de logo'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_menu_opcoes():
    '''Função do menu principal'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Função que finaliza o app'''
    exibir_subtitulo('Finalizando o app')

def opcao_invalida():
    '''Função para informar uma opção inválida'''
    print('Opção inválida!\n')
    voltar_menu_principal()

def cadastrar_novo_restaurante():
    '''
    Função para cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante à lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante para cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_menu_principal()

def listar_restaurante():
    '''Função para listar os restaurantes cadastrados'''
    exibir_subtitulo('Lista de restaurantes cadastrados')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_menu_principal()

def exibir_subtitulo(texto):
    '''Função para mostrar subtitulo de cada item do menu'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_menu_principal():
    '''Função para voltar ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def alternar_estado_restaurante():
    '''Função que altera o estado do restaurante selecionado'''
    exibir_subtitulo('Alterar estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante para alterar seu estado: ')
    restaurantes_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurantes_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)   
    if not restaurantes_encontrado:
        print('Restaurante não encontrado')
    voltar_menu_principal()

def escolher_opcao():
    '''Função que escolhe o opção no menu e chama a próxima função'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()    
    except:
        opcao_invalida()     

def main():
    '''Função main'''
    os.system('cls')
    exibir_nome_programa()
    exibir_menu_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()