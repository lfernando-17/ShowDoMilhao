import sys
import time
import random
import emoji
import time
import ansicon
ansicon.load()
dinheiros = [['R$ 1 mil','R$ 0','R$ 0'] ,['R$ 2 mil','R$ 1 mil','R$ 500'],['R$ 3 mil','R$ 2 mil','R$ 1 mil'],['R$ 4 mil','R$ 3 mil','R$ 1.500'],['R$ 5 mil','R$ 4 mil','R$ 2 mil'],['R$ 10 mil','R$ 5 mil','R$ 2.500'],['R$ 20 mil','R$ 10 mil','R$ 5 mil'],['R$ 30 mil','R$ 20 mil','R$ 10 mil'],['R$ 40 mil','R$ 30 mil','R$ 15 mil'],['R$ 50 mil','R$ 40 mil','R$ 20 mil'],['R$ 100 mil','R$ 50 mil','R$ 25 mil'],['R$ 200 mil','R$ 100 mil','R$ 50 mil'],['R$ 300 mil','R$ 200 mil','R$ 100 mil'],['R$ 400 mil','R$ 300 mil','R$ 150 mil'],['R$ 500 mil','R$ 400 mil','R$ 200 mil'],['R$ 1 milhão','R$ 500 mil','R$ 0']]
#Ordem : Placas , Cartas , Convidados
dicas_gastas=[1,1,1]
class Question(object):
    
    def __init__(self,pergunta,resp,rodada):
        self.rodada = rodada
        self.pergunta = pergunta
        self.resp = resp
        print()
        print('='*int((len(self.pergunta))/2),end=' ')
        print(self.pergunta)
        print('='*int((len(self.pergunta))/2))

    def açao(self):
        print('\n'*2)
        action = input('\nDeseja Responder , Parar ou Dica? ')
        if action.lower() == 'responder':
            self.resposta()
        elif action.lower()=='parar' :
            self.parar()
        elif action.lower()=='dica' :
            self.dica()
        else :
            print('\nTente Novamente')
            self.açao()
    def resposta(self):
        answer = input('\nDigite a resposta : ')
        if answer.lower()==self.resp:
            print(f'\nResposta certa \nVocê está com {dinheiros[self.rodada][0]} reais')
            print('\n'*20)
        else :
            self.errou()  
    def errou (self):
        print(f'\nResposta Errada \nVocê ficou com {dinheiros[self.rodada][2]} reais')
        time.sleep(2)
        sys.exit()
    def parar(self):
        print(f'\nVocê ficou com {dinheiros[self.rodada][1]} reais')
        time.sleep(2)
        sys.exit()
        
    def opçoes(self):
        ansicon.load()
        print(f'\033[1;32m\nAcertar : {dinheiros[self.rodada][0]}')
        print(f'\033[1;31mParar : {dinheiros[self.rodada][1]}')
        print(f'\033[1;31mErrar : {dinheiros[self.rodada][2]}')
        ansicon.unload()        
    def dica(self):
        print('\n'*3)
        print('Escolha entre : ')
        if dicas_gastas[0]!=0 :
             print('\nPlacas')
        if dicas_gastas[1]!=0 :
            print('\nCartas')
        if dicas_gastas[2]!=0 :
            print('\nConvidados\n')
        ajuda = input()
        letras = ['a','b','c','d']
        options = letras
        options.remove(self.resp)
        a = random.randint(0,3)
        b = random.randint(0,3)
        c = random.randint(0,3)
        cartas = ['Rei','Ás','2','3']
        if ajuda.lower() =='placas' and dicas_gastas[0]!=0:
            print(f'{self.resp} {letras[a]} {self.resp} {letras[b]} \n{letras[a]} {self.resp} {letras[b]} {letras[c]}')
            dicas_gastas[0] = 0
            self.açao()
        elif ajuda.lower()=='cartas' and dicas_gastas[1]!=0:
            print()
            print(emoji.emojize(':diamonds:',use_aliases=True),end=' ')
            print(emoji.emojize(':diamonds:',use_aliases=True),end=' ')
            print(emoji.emojize(':diamonds:',use_aliases=True),end=' ')
            print(emoji.emojize(':diamonds:',use_aliases=True))
            num = int(input('\nEscolha entre 1 a 4 : '))
            if num > 4 or num < 1 :
                print('Tente Novamente')
                self.dica()
            random.shuffle(cartas)
            if cartas[num-1] == '2' :
                print(f'\nVocê recebeu a carta :  {cartas[num-1]}')
                for letra in range(0,2) :
                    print(f'Não é : {options[letra]}')
            elif cartas[num-1] == '3' :
                print(f'\nVocê recebeu a carta :  {cartas[num-1]}')
                for letra in range(0,3) :
                    print(f'Não é : {options[letra]}')
            elif cartas[num-1]=='Ás':
                print(f'\nVocê recebeu a carta :  {cartas[num-1]}')
                print(f'Não é : {options[letra]}')
            elif cartas[num-1]=='Rei':
                print(f'\nVocê recebeu a carta :  {cartas[num-1]}')
            else :
                print('Tente Novamente')
                self.dica()
            dicas_gastas[1] = 0
            self.açao()
        elif ajuda.lower()=='convidados' and dicas_gastas[2]!=0 :
            letter=['a','b','c','d']
            print(f'{self.resp} {letter[a]} {self.resp} {letter[b]} \n{letter[a]} {self.resp} {letter[b]} {letter[c]}')
            dicas_gastas[2] = 0
            self.açao()
        else :
            print('\nTente Novamente')
            self.dica()
        #convidados a a a b
        # placas 8 opções
        # cartas 4 opçoes 
              

print('\033[1;35m='*38)
print('\033[1;35m==',end=' ')
print('\033[1;33mSeja bem vindo ao Show do Milhão',end=' ')
print('\033[1;35m==')
print('\033[1;35m='*38)
ansicon.unload()

Perguntas = [
             '\nQual o símbolo do quilômetro? \n\n A - qm \n B - km \n C - kg/m3 \n D - kg ' ,
             '\nQual bicho transmite Doença de Chagas? \n\n A - Abelha \n B - Barata \n C - Pulga \n D - Barbeiro ',
             '\nQual fruto é conhecido no Norte e Nordeste como "jerimum"? \n\n A - Caju \n B - Abóbora \n C - Chuchu \n D - Côco ',
             '\nQual é o coletivo de cães? \n\n A - Matilha \n B - Rebanho \n C - Alcateia \n D - Manada ' ,
             '\nQual é o triângulo que tem todos os lados diferentes? \n\n A - Equilátero \n B - Isósceles \n C - Escaleno \n D - Trapézio ',
             '\nQuem compôs o Hino da Independência? \n\n A - Dom Pedro I \n B - Manuel Bandeira \n C - Castro Alvez \n D - Carlos Gomes ',
             '\nQual é o antônimo de "malograr"? \n\n A - Perder \n B - Fracassar \n C - Conseguir \n D - Desprezar ',
             '\nEm que país nasceu Carmem Miranda? \n\n A - Brasil \n B - Espanha \n C - Portugal \n D - Argentina ',
             '\nQual foi o último Presidente do período da ditadura militar no Brasil? \n\n A - Costa e Silva \n B - João Figueiredo \n C - Ernesto Geisel \n D - Emílio Médici',
             '\nSeguindo a sequência do baralho, qual carta vem depois do dez? \n\n A - Rei \n B - Valete \n C - Nove \n D - Ás ',
             '\nO adjetivo "venoso" está relacionado a: \n\n A - Vela \n B - Vento \n C - Vênia \n D - Veia ',
             '\nQue nome se dá à purificação por meio da água? \n\n A - Abolição \n B - Abnegação \n C - Ablução \n D - Abrupção ',
             '\nQual montanha se localiza entre a fronteira do Tibet com o Nepal? \n\n A - Monte Everest \n B - Monte Carlo \n C - Monte Fuji \n D - Monte Branco ',
             '\nEm que parte do corpo se encontra a epiglote? \n\n A - Estômago \n B - Pâncreas \n C - Rim \n D - Boca ',
             '\nA compensação por perda é chamada de... \n\n A - Déficit \n B - Indenização \n C - Indexação \n D - Indébito ',
             '\nEm que dia nasceu e em que dia foi registrado o Presidente Lula? \n\n A - 6 e 27 de Outubro \n B - 8 e 27 de Outubro \n C - 9 e 26 de Outubro \n D - 7 e 23 de Outubro ',
             ]

respostas=['b','d','b','a','c','a','c','c','b','b','d','c','a','d','b','a']
for perg in range(0,len(Perguntas)):
    um = Question(Perguntas[perg],respostas[perg],perg)
    um.opçoes()
    um.açao()


