lista_pessoas = []


class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        
def adicionar_pessoa():
    nome_pessoa = input("Nome: ")
    idade_pessoa = int(input("Idade: "))
    altura_pessoa = int(input("Altura (cm):"))
    pessoa = Pessoa(nome_pessoa, idade_pessoa, altura_pessoa)
    lista_pessoas.append(pessoa)
    print("Pessoa adicionada com sucesso!")
    
def visualizar_pessoa():
    nome_busca = input("\nDigite o nome da pessoa que deseja visualizar: ")
    for pessoa in lista_pessoas:
        if pessoa.nome == nome_busca:
            print("Detalhes da pessoa:")
            print("Nome:", pessoa.nome)
            print("Idade:", pessoa.idade)
            print("Altura:", pessoa.altura)
            return
    print("Pessoa não encontrada! Letras maiúsculas e minúsculas importam.")
    
def editar_pessoa():
    nome_busca = input("\nDigite o nome da pessoa que deseja editar:\n ")
    for pessoa in lista_pessoas:
        if pessoa.nome == nome_busca:
            atributo_selecionado = int(input("\nDigite o que deseja editar:\n1-Nome\n2-Idade\n3-Altura\n4-Todos\n"))
            
            if atributo_selecionado == 1:
                novo_nome = input("Nome atualizado: ")
                pessoa.nome = novo_nome
                print("Pessoa atualizada com sucesso!")
            
            if atributo_selecionado == 2:
                nova_idade = input("idade atualizada: ")
                pessoa.idade = nova_idade
                print("Pessoa atualizada com sucesso!")
            
            if atributo_selecionado == 3:
                nova_altura = input("altura atualizada: ")
                pessoa.altura = nova_altura
                print("Pessoa atualizada com sucesso!")
            
            if atributo_selecionado == 4:
                novo_nome = input("Nome atualizado: ")
                nova_idade = input("idade atualizada: ")
                nova_altura = input("altura atualizada: ")             
                pessoa.nome = novo_nome
                pessoa.altura = nova_altura
                pessoa.idade = nova_idade
                print("Pessoa atualizada com sucesso!")
        print("Pessoa não encontrada")
        
    
while True:
    menu = int(input("\nBem-vindo ao nosso banco de dados! O que deseja fazer?\n1-Adicionar pessoa\n2-Buscar por pessoa\n3-Editar dados de alguma pessoa\n4-Sair:\n "))
    if menu == 1:
        adicionar_pessoa()
    elif menu == 2:
        visualizar_pessoa()
    elif menu == 3:
        editar_pessoa()
    elif menu == 4:
        print("KAJSKAJJSKA MEU CODIGO FUNCIONA HAHAHAHAHHA")
        break