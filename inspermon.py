import time,sys,json,random
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.005)
#perguntas de inicio
print_slow("Hora de começar sua aventura! Qual o seu nome? "+"\n")
nome=input("-> ").title()
print_slow("Você é uma menina ou um menino? "+"\n")
sexo=input("-> ").title()
secure_random=random.SystemRandom()
print_slow("Para começar, nessa sua incrível jornada, você terá de escolher um Inspermon inicial para te acompanhar! "+"\n")
insperdex=json.loads(open("inspermons.json", encoding='UTF-8').read())
for x in insperdex:
	print_slow("\n- Nome: "+str(x['nome'])+" ("+str(x['numb'])+")"+"\n  Tipo: "+str(x['tipo'])+"\n")
print_slow("\nEscolha apenas um inspermon! "+"\n")
inspermon_inicial=int(input("-> "))
insperdex_n=insperdex[inspermon_inicial]["numb"]
print_slow("\nVocê agora possui um "+str(insperdex[inspermon_inicial]['nome'])+"!\n")
# TESTE DE BATALHA
print_slow("\nVocê foi andar pela floresta\n")
import batalha_inspermon