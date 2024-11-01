import pygame 

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size, speed=6):
         self.game = game 
         self.type = e_type 
         self.pos = list(pos) #if you spawn 3 entities you could have all of those referencing the same list 
         self.size = size 
         self.velocity = [0, 0]
         self.speed = speed 
         self.collisions = {'up': False , 'down': False , 'right': False , 'left': False}
         self.animation_frames = self.game.assets['player']
         self.current_frame = 0 
         self.frame_time = 0  
         self.animation_speed = 0.1  
         self.facing_right = True

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], 200, 200)

    def update(self, tilemap, movement=(0, 0)):
         frame_movement = ((movement[0] * self.speed) + self.velocity[0], 
                      (movement[1] * self.speed) + self.velocity[1])

         if movement[0] < 0:
             self.facing_right = False 
         elif movement[0] > 0:
             self.facing_right = True 

         self.pos[0] += frame_movement[0]  
         entity_rect = self.rect()
         for rect in tilemap.physics_rects_around(self.pos):
             if entity_rect.colliderect(rect):
                 if frame_movement[0] > 0:
                     entity_rect.right = rect.left
                     self.collisions['right'] = True 
                 if frame_movement[0] < 0: 
                     entity_rect.left = rect.right 
                     self.collisions['left'] = True 

                 self.pos[0] = entity_rect.x

         self.velocity[1] = min(5, self.velocity[1] + 0.1)
         self.pos[1] += frame_movement[1] + self.velocity[1]

         entity_rect = self.rect()
         for rect in tilemap.physics_rects_around(self.pos):
             if entity_rect.colliderect(rect):
                 if frame_movement[1] > 0:
                     entity_rect.bottom = rect.top
                     self.collisions['down'] = True 
                     self.velocity[1]=0
                 if frame_movement[1] < 0: 
                     entity_rect.top = rect.bottom 
                     self.collisions['up'] = True 

                 self.pos[1] = entity_rect.y


                   
         if not self.collisions['down']:
             self.velocity[1] = min(5, self.velocity[1])

         self.collisions['up'] = False
         self.collisions['down'] = False
         self.collisions['left'] = False
         self.collisions['right'] = False

         self.frame_time += self.animation_speed
         if self.frame_time >= 1:  # Change frame every second (or adjust as necessary)
            self.current_frame = (self.current_frame + 1) % len(self.animation_frames)
            self.frame_time = 0


    def render(self, surf , offset = (0, 0 )):
         scaled_player_image = pygame.transform.scale(self.animation_frames[self.current_frame], (200, 200))  
         if not self.facing_right:  
             scaled_player_image = pygame.transform.flip(scaled_player_image, True, False) 
         surf.blit(scaled_player_image, self.pos)



    