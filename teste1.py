# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

#Função para simular "Typing"
import time,sys,random,os
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
#Início
print_slow("Bem-vindo ao Inspermon!")
print_slow("Deseja iniciar o jogo? 0 para sair, 1 para iniciar e 2 para continuar seu jogo salvo: ")
escolha=int(input("\n"+"->"))
if (escolha==1):
    print_slow("Boa sorte")
else:
    print_slow("Até a próxima vez então")

#perguntas de inicio
print_slow("\n"+"Bem-vindo ao Inspermon! Qual o seu nome? ")
nome=input("\n"+"->").title()
print_slow("Você é uma menina ou um menino? ")
sexo=input("\n"+"->").title()
print_slow("Em que semestre você está? ")
semestre=int(input("\n"+"->"))
secure_random=random.SystemRandom()
if (semestre==1):
	lista_inspermon_inicial={"Pelicano": "Fogo","Carareto": "Elétrico","Luciano": "Água"}

print_slow("Para começar, nessa sua incrível aventura, você terá de escolher um Inspermon inicial para te acompanhar! "+"\n")
for f, g in lista_inspermon_inicial.items():
	print("\n"+"{0}: {1}".format(f, g))
inspermon_inicial=input("\n"+"Escolha apenas um inspermon! ")
print_slow("Que otima escolha"+"\n"+"Agora vamos iniciar a aventura de verdade"+"\n")
print_slow("{0}, você acorda e está em sua casa em Olímpia Town".format(nome))


#Música de fundo
os.startfile('tema.mp3')

#Dar rest ou se aventurar
print_slow("\n"+"Você deseja passear ou dormir?")
escolha=input("\n"+"->").title()
while escolha=="Dormir":
	print_slow("..........."+"\n"+"Você se sente cheio de determinação.")
	print_slow("\n"+"Agora você deseja passear ou dormir?")
	escolha=input("\n"+"->").title()


#Opções de lugares para ir
lugares={"FabLab":"Recupera seus inspermons","Grama alta":"Pode encontrar inspermons selvagens","Lago":"Pode encontrar inspermons aquáticos","Floresta":"Pode encontrar inspermons mais fortes"}
print_slow("Escolha um lugar para ir: ")
for f, g in lugares.items():
	print_slow("\n"+"{0}: {1}".format(f, g))
lugar_escolha=input("\n"+"->")

