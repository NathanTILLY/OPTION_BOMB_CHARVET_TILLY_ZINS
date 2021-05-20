import pygame
from pygame.locals import *
from datetime import datetime, timedelta

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
        perso2 = Perso2(p2_droite, p2_gauche, p2_haut, p2_bas, niveau)

        bombe = Bomb(image_bombe, niveau, perso, perso2)
        bombe2 = Bomb(image_bombe2, niveau, perso, perso2)

        flamme = Flammes(flamme_d, flamme_g, flamme_h, flamme_b)

    while continuer_jeu:

        pygame.time.Clock().tick(20)

        for event in pygame.event.get():
            if event.type == QUIT:
                continuer_jeu = 0
                continuer = 0

            #retour au menu
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continuer_jeu = 0
                if event.key == K_SPACE:
                    if bombe.autoriser_poser():
                        bombe.poser(perso.x, perso.y, image_bombe)

            #commandes J1

                elif event.key == K_RIGHT:
                    perso.deplacer("droite")
                elif event.key == K_LEFT:
                    perso.deplacer("gauche")
                elif event.key == K_DOWN:
                    perso.deplacer("bas")
                elif event.key == K_UP:
                    perso.deplacer("haut")

            # touches de perso2

                if event.key == K_e:
                    bombe2.poser(perso2.x, perso2.y, image_bombe)
                elif event.key == K_d:
                    perso2.deplacer("droite")
                elif event.key == K_q:
                    perso2.deplacer("gauche")
                elif event.key == K_s:  
                    perso2.deplacer("bas")
                elif event.key == K_z:
                    perso2.deplacer("haut")

        niveau.afficher(fenetre)
        fenetre.blit(perso.direction, (perso.x, perso.y))
        fenetre.blit(perso2.direction, (perso2.x, perso2.y))
        fenetre.blit(bombe.bomb, (bombe.x, bombe.y))
        fenetre.blit(bombe2.bomb, (bombe2.x, bombe2.y))

        if bombe.explosion == 1:
            fenetre.blit(flamme.fflamme_b, (bombe.x, bombe.y + taille_sprite))
            fenetre.blit(flamme.fflamme_h, (bombe.x, bombe.y - taille_sprite))
            fenetre.blit(flamme.fflamme_g, (bombe.x - taille_sprite, bombe.y))
            fenetre.blit(flamme.fflamme_d, (bombe.x + taille_sprite, bombe.y))

        if bombe2.explosion == 1:
            fenetre.blit(flamme.fflamme_b, (bombe2.x, bombe2.y + taille_sprite))
            fenetre.blit(flamme.fflamme_h, (bombe2.x, bombe2.y - taille_sprite))
            fenetre.blit(flamme.fflamme_g, (bombe2.x - taille_sprite, bombe2.y))
            fenetre.blit(flamme.fflamme_d, (bombe2.x + taille_sprite, bombe2.y))

        pygame.display.flip()

        game_over = bombe.exploser()
        if game_over == 1:
            continuer_jeu = 0
            print("game over")
        game_over = bombe2.exploser()
        if game_over == 1:
            continuer_jeu = 0
            print("game over")