import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Stickman Noob Runner')
clock = pygame.time.Clock()
sandRect = groundSand.get_rect(bottomleft = (200,400))
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		
		# keymaps here:
		
	# surfaces is coded in here.
	screen.fill('skyblue')
	
	
	pygame.display.update()
	clock.tick(60)