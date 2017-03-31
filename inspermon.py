import random
#perguntas de inicio
nome=input("Bem-vindo ao Inspermon! Qual o seu nome? ").title()
sexo=input("Você é uma menina ou um menino? ").title()
semestre=int(input("Em que semestre você está? "))
secure_random=random.SystemRandom()
if (semestre==1):
	lista_inspermon_inicial={"Pelicano": "Fogo","Carareto": "Elétrico","Luciano": "Água"}
#elif (semestre==3):
	#lista_inspermon_inicial=["","",""]
print("Para começar, nessa sua incrível aventura, você terá de escolher um Inspermon inicial para te acompanhar! ")
for f, g in lista_inspermon_inicial.items():
	print("{0}: {1}".format(f, g))
inspermon_inicial=input("Escolha apenas um inspermon! ")
