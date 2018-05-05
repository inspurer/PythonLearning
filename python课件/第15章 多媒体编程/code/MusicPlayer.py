import os
import pygame
import random
import time

folder = r'h:\music'
musics = [folder+'\\'+music for music in os.listdir(folder) if music.endswith('.mp3')]
total = len(musics)

pygame.mixer.init()
while True:
    if not pygame.mixer.music.get_busy():
        nextMusic = random.choice(musics)
        pygame.mixer.music.load(nextMusic)
        pygame.mixer.music.play(1)
        print('playing....',nextMusic)
    else:
        time.sleep(1)
