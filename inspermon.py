import time,sys,json,random,os
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

clear = lambda: os.system('cls')



#perguntas de inicio
print_slow("Hora de começar sua aventura! Qual o seu nome? "+"\n")
nome=input("-> ").title()
time.sleep(0.5)
clear()
print_slow("Você é uma menina ou um menino? "+"\n")
sexo=input("-> ").title()
time.sleep(0.5)
clear()
secure_random=random.SystemRandom()
print_slow("Para começar, nessa sua incrível jornada, você terá de escolher um Inspermon inicial para te acompanhar! "+"\n")
insperdex=json.loads(open("inspermons.json", encoding='UTF-8').read())
for x in insperdex:
	print_slow("\n- Nome: "+str(x['nome'])+" ("+str(x['numb'])+")"+"\n  Tipo: "+str(x['tipo'])+"\n")
print_slow("\nEscolha apenas um inspermon! "+"\n")
inspermon_inicial=int(input("-> "))
insperdex_n=insperdex[inspermon_inicial]["numb"]
print_slow("Ótima escolha\n")
print_slow("\nVocê agora possui um "+str(insperdex[inspermon_inicial]['nome'])+"!\n")

time.sleep(0.5) 	
clear()

print_slow("Está na hora de começar a aventura de verdade")
print_slow("\n"+nome+", você acorda e está em sua casa em Olímpia Town")
time.sleep(1)
clear()

import continua