import pygame
from pygame.locals import *
from constantes import *
from datetime import datetime

class Niveau:
    """class de l'ffichage du terrain"""
    def __init__(self, fichier):
        """initialisation des variables de la class"""
        self.fichier = fichier
        self.structure = [[]]

    def generer(self):
        with open(self.fichier, "r") as fichier:
            structure_niveau = []
            for ligne in fichier:
                ligne_niveau = []
                for sprite in ligne:
                    if sprite != "\n":
                        ligne_niveau.append(sprite)
                structure_niveau.append(ligne_niveau)
            self.structure = structure_niveau

    def afficher(self, fenetre):
        bloc_destructible = pygame.image.load(image_bloc_destructible)
        bloc_indestructible = pygame.image.load(image_bloc_indestructible)
        sol = pygame.image.load(image_sol)

        num_ligne = 0
        for ligne in self.structure:
            num_case = 0
            for sprite in ligne:
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite

                if sprite == "p":
                    fenetre.blit(bloc_indestructible, (x, y))
                elif sprite == "s":
                    fenetre.blit(sol, (x, y))
                elif sprite == "b":
                    fenetre.blit(bloc_destructible, (x, y))
                num_case += 1
            num_ligne += 1

class Perso:

    def __init__(self, droite, gauche, haut, bas, niveau):

        self.droite = pygame.image.load(droite).convert()
        self.droite.set_colorkey((255, 255, 255))
        self.gauche = pygame.image.load(gauche).convert()
        self.gauche.set_colorkey((255, 255, 255))
        self.haut = pygame.image.load(haut).convert()
        self.haut.set_colorkey((255, 255, 255))
        self.bas = pygame.image.load(bas).convert()
        self.bas.set_colorkey((255, 255, 255))

        self.case_x = 1
        self.case_y = 1
        self.x = taille_sprite * self.case_x
        self.y = taille_sprite * self.case_y

        self.direction = self.droite
        self.niveau = niveau

    def deplacer(self, direction):

        if direction == "droite":

            if self.case_x < (nombre_sprite_cote - 1):

                if self.niveau.structure[self.case_y][self.case_x + 1] == "s":

                    self.case_x += 1

                    self.x = self.case_x * taille_sprite

            self.direction = self.droite

        if direction == "gauche":
            if self.case_x > 0:
                if self.niveau.structure[self.case_y][self.case_x - 1] == "s":
                    self.case_x -= 1
                    self.x = self.case_x * taille_sprite
            self.direction = self.gauche

        if direction == "haut":
            if self.case_y > 0:
                if self.niveau.structure[self.case_y - 1][self.case_x] == "s":
                    self.case_y -= 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.haut

        if direction == "bas":
            if self.case_y < (nombre_sprite_cote - 1):
                if self.niveau.structure[self.case_y + 1][self.case_x] == "s":
                    self.case_y += 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.bas


class Bomb:

    def __init__(self, bomb, niveau, perso1):

        self.bomb = pygame.image.load(bomb).convert()

        self.x = 640
        self.y = 640
        self.case_x = 255
        self.case_y = 255
        self._time_created = datetime.now()

        self.niveau = niveau
        self.perso1 = perso1
        self.explosion = 0

    def poser(self, x, y, bomb):
        self.bomb = pygame.image.load(bomb).convert()
        self.bomb.set_colorkey((255, 255, 255))
        self.x = x
        self.y = y
        self.case_x = int(x / taille_sprite)
        self.case_y = int(y / taille_sprite)
        self._time_created = datetime.now()
        self.explosion = 0
