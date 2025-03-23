import random
import pygame

# Liste des groupes d'images de cinematique disponibles et du nombre d'images associés (ex : hero contient 3 images ou fire_opponent en contient 5)
character_dictionary = {"hero": 3, "fire_opponent": 5, "plant_opponent":4, "rock_opponent" : 4, 'water_opponent' : 4,'troll_opponent' : 4,'demon_boss_opponent' : 4}

class cutscene():
    ''' Classe créant une cinématique '''
    
    def __init__(self, window_width, personnage):
        ''' Création du cinématique en fonction du personnage selectionné '''
        
        if personnage in character_dictionary: # Si le personnage est dans la liste des groupes de personnages ...            
            texture = random.randint(1,character_dictionary[personnage]) # Texture est un nombre au hazard entre 1 et le nombre d'image du groupe 
            
            if personnage == 'hero': # Si le personnage est un hero ( Chemin différent ) ...
                image_path = 'textures/Translucent/main_hero_' + str(texture) + '.png' # Definition du chemin d'acces de l'image 
                
            else: # Sinon 
                image_path = 'textures/Translucent/' + personnage + '_' + str(texture) + '.png' # Definition du chemin d'acces de l'image 

        elif personnage == 'gameover': # Exception si le personnage est gameover  
            texture = random.randint(1,character_dictionary['hero']) # Groupes d'image du personnage 'hero'
            image_path = 'textures/Translucent/main_hero_' + str(texture) + '.png' # Definition du chemin d'acces de l'image 
                
        
        if personnage == 'hero': # Phrases dites au hasard par le personnage hero 
            phrase = random.choice(["Au cœur des astéroïdes, nous forgerons notre victoire !",
                                    "Parmi les astéroïdes, nous serons le phare de la résistance.",
                                    "Les rochers spatiaux ne font que renforcer notre détermination.",
                                    "Les étoiles ne peuvent pas éteindre la flamme qui brûle en nous.",
                                    "Dans le labyrinthe des astéroïdes, nous resterons intrépide.",
                                    "Les cailloux cosmiques ne font que nourrir notre détermination.",
                                    "À travers les champs d'astéroïdes, nous tracerons notre route vers la gloire.",
                                    "Les astéroïdes ne sont que des défis à surmonter, nous nous'élèverons au-dessus d'eux."])
            
        elif personnage == 'plant_opponent': # Phrases dites au hasard par le personnage plante 
            phrase = random.choice(["Intrus, la colère de la nature vous frappera !",
                                    "Énergies végétales vous vaincront, aventurier.",
                                    "Nos racines vous enserreront, votre destin est scellé.",
                                    "Que les plantes cosmiques commencent votre destruction !",
                                    "La sève stellaire coule, votre défaite est proche.",
                                    "Le cosmos végétal rugit, succombez à sa beauté mortelle !",
                                    "Le règne vert triomphera.",
                                    "La jungle sera ton tombeau."])
                                                
        elif personnage == 'fire_opponent': # Phrases dites au hasard par le personnage feu
            phrase = random.choice(["Le feu stellaire dévore, humain, tu brûleras.",
                                    "Flammes interstellaires, prépare-toi à l'anéantissement.",
                                    "Les cendres célestes engloutiront ton existence.",
                                    "La furie des étoiles de feu t'engloutira, intrus.",
                                    "L'enfer cosmique est prêt à te consumer, mortel.",
                                    "Que les flammes intergalactiques purifient ce monde !",
                                    "Brûle dans l'ombre de notre pouvoir, faible créature.",
                                    "L'embrasement spatial annonce ta fin imminente."])
            
        elif personnage == 'rock_opponent': # Phrases dites au hasard par le personnage roche
            phrase = random.choice(["Les cristaux cosmiques résonnent, ta destruction est inévitable !",
                                    "Les météorites de l'espace forgeant ta défaite s'approchent.",
                                    "Que les minéraux galactiques scellent ton destin, intrus !",
                                    "Les pierres célestes te réduiront en poussière, aventurier.",
                                    "Le règne minéral de l'espace broie tout sur son passage.",
                                    "Les cristaux stellaires annoncent ton anéantissement imminent.",
                                    "La colère des astéroïdes pulvérisera ta faible défense.",
                                    "Les roches cosmiques te briseront, et tu seras oublié."])
            
        elif personnage == 'water_opponent': # Phrases dites au hasard par le personnage eau
            phrase = random.choice(["Les vagues célestes engloutiront tout sur leur passage !",
                                    "Les abysses de l'espace te dévoreront, intrus.",
                                    "Plonge dans l'oubli galactique, pauvre aventurier.",
                                    "Les marées interstellaires te submergeront, mortel.",
                                    "Les eaux de l'univers t'emporteront vers ta fin.",
                                    "Que les courants cosmiques te guident vers l'anéantissement !",
                                    "La puissance aquatique des étoiles scellera ton destin.",
                                    "Les profondeurs spatiales murmurent ta défaite imminente."])
            
        elif personnage == 'troll_opponent': # Phrases dites au hasard par le personnage troll
            phrase = random.choice(["Les rires cosmiques des trolls résonnent, prépare-toi à la folie !",
                                    "Les farces interstellaires des trolls vont te tourmenter, intrus.",
                                    "Que les gaffes galactiques des trolls t'emportent vers l'humiliation !",
                                    "Les ruses stellaires des trolls vont dérouter ta destinée, aventurier.",
                                    "Que nos farces intergalactiques soient ton cauchemar !",
                                    "Les farfadets cosmiques t'attendent, et ton destin sera leur plaisanterie.",
                                    "La plaisanterie des étoiles est sur le point de te consumer, mortel.",
                                    "Les tours des trolls célestes vont te faire tourner la tête."])
            
        elif personnage == 'demon_boss_opponent': # Phrases dites au hasard par le personnage boss
            phrase = random.choice(["Les flammes infernales dévoreront ton âme !",
                                    "Prépare-toi à l'apocalypse galactique, misérable créature.",
                                    "Les démons de l'espace réclament ton anéantissement, intrus !",
                                    "L'enfer cosmique s'éveille, et tu en seras la victime.",
                                    "Que les ombres démoniaques de l'univers te submergent, aventurier.",
                                    "Les légions infernales de l'espace te condamnent à l'oubli.",
                                    "Les cris des démons résonnent, ton jugement est proche, mortel.",
                                    "La fureur démonique des étoiles sera ton ultime tourment."])
            
        elif personnage == 'gameover': # Phrases dites au hasard lors du gameover, par le hero
            phrase = random.choice(["Mes rêves se dissipent dans l'obscurité de la défaite.",
                                    "La bataille est perdue, mais la guerre continue dans l'ombre.",
                                    "Les étoiles témoignent de ma défaite, mais je renaitrai.",
                                    "La mort n'est qu'une pause, je renaîtrai plus fort.",
                                    "Le cosmos a enregistré ma défaite, mais ma légende persiste.",
                                    "Le silence de l'espace résonne avec ma défaite temporaire.",
                                    "Ma destinée est suspendue dans l'oubli, mais je reprendrai mon chemin.",
                                    "Le néant m'entoure, mais la renaissance émerge de l'ombre."])
            
        # Initialisation du texte de cinematique 
        cutscene_font = pygame.font.Font(None, 50)  # Creation d'une police de texte taille 50
        cutscene_color = (255, 255, 255) # Définition d'une couleur [Blanc]
        
        self.display = pygame.image.load(image_path) # Definition de l'image avec le chemin d'acces
        self.speech = cutscene_font.render(phrase, True, cutscene_color)  # Conversion de la phrase en affichage de texte
        
        # Mise à jour de la position de l'image
        self.rect = self.display.get_rect()
        self.rect.x = window_width // 2
        self.rect.y = -100