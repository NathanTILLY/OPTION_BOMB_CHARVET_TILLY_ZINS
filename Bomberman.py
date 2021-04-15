import pygame
from pygame.locals import *

from constantes import *
from classes import *

pygame.display.init()

fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
pygame.display.set_caption(titre_fenetre)

continuer = 1

while continuer:

    accueil = pygame.image.load(image_accueil).convert()
    fenetre.blit(accueil, (0, 0))

    pygame.display.flip()

    continuer_jeu = 1
    continuer_accueil = 1

    while continuer_accueil:

        pygame.time.Clock().tick(30)

        choix = 0

        for event in pygame.event.get():

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0

            elif event.type == KEYDOWN and event.key == K_SPACE:
                continuer_accueil = 0
                choix = "n1"

    if choix != 0:

        niveau = Niveau("level.txt")
        niveau.generer()
        niveau.afficher(fenetre)

        perso = Perso(p1_droite, p1_gauche, p1_haut, p1_bas, niveau)

        bombe = Bomb(image_bombe, niveau, perso)

    while continuer_jeu:

        pygame.time.Clock().tick(20)

        for event in pygame.event.get():
            if event.type == QUIT:
                continuer_jeu = 0
                continuer = 0

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continuer_jeu = 0
                if event.key == K_SPACE:
                    bombe.poser(perso.x, perso.y, image_bombe)

                elif event.key == K_RIGHT:
                    perso.deplacer("droite")
                elif event.key == K_LEFT:
                    perso.deplacer("gauche")
                elif event.key == K_DOWN:
                    perso.deplacer("bas")
                elif event.key == K_UP:
                    perso.deplacer("haut")

        niveau.afficher(fenetre)
        fenetre.blit(perso.direction, (perso.x, perso.y))
        fenetre.blit(bombe.bomb, (bombe.x, bombe.y))

        pygame.display.flip()