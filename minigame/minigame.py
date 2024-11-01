import sys 
import pygame 
from scripts.entities import PhysicsEntity
from scripts.utils import load_image , load_images
from scripts.tilemap import Tilemap

class Game:
    def __init__(self):
        pygame.init()  
        pygame.mixer.init()
        pygame.font.init()

        pygame.display.set_caption('Mito Vs The Watchers')
        self.screen = pygame.display.set_mode((1280, 720))

        self.clock = pygame.time.Clock()  
        self.movement = [False, False]

        # Load background image
        self.background_img = load_image('mito background.png')  # Make sure to provide the correct path

        self.load_audio()
        self.play_background_music()

        tile_size = 128 
        self.assets = {
            'grass': [pygame.transform.scale(img, (tile_size, tile_size)) for img in load_images('tiles/grass')],
            'stone': [pygame.transform.scale(img, (tile_size, tile_size)) for img in load_images('tiles/stone')],

            'player': load_images('player/idle') 

        }

        self.player = PhysicsEntity(self, 'player', (400, 450), (8, 15), speed = 5)
        self.tilemap = Tilemap(self,tile_size=tile_size)
        self.scroll = [0, 0]

        self.font = pygame.font.Font(None, 25)

    def render_text(self , text , position):
        text_surface = self.font.render(text, True , (255, 255 , 0))
        self.screen.blit(text_surface, position)

    def load_audio(self):
        self.background_music = pygame.mixer.Sound('sound/background music.wav')  
        

    def play_background_music(self):
        self.background_music.play(-1)  # Play the background music in a loop

    def run(self):  # Run function 
        while True:
            # Draw the background image
            self.screen.blit(self.background_img, (0, 0))

            self.scroll[0] += (self.player.rect().centerx - self.screen.get_width() / 2 - self.scroll[0])/30
            self.scroll[0] += (self.player.rect().centery - self.screen.get_height() / 2 - self.scroll[1])/30
            render_scroll = (int(self.scroll[0]),int(self.scroll[1]))

            self.tilemap.render(self.screen , offset=render_scroll)

            self.player.update(self.tilemap,(self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen, offset=render_scroll)
            
            self.render_text("Use left and right arrow keys to move, use up arrow key to jump", (10, 10))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True 
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -5 
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False 
                
            pygame.display.update()
            self.clock.tick(60)  # 60 fps 

Game().run()
