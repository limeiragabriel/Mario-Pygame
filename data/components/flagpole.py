import pygame as pg
from .. import setup
from .. import constants as c

class Flag(pg.sprite.Sprite):
    """===================================================="""
    def __init__(self, x, y):
        super(Flag, self).__init__()
        self.sprite_sheet = setup.GFX['item_objects']
        self.setup_images()
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.right = x
        self.rect.y = y
        self.state = c.TOPO_POSTE


    def setup_images(self):
        """===================================================="""
        self.frames = []

        self.frames.append(
            self.get_image(128, 32, 16, 16))


    def get_image(self, x, y, width, height):
        """===================================================="""
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.PRETO)
        image = pg.transform.scale(image,
                                   (int(rect.width*c.MULTILICADOR_TAMANHO_BLOCO),
                                    int(rect.height*c.MULTILICADOR_TAMANHO_BLOCO)))
        return image


    def update(self, *args):
        """===================================================="""
        self.handle_state()


    def handle_state(self):
        """===================================================="""
        if self.state == c.TOPO_POSTE:
            self.image = self.frames[0]
        elif self.state == c.DESLIZAR_PARA_BAIXO:
            self.sliding_down()
        elif self.state == c.BASE_POSTE:
            self.image = self.frames[0]


    def sliding_down(self):
        """===================================================="""
        self.y_vel = 5
        self.rect.y += self.y_vel

        if self.rect.bottom >= 485:
            self.state = c.BASE_POSTE


class Pole(pg.sprite.Sprite):
    """===================================================="""
    def __init__(self, x, y):
        super(Pole, self).__init__()
        self.sprite_sheet = setup.GFX['tile_set']
        self.setup_frames()
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def setup_frames(self):
        """===================================================="""
        self.frames = []

        self.frames.append(
            self.get_image(263, 144, 2, 16))


    def get_image(self, x, y, width, height):
        """===================================================="""
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.PRETO)
        image = pg.transform.scale(image,
                                   (int(rect.width*c.MULTILICADOR_TAMANHO_BLOCO),
                                    int(rect.height*c.MULTILICADOR_TAMANHO_BLOCO)))
        return image


    def update(self, *args):
        """===================================================="""
        pass


class Finial(pg.sprite.Sprite):
    """===================================================="""
    def __init__(self, x, y):
        super(Finial, self).__init__()
        self.sprite_sheet = setup.GFX['tile_set']
        self.setup_frames()
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y


    def setup_frames(self):
        """===================================================="""
        self.frames = []

        self.frames.append(
            self.get_image(228, 120, 8, 8))


    def get_image(self, x, y, width, height):
        """===================================================="""
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.PRETO)
        image = pg.transform.scale(image,
                                   (int(rect.width*c.MULTILICADOR_TAMANHO),
                                    int(rect.height*c.MULTILICADOR_TAMANHO)))
        return image


    def update(self, *args):
        pass
