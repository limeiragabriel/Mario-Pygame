ALTURA_TELA = 600
LARGURA_TELA = 800

TAMANHO_TELA = (LARGURA_TELA,ALTURA_TELA)

LEGENDA = "Super Mario Bros" #ORIGINAL_CAPTION

############# CORES #############
#                  R    G    B
CINZA          = (100, 100, 100)
AZULMARINHO    = ( 60,  60, 100)
BRANCO         = (255, 255, 255)
VERMELHO       = (255,   0,   0)
VERDE          = (  0, 255,   0)
VERDE_FLORESTA = ( 31, 162,  35)
AZUL           = (  0,   0, 255)
AZUL_CEU       = ( 39, 145, 251)
AMARELO        = (255, 255,   0)
LARANJA        = (255, 128,   0)
PURPURA        = (255,   0, 255)
CYAN           = (  0, 255, 255)
PRETO          = (  0,   0,   0)
NEAR_BLACK     = ( 19,  15,  48)
COMBLUE        = (233, 232, 255)
OURO           = (255, 215,   0)

COR_DO_FUNDO = BRANCO

MULTILICADOR_TAMANHO       = 2.5
MULTILICADOR_TAMANHO_BLOCO = 2.69
MULTIPLICADOR_FUNDO        = 2.679
ALTURA_CHAO                = ALTURA_TELA - 62

####  MARIO #######
ANDAR_ACELERACAO  = .15
CORRER_ACELERACAO = 20
PEQUENO_GIRAR     = .35

GRAVIDADE              = 1.01
GRAVIDADE_PULO         = .31
VELOCIDADE_PULO        = -11
PULO_RAPPIDO_VEOCIDADE = -12.5
MAX_Y_VEL       = 11

MAX_CORRER_VELOCIDADE  = 800
MAX_ANDAR_VELOCIDADE   = 6


#MARIO ESTADOS

PARADO                = 'standing'
ANDAR                 = 'walk'
PULO                  = 'jump'
QUEDA                 = 'fall'
PEQUENO_PARA_GRANDE   = 'small to big'
GRANDE_PARA_FOGO      = 'big to fire'
GRANDE_PARA_PEQUENO   = 'big to small'
BANDEIRA              = 'flag pole'
WALKING_TO_CASTLE     = 'walking to castle'
FIM_DO_NIVEL_QUEDA    = 'end of level fall'


#GOOMBA

ESQUERDA    = 'left'
DIREITA     = 'right'
SALTO       = 'jumped on'
PULO_MORTE  = 'death jump'

#KOOPA

CASCO_DESLIZE = 'shell slide'

#BLOCO STATES

INERTE    = 'resting'
ATINGIDO  = 'bumped'

#MOEDA STATES
ABERTO  = 'opened'
SPIN    = 'spin'
#COGUMELO STATES

REVELAR   = 'reveal'
DESLIZAR  = 'slide'

#ESTRELA STATES

BOUNCE = 'bounce'

#FOGO STATES

VOANDO    = 'flying'
BOUNCING  = 'bouncing'
EXLODINDO = 'exploding'

#BLOCO E CAIXA DE MOEDA - CONTEUDO

COGUMELO        = 'mushroom'
ESTRELA         = 'star'
FLOR_DE_FOGO    = 'fireflower'
SEIS_MOEDAS     = '6coins'
MOEDA           = 'coin'
VIDA_COGUMELO   = '1up_mushroom'

BOLA_FOGO      = 'fireball'

#INIMIGOS

GOOMBA = 'goomba'
KOOPA = 'koopa'

#ESTADO DOS NIVEIS

CONGELADO          = 'frozen'
NAO_CONGELADO      = 'not frozen'
NO_CASTELO         = 'in castle'
BANDEIRA_E_FOGOS   = 'flag and fireworks'

#ESTADO BANDEIRA
TOPO_POSTE          = 'top of pole'
DESLIZAR_PARA_BAIXO = 'slide down'
BASE_POSTE          = 'bottom of pole'

#1UP
ONE_UP = '379'

#MAIN MENU
PLAYER1 = '1 player'
PLAYER2 = '2 player'

#INFORMACAO GERAL
MENU_PRINCIAL         = 'main menu'
TELA_CARREGAMENTO     = 'loading screen'
LEVEL                 = 'level'
GAME_OVER             = 'game over'
CONTAGEM_REGRESSIVA   = 'fast count down'
END_OF_LEVEL          = 'end of level'


#DICTIONARY KEYS
TOTAL_MOEDAS         = 'coin total'
PONTOS               = 'score'
MAIOR_PONTUACAO      = 'top score'
VIDAS                = 'lives'
TEMPO_ATUAL          = 'current time'
ESTADO_NIVEL         = 'level state'
CAMERA_START_X       = 'camera start x'
MARIO_DEAD           = 'mario dead'

#ESTADOS PARA todo O JOGO
MAIN_MENU    = 'main menu'
LOAD_SCREEN  = 'load screen'
TIME_OUT     = 'time out'
GAME_OVER    = 'game over'
LEVEL1       = 'level1'

#ESTADOS SOM
NORMAL           = 'normal'
STAGE_CLEAR      = 'stage clear'
WORLD_CLEAR      = 'world clear'
TIME_WARNING     = 'time warning'
SPED_UP_NORMAL   = 'sped up normal'
MARIO_INVINCIBLE = 'mario invincible'
