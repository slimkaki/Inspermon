# -*- coding: utf-8 -*-
import pygame,random,sys
from pygame.locals import *
pygame.init()
img_menu=pygame.image.load('inspermon_inicio.jpg')
img_1=pygame.image.load('inspermon_1.jpg')
pygame.image.load('inspermon_1.jpg')
screen=pygame.display.set_mode((640,480))
background=pygame.Surface(screen.get_size())
background=background.convert()
screen.blit(img_menu,(0,0))
mainloop=True
clock=pygame.time.Clock()
FPS=30
#while True:
#	if random.randint(0,1)==0:
#		pygame.mixer.music.load('menu.mp3')
#	else:
#		pygame.mixer.music.load('menu.mp3')
#	pygame.mixer.music.play(-1,0.0)
#	pygame.mixer.music.stop()


playtime=0.0
while mainloop:
	milliseconds=clock.tick(FPS)
	playtime+=milliseconds/1000
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			mainloop=False
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_0:
				mainloop=False
			elif event.type==pygame.K_1:
				mainloop=True
				while(True):
					screen=pygame.display.set_mode((640,480))
					gameDisplay.blit(img_1,(0,0))
	text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime)
	pygame.display.set_caption(text)
	pygame.display.flip()
pygame.quit()
print("This game was played for {0:.2f} seconds".format(playtime))