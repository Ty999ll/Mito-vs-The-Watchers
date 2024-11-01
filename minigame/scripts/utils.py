import os

import pygame


BASE_IMG_PATH = 'C:/Users/kimat/source/repos/minigame/minigame/'
BASE_AUDIO_PATH = 'C:/Users/kimat/source/repos/minigame/minigame/sound/'


def load_image(path):  
        img = pygame.image.load(BASE_IMG_PATH + path).convert_alpha()
        return img

def load_images(path):
        images=[]
        for img_name in sorted( os.listdir(BASE_IMG_PATH + path)):
            images.append(load_image(path + '/' + img_name))

        return images

def load_audio(path):
    audio_files = []
    for audio_name in sorted(os.listdir(BASE_AUDIO_PATH + path)):
        audio_files.append(pygame.mixer.Sound(BASE_AUDIO_PATH + path + '/' + audio_name))
    return audio_files