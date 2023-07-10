
import random

class Personagem:
    def __init__(self, nome, pontos_vida, pontos_ataque, habilidade_especial):
        self.nome = nome
        self.pontos_vida = pontos_vida
        self.pontos_ataque = pontos_ataque
        self.habilidade_especial = habilidade_especial

    def atacar(self, outro_personagem):
        if self.sorte():
            dano = random.randint(int(self.pontos_ataque * 0.8), int(self.pontos_ataque * 1.2))
            print("Ataque crítico! " + self.nome + " causou dano aumentado!")
        else:
            dano = random.randint(1, self.pontos_ataque)

        outro_personagem.receber_dano(dano)

    def usar_habilidade_especial(self, outro_personagem):
        if self.habilidade_especial:
            dano = random.randint(1, int(self.pontos_ataque * 1.5))
            print(self.nome, "usou a habilidade especial!")
            outro_personagem.receber_dano(dano)
        else:
            print(self.nome, "não possui habilidade especial.")

    def curar(self):
        cura = random.randint(1, int(self.pontos_vida * 0.5))
        self.pontos_vida += cura
        print(self.nome, "se curou em", cura, "pontos de vida.")

    def receber_dano(self, dano):
        self.pontos_vida -= dano
        if self.pontos_vida <= 0:
            print(self.nome, "foi derrotado(a).")

    def sorte(self):
        chance_critico = random.randint(1, 100)
        return chance_critico <= 20  # 20% de chance de golpe crítico

    def esta_vivo(self):
        return self.pontos_vida > 0

def jogar_batalha():
    print("Bem-vindo ao Simulador de Batalha de RPG!")

    nome1 = input("Digite o nome do primeiro personagem: ")
    pontos_vida1 = int(input("Digite os pontos de vida do primeiro personagem: "))
    pontos_ataque1 = int(input("Digite os pontos de ataque do primeiro personagem: "))
    habilidade_especial1 = input("O primeiro personagem possui habilidade especial? (s/n): ").lower() == "s"
    personagem1 = Personagem(nome1, pontos_vida1, pontos_ataque1, habilidade_especial1)

    nome2 = input("Digite o nome do segundo personagem: ")
    pontos_vida2 = int(input("Digite os pontos de vida do segundo personagem: "))
    pontos_ataque2 = int(input("Digite os pontos de ataque do segundo personagem: "))
    habilidade_especial2 = input("O segundo personagem possui habilidade especial? (s/n): ").lower() == "s"
    personagem2 = Personagem(nome2, pontos_vida2, pontos_ataque2, habilidade_especial2)

    print("Começou a batalha!")

    while personagem1.esta_vivo() and personagem2.esta_vivo():
        print("Turno de", personagem1.nome)
        print("Escolha a ação:")
        print("1 - Atacar")
        print("2 - Usar habilidade especial")
        print("3 - Curar")

        escolha = int(input("Digite o número da ação desejada: "))

        if escolha == 1:
            personagem1.atacar(personagem2)
        elif escolha == 2:
            personagem1.usar_habilidade_especial(personagem2)
        elif escolha == 3:
            personagem1.curar()
        else:
            print("Ação inválida. Perdeu o turno.")

        if personagem2.esta_vivo():
            print("Turno de", personagem2.nome)
            print("Escolha a ação:")
            print("1 - Atacar")
            print("2 - Usar habilidade especial")
            print("3 - Curar")

            escolha = int(input("Digite o número da ação desejada: "))

            if escolha == 1:
                personagem2.atacar(personagem1)
            elif escolha == 2:
                personagem2.usar_habilidade_especial(personagem1)
            elif escolha == 3:
                personagem2.curar()
            else:
                print("Ação inválida. Perdeu o turno.")

    print("Fim da batalha!")

jogar_batalha()

#O programa começa com uma mensagem de boas-vindas ao simulador de batalha de RPG. 

#O jogador é solicitado a inserir informações para o primeiro personagem, como nome, pontos de vida, pontos de ataque e se possui habilidade especial.

#O jogador é solicitado a inserir informações para o segundo personagem da mesma forma.

#Após as informações dos personagens serem fornecidas, a batalha começa.

#Enquanto ambos os personagens estiverem vivos, o programa continua executando os turnos.

#No turno de cada personagem, o programa exibe o nome do personagem e as opções de ação disponíveis: atacar, usar habilidade especial ou curar.

#O jogador seleciona a ação desejada, inserindo o número correspondente.

#O programa executa a ação escolhida pelo jogador, chamando os métodos apropriados da classe Personagem.

#O programa verifica se o outro personagem ainda está vivo. Se estiver, passa para o próximo turno. Caso contrário, vai para o passo 12.

#O fluxo de execução continua alternando entre os personagens até que um deles seja derrotado.

#Quando a batalha termina, o programa exibe uma mensagem informando o resultado final.

#O programa exibe uma mensagem de encerramento e finaliza.