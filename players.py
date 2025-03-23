# Importations des modules externes 
import pygame
import sys # Module permettant de fermer la fenetre proprement

# Importations des modules internes  
import lasers

class Joueur:
    
    def __init__(self,window_width,window_height):
        ''' Creation d'un joueur en fonction des meusures de la fenêtre '''
        
        # Importation de l'image de hero
        self.image = pygame.image.load('textures/spaceship.png') # Définition de l'image avec le chemin d'acces
        
        # Initialisation des attributs
        self.boostbattery = 8000 # Batterie de boost de base à 8000 
        self.speed = 10 # Vitesse du joueur à 10
        self.vie = 5 # Vie de base du joueur à 5
        self.score = 0 # Score de base à 0
        self.vague = 0 #Numéro de vague de base à 0 

        self.laserlist = [] # Liste de tout les lasers tirés devant etre mis à jour
        self.dernier_tir = 0 # Attribut pour stocker le temps du dernier tir de laser
        
        # Prise en compte du facteur de taille 
        self.scale_factor = 1.75 # Facteur de taille pouvant être modifié pour un jeu avec des images plus ou moins grosses 
        
        
        # Mise à jour de la taille de l'image avec le scale_factor
        self.rect = self.image.get_rect() # Définition de la hitbox 
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * self.scale_factor*0.075), int(self.rect.height * self.scale_factor*0.075))) # Modification de la taille par 0.075 fois le facteur de taille 

        # Mise à jour de la hitbox après le redimensionnement de l'image avec le scale_factor
        self.rect = self.image.get_rect() # Redéfinition de la hitbox 
        
        # Mise en place des coordonees en fonction de la taille de la fenetre
        self.rect.x = window_width // 2 # Milieux de la page en x
        self.rect.y = window_height // 1.25 # Position y en bas de page 
        
        
    def deplacer(self,window_width,window_height,keys):
        ''' Deplacement et actions possibles par le vaisseau en fonction des mesures de la fenêtre et des touches enfoncée '''
        
        space = keys[pygame.K_SPACE] # Définition de la touche espace
        
        # Definition des touches et des limites de deplacement sur l'ecran
        left = keys[pygame.K_LEFT] and self.rect.x > -25 # Flèche de gauche et limite à x:-25
        right = keys[pygame.K_RIGHT] and self.rect.x < window_width  - 80 # Flèche de droite et limite en x au bout de la page -80
        up = keys[pygame.K_UP] and self.rect.y > -25 # Flèche haut et limite à y:-25
        down = keys[pygame.K_DOWN] and self.rect.y < window_height - 80 # Flèche bas et limite en y au bout de la page -80
        
        maj = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] # Touches maj droite et gauche 
        
        # ACTIONS DE BASE [GAUCHE, DROITE, HAUT, BAS]
        if left and not (up or down): # Deplacement [Gauche] 
            self.rect.x -= self.speed # Déplacement négatif en x 

        elif right and not (up or down): # Deplacement [Droit] 
            self.rect.x += self.speed # Déplacement positif en x 
                
        elif up and not (left or right): # Deplacement [Haut] 
            self.rect.y -= self.speed # Déplacement négatif en y
               
        elif down and not (left or right): # Deplacement [Bas] 
            self.rect.y += self.speed # Déplacement positif en y
            
        # ACTIONS DIAGONALES
        if left and up: # Deplacement [Gauche - Haut] 
            self.rect.x -= self.speed # Déplacement négatif en x 
            self.rect.y -= self.speed # Déplacement négatif en y
            
            
        elif right and up: # Deplacement [Droite - Haut] 
            self.rect.x += self.speed # Déplacement positif en x 
            self.rect.y -= self.speed # Déplacement négatif en y
            
            
        elif left and down: # Deplacement [Gauche - Bas] 
            self.rect.x -= self.speed # Déplacement négatif en x 
            self.rect.y += self.speed # Déplacement positif en y
            
            
        elif right and down: # Deplacement [Droite - Bas]
            self.rect.x += self.speed # Déplacement positif en x 
            self.rect.y += self.speed # Déplacement positif en y
            
            
        # BOOST DE VITESSE OU DE TIR
        if maj and (left or right or up or down) and self.boostbattery > 0 : # Touche boost activée + boost non vide
            self.boostbattery -= 25 # Epuisement du boost de -25
            self.speed = 20 # Vitesse acceleree x2 (de 10 à 20)
        
        if maj and self.boostbattery > 0 and space : # Touche boost activée + boost non vide
            self.boostbattery -= 25 # Epuisement du boost de -25
            self.tirer(1,keys) # Tir acceleree
            
        elif not maj: # Touche boost desactivee
            self.speed = 10 # Retablissement de la vitesse normale
            
        elif self.boostbattery <= 0: # Boost vide
            self.speed = 10 # Retablissement de la vitesse normale


    def retour_milieu(self,window_width,window_height):
        ''' Procède au retour dans un endroit plus sur pour le joueur '''
        self.rect.x = window_width // 2 # Milieux de la page en x
        self.rect.y = window_height // 1.25 # Position y en bas de page 
            
            
    def tirer(self,power,keys):
        ''' Fais en sorte que le joueur puisse tirer avec différents niveaux de puissance, 0,1,2 en appuyant sur la touche espace'''

        space = keys[pygame.K_SPACE] # Définition de la touche espace
        
        laser_sound = pygame.mixer.Sound("sounds/blaster.mp3") # Importation du son de tir laser
        laser_sound.set_volume(0.1) # Ajustement de la hauteur du son
        
        if power == 0: # Si la puissance de tir est de 0 
            if space: # Tir à puissance 0 toujours actif donc si espace pressé

                # Vérification du cooldown entre chaque tir
                temps_actuel = pygame.time.get_ticks() # Définition du temps actuel

                if temps_actuel - self.dernier_tir >= 400:  # 1000 millisecondes = 1 seconde donc 400 millisecondes = 0.4 sec --> Cooldown de 0.4 sec
                    
                    laser = lasers.laser(self.rect.x + self.rect.width//2 , self.rect.y + 10, self.scale_factor) # Création du laser 
                    self.laserlist.append(laser) # Ajout du laser à la liste de tout les lasers tirés à mettre à jour 
                    
                    laser_sound.play() # Son de tir de laser 

                    if temps_actuel - self.dernier_tir < 450: # Son plus bas si serie de tir 
                        laser_sound.set_volume(0.05) 
                    else: # Sinon volume normal
                        laser_sound.set_volume(0.1)
                        
                    self.dernier_tir = temps_actuel  # Mise à jour du temps de dernier tir de laser

        elif power == 1: # Tir de puissance 1 ( Boost utilisé pour tirs + rapides )

             # Vérification du cooldown entre chaque tir
            temps_actuel = pygame.time.get_ticks() # Définition du temps actuel
            if temps_actuel - self.dernier_tir >= 100:  # 1000 millisecondes = 1 seconde donc 100 millisecondes = 0.1 sec --> Cooldown de 0.1 sec
                
                laser = lasers.laser(self.rect.x + 39.5, self.rect.y + 10, self.scale_factor) # Création du laser 
                self.laserlist.append(laser) # Ajout du laser à la liste de tout les lasers tirés à mettre à jour 

                laser_sound.play() # Son de tir de laser 

                self.dernier_tir = temps_actuel  # Mise à jour du temps de dernier tir de laser
                
                
        elif power == 2: # Tir de puissance 2 ( Cheat activés )
            if space: # Tir à puissance 2 toujours actif donc si espace pressé

                laser = lasers.laser(self.rect.x + 39.5, self.rect.y + 10, self.scale_factor) # Création du laser 
                self.laserlist.append(laser) # Ajout du laser à la liste de tout les lasers tirés à mettre à jour     

                laser_sound.play() # Son de tir de laser 
            
    def perdre_vie(self, points):
        ''' Le joueur perd le nombre de vie indiqué par 'points' '''
        
        self.vie -= points # Reduction du nombre de vie indiqué par 'points' 
        
    def quitter(self):
        ''' Fermeture de programme sur demande '''
        pygame.quit() # Fermeture de la fenêtre pygame 
        sys.exit() # Fin propre du programme 
