

import pygame 
NEIGHBOUR_OFFSETS = [
    (-2, -2), (-2, -1), (-2, 0), (-2, 1),
    (-1, -2), (-1, -1), (-1, 0), (-1, 1),
    (0, -2), (0, -1), (0, 0), (0, 1),
    (1, -2), (1, -1), (1, 0), (1, 1)
]




PHYSICS_TILES  = {'grass', 'stone'}

class Tilemap:
    def __init__(self, game, tile_size=128):
        self.game = game 
        self.tile_size = tile_size
        self.tilemap = {}     # on square grid 
        self.offgrid_tiles = []   # does not line up with grid 


        
        for i in range(10):
            self.tilemap[str(i) + ';1'] = {'type': 'grass', 'variant': 1, 'pos': (i, 4.65)}  # horizontal line of grass tiles 
            #self.tilemap[str(10) + ';' + str(1 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 2 + i)}  # vertical line of stone tiles

    def tiles_around(self , pos):
        tiles=[]
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHBOUR_OFFSETS:
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles

    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size,tile['pos'][1] * self.tile_size , self.tile_size,self.tile_size))
        return rects


    def render(self, surf, offset = (0, 0)):
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1]))

        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surf.blit(
                self.game.assets[tile['type']][tile['variant']], 
                (tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1])
            )        
