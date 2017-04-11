#imports
import time,sys,random,json

#slow digit
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.005)

#Código
insperdex=json.loads(open("inspermons.json", encoding='UTF-8').read())
secure_random=random.SystemRandom()
print_slow("\nUm inspermon selvagem apareceu!"+"\n")
n=len(insperdex)
lista=range(n)
pokemon=random.choice(lista)
print_slow("\nÉ um "+str(insperdex[pokemon]['nome'])+"!!!"+"\n")
print_slow("Você deseja: "+"\n"+"- Lutar (1)"+"\n"+"- Correr (2)"+"\n")
esc=input("-> ")
if (esc=="2"):
	fuga=["Você correu com êxito!", "Deu ruim!!! Vai ter que lutar!\n"]
	x=(random.choice(fuga))
	if (x==fuga[1]):
		print_slow(fuga[1])
		print_slow("\nDados do "+str(insperdex[pokemon]['nome'])+":"+"\n"+"- Vida: "+str(insperdex[pokemon]['vida'])+"\n"+"- Poder 1: "+str(insperdex[pokemon]['attack'])+"\n- Defesa: "+str(insperdex[pokemon]['defesa'])+"\n"+"- Tipo: "+str(insperdex[pokemon]['tipo'])+"\n")
		from inspermon import inspermon_inicial,insperdex_n
		print_slow("\nDados do seu "+str(insperdex[insperdex_n]['nome'])+": "+"\n- Vida: "+str(insperdex[insperdex_n]['vida'])+"\n- Poder 1: "+str(insperdex[insperdex_n]['attack'])+"\n- Defesa: "+str(insperdex[insperdex_n]['defesa'])+"\n- Tipo: "+str(insperdex[insperdex_n]['tipo'])+"\n")
		
		if (insperdex[insperdex_n]['tipo']=="Fogo" and insperdex[pokemon]['tipo']=="Gelo"):
			insperdex[insperdex_n]['attack']=2*insperdex[insperdex_n]['attack']
			#insperdex[insperdex_n]['power']=2*insperdex[insperdex_n]['power']
		if (insperdex[pokemon]['tipo']=="Fogo" and insperdex[insperdex_n]['tipo']=="Gelo"):
			insperdex[pokemon]['attack']==2*insperdex[pokemon]['attack']
			#insperdex[pokemon]['power']==2*insperdex[pokemon]['power']

		if (insperdex[insperdex_n]['tipo']=="Elétrico" and insperdex[pokemon]['tipo']=="Água"):
			insperdex[insperdex_n]['attack']=2*insperdex[insperdex_n]['attack']
			#insperdex[insperdex_n]['power']=2*insperdex[insperdex_n]['power']
		if (insperdex[pokemon]['tipo']=="Elétrico" and insperdex[insperdex_n]['tipo']=="Água"):
			insperdex[pokemon]['attack']==2*insperdex[pokemon]['attack']
			#insperdex[pokemon]['power']==2*insperdex[pokemon]['power']

		if (insperdex[insperdex_n]['tipo']=="Água" and insperdex[pokemon]['tipo']=="Fogo"):
			insperdex[insperdex_n]['attack']=2*insperdex[insperdex_n]['attack']
			#insperdex[insperdex_n]['power']=2*insperdex[insperdex_n]['power']
		if (insperdex[pokemon]['tipo']=="Água" and insperdex[insperdex_n]['tipo']=="Fogo"):
			insperdex[pokemon]['attack']==2*insperdex[pokemon]['attack']
			#insperdex[pokemon]['power']==2*insperdex[pokemon]['power']

		if (insperdex[insperdex_n]['tipo']=="Pedra" and insperdex[pokemon]['tipo']=="Elétrico"):
			insperdex[insperdex_n]['attack']=2*insperdex[insperdex_n]['attack']
			#insperdex[insperdex_n]['power']=2*insperdex[insperdex_n]['power']
		if (insperdex[pokemon]['tipo']=="Pedra" and insperdex[insperdex_n]['tipo']=="Elétrico"):
			insperdex[pokemon]['attack']==2*insperdex[pokemon]['attack']
			#insperdex[pokemon]['power']==2*insperdex[pokemon]['power']

		if (insperdex[insperdex_n]['tipo']=="Gelo" and insperdex[pokemon]['tipo']=="Pedra"):
			insperdex[insperdex_n]['attack']=2*insperdex[insperdex_n]['attack']
			#insperdex[insperdex_n]['power']=2*insperdex[insperdex_n]['power']
		if (insperdex[pokemon]['tipo']=="Gelo" and insperdex[insperdex_n]['tipo']=="Pedra"):
			insperdex[pokemon]['attack']==2*insperdex[pokemon]['attack']
			#insperdex[pokemon]['power']==2*insperdex[pokemon]['power']

		print_slow("\nQual poder você deseja usar?\n"+"- Poder 1: "+str(insperdex[insperdex_n]['attack'])+"\n- Poder 2: "+str(insperdex[insperdex_n]['power'])+"\n")
		ataque=int(input("-> "))
		def seusAtaques(ataque):
			miss=["Errou!","Acertou"]
			if (ataque==1):
				miss_chance=(random.choice(miss))
				if (miss_chance==0):
					return print_slow("Miss attack")
				else:
					insperdex[pokemon]['vida']=insperdex[pokemon]['vida']-insperdex[insperdex_n]['attack']+insperdex[pokemon]['defesa']
					dano=insperdex[insperdex_n]['attack']-insperdex[pokemon]['defesa']
					if (dano<=0):
						dano=0
					return print_slow("\nVocê causou "+str(dano)+" de dano no "+str(insperdex[pokemon]['nome'])+"!!!")
			elif (ataque==2):
				return print_slow("Ainda sem ataques")
	elif (x==fuga[0]):
		print_slow(fuga[0])
else:
	print_slow("Prepare-se para a luta!"+"\n")
	print_slow("\nDados do "+str(insperdex[pokemon]['nome'])+" selvagem:"+"\n"+"- Vida: "+str(insperdex[pokemon]['vida'])+"\n"+"- Ataque 1: "+str(insperdex[pokemon]['attack'])+"\n"+"- Defesa: "+str(insperdex[pokemon]['defesa'])+"\n"+"- Tipo: "+str(insperdex[pokemon]['tipo']+"\n"))
	from inspermon import inspermon_inicial,insperdex_n
	print_slow("\nDados do seu "+str(insperdex[insperdex_n]['nome'])+": "+"\n- Vida: "+str(insperdex[insperdex_n]['vida'])+"\n- Ataque 1: "+str(insperdex[insperdex_n]['attack'])+"\n- Defesa: "+str(insperdex[insperdex_n]['defesa'])+"\n- Tipo: "+str(insperdex[insperdex_n]['tipo'])+"\n")
	
	if (insperdex[insperdex_n]['tipo']=="Fogo" and insperdex[pokemon]['tipo']=="Gelo"):
		insperdex[insperdex_n]['attack']=2*insperdex[insperdex_n]['attack']
		#insperdex[insperdex_n]['power']=2*insperdex[insperdex_n]['power']
	if (insperdex[pokemon]['tipo']=="Fogo" and insperdex[insperdex_n]['tipo']=="Gelo"):
		insperdex[pokemon]['attack']==2*insperdex[pokemon]['attack']
		#insperdex[pokemon]['power']==2*insperdex[pokemon]['power']

	if (insperdex[insperdex_n]['tipo']=="Elétrico" and insperdex[pokemon]['tipo']=="Água"):
		insperdex[insperdex_n]['attack']=2*insperdex[insperdex_n]['attack']
		#insperdex[insperdex_n]['power']=2*insperdex[insperdex_n]['power']
	if (insperdex[pokemon]['tipo']=="Elétrico" and insperdex[insperdex_n]['tipo']=="Água"):
		insperdex[pokemon]['attack']==2*insperdex[pokemon]['attack']
		#insperdex[pokemon]['power']==2*insperdex[pokemon]['power']

	if (insperdex[insperdex_n]['tipo']=="Água" and insperdex[pokemon]['tipo']=="Fogo"):
		insperdex[insperdex_n]['attack']=2*insperdex[insperdex_n]['attack']
		#insperdex[insperdex_n]['power']=2*insperdex[insperdex_n]['power']
	if (insperdex[pokemon]['tipo']=="Água" and insperdex[insperdex_n]['tipo']=="Fogo"):
		insperdex[pokemon]['attack']==2*insperdex[pokemon]['attack']
		#insperdex[pokemon]['power']==2*insperdex[pokemon]['power']

	if (insperdex[insperdex_n]['tipo']=="Pedra" and insperdex[pokemon]['tipo']=="Elétrico"):
		insperdex[insperdex_n]['attack']=2*insperdex[insperdex_n]['attack']
		#insperdex[insperdex_n]['power']=2*insperdex[insperdex_n]['power']
	if (insperdex[pokemon]['tipo']=="Pedra" and insperdex[insperdex_n]['tipo']=="Elétrico"):
		insperdex[pokemon]['attack']==2*insperdex[pokemon]['attack']
		#insperdex[pokemon]['power']==2*insperdex[pokemon]['power']

	if (insperdex[insperdex_n]['tipo']=="Gelo" and insperdex[pokemon]['tipo']=="Pedra"):
		insperdex[insperdex_n]['attack']=2*insperdex[insperdex_n]['attack']
		#insperdex[insperdex_n]['power']=2*insperdex[insperdex_n]['power']
	if (insperdex[pokemon]['tipo']=="Gelo" and insperdex[insperdex_n]['tipo']=="Pedra"):
		insperdex[pokemon]['attack']==2*insperdex[pokemon]['attack']
		#insperdex[pokemon]['power']==2*insperdex[pokemon]['power']
	
	#Funções de ataques
	def seusAtaques(ataque):
		miss=["Errou","Acertou"]
		if (ataque==1):
			miss_chance=(random.choice(miss))
			if (miss_chance==0):
				return print_slow("\nMiss attack")
			else:
				insperdex[pokemon]['vida']=insperdex[pokemon]['vida']-insperdex[insperdex_n]['attack']+insperdex[pokemon]['defesa']
				dano=insperdex[insperdex_n]['attack']-insperdex[pokemon]['defesa']
				if (dano<=0):
					dano=0
				if (insperdex[pokemon]['vida']<=0):
					insperdex[pokemon]['vida']=0
				#return print_slow("Você derrotou o "+str(insperdex[pokemon]['nome']))
		elif (ataque==2):
			#return print_slow("\nAinda sem ataques")
			return print_slow("\nVocê causou "+str(dano)+" de dano no "+str(insperdex[pokemon]['nome'])+"!!!")
		
	def ataqueOutro():
		miss=["Errou","Acertou"]
		miss_chance=(random.choice(miss))
		if (miss_chance==0):
			return print_slow("\nMiss attack do inimigo")
		else:
			insperdex[insperdex_n]['vida']=insperdex[insperdex_n]['vida']-insperdex[pokemon]['attack']+insperdex[insperdex_n]['defesa']
			dano=insperdex[pokemon]['attack']-insperdex[insperdex_n]['defesa']
			if (dano<=0):
				dano=0
			if (insperdex[insperdex_n]['vida']<=0):
				insperdex[insperdex_n]['vida']=0
			#return insperdex[insperdex_n]['vida']
			return print_slow("\nVocê levou "+str(dano)+" de dano do "+str(insperdex[pokemon]['nome'])+"!!!")
			("\nVocê levou "+str(dano)+" de dano do "+str(insperdex[pokemon]['nome'])+"!!!")
	insperdex[insperdex_n]['vida']=insperdex[insperdex_n]['vida']
	insperdex[pokemon]['vida']=insperdex[pokemon]['vida']
	while (insperdex[insperdex_n]['vida']>0 or insperdex[pokemon]['vida']>0):
		print_slow("\nQual ataque você deseja usar agora?\n"+"- Ataque 1: "+str(insperdex[insperdex_n]['attack'])+"\n")
		ataque=int(input("-> "))
		print_slow("\n"+str(seusAtaques(ataque)))
		if (insperdex[pokemon]['vida']==0):
			break
		print_slow("\nAgora a vida do "+str(insperdex[pokemon]['nome'])+" é: "+str(insperdex[pokemon]['vida'])+"!")
		print_slow("\n"+str(ataqueOutro()))
		print_slow("\nAgora a vida do seu "+str(insperdex[insperdex_n]['nome'])+" é: "+str(insperdex[insperdex_n]['vida'])+"!")
	if (insperdex[pokemon]['vida']==0):
		print_slow("\nParabéns! Você derrotou o "+str(insperdex[pokemon]['nome'])+"! Agora você pode continuar sua jornada ou seguir para o FabLab recuperar a vida dos seus inspermons!")
	elif (insperdex[insperdex_n]['vida']==0):
		print_slow("\nInfelizmente você perdeu a batalha contra o "+str(inspermon[pokemon]['nome']+"! Agora seu "+str(insperdex[insperdex_n]['nome']))+"Deve ser recuperado no FabLab!")