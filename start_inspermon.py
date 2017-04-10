import time,sys
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.005)
print_slow("Bem-vindo ao Inspermon!")
print_slow("\n"+"Deseja iniciar o jogo? 0 para quitar, 1 para iniciar: "+"\n")
escolha=int(input("-> "))
if (escolha==1):
	import inspermon
else:
	print_slow("Até a próxima vez então")