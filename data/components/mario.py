import pygame as pg
from .. import setup, tools
from .. import constants as c
from . import powerups


class Mario(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['mario_bros']

        self.setup_timers()
        self.setup_state_booleans()
        self.setup_forces()
        self.setup_counters()
        self.load_images_from_sheet()

        self.state = c.ANDAR
        self.image = self.right_frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

        self.key_timer = 0


    def setup_timers(self):
        """===================================================="""
        self.walking_timer = 0
        self.invincible_animation_timer = 0
        self.invincible_start_timer = 0
        self.fire_transition_timer = 0
        self.death_timer = 0
        self.transition_timer = 0
        self.last_fireball_time = 0
        self.hurt_invisible_timer = 0
        self.hurt_invisible_timer2 = 0
        self.flag_pole_timer = 0


    def setup_state_booleans(self):
        """===================================================="""
        self.facing_right = True
        self.allow_jump = True
        self.dead = False
        self.invincible = False
        self.big = False
        self.fire = False
        self.allow_fireball = True
        self.in_transition_state = False
        self.hurt_invincible = False
        self.in_castle = False
        self.crouching = False
        self.losing_invincibility = False


    def setup_forces(self):
        """===================================================="""
        self.x_vel = 0
        self.y_vel = 0
        self.max_x_vel = c.MAX_ANDAR_VELOCIDADE
        self.max_y_vel = c.MAX_Y_VEL
        self.x_accel = c.ANDAR_ACELERACAO
        self.jump_vel = c.VELOCIDADE_PULO
        self.gravity = c.GRAVIDADE


    def setup_counters(self):
        """===================================================="""
        self.frame_index = 0
        self.invincible_index = 0
        self.fire_transition_index = 0
        self.fireball_count = 0
        self.flag_pole_right = 0


    def load_images_from_sheet(self):
        """===================================================="""
        self.right_frames = []
        self.left_frames = []

        self.right_small_normal_frames = []
        self.left_small_normal_frames = []
        self.right_small_green_frames = []
        self.left_small_green_frames = []
        self.right_small_red_frames = []
        self.left_small_red_frames = []
        self.right_small_black_frames = []
        self.left_small_black_frames = []

        self.right_big_normal_frames = []
        self.left_big_normal_frames = []
        self.right_big_green_frames = []
        self.left_big_green_frames = []
        self.right_big_red_frames = []
        self.left_big_red_frames = []
        self.right_big_black_frames = []
        self.left_big_black_frames = []

        self.right_fire_frames = []
        self.left_fire_frames = []


        self.right_small_normal_frames.append(
            self.get_image(178, 32, 12, 16))  # Right [0]
        self.right_small_normal_frames.append(
            self.get_image(80,  32, 15, 16))  # Right walking 1 [1]
        self.right_small_normal_frames.append(
            self.get_image(96,  32, 16, 16))  # Right walking 2 [2]
        self.right_small_normal_frames.append(
            self.get_image(112,  32, 16, 16))  # Right walking 3 [3]
        self.right_small_normal_frames.append(
            self.get_image(144, 32, 16, 16))  # Right jump [4]
        self.right_small_normal_frames.append(
            self.get_image(130, 32, 14, 16))  # Right skid [5]
        self.right_small_normal_frames.append(
            self.get_image(160, 32, 15, 16))  # Death frame [6]
        self.right_small_normal_frames.append(
            self.get_image(320, 8, 16, 24))  # Transition small to big [7]
        self.right_small_normal_frames.append(
            self.get_image(241, 33, 16, 16))  # Transition big to small [8]
        self.right_small_normal_frames.append(
            self.get_image(194, 32, 12, 16))  # Frame 1 of flag pole Slide [9]
        self.right_small_normal_frames.append(
            self.get_image(210, 33, 12, 16))  # Frame 2 of flag pole slide [10]


        self.right_small_green_frames.append(
            self.get_image(178, 224, 12, 16))  # Right standing [0]
        self.right_small_green_frames.append(
            self.get_image(80, 224, 15, 16))  # Right walking 1 [1]
        self.right_small_green_frames.append(
            self.get_image(96, 224, 16, 16))  # Right walking 2 [2]
        self.right_small_green_frames.append(
            self.get_image(112, 224, 15, 16))  # Right walking 3 [3]
        self.right_small_green_frames.append(
            self.get_image(144, 224, 16, 16))  # Right jump [4]
        self.right_small_green_frames.append(
            self.get_image(130, 224, 14, 16))  # Right skid [5]


        self.right_small_red_frames.append(
            self.get_image(178, 272, 12, 16))  # Right standing [0]
        self.right_small_red_frames.append(
            self.get_image(80, 272, 15, 16))  # Right walking 1 [1]
        self.right_small_red_frames.append(
            self.get_image(96, 272, 16, 16))  # Right walking 2 [2]
        self.right_small_red_frames.append(
            self.get_image(112, 272, 15, 16))  # Right walking 3 [3]
        self.right_small_red_frames.append(
            self.get_image(144, 272, 16, 16))  # Right jump [4]
        self.right_small_red_frames.append(
            self.get_image(130, 272, 14, 16))  # Right skid [5]


        self.right_small_black_frames.append(
            self.get_image(178, 176, 12, 16))  # Right standing [0]
        self.right_small_black_frames.append(
            self.get_image(80, 176, 15, 16))  # Right walking 1 [1]
        self.right_small_black_frames.append(
            self.get_image(96, 176, 16, 16))  # Right walking 2 [2]
        self.right_small_black_frames.append(
            self.get_image(112, 176, 15, 16))  # Right walking 3 [3]
        self.right_small_black_frames.append(
            self.get_image(144, 176, 16, 16))  # Right jump [4]
        self.right_small_black_frames.append(
            self.get_image(130, 176, 14, 16))  # Right skid [5]


        self.right_big_normal_frames.append(
            self.get_image(176, 0, 16, 32))  # Right standing [0]
        self.right_big_normal_frames.append(
            self.get_image(81, 0, 16, 32))  # Right walking 1 [1]
        self.right_big_normal_frames.append(
            self.get_image(97, 0, 15, 32))  # Right walking 2 [2]
        self.right_big_normal_frames.append(
            self.get_image(113, 0, 15, 32))  # Right walking 3 [3]
        self.right_big_normal_frames.append(
            self.get_image(144, 0, 16, 32))  # Right jump [4]
        self.right_big_normal_frames.append(
            self.get_image(128, 0, 16, 32))  # Right skid [5]
        self.right_big_normal_frames.append(
            self.get_image(336, 0, 16, 32))  # Right throwing [6]
        self.right_big_normal_frames.append(
            self.get_image(160, 10, 16, 22))  # Right crouching [7]
        self.right_big_normal_frames.append(
            self.get_image(272, 2, 16, 29))  # Transition big to small [8]
        self.right_big_normal_frames.append(
            self.get_image(193, 2, 16, 30))  # Frame 1 of flag pole slide [9]
        self.right_big_normal_frames.append(
            self.get_image(209, 2, 16, 29))  # Frame 2 of flag pole slide [10]


        self.right_big_green_frames.append(
            self.get_image(176, 192, 16, 32))  # Right standing [0]
        self.right_big_green_frames.append(
            self.get_image(81, 192, 16, 32))  # Right walking 1 [1]
        self.right_big_green_frames.append(
            self.get_image(97, 192, 15, 32))  # Right walking 2 [2]
        self.right_big_green_frames.append(
            self.get_image(113, 192, 15, 32))  # Right walking 3 [3]
        self.right_big_green_frames.append(
            self.get_image(144, 192, 16, 32))  # Right jump [4]
        self.right_big_green_frames.append(
            self.get_image(128, 192, 16, 32))  # Right skid [5]
        self.right_big_green_frames.append(
            self.get_image(336, 192, 16, 32))  # Right throwing [6]
        self.right_big_green_frames.append(
            self.get_image(160, 202, 16, 22))  # Right Crouching [7]


        self.right_big_red_frames.append(
            self.get_image(176, 240, 16, 32))  # Right standing [0]
        self.right_big_red_frames.append(
            self.get_image(81, 240, 16, 32))  # Right walking 1 [1]
        self.right_big_red_frames.append(
            self.get_image(97, 240, 15, 32))  # Right walking 2 [2]
        self.right_big_red_frames.append(
            self.get_image(113, 240, 15, 32))  # Right walking 3 [3]
        self.right_big_red_frames.append(
            self.get_image(144, 240, 16, 32))  # Right jump [4]
        self.right_big_red_frames.append(
            self.get_image(128, 240, 16, 32))  # Right skid [5]
        self.right_big_red_frames.append(
            self.get_image(336, 240, 16, 32))  # Right throwing [6]
        self.right_big_red_frames.append(
            self.get_image(160, 250, 16, 22))  # Right crouching [7]


        self.right_big_black_frames.append(
            self.get_image(176, 144, 16, 32))  # Right standing [0]
        self.right_big_black_frames.append(
            self.get_image(81, 144, 16, 32))  # Right walking 1 [1]
        self.right_big_black_frames.append(
            self.get_image(97, 144, 15, 32))  # Right walking 2 [2]
        self.right_big_black_frames.append(
            self.get_image(113, 144, 15, 32))  # Right walking 3 [3]
        self.right_big_black_frames.append(
            self.get_image(144, 144, 16, 32))  # Right jump [4]
        self.right_big_black_frames.append(
            self.get_image(128, 144, 16, 32))  # Right skid [5]
        self.right_big_black_frames.append(
            self.get_image(336, 144, 16, 32))  # Right throwing [6]
        self.right_big_black_frames.append(
            self.get_image(160, 154, 16, 22))  # Right Crouching [7]



        self.right_fire_frames.append(
            self.get_image(176, 48, 16, 32))  # Right standing [0]
        self.right_fire_frames.append(
            self.get_image(81, 48, 16, 32))  # Right walking 1 [1]
        self.right_fire_frames.append(
            self.get_image(97, 48, 15, 32))  # Right walking 2 [2]
        self.right_fire_frames.append(
            self.get_image(113, 48, 15, 32))  # Right walking 3 [3]
        self.right_fire_frames.append(
            self.get_image(144, 48, 16, 32))  # Right jump [4]
        self.right_fire_frames.append(
            self.get_image(128, 48, 16, 32))  # Right skid [5]
        self.right_fire_frames.append(
            self.get_image(336, 48, 16, 32))  # Right throwing [6]
        self.right_fire_frames.append(
            self.get_image(160, 58, 16, 22))  # Right crouching [7]
        self.right_fire_frames.append(
            self.get_image(0, 0, 0, 0))  # Place holder [8]
        self.right_fire_frames.append(
            self.get_image(193, 50, 16, 29))  # Frame 1 of flag pole slide [9]
        self.right_fire_frames.append(
            self.get_image(209, 50, 16, 29))  # Frame 2 of flag pole slide [10]




        for frame in self.right_small_normal_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_small_normal_frames.append(new_image)

        for frame in self.right_small_green_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_small_green_frames.append(new_image)

        for frame in self.right_small_red_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_small_red_frames.append(new_image)

        for frame in self.right_small_black_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_small_black_frames.append(new_image)

        for frame in self.right_big_normal_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_big_normal_frames.append(new_image)

        for frame in self.right_big_green_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_big_green_frames.append(new_image)

        for frame in self.right_big_red_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_big_red_frames.append(new_image)

        for frame in self.right_big_black_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_big_black_frames.append(new_image)

        for frame in self.right_fire_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_fire_frames.append(new_image)


        self.normal_small_frames = [self.right_small_normal_frames,
                              self.left_small_normal_frames]

        self.green_small_frames = [self.right_small_green_frames,
                             self.left_small_green_frames]

        self.red_small_frames = [self.right_small_red_frames,
                           self.left_small_red_frames]

        self.black_small_frames = [self.right_small_black_frames,
                             self.left_small_black_frames]

        self.invincible_small_frames_list = [self.normal_small_frames,
                                          self.green_small_frames,
                                          self.red_small_frames,
                                          self.black_small_frames]

        self.normal_big_frames = [self.right_big_normal_frames,
                                  self.left_big_normal_frames]

        self.green_big_frames = [self.right_big_green_frames,
                                 self.left_big_green_frames]

        self.red_big_frames = [self.right_big_red_frames,
                               self.left_big_red_frames]

        self.black_big_frames = [self.right_big_black_frames,
                                 self.left_big_black_frames]

        self.fire_frames = [self.right_fire_frames,
                            self.left_fire_frames]

        self.invincible_big_frames_list = [self.normal_big_frames,
                                           self.green_big_frames,
                                           self.red_big_frames,
                                           self.black_big_frames]

        self.all_images = [self.right_big_normal_frames,
                           self.right_big_black_frames,
                           self.right_big_red_frames,
                           self.right_big_green_frames,
                           self.right_small_normal_frames,
                           self.right_small_green_frames,
                           self.right_small_red_frames,
                           self.right_small_black_frames,
                           self.left_big_normal_frames,
                           self.left_big_black_frames,
                           self.left_big_red_frames,
                           self.left_big_green_frames,
                           self.left_small_normal_frames,
                           self.left_small_red_frames,
                           self.left_small_green_frames,
                           self.left_small_black_frames]


        self.right_frames = self.normal_small_frames[0]
        self.left_frames = self.normal_small_frames[1]


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


    def update(self, keys, game_info, fire_group):
        """===================================================="""
        self.current_time = game_info[c.TEMPO_ATUAL]
        self.handle_state(keys, fire_group)
        self.check_for_special_state()
        self.animation()


    def handle_state(self, keys, fire_group):
        """===================================================="""
        if self.state == c.PARADO:
            self.standing(keys, fire_group)
        elif self.state == c.ANDAR:
            self.walking(keys, fire_group)
        elif self.state == c.PULO:
            self.jumping(keys, fire_group)
        elif self.state == c.QUEDA:
            self.falling(keys, fire_group)
        elif self.state == c.PULO_MORTE:
            self.jumping_to_death()
        elif self.state == c.PEQUENO_PARA_GRANDE:
            self.changing_to_big()
        elif self.state == c.GRANDE_PARA_FOGO:
            self.changing_to_fire()
        elif self.state == c.GRANDE_PARA_PEQUENO:
            self.changing_to_small()
        elif self.state == c.BANDEIRA:
            self.flag_pole_sliding()
        elif self.state == c.BASE_POSTE:
            self.sitting_at_bottom_of_pole()
        elif self.state == c.WALKING_TO_CASTLE:
            self.walking_to_castle()
        elif self.state == c.FIM_DO_NIVEL_QUEDA:
            self.falling_at_end_of_level()


    def standing(self, keys, fire_group):
        """===================================================="""
        self.check_to_allow_jump(keys)
        self.check_to_allow_fireball(keys)

        self.frame_index = 0
        self.x_vel = 0
        self.y_vel = 0

        if keys[tools.keybinding['action']]:
            if self.fire and self.allow_fireball:
                self.shoot_fireball(fire_group)

        if keys[tools.keybinding['down']]:
            self.crouching = True

        if keys[tools.keybinding['left']]:
            self.facing_right = False
            self.get_out_of_crouch()
            self.state = c.ANDAR
        elif keys[tools.keybinding['right']]:
            self.facing_right = True
            self.get_out_of_crouch()
            self.state = c.ANDAR
        elif keys[tools.keybinding['jump']]:
            if self.allow_jump:
                if self.big:
                    setup.SFX['big_jump'].play()
                else:
                    setup.SFX['small_jump'].play()
                self.state = c.PULO
                self.y_vel = c.VELOCIDADE_PULO
        else:
            self.state = c.PARADO

        if not keys[tools.keybinding['down']]:
            self.get_out_of_crouch()


    def get_out_of_crouch(self):
        """===================================================="""
        bottom = self.rect.bottom
        left = self.rect.x
        if self.facing_right:
            self.image = self.right_frames[0]
        else:
            self.image = self.left_frames[0]
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom
        self.rect.x = left
        self.crouching = False


    def check_to_allow_jump(self, keys):
        """===================================================="""
        if not keys[tools.keybinding['jump']]:
            self.allow_jump = True


    def check_to_allow_fireball(self, keys):
        """===================================================="""
        if not keys[tools.keybinding['action']]:
            self.allow_fireball = True


    def shoot_fireball(self, powerup_group):
        """===================================================="""
        setup.SFX['fireball'].play()
        self.fireball_count = self.count_number_of_fireballs(powerup_group)

        if (self.current_time - self.last_fireball_time) > 200:
            if self.fireball_count < 2:
                self.allow_fireball = False
                powerup_group.add(
                    powerups.FireBall(self.rect.right, self.rect.y, self.facing_right))
                self.last_fireball_time = self.current_time

                self.frame_index = 6
                if self.facing_right:
                    self.image = self.right_frames[self.frame_index]
                else:
                    self.image = self.left_frames[self.frame_index]


    def count_number_of_fireballs(self, powerup_group):
        """===================================================="""
        fireball_list = []

        for powerup in powerup_group:
            if powerup.name == c.BOLA_FOGO:
                fireball_list.append(powerup)

        return len(fireball_list)


    def walking(self, keys, fire_group):
        """===================================================="""

        self.check_to_allow_jump(keys)
        self.check_to_allow_fireball(keys)

        if self.frame_index == 0:
            self.frame_index += 1
            self.walking_timer = self.current_time
        else:
            if (self.current_time - self.walking_timer >
                    self.calculate_animation_speed()):
                if self.frame_index < 3:
                    self.frame_index += 1
                else:
                    self.frame_index = 1

                self.walking_timer = self.current_time

        if keys[tools.keybinding['action']]:
            self.max_x_vel = c.MAX_CORRER_VELOCIDADE
            self.x_accel = c.CORRER_ACELERACAO
            if self.fire and self.allow_fireball:
                self.shoot_fireball(fire_group)
        else:
            self.max_x_vel = c.MAX_ANDAR_VELOCIDADE
            self.x_accel = c.ANDAR_ACELERACAO

        if keys[tools.keybinding['jump']]:
            if self.allow_jump:
                if self.big:
                    setup.SFX['big_jump'].play()
                else:
                    setup.SFX['small_jump'].play()
                self.state = c.PULO
                if self.x_vel > 4.5 or self.x_vel < -4.5:
                    self.y_vel = c.VELOCIDADE_PULO - .5
                else:
                    self.y_vel = c.VELOCIDADE_PULO


        if keys[tools.keybinding['left']]:
            self.get_out_of_crouch()
            self.facing_right = False
            if self.x_vel > 0:
                self.frame_index = 5
                self.x_accel = c.PEQUENO_GIRAR
            else:
                self.x_accel = c.ANDAR_ACELERACAO

            if self.x_vel > (self.max_x_vel * -1):
                self.x_vel -= self.x_accel
                if self.x_vel > -0.5:
                    self.x_vel = -0.5
            elif self.x_vel < (self.max_x_vel * -1):
                self.x_vel += self.x_accel

        elif keys[tools.keybinding['right']]:
            self.get_out_of_crouch()
            self.facing_right = True
            if self.x_vel < 0:
                self.frame_index = 5
                self.x_accel = c.PEQUENO_GIRAR
            else:
                self.x_accel = c.ANDAR_ACELERACAO

            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel
                if self.x_vel < 0.5:
                    self.x_vel = 0.5
            elif self.x_vel > self.max_x_vel:
                self.x_vel -= self.x_accel

        else:
            if self.facing_right:
                if self.x_vel > 0:
                    self.x_vel -= self.x_accel
                else:
                    self.x_vel = 0
                    self.state = c.PARADO
            else:
                if self.x_vel < 0:
                    self.x_vel += self.x_accel
                else:
                    self.x_vel = 0
                    self.state = c.PARADO


    def calculate_animation_speed(self):
        """===================================================="""
        if self.x_vel == 0:
            animation_speed = 130
        elif self.x_vel > 0:
            animation_speed = 130 - (self.x_vel * (13))
        else:
            animation_speed = 130 - (self.x_vel * (13) * -1)

        return animation_speed


    def jumping(self, keys, fire_group):
        """===================================================="""
        self.allow_jump = False
        self.frame_index = 4
        self.gravity = c.GRAVIDADE_PULO
        self.y_vel += self.gravity
        self.check_to_allow_fireball(keys)

        if self.y_vel >= 0 and self.y_vel < self.max_y_vel:
            self.gravity = c.GRAVIDADE
            self.state = c.QUEDA

        if keys[tools.keybinding['left']]:
            if self.x_vel > (self.max_x_vel * - 1):
                self.x_vel -= self.x_accel

        elif keys[tools.keybinding['right']]:
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel

        if not keys[tools.keybinding['jump']]:
            self.gravity = c.GRAVIDADE
            self.state = c.QUEDA

        if keys[tools.keybinding['action']]:
            if self.fire and self.allow_fireball:
                self.shoot_fireball(fire_group)


    def falling(self, keys, fire_group):
        """===================================================="""
        self.check_to_allow_fireball(keys)
        if self.y_vel < c.MAX_Y_VEL:
            self.y_vel += self.gravity

        if keys[tools.keybinding['left']]:
            if self.x_vel > (self.max_x_vel * - 1):
                self.x_vel -= self.x_accel

        elif keys[tools.keybinding['right']]:
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel

        if keys[tools.keybinding['action']]:
            if self.fire and self.allow_fireball:
                self.shoot_fireball(fire_group)


    def jumping_to_death(self):
        """===================================================="""
        if self.death_timer == 0:
            self.death_timer = self.current_time
        elif (self.current_time - self.death_timer) > 500:
            self.rect.y += self.y_vel
            self.y_vel += self.gravity


    def start_death_jump(self, game_info):
        """===================================================="""
        self.dead = True
        game_info[c.MARIO_DEAD] = True
        self.y_vel = -11
        self.gravity = .5
        self.frame_index = 6
        self.image = self.right_frames[self.frame_index]
        self.state = c.PULO_MORTE
        self.in_transition_state = True


    def changing_to_big(self):
        """===================================================="""
        self.in_transition_state = True

        if self.transition_timer == 0:
            self.transition_timer = self.current_time
        elif self.timer_between_these_two_times(135, 200):
            self.set_mario_to_middle_image()
        elif self.timer_between_these_two_times(200, 365):
            self.set_mario_to_small_image()
        elif self.timer_between_these_two_times(365, 430):
            self.set_mario_to_middle_image()
        elif self.timer_between_these_two_times(430, 495):
            self.set_mario_to_small_image()
        elif self.timer_between_these_two_times(495, 560):
            self.set_mario_to_middle_image()
        elif self.timer_between_these_two_times(560, 625):
            self.set_mario_to_big_image()
        elif self.timer_between_these_two_times(625, 690):
            self.set_mario_to_small_image()
        elif self.timer_between_these_two_times(690, 755):
            self.set_mario_to_middle_image()
        elif self.timer_between_these_two_times(755, 820):
            self.set_mario_to_big_image()
        elif self.timer_between_these_two_times(820, 885):
            self.set_mario_to_small_image()
        elif self.timer_between_these_two_times(885, 950):
            self.set_mario_to_big_image()
            self.state = c.ANDAR
            self.in_transition_state = False
            self.transition_timer = 0
            self.become_big()


    def timer_between_these_two_times(self,start_time, end_time):
        """===================================================="""
        if (self.current_time - self.transition_timer) >= start_time\
            and (self.current_time - self.transition_timer) < end_time:
            return True


    def set_mario_to_middle_image(self):
        """===================================================="""
        if self.facing_right:
            self.image = self.normal_small_frames[0][7]
        else:
            self.image = self.normal_small_frames[1][7]
        bottom = self.rect.bottom
        centerx = self.rect.centerx
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom
        self.rect.centerx = centerx


    def set_mario_to_small_image(self):
        """===================================================="""
        if self.facing_right:
            self.image = self.normal_small_frames[0][0]
        else:
            self.image = self.normal_small_frames[1][0]
        bottom = self.rect.bottom
        centerx = self.rect.centerx
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom
        self.rect.centerx = centerx


    def set_mario_to_big_image(self):
        """===================================================="""
        if self.facing_right:
            self.image = self.normal_big_frames[0][0]
        else:
            self.image = self.normal_big_frames[1][0]
        bottom = self.rect.bottom
        centerx = self.rect.centerx
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom
        self.rect.centerx = centerx


    def become_big(self):
        self.big = True
        self.right_frames = self.right_big_normal_frames
        self.left_frames = self.left_big_normal_frames
        bottom = self.rect.bottom
        left = self.rect.x
        image = self.right_frames[0]
        self.rect = image.get_rect()
        self.rect.bottom = bottom
        self.rect.x = left


    def changing_to_fire(self):
        """===================================================="""
        self.in_transition_state = True

        if self.facing_right:
            frames = [self.right_fire_frames[3],
                      self.right_big_green_frames[3],
                      self.right_big_red_frames[3],
                      self.right_big_black_frames[3]]
        else:
            frames = [self.left_fire_frames[3],
                      self.left_big_green_frames[3],
                      self.left_big_red_frames[3],
                      self.left_big_black_frames[3]]

        if self.fire_transition_timer == 0:
            self.fire_transition_timer = self.current_time
        elif (self.current_time - self.fire_transition_timer) > 65 and (self.current_time - self.fire_transition_timer) < 130:
            self.image = frames[0]
        elif (self.current_time - self.fire_transition_timer) < 195:
            self.image = frames[1]
        elif (self.current_time - self.fire_transition_timer) < 260:
            self.image = frames[2]
        elif (self.current_time - self.fire_transition_timer) < 325:
            self.image = frames[3]
        elif (self.current_time - self.fire_transition_timer) < 390:
            self.image = frames[0]
        elif (self.current_time - self.fire_transition_timer) < 455:
            self.image = frames[1]
        elif (self.current_time - self.fire_transition_timer) < 520:
            self.image = frames[2]
        elif (self.current_time - self.fire_transition_timer) < 585:
            self.image = frames[3]
        elif (self.current_time - self.fire_transition_timer) < 650:
            self.image = frames[0]
        elif (self.current_time - self.fire_transition_timer) < 715:
            self.image = frames[1]
        elif (self.current_time - self.fire_transition_timer) < 780:
            self.image = frames[2]
        elif (self.current_time - self.fire_transition_timer) < 845:
            self.image = frames[3]
        elif (self.current_time - self.fire_transition_timer) < 910:
            self.image = frames[0]
        elif (self.current_time - self.fire_transition_timer) < 975:
            self.image = frames[1]
        elif (self.current_time - self.fire_transition_timer) < 1040:
            self.image = frames[2]
            self.fire = True
            self.in_transition_state = False
            self.state = c.ANDAR
            self.transition_timer = 0


    def changing_to_small(self):
        """===================================================="""
        self.in_transition_state = True
        self.hurt_invincible = True
        self.state = c.GRANDE_PARA_PEQUENO

        if self.facing_right:
            frames = [self.right_big_normal_frames[4],
                      self.right_big_normal_frames[8],
                      self.right_small_normal_frames[8]
                      ]
        else:
            frames = [self.left_big_normal_frames[4],
                      self.left_big_normal_frames[8],
                      self.left_small_normal_frames[8]
                     ]

        if self.transition_timer == 0:
            self.transition_timer = self.current_time
        elif (self.current_time - self.transition_timer) < 265:
            self.image = frames[0]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 330:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 395:
            self.image = frames[2]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 460:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 525:
            self.image = frames[2]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 590:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 655:
            self.image = frames[2]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 720:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 785:
            self.image = frames[2]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 850:
            self.image = frames[1]
            self.hurt_invincible_check()
            self.adjust_rect()
        elif (self.current_time - self.transition_timer) < 915:
            self.image = frames[2]
            self.adjust_rect()
            self.in_transition_state = False
            self.state = c.ANDAR
            self.big = False
            self.transition_timer = 0
            self.hurt_invisible_timer = 0
            self.become_small()


    def adjust_rect(self):
        """===================================================="""
        x = self.rect.x
        bottom = self.rect.bottom
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = bottom


    def become_small(self):
        self.big = False
        self.right_frames = self.right_small_normal_frames
        self.left_frames = self.left_small_normal_frames
        bottom = self.rect.bottom
        left = self.rect.x
        image = self.right_frames[0]
        self.rect = image.get_rect()
        self.rect.bottom = bottom
        self.rect.x = left


    def flag_pole_sliding(self):
        """===================================================="""
        self.state = c.BANDEIRA
        self.in_transition_state = True
        self.x_vel = 0
        self.y_vel = 0

        if self.flag_pole_timer == 0:
            self.flag_pole_timer = self.current_time
        elif self.rect.bottom < 493:
            if (self.current_time - self.flag_pole_timer) < 65:
                self.image = self.right_frames[9]
            elif (self.current_time - self.flag_pole_timer) < 130:
                self.image = self.right_frames[10]
            elif (self.current_time - self.flag_pole_timer) >= 130:
                self.flag_pole_timer = self.current_time

            self.rect.right = self.flag_pole_right
            self.y_vel = 5
            self.rect.y += self.y_vel

            if self.rect.bottom >= 488:
                self.flag_pole_timer = self.current_time

        elif self.rect.bottom >= 493:
            self.image = self.right_frames[10]


    def sitting_at_bottom_of_pole(self):
        """===================================================="""
        if self.flag_pole_timer == 0:
            self.flag_pole_timer = self.current_time
            self.image = self.left_frames[10]
        elif (self.current_time - self.flag_pole_timer) < 210:
            self.image = self.left_frames[10]
        else:
            self.in_transition_state = False
            if self.rect.bottom < 485:
                self.state = c.FIM_DO_NIVEL_QUEDA
            else:
                self.state = c.WALKING_TO_CASTLE


    def set_state_to_bottom_of_pole(self):
        """===================================================="""
        self.image = self.left_frames[9]
        right = self.rect.right
        #self.rect.bottom = 493
        self.rect.x = right
        if self.big:
            self.rect.x -= 10
        self.flag_pole_timer = 0
        self.state = c.BASE_POSTE


    def walking_to_castle(self):
        """===================================================="""
        self.max_x_vel = 5
        self.x_accel = c.ANDAR_ACELERACAO

        if self.x_vel < self.max_x_vel:
            self.x_vel += self.x_accel

        if (self.walking_timer == 0 or (self.current_time - self.walking_timer) > 200):
            self.walking_timer = self.current_time

        elif (self.current_time - self.walking_timer) > \
                self.calculate_animation_speed():
            if self.frame_index < 3:
                self.frame_index += 1
            else:
                self.frame_index = 1
            self.walking_timer = self.current_time


    def falling_at_end_of_level(self, *args):
        """===================================================="""
        self.y_vel += c.GRAVIDADE



    def check_for_special_state(self):
        """===================================================="""
        self.check_if_invincible()
        self.check_if_fire()
        self.check_if_hurt_invincible()
        self.check_if_crouching()


    def check_if_invincible(self):
        if self.invincible:
            if ((self.current_time - self.invincible_start_timer) < 10000):
                self.losing_invincibility = False
                self.change_frame_list(30)
            elif ((self.current_time - self.invincible_start_timer) < 12000):
                self.losing_invincibility = True
                self.change_frame_list(100)
            else:
                self.losing_invincibility = False
                self.invincible = False
        else:
            if self.big:
                self.right_frames = self.right_big_normal_frames
                self.left_frames = self.left_big_normal_frames
            else:
                self.right_frames = self.invincible_small_frames_list[0][0]
                self.left_frames = self.invincible_small_frames_list[0][1]


    def change_frame_list(self, frame_switch_speed):
        if (self.current_time - self.invincible_animation_timer) > frame_switch_speed:
            if self.invincible_index < (len(self.invincible_small_frames_list) - 1):
                self.invincible_index += 1
            else:
                self.invincible_index = 0

            if self.big:
                frames = self.invincible_big_frames_list[self.invincible_index]
            else:
                frames = self.invincible_small_frames_list[self.invincible_index]

            self.right_frames = frames[0]
            self.left_frames = frames[1]

            self.invincible_animation_timer = self.current_time


    def check_if_fire(self):
        if self.fire and self.invincible == False:
            self.right_frames = self.fire_frames[0]
            self.left_frames = self.fire_frames[1]


    def check_if_hurt_invincible(self):
        """===================================================="""
        if self.hurt_invincible and self.state != c.GRANDE_PARA_PEQUENO:
            if self.hurt_invisible_timer2 == 0:
                self.hurt_invisible_timer2 = self.current_time
            elif (self.current_time - self.hurt_invisible_timer2) < 2000:
                self.hurt_invincible_check()
            else:
                self.hurt_invincible = False
                self.hurt_invisible_timer = 0
                self.hurt_invisible_timer2 = 0
                for frames in self.all_images:
                    for image in frames:
                        image.set_alpha(255)


    def hurt_invincible_check(self):
        """===================================================="""
        if self.hurt_invisible_timer == 0:
            self.hurt_invisible_timer = self.current_time
        elif (self.current_time - self.hurt_invisible_timer) < 35:
            self.image.set_alpha(0)
        elif (self.current_time - self.hurt_invisible_timer) < 70:
            self.image.set_alpha(255)
            self.hurt_invisible_timer = self.current_time


    def check_if_crouching(self):
        """===================================================="""
        if self.crouching and self.big:
            bottom = self.rect.bottom
            left = self.rect.x
            if self.facing_right:
                self.image = self.right_frames[7]
            else:
                self.image = self.left_frames[7]
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
            self.rect.x = left


    def animation(self):
        """===================================================="""
        if self.state == c.PULO_MORTE \
            or self.state == c.PEQUENO_PARA_GRANDE \
            or self.state == c.GRANDE_PARA_FOGO \
            or self.state == c.GRANDE_PARA_PEQUENO \
            or self.state == c.BANDEIRA \
            or self.state == c.BASE_POSTE \
            or self.crouching:
            pass
        elif self.facing_right:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image = self.left_frames[self.frame_index]
