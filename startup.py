# Importations des modules externes 
import pygame
import random

# Importations des modules internes     
import players
import opponents
import cutscenes

# INITIALISATION DE LA FENETRE ------------------------------------------------------------

pygame.quit() # Fermeture pour lancement propre, sinon peu causer des bugs
pygame.init() # Initialisation de pygame 

pygame.display.set_caption('Space Invader') # Changement du titre de la page pour 'Space Invader'

# Stockage des variables de la taille de la fenetre sous 'window_width' et 'window_height'
window_width = pygame.display.Info().current_w - 150
window_height = pygame.display.Info().current_h - 150

# INITIALISATION DES BRUITAGES ------------------------------------------------------------

pygame.mixer.init() # Initialisation du module son de pygame 

# Définition des sons 
hit_sound = pygame.mixer.Sound("sounds/hit.wav") # Importation du son de touché
collide_sound = pygame.mixer.Sound("sounds/collide.mp3") # Importation du son de collision avec le joueur 
elimination_sound = pygame.mixer.Sound("sounds/elimination.mp3") # Importation du son d'elimination d'ennemis
wave_passed_sound = pygame.mixer.Sound("sounds/wave_passed.wav") # Importation du son de victoire d'une vague

# Ajustement du sons 
hit_sound.set_volume(0.2) # Ajustement de la hauteur du son
collide_sound.set_volume(0.3) # Ajustement de la hauteur du son
elimination_sound.set_volume(0.3) # Ajustement de la hauteur du son
wave_passed_sound.set_volume(0.3) # Ajustement de la hauteur du son

def play():    
    ''' Lancement d'une partie, cette fonction peut s'appeller elle même pour relancer après avoir perdu '''
    
    # PARAMETRES CHANGEABLES ------------------------------------------------------
    
    # Affichage des contour de zones de collisions
    toggle_hitbox = False
    
    # Activation des cinématiques 
    toggle_cutscenes = True
    
    # Vagues d'attaques aléatoires 
    randomwave = False
    
    # Decider de la prochaine vague
    toggle_next_wave = False
    next_wave = ['demon_boss_opponent']
    
    # Mode dieu ( triche --> pas d'enregistrement de meilleur score )
    toggle_godmode = False
     
    # Mode lasers illimités ( triche --> pas d'enregistrement de meilleur score )
    toggle_cheat = False

    # INITIALISATION DU JEU -------------------------------------------------------
    
    # Définition de l'arrière plan 
    background = pygame.image.load('textures/background.png') # Chargement de l'image 'background.png'
    background = pygame.transform.scale(background, (window_width ,  window_height)) # Mise en forme de l'image 'background.png' pour prendre toute la fenetre 
    
    # Définition de la fenêtre et du joueur 
    window = pygame.display.set_mode((window_width, window_height)) # Définition de la fenetre
    player = players.Joueur(window_width,window_height) # Définition du joueur 'player'  
    
    # Listes de stockages d'objets à charger 
    cutscenes_list = [] # Stockage des cinematiques à charger 
    opponent_list = [] # Stockage des ennemis à charger 
    
    # Vagues d'attaques
    waves_list = ['asteriods','troll_opponent','fire_opponent','water_opponent','rock_opponent','plant_opponent','demon_boss_opponent'] # Stockage des vagues sous une liste pour ne pas avoir de répétition de la même vague de suite
    save_waves_list = waves_list # Sauvegarde de la liste de toutes les vagues 
    
    # VARIABLE DE JEU
    is_gameover = False # Parametre établissant la fin du jeu 'Game OVER' 
    running = True # Variable pour laisser la fenêtre ouverte
    
    # Passage de cinématique 
    font = pygame.font.Font(None, 36)  # Creation d'une police de texte taille 36
    press_1 = font.render("Press [ 1 ]", True, 'white') # Creation du texte passage de cinématique 
    
    cheat_texte = font.render("Cheats enabled", True, 'white') # Creation du texte triche activée
    
    meilleur_score = 0 # Si le fichier meilleur_score est vide, il se met à 0 
    
    # Vérifier si le fichier de meilleur score existe
    try:
        with open("meilleur_score.txt", "r") as file:
            contenu_fichier = file.read()
            if contenu_fichier.strip():  # Vérifiez si la chaîne n'est pas vide après suppression des espaces
                meilleur_score = int(contenu_fichier)
            else:
                print("Le fichier de meilleur score est vide.")
                
    except FileNotFoundError:
        print("Fichier meilleur_score.txt introuvable. Un nouveau fichier sera créé.")
    except ValueError:
        print("Le fichier de meilleur-score.txt contient une valeur non valide.")
        
    # LANCEMENT DU JEU ------------------------------------------------------------
    
    while running: # Boucle toujours active durant le lancement du jeu 
        
        keys = pygame.key.get_pressed() # Stockage des touches sous un élément 'keys'
        
        # FERMETURE DU JEU ------------------------------------------------------------
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]: # Si touches fermeture de la fenêtre pressée ou touche 'echap' enfoncée
                running = False # Fermeture de la fenêtre
                player.quitter() # Fermeture du jeu sous la méthode .quitter() de la classe Joueur
        
        # LANCEMENT DU JEU EN FONCTION DES CINEMATIQUES ------------------------------------------------------------
        
        if opponent_list == [] and toggle_cutscenes: # Plus d'ennemis + cinématiques activées
            cutscene_in_progress = True # Cinematique en cours 
        
        if toggle_cutscenes and cutscene_in_progress: # Cinématiques activées + une cinématique en cours
            lancement = False # Pas de lancement du jeu ( Joueur ne se deplacera pas et ennemis n'apparaissent pas )
        
        elif toggle_cutscenes and not cutscene_in_progress: # Cinématiques activées mais pas de cinématique en cours
            lancement = True # Lancement du jeu
        
        elif not toggle_cutscenes: # Si cinématiques désactivées
            lancement = True # Lancement toujours actif
        
        # DEPLACEMENT ET TIRS DU JOUEUR ------------------------------------------------------------
        
        if player.vie > 0 and lancement: # Si le joueur n'est pas mort et que le lancement est possible (pas de cinématique en cours)
            player.deplacer(window_width,window_height,keys) # Faire que le joueur puisse se déplacer
            
            if toggle_cheat:
                player.tirer(2,keys) # Faire que le joueur puisse tirer sans limites
            else:
                player.tirer(0,keys) # Faire que le joueur puisse tirer normalement
            
        # AFFICHAGE DU FOND ET DU JOUEUR EN FONCTION DE SA POSITION ------------------------------------------------------------
        
        window.blit(background,(0,0)) # Affichage du fond 'background.png'
        window.blit(player.image, player.rect) # Affichage du joueur en fonction de sa position
        
        if toggle_hitbox: # Si le paramètre hitbox est activé
            pygame.draw.rect(window, (255, 0, 0), player.rect, 2)  # Couleur rouge, 2 pixels d'épaisseur
        
        # CREATION D'UNE NOUVELLE VAGUE ------------------------------------------------------------
    
        if opponent_list == [] and player.vie > 0: # Si il n'y a plus d'adversaire à tuer et que la joueur n'est pas mort
            player.retour_milieu(window_width,window_height) # Nouvelle vague --> Joueur retourne au milieu pour être en securité
            player.vague += 1 # Une vague de plus passée ( Débute à 0 donc commence bien par la vague 1 )
            
            wave_passed_sound.play() # Sons de victoire d'une vague 
            
            if waves_list == []: # Si il n'y a plus de vague à faire, reprendre un cycle depuis la liste des vagues sauvegardés
                waves_list = save_waves_list            
            
            if randomwave: # Si le paramètre vague aléatoire est activé
                random.shuffle(waves_list) # Mélange de la liste des vagues suivantes 
                
            if toggle_next_wave: # Si le paramètre décision de la prochaine vague est activé
                waves_list = next_wave + waves_list # La liste des prochaines vague inclut la vague decidée en premier
                toggle_next_wave = False # La vague est donc dans la liste, il n'y a plus besoin de repeter cela d'autres fois, desactivation du paramètre
                
          
            # CHOIX DE LA PREMIERE VAGUE PARMIS LA LISTE DES VAGUES SUIVANTES
            
            if waves_list[0] == 'asteriods': # Si la vague suivante est la vague des asteriodes
                
                for i in range(50): # Genere 50 asteriod
                
                    # POSITIONS ET COMPORTEMENT
                    x = random.randint(0, window_width) # Position horizontale aleatoire entre les deux bout de la largeur de la fenetre 
                    y = random.randint(0, window_height// 2) # Position verticale aleatoire entre le haut de la fenêtre et le milieu 
                    
                    comportement = random.randint(0,1) # Comportement de l'asteriode aléatoire '0 : asteriod normal'  ou ' 1 : asteriod rapide '
                    
                    # GENERATION DE L'ADVERSAIRE
                    asteriod = opponents.opponent(x,y,player.scale_factor, 'asteriod', comportement) # Generation de l'asteriode 
                    opponent_list.append(asteriod) # Ajout à la liste des ennemis à mettre à jour 
                
                # CINEMATIQUE 
                if toggle_cutscenes: # Si les cinématiques sont activées
                    asteriod_cutscene = cutscenes.cutscene(window_width,'hero') # Cinematique de hero
                    cutscenes_list.append(asteriod_cutscene) # Ajout de la cinématique à la liste des cinématiques à afficher
                
                    
            elif waves_list[0] == 'plant_opponent': # Si la vague suivante est la vague des ennemis de plante
                
                for i in range(30): # Genere 30 plant_opponent
                
                    # POSITIONS ET COMPORTEMENT
                    x= i * (window_width // 30 ) # Position x étendu sur les deux cotés de la page, à un écart égal entre chaque ennemi
                    
                    if i % 2 == 0 : # Un plant_opponent sur 2 commencera avec le comportement 1 : Avancer jusqu'au bas de la fenetre
                        comportement = 1
                    else: # Un plant_opponent sur 2 commencera avec le comportement 0 : Avancer jusqu'au haut de la fenetre
                        comportement = 0
                    
                    # GENERATION DE L'ADVERSAIRE
                    if x not in range ( window_width //2 - 300, window_width//2 +300 ): # Ne pas generer d'ennemis eu milieu (milieu de la page avec 300 pixels d'écart de chaque coté)
                        plant_opponent = opponents.opponent(x,300,player.scale_factor, 'plant_opponent', comportement) # Generation de l'ennemi plante à y:300
                        opponent_list.append(plant_opponent) # Ajout à la liste des ennemis à mettre à jour 
                
                # CINEMATIQUE 
                if toggle_cutscenes: # Si les cinématiques sont activées
                    plant_cutscene = cutscenes.cutscene(window_width,'plant_opponent') # Cinematique d'ennemi plante
                    cutscenes_list.append(plant_cutscene) # Ajout de la cinématique à la liste des cinématiques à afficher
               
                    
            elif waves_list[0] == 'fire_opponent': # Si la vague suivante est la vague des ennemis de feu
                
                for i in range(10): # Genere 10 fire_opponent
                
                    # POSITIONS
                    x= i * (window_width // 10 ) # Position x sur les deux cotés de la page, à un écart égal entre chaque ennemi
                    
                    # GENERATION DE L'ADVERSAIRE
                    opponent = opponents.opponent(x,100,player.scale_factor, 'fire_opponent', 0) # Generation de l'ennemi feu à y:100
                    opponent_list.append(opponent) # Ajout à la liste des ennemis à mettre à jour 
                
                # CINEMATIQUE 
                if toggle_cutscenes: # Si les cinématiques sont activées
                    fire_cutscene = cutscenes.cutscene(window_width,'fire_opponent') # Cinematique d'ennemi de feu
                    cutscenes_list.append(fire_cutscene) # Ajout de la cinématique à la liste des cinématiques à afficher
              
                    
            elif waves_list[0] == 'rock_opponent': # Si la vague suivante est la vague des ennemis de roche
                
                for i in range (5): # Genere 5 rock_opponent
                
                    # POSITIONS
                    
                    for x in [-100,100,window_width-150,window_width+50]: # pour x dans ces quatre position x 
                        y = i * window_height //6  # Position y étendu sur les deux cotés de la page, à un écart égal entre chaque ennemi
                        
                        if x == -100 or x == 100:
                            rock_opponent = opponents.opponent(x,y,player.scale_factor, 'rock_opponent', 0) # Generation de l'ennemi de roche 
                            opponent_list.append(rock_opponent) # Ajout à la liste des ennemis à mettre à jour 
              
                        else:
                            rock_opponent = opponents.opponent(x,y,player.scale_factor, 'rock_opponent', 1) # Generation de l'ennemi de roche 
                            opponent_list.append(rock_opponent) # Ajout à la liste des ennemis à mettre à jour 
              
                # CINEMATIQUE 
                if toggle_cutscenes: # Si les cinématiques sont activées
                    rock_cutscene = cutscenes.cutscene(window_width,'rock_opponent') # Cinematique d'ennemi de roche
                    cutscenes_list.append(rock_cutscene) # Ajout de la cinématique à la liste des cinématiques à afficher
    
    
            elif waves_list[0] == 'water_opponent': # Si la vague suivante est la vague des ennemis d'eau
                
                # GENERATION DE L'ADVERSAIRE
                opponent = opponents.opponent(window_width // 2,window_height // 2,player.scale_factor, 'water_opponent', 0) # Generation de l'ennemi d'eau au milieu de la page 
                opponent_list.append(opponent) # Ajout à la liste des ennemis à mettre à jour 
                
                # CINEMATIQUE 
                if toggle_cutscenes: # Si les cinématiques sont activées
                    rock_cutscene = cutscenes.cutscene(window_width,'water_opponent') # Cinematique d'ennemi d'eau
                    cutscenes_list.append(rock_cutscene) # Ajout de la cinématique à la liste des cinématiques à afficher
            
            
            elif waves_list[0] == 'troll_opponent': # Si la vague suivante est la vague des ennemis trolls
                
                for i in range(50): # Genere 50 troll_opponent
                    
                    # POSITIONS
                    x = i * (window_width // 50 ) 
                    
                    # GENERATION DE L'ADVERSAIRE
                    opponent = opponents.opponent(x,100,player.scale_factor, 'troll_opponent', 0) # Generation de l'ennemi troll en y:100
                    opponent_list.append(opponent) # Ajout à la liste des ennemis à mettre à jour 
                
                # CINEMATIQUE 
                if toggle_cutscenes: # Si les cinématiques sont activées
                    rock_cutscene = cutscenes.cutscene(window_width,'troll_opponent') # Cinematique d'ennemi troll
                    cutscenes_list.append(rock_cutscene) # Ajout de la cinématique à la liste des cinématiques à afficher
              
                
            elif waves_list[0] == 'demon_boss_opponent': # Si la vague suivante est la vague du boss demon
                   
                # GENERATION DE L'ADVERSAIRE
                opponent = opponents.opponent(window_width // 2 - 100,200,player.scale_factor, 'demon_boss_opponent', 'main_boss') # Generation de l'ennemi boss en x: window_width // 2 - 100 et y:200
                opponent_list.append(opponent) # Ajout à la liste des ennemis à mettre à jour 
                
                # CINEMATIQUE 
                if toggle_cutscenes: # Si les cinématiques sont activées
                    rock_cutscene = cutscenes.cutscene(window_width,'demon_boss_opponent') # Cinematique d'ennemi bossS
                    cutscenes_list.append(rock_cutscene) # Ajout de la cinématique à la liste des cinématiques à afficher
                    
                    
            waves_list = waves_list[1:] # Suppression de la première vague de la liste des vagues
            
        # MISE A JOUR DES LASERS ------------------------------------------------------------
        
        for laser in player.laserlist: # Pour tout laser dans la liste des laser à charger
            laser.deplacer() # Déplacement du laser
            laser.afficher(window) # Affichage du laser
            
            if toggle_hitbox: # Si le paramètre hitbox est activé
                pygame.draw.rect(window, (0, 255, 0), laser.rect, 2)  # Couleur bleue, 2 pixels d'épaisseur
                
            if laser.rect.y < 0: # Suppression du laser s'il sort de l'écran
                player.laserlist.remove(laser) # Suppression du laser de la liste des lasers existants
                del laser # Suppression du laser
        
        # MISE A JOUR DES ENNEMIS ------------------------------------------------------------

        if lancement: # Si le jeu peu se lancer (pas de cinématique ne cours)
            for opponent in opponent_list : # Pour tout adversaire dans la liste des adversaires à charger

                opponent.move(player.rect,window_width,window_height) # Déplacement de l'adversaire
                opponent.display(window) # Affichage de l'adversaire
                
                # Vérification des collisions entre ennemi et lasers
                if len(player.laserlist) != 0: # Ligne permettant de ne pas rencontrer de problème quand aucun laser n'existe
                    
                    for laser in player.laserlist: # Pour tout laser dans la liste des laser à charger
                        if opponent.rect.colliderect(laser.rect): # Si il y a collision laser - ennemi 
                            opponent.perdre_vie(1) # L'ennemi perd une vie 
                            
                            player.laserlist.remove(laser) # Suppression du laser de la liste des lasers existants
                            del laser # Suppression du laser
                            
                            hit_sound.play() # Son de touché de l'adversaire
                            
                            if opponent.type == 'main_boss': # Comportement spécial : main_boss --> apparition de deux sbires 
                                
                                new_opponent = opponents.opponent( window_width // 2 + 300, window_height // 5, opponent.scale_factor // 2, 'demon_boss_opponent', 0)
                                opponent_list.append(new_opponent)
                                
                                new_opponent = opponents.opponent(window_width // 2 - 300, window_height // 5, opponent.scale_factor //2 , 'demon_boss_opponent', 0)
                                opponent_list.append(new_opponent)

                            elif opponent.type == 'demon_boss_opponent': # Si un mini boss se fais toucher 

                                for ennemi in opponent_list : # Pour tout adversaire dans la liste des adversaires à charger
                                    if ennemi.type == 'main_boss': # Si le boss principal est dedans 
                                        if ennemi.vitesse == 4: # Si sa vitesse est de deux elle passe à 1 
                                            ennemi.vitesse = 1
                                        else: # Sinon elle passe à 4
                                            ennemi.vitesse = 4
                                
                # Vérification des collisions entre ennemi et joueur
                if not toggle_godmode: # Si le mode dieu n'est pas activé 
                
                    if opponent.rect.colliderect(player.rect): # Si il y a collision joueur - ennemi 
                        if player.vie > 0: # Si le joueur à plus de 0 de vie (il peut arriver d'avoir une vie négative si touché très rapidement sinon)
                            player.perdre_vie(1)  # Le joueur perd un de vie 
                        opponent.perdre_vie(1) # L'ennemi perd de la vie
                        
                        player.retour_milieu(window_width,window_height) # Teleportation du joueur dans un lieu + sur
                        collide_sound.play() # Son de collision du joueur 
                
                if opponent.vie <= 0: # Si l'ennemi a été vaincu
                
                    opponent.marquer_a_supprimer = True # Ennemi marqué pour suppression 
                    elimination_sound.play() # Son d'elimination de l'ennemi
                    player.score += 1 # Un ennemi mort --> +1 au score 
                    
                    if opponent.type == 'plant_opponent' and opponent.giveboost == 1: # Si l'ennemi tué est un plant_opponent
                        player.boostbattery += 2500 # Donne 2500 de boost au joueur
                        
                    elif opponent.type == 'asteriod' and opponent.giveboost == 1: # Si l'ennemi tué est un asteriode
                         player.boostbattery += 100 # Donne 100 de boost au joueur
                    
                    elif opponent.type == 'fire_opponent': # Si l'ennemi tué est un fire_opponent
                         player.boostbattery += 200 # Donne 200 de boost au joueur
                    
                    elif opponent.type == 'rock_opponent': # Si l'ennemi tué est un rock_opponent
                        opponent = opponents.opponent(opponent.rect.x,opponent.rect.y,opponent.scale_factor, 'asteriod', 1) # Generation d'un asteriode au lieu de sa mort 
                        opponent_list.append(opponent) # Ajout à la liste des ennemis à mettre à jour 
                    
                    elif opponent.type == 'water_opponent' and opponent.comportement < 8: # Si l'ennemi tué est un water_opponent et qu'il n'a pas un comportement excedant 8 
                        
                        for i in range(2): # Création de deux autres ennemis de l'eau 
                            x = random.randint(0,window_width) # Position x aléatoire entre 0 et la moitié de la largeur de la page 
                            y = random.randint(0,window_height //2 ) # Position y aléatoire entre 0 et la moitié de la hauteur de la page 
                            
                            opponent = opponents.opponent(x,y,opponent.scale_factor, 'water_opponent', opponent.comportement + 1) # Generation de l'ennemi eau avec un comportement + 1 
                            opponent_list.append(opponent) # Ajout à la liste des ennemis à mettre à jour 
                            
                    elif opponent.type == 'water_opponent' and opponent.comportement == 8 : # Si l'ennemi tué est un water_opponent et qu'il a un comportement de 8 
                        player.boostbattery += 150 # Donne 150 de boost au joueur  
                    
                    elif opponent.type == 'demon_boss_opponent': # Si l'ennemi tué est un demon_boss_opponent
                        player.boostbattery += 200 # Donne 200 de boost au joueur

                    elif opponent.type == 'main_boss':
                        player.boostbattery += 3000 # Donne 3000 de boost au joueur
                    
                if toggle_hitbox: # Si le paramètre hitbox est activé
                    pygame.draw.rect(window, (0, 0, 255), opponent.rect, 2)  # Couleur bleue, 2 pixels d'épaisseur
        
        # DECLANCHEMENT DU GAME OVER ------------------------------------------------------------
        if player.vie <= 0 and lancement and not is_gameover: # Si le joueur est mort et que is_gameover n'est pas déjà vrai 
            opponent_list = [] # Plus d'ennemis à mettre à jour 
            gameover = cutscenes.cutscene(window_width,'gameover') # Cinématique de hero pour la fin du jeu 
            cutscenes_list.append(gameover) # Ajout de la cinématique à la liste des cinématiques à afficher
            is_gameover = True # Changement de is_gameover pour une fin de jeu donc True
        
        if toggle_cutscenes: # Si les cinématiques sont activée 
            for cine in cutscenes_list: # Pour tout cinématique dans la liste des cinématiques à charger
                    
                    window.blit(cine.display, cine.rect) # Affichage de l'image de personnage
                    window.blit(cine.speech, (100, window_height//2)) # Affichage du texte dit par le personnage 
                    
                    window.blit(press_1, (50 , window_height -50)) # Affichage de press_1 pour passé la cinématique
                    
                    if pygame.key.get_pressed()[pygame.K_1] and not is_gameover: # Si 1 est pressé et ce n'est pas la fin du jeu 
                            cutscene_in_progress = False # Plus de cinématique en cours 
                            cutscenes_list.remove(cine) # Plus de cinématique à charger
                            
                            
                    elif pygame.key.get_pressed()[pygame.K_1] and is_gameover: # Si 1 est pressé et c'est la fin du jeu 
                            cutscene_in_progress = False # Plus de cinématique en cours 
                            cutscenes_list.remove(cine) # Plus de cinématique de fin à charger
                            play() # Lancement d'une nouvelle partie
               
        # Suppression les ennemis marqués pour suppression
        opponent_list = [opponent for opponent in opponent_list if not opponent.marquer_a_supprimer] # La liste est égale à tout le monde n'étant pas marqué 
        
        # AFFICHAGES DE TEXTES ------------------------------------------------------------
        
        # Définition des textes de l'ATH
        score_texte = font.render("Score: " + str(player.score), True, 'white')  # Conversion du score en texte
        life_texte = font.render("Vie: " + str(player.vie), True, 'white') # Conversion de la vie du joueur en texte
        boost_texte = font.render("Boost: " + str(player.boostbattery), True, 'white') # Conversion de la batterie du joueur en texte
        vague_texte = font.render("Vague " + str(player.vague), True, 'white') # Conversion du nombre de vague atteint en texte
        
        # Affichage de l'ATH
        window.blit(score_texte, (25, 25))  # Affichage du texte de score en x:25 y:25
        window.blit(life_texte, (25, 55)) # Affichage du texte de vie du joueur en x:25 y:55
        window.blit(boost_texte, (25, 85)) # Affichage du texte de batterie du joueur en x:25 y:85
        window.blit(vague_texte, (25, 115)) # Affichage du texte du nombre de vague atteint en x:25 y:115
        
        
        if not toggle_godmode and not toggle_cheat:
            if player.score > meilleur_score: # Si le joueur dépasse le meilleur score
                meilleur_score = player.score # Mise à jour du meilleur score
                with open("meilleur_score.txt", "w") as file:
                    file.write(str(meilleur_score)) # Enregistrement meilleur score dans le fichier meilleur_score.txt
        
        meilleur_score_texte = font.render("Meilleur score: " + str(meilleur_score), True, 'white') # Conversion du meilleur score en texte
        window.blit(meilleur_score_texte, (25, 145)) # Affichage du texte de meilleur_score en x:25 y:145
        
        if toggle_cheat or toggle_godmode: # Si un système de triche est activé
            window.blit(cheat_texte, (25, 175)) # Affichage du texte triche activée
            
        # AFFICHAGE ------------------------------------------------------------
        pygame.display.flip() # Mise à jour de l'affichage
        pygame.time.Clock().tick(60) # Limite du taux de rafraîchissement à 60 FPS
         
play() # Lancement de la première partie de jeu  
    
    
    
    
    
              