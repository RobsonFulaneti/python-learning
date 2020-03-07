#import pygame
#pygame.init()
#pygame.mixer.music.load('musicmp3.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()


from pygame import mixer
mixer.init()
mixer.music.load('teste.mpeg')
mixer.music.play()
input('Agora você escuta?')
mixer.event.wait()