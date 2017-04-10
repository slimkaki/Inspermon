# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

#Função para simular "Typing"
import time,sys
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.005)
#Dar rest ou se aventurar
print_slow("Você deseja passear ou dormir?")
escolha=input("\n"+"-> ").title()
while escolha=="Dormir":
	print_slow("..........."+"\n"+"Você se sente cheio de determinação.")
	print_slow("\n"+"Agora você deseja passear ou dormir?")
	escolha=input("\n"+"-> ").title()


#Opções de lugares para ir
lugares={"FabLab":"Recupera seus inspermons","Grama alta":"Pode encontrar inspermons selvagens","Lago":"Pode encontrar inspermons aquáticos","Floresta":"Pode encontrar inspermons mais fortes"}
print_slow("Escolha um lugar para ir: ")
for f, g in lugares.items():
	print_slow("\n"+"{0}: {1}".format(f, g))
lugar_escolha=input("\n"+"->")

#if lugar_escolha in lugares:

#else:
	#lugar_escolha=input("Escolha um lugar para ir: ")