# Importations de modules
import pygame

class laser:
    
    def __init__(self, x, y, scale_factor):
        ''' Definition des lasers en fonction du facteur de taille utilisé dans tout le jeu et des coordonnées x ; y '''
        
        self.image = pygame.image.load("textures/laser.png")  # Importation de l'image du laser
        
        self.scale_factor = scale_factor
        self.rect = self.image.get_rect() # Définition de la hitbox du laser
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * self.scale_factor), int(self.rect.height * self.scale_factor)))
        
        # Mise à jour de la hitbox après le redimensionnement de l'image avec le scale_factor
        self.rect = self.image.get_rect()
        
        self.rect.x = x - self.rect.width//2 # Deplacement de l'entité dans l'axe x 
        self.rect.y = y # Deplacement de l'entité dans l'axe x 
        
        self.vitesse = 20  # Vitesse de déplacement du laser
        
        
      
    def deplacer(self):
        ''' Deplacement du laser en axe y, vitesse de plus en plus rapide '''
        self.rect.y -= self.vitesse  # Déplacement vers le haut
        self.vitesse += 2 

    def afficher(self, window):
        ''' Affichage de l'entité dans la fenetre pygame '''
        window.blit(self.image, self.rect) # Simple affichage de l'entité
        
    
    def __del__(self):
        ''' Suppression de l'entité laser '''
        pass # pass pour pas de crash du programme 
    
    
