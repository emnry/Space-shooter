# Importations de modules
import pygame
import random
import math

class opponent():
    def __init__(self, x, y, scale_factor, ennemistype, comportement):
        ''' Definition de l'ennemi en fonction de son type, du facteur de taille utilisé dans tout le jeu, de son comportement et des coordonnées x ; y '''
        
        self.comportement = comportement # Attribution à l'ennemi de son comportement donné
        self.type = ennemistype # Attribution à l'ennemi de son type donné
        
        # ASTERIODE
        if self.type == 'asteriod': # Si l'ennemi est un asteriode
            
            texture = random.randint(0,11) # Definition du nombre de la texture au hasard entre les 12 textures disponibles pour un astériode
            image_path = "textures/asteriods/asteriod" + str(texture) + ".png" # Création du chemin d'accès de la texture
            self.image = pygame.image.load(image_path) # Definition de l'image asteriode
            
            self.vie = 2 # Definition de la vie d'un asteriod à 2 
            
            if self.comportement == 0: # Comportement 0 --> Asteriode normal
                self.vitesse = 1  # Vitesse de déplacement par defaut de l'asteriod
                self.giveboost = 0 # L'astériode ne donnera pas de boost au joueur à sa mort 
                
            elif self.comportement == 1: # Comportement 1 --> Asteriode rapide
                  self.vitesse = 2  # Vitesse de déplacement rapide de l'asteriod
                  self.giveboost = 1 # L'astériode donnera du boost au joueur à sa mort 
                  
                  
        # ADVERSAIRE DU ROYAUME DES PLANTES  
        elif self.type == 'plant_opponent': # Si l'ennemi est un plant_opponent
        
            texture = random.randint(1,4) # Definition du nombre de la texture au hasard entre les 4 textures disponibles pour un plant_opponent
            image_path = 'textures/opponents/plant_opponent_' + str(texture) + '.png' # Création du chemin d'accès de la texture
            self.image = pygame.image.load(image_path) # Definition de l'image d'un ennemi 'plant_opponent'
            
            self.vie = 2 # Definition de la vie de l'ennemi
            self.vitesse = 10  # Definition de la vitesse de l'ennemi
            
            giveboost = random.randint(1,20) # Un plant_opponent sur 20 donnera du boost

            if giveboost == 1: # Si l'ennemi à eu 1 chance sur 20 de donner du boost 
                self.giveboost = 1 # L'ennemi donnera du boost au joueur à sa mort 
            else: # Sinon 
                self.giveboost = 0 # L'ennemi ne donnera pas de boost au joueur à sa mort 
                        
        
        # ADVERSAIRE DU ROYAUME DE FEU  
        elif self.type == 'fire_opponent': # Si l'ennemi est un fire_opponent
            
            texture = random.randint(1,5) # Definition du nombre de la texture au hasard entre les 5 textures disponibles pour un fire_opponent
            image_path = 'textures/opponents/fire_opponent_' + str(texture) + '.png' # Création du chemin d'accès de la texture
            self.image = pygame.image.load(image_path) # Definition de l'image d'un ennemi 'fire_opponent'
            
            self.vitesse = 1 # Definition de la vitesse de l'ennemi
            self.vie = 5 # Definition de la vie de l'ennemi
            
            
        # ADVERSAIRE DU ROYAUME DE ROCHE  
        elif self.type == 'rock_opponent': # Si l'ennemi est un rock_opponent
            
            texture = random.randint(1,4) # Definition du nombre de la texture au hasard entre les 4 textures disponibles pour un rock_opponent
            image_path = 'textures/opponents/rock_opponent_' + str(texture) + '.png' # Création du chemin d'accès de la texture
            self.image = pygame.image.load(image_path) # Definition de l'image des enemis 'rock_opponent'
            
            self.vitesse = 5 # Definition de la vitesse de l'ennemi
            self.vie = 5 # Definition de la vie de l'ennemi
        
        # ADVERSAIRE DU ROYAUME DE L'EAU  
        elif self.type == 'water_opponent':
            
            texture = random.randint(1,4) # Definition du nombre de la texture au hasard entre les 4 textures disponibles pour un water_opponent
            image_path = 'textures/opponents/water_opponent_' + str(texture) + '.png' # Création du chemin d'accès de la texture
            self.image = pygame.image.load(image_path) # Definition de l'image des enemis 'water_opponent'
        
            self.vitesse = 1 # Definition de la vitesse de l'ennemi
            self.vie = 1 # Definition de la vie de l'ennemi
        
        elif self.type == 'troll_opponent':
            
            texture = random.randint(1,4) # Definition du nombre de la texture au hasard entre les 4 textures disponibles pour un troll_opponent
            image_path = 'textures/opponents/troll_opponent_' + str(texture) + '.png' # Création du chemin d'accès de la texture
            self.image = pygame.image.load(image_path) # Definition de l'image des enemis 'troll_opponent'
            
            self.vitesse = 1 # Definition de la vitesse de l'ennemi
            self.vie = random.randint(3,10) # Definition de la vie d'un troll 
            
        elif self.type == 'demon_boss_opponent':
            
            texture = random.randint(1,4) # Definition du nombre de la texture au hasard entre les 4 textures disponibles pour un demon_boss_opponent
            image_path = 'textures/opponents/demon_boss_opponent_' + str(texture) + '.png' # Création du chemin d'accès de la texture
            self.image = pygame.image.load(image_path) # Definition de l'image des enemis 'demon_boss_opponent'
            
            
            if self.comportement == 'main_boss': # Si son comportement est main_boss (boss principal)
                self.vie = 10 # Definition de la vie du boss principal
                
                self.vitesse = 1

                scale_factor *= 2 # Agrandir encore + le boss principal
                self.type = 'main_boss' # Changement de type sans pour autant définir de nouveau un type car les textures sont les mêmes 
                
            elif self.comportement == 0:
                self.vie = 4 # Definition de la vitesse d'un boss
                self.vitesse = 4 # Definition de la vie d'un boss 
                
        else: # Sinon --> Erreur de syntaxe
            raise SyntaxError
        
        self.rect = self.image.get_rect() # Définition de la hitbox de l'ennemi
        self.rect.x = x # Deplacement de l'entité dans l'axe x 
        self.rect.y = y # Deplacement de l'entité dans l'axe x 
        
        # Agrandissement de l'image en fonction du facteur de taille 
        self.scale_factor = scale_factor
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * self.scale_factor), int(self.rect.height * self.scale_factor)))

        # Mise à jour de la hitbox après le redimensionnement de l'image avec le scale_factor
        self.rect.width = int(self.rect.width * self.scale_factor)
        self.rect.height = int(self.rect.height * self.scale_factor)
        
        
        self.marquer_a_supprimer = False # Marquage "à supprimer" permettant de supprimer l'entité sans bug quand il meurt

            
    def display(self, window):
        ''' Affichage de l'entité dans la fenetre pygame '''
        
        window.blit(self.image, self.rect) # Simple affichage de l'entité
        
    def move(self, joueur_rect,window_width,window_height):
        ''' Déplacement de l'entité en fonction de son type, peut nécessiter la position du joueur et les mesures de la fenêtre '''
        

        # DEPLACEMENT DE L'ENTITE 'ASTERIOD'
        if self.type == 'asteriod': # Type d'ennemi = asteriode 
            self.move_to_player(joueur_rect) # Déplacement vers le joueur 
        

        # DEPLACEMENT DE L'ENTITE 'PLANT_OPPONENT' 
        elif self.type == 'plant_opponent': # Type d'ennemi = ennemi - plante 
            
            # Déplacement en l'axe y 
            if self.comportement == 1: # Si comportement 1 

                if self.rect.y < window_height - 50 : # Si le bas de la fenêtre n'est pas atteint 
                    self.rect.y += self.vitesse # Déplacement positif en y 
                else: # Sinon 
                    self.comportement = 0 # Changement de comportement 
                    
            elif self.comportement == 0: # Si comportement 0
            
                if self.rect.y > 0: # Si le haut de la fenêtre n'est pas atteint 
                    self.rect.y -= self.vitesse # Déplacement négatif en y 
                else: # Sinon 
                    self.comportement = 1 # Changement de comportement 
            
            # Déplacement en l'axe x
            diff_x = joueur_rect.x - self.rect.x # Calcul de la difference entre la position x du joueur et celle de l'ennemi
            
            if diff_x < 0 : # Si l'ennemi est à droite du joueur 
                self.rect.x -= 1 # Il se rapproche en allant à gauche
            elif diff_x > 0: # Si l'ennemi est à gauche du joueur 
                self.rect.x += 1 # Il se rapproche en allant à droite
        

        # DEPLACEMENT DE L'ENTITE 'FIRE_OPPONENT' 
        elif self.type == 'fire_opponent': # Type d'ennemi = ennemi - feu 

            if self.comportement == 0: # Si comportement 0
                if self.rect.y < window_height - 50 : # Si le bas de la fenêtre n'est pas atteint 
                    self.rect.y += self.vitesse # Deplacement positif en y 
                else: # Sinon
                    self.comportement = 1 # Comportement 1 

            elif self.comportement == 1: # Si comportement 1 
                self.move_to_player(joueur_rect) # Deplacement vers joueur 
                

        # DEPLACEMENT DE L'ENTITE 'ROCK_OPPONENT'  
        elif self.type == 'rock_opponent': # Type d'ennemi = ennemi - roche 

            if self.comportement == 0: # Si comportement 0
                if self.rect.x < window_width -75 : # Si la limite à droite de la fenêtre n'est pas atteint 
                    self.rect.x += self.vitesse # Deplacement positif en x 
                else: # Sinon 
                    self.comportement = 1 # Changement de comportement 
                
            elif self.comportement == 1: # Si comportement 1
                if self.rect.x > 0 : # Si la limite à gauche de la fenêtre n'est pas atteint 
                    self.rect.x -= self.vitesse # Deplacement negatif en x 
                else: # Sinon
                    self.comportement = 0 # Changement de comportement 


        # DEPLACEMENT DE L'ENTITE 'WATER_OPPONENT'            
        elif self.type == 'water_opponent': # Type d'ennemi = ennemi - eau 
            
            self.move_to_player(joueur_rect) # Deplacement vers le joueur 
            self.vitesse *= 1.00125 # Acceleration minime de la vitesse 
        

        # DEPLACEMENT DE L'ENTITE 'TROLL_OPPONENT'      
        elif self.type == 'troll_opponent': # Type d'ennemi = ennemi - troll 
            
            if self.comportement == 0: # Si comportement 0
                self.objectifx = random.randint(0, window_width) # Creation d'un objectif de coordonnée aleatoire x 
                self.objectify = random.randint(0, window_height) # Creation d'un objectif de coordonnée aleatoire y
                self.comportement = 1 # Changement de comportement 
                    
            elif self.comportement == 1: # Si comportement 1
                
                # Calcul de la différence entre les coordonnées x et y de l'objectif et du troll
                diff_x = self.objectifx - self.rect.x
                diff_y = self.objectify - self.rect.y
                    
                # Calcul de l'angle entre l'ennemi et l'objectif en utilisant la fonction atan2
                angle = math.atan2(diff_y, diff_x)
                    
                # Calcul des composantes x et y de la vitesse en utilisant l'angle
                vitesse_x = self.vitesse * math.cos(angle)
                vitesse_y = self.vitesse * math.sin(angle)
                    
                # Mise à jour de la position et du troll en fonction de la vitesse calculée
                self.rect.x += vitesse_x 
                self.rect.y += vitesse_y
            
                if self.rect.x == self.objectifx and self.rect.y == self.objectify: # Si coordonées de l'objectif atteintes 
                    self.comportement = 0 # Changement de comportement 
                    
            elif self.comportement == 2: # Si comportement 2 
                self.move_to_player(joueur_rect) # Deplacement vers le joueur 
                
            self.vie -= 0.005 # Vie diminue petit à petit quand le troll se déplace 
            
        # DEPLACEMENT DE L'ENTITE 'DEMON_BOSS_OPPONENT'      
        elif self.type == 'demon_boss_opponent': # Type d'ennemi = ennemi - boss - demon 
 
            if self.comportement == 0: # Si comportement 0
                self.objectifx = random.randint(0, window_width) # Creation d'un objectif de coordonnée aleatoire x 
                self.objectify = random.randint(0, window_height) # Creation d'un objectif de coordonnée aleatoire y
                self.comportement = 1 # Changement de comportement 
                    
            elif self.comportement == 1: # Si comportement 1
                
                # Calcul de la différence entre les coordonnées x et y de l'objectif et du troll
                diff_x = self.objectifx - self.rect.x
                diff_y = self.objectify - self.rect.y
                    
                # Calcul de l'angle entre l'ennemi et l'objectif en utilisant la fonction atan2
                angle = math.atan2(diff_y, diff_x)
                    
                # Calcul des composantes x et y de la vitesse en utilisant l'angle
                vitesse_x = self.vitesse * math.cos(angle)
                vitesse_y = self.vitesse * math.sin(angle)
                    
                # Mise à jour de la position et du troll en fonction de la vitesse calculée
                self.rect.x += vitesse_x 
                self.rect.y += vitesse_y
            
                if abs(self.rect.x - self.objectifx) < 5 and abs(self.rect.y - self.objectify) < 5: # Si coordonées de l'objectif approximativement atteintes (peut causé des bugs de déplacement sinon) 
                    self.comportement = 2 # Changement de comportement 
            
            elif self.comportement == 2: # Si comportement 2 
                self.move_to_player(joueur_rect) # Deplacement vers le joueur 
            
        # DEPLACEMENT DE L'ENTITE 'MAIN_BOSS'      
        elif self.type == 'main_boss': # Type d'ennemi = boss principal
            self.move_to_player(joueur_rect) # Déplacement vers le joueur 


    def move_to_player  (self,joueur_rect):
        ''' Calcul du deplacement et deplacement du joueur en fonction des poitions x et y du joueur et de l'ennemi '''
        
        # Calcul de la différence entre les coordonnées x et y du joueur et de l'ennemi
        diff_x = joueur_rect.x - self.rect.x
        diff_y = joueur_rect.y - self.rect.y
        
        # Calcul de l'angle entre l'ennemi et le joueur en utilisant la fonction atan2
        angle = math.atan2(diff_y, diff_x)
        
        # Calcul des composantes x et y de la vitesse en utilisant l'angle
        vitesse_x = self.vitesse * math.cos(angle)
        vitesse_y = self.vitesse * math.sin(angle)
        
        # Mise à jour de la position de l'ennemi en fonction de la vitesse calculée
        self.rect.x += vitesse_x
        self.rect.y += vitesse_y
        
   
    def perdre_vie(self, points):
        
        ''' L'ennemi perd de la vie '''
        
        self.vie -= points # Perte de la vie indiqué par points 

        if self.type == 'troll_opponent': # Type d'ennemi = ennemi - troll 
            self.vitesse += 10 # Gain de vitesse 
            self.comportement = 2 # Changement de comportement (Déplacement vers joueur) 
        
        if self.type == 'fire_opponent': # Type d'ennemi = ennemi - feu 
            self.comportement = 1 # Changement de comportement (Déplacement vers joueur) 
            self.vitesse = 5 # Gain de vitesse 
        
        elif self.type == 'rock_opponent': # Type d'ennemi = ennemi - roche 
            self.vitesse += 4.5 # Gain de vitesse 

            if self.comportement == 1: 
                self.comportement = 0 # Changement de direction
            else:
                self.comportement = 1 # Changement de direction        
        

    

