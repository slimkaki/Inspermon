 # -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

#Função para simular "Typing"
import time,sys,random,os,json
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.001)
def print_sleep(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

#função para vida nas batalhas
clear = lambda: os.system('cls')

#Início
print_slow("Inspermon!"+"\n")
os.startfile('menu.mp3')
print_slow("\n"+"Oque deseja fazer?"+"\n"+"Pressione"+"\n"+" 0 para sair"+"\n"+" 1 para iniciar um jogo novo"+"\n"+" 2 para continuar seu jogo salvo")
escolha=int(input("\n"+"->"))
if (escolha==1):
    print_slow("Boa sorte")
    time.sleep(1)
    clear()

elif (escolha==2):
    print_slow("Aguarde uns instantes. . . . . . . . . . . . ")
    time.sleep(0.5)
    clear()

else:
    print_slow("Até a próxima vez então")
    time.sleep(2)
    quit()

    

#perguntas de inicio
print_slow("Bem-vindo ao Inspermon! Qual o seu nome? ")
nome=input("\n"+"->").title()
time.sleep(0.5)
clear()
print_slow("Você é uma menina ou um menino? ")
sexo=input("\n"+"->").title()
time.sleep(0.5)
clear()

#Inspermon inicial
secure_random=random.SystemRandom()
print_slow("Para começar, nessa sua incrível jornada, você terá de escolher um Inspermon inicial para te acompanhar! "+"\n")
insperdex=json.loads(open("inspermons.json", encoding='UTF-8').read())
for x in insperdex:
    print_slow("\n- Nome: "+str(x['nome'])+" ("+str(x['numb'])+")"+"\n  Tipo: "+str(x['tipo'])+"\n")
print_slow("\nEscolha apenas um inspermon! "+"\n")
inspermon_inicial=int(input("->"))
insperdex_n=insperdex[inspermon_inicial]["numb"]
print_slow("\nVocê agora possui um "+str(insperdex[inspermon_inicial]['nome'])+"!\n")
print_slow("Que ótima escolha")
time.sleep(2)
clear()
print_slow("Agora vamos iniciar sua jornada"+"\n"+"....")
time.sleep(2)
clear()
print_slow(nome+" ,você acorda e está em sua casa em Olímpia Town")


#Música de fundo
os.startfile('tema.mp3')

#Dar rest ou se aventurar
print_slow("\n"+"Você deseja passear ou dormir?")
escolha=input("\n"+"->").title()
while escolha=="Dormir":
    print_sleep(". . . . . . . . . . . . . . . . ."+"\n")
    time.sleep(0.5)
    clear()
    print_slow("Você se sente cheio de determinação.")
    time.sleep(0.5)
    clear()
    print_slow("Agora você deseja passear ou dormir?")
    escolha=input("\n"+"->").title()
    time.sleep(0.5)
    clear()



#Opções de lugares para ir
os.startfile('rota.mp3')
print_slow("Escolha um lugar para ir: ")
print_slow("\nFablab:Recupera seus inspermons(1)\n"+"\nGrama Alta:Pode encontrar inspermons selvagens(2)\n"+"\nLago:Pode encontrar inspermons aquáticos(3)\n"+"\nFloresta:Pode encontrar inspermons mais fortes(4)\n")

lugar_escolha=int(input("\n"+"->"))

#Passear
if lugar_escolha==1:
    print_slow("\nVocê foi ao FabLab\n")
    print_slow("\nAguarde enquanto seus inspermons são recuperados\n"+". . . . .")
    os.startfile('heal.mp3')
    time.sleep(3)
    os.startfile('rota.mp3')
    print_slow("Seus inspermons foram recuperados")


elif lugar_escolha==2:
    print_slow("\nVocê foi andar pela grama alta\n")
    time.sleep(1)
    clear()
    import batalha_inspermon.py

elif lugar_escolha==3:
    print_slow("\nVocê foi andar pela beira do lago\n")
    time.sleep(1)
    clear()
    import batalha_inspermon.py
    
elif lugar_escolha==4:
    print_slow("\nVocê foi andar pela floresta\n")
    time.sleep(1)
    clear()
    import batalha_inspermon.py

