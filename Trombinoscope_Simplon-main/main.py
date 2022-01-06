# Importation des librairies

import os.path
import mysql.connector as msc
from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk

# Définition de la fonction de recherche dans la base de données avec mise à jour de la photo
def recherche_db():

    # Connection à la db
    bdd = msc.connect(user='ISEN', password='ISEN', host='127.0.0.1', port='8081', database='trombinoscope')
    cursor = bdd.cursor()

    # Récupération des saisies de l'utilisateur avec vérification de l'écriture
    # Fenêtre d'avertissement si un de ces caractères (, ), ou ;, compose la saisie
    if '(' in nom_editeur.get() or ')' in nom_editeur.get() or ';' in nom_editeur.get() : # Condition vérifiant la conformité de nom
        showwarning(messag='nom invalide') # Fenêtre d'avertissement
        return
    else:
        nom_saisi = nom_editeur.get() # Récupération de la saisie nom

    if '(' in prenom_editeur.get() or ')' in prenom_editeur.get() or ';' in prenom_editeur.get() : # Condition vérifiant la conformité de prenom
        showwarning(message='prenom invalide') # Fenêtre d'avertissement
        return
    else:
        prenom_saisi = prenom_editeur.get() # Récupération de la saisie prenom

    # Initialisation des variables utilisées pour la recherche dans la requête SQL
    nom_colonne = ""
    prenom_colonne = ""

    # Vérification si champ de saisi vide
    if not nom_saisi and prenom_saisi: # Condition champ nom vide
        prenom_colonne = "prenom_personne =\'" + prenom_saisi + "\'" # Formatage de la saisie prenom pour la requête SQL
    elif not prenom_saisi and nom_saisi: # Condition champ prénom vide
        nom_colonne = "nom_personne =\'" + nom_saisi + "\'" # Formatage de la saisie nom pour la requête SQL
    elif nom_saisi and prenom_saisi:
        nom_colonne = "nom_personne =\'" + nom_saisi + "\'" # Formatage de la saisie nom pour la requête SQL
        prenom_colonne = " AND prenom_personne =\'" + prenom_saisi + "\'" # Formatage de la saisie prenom pour la requête SQL
    else: # Tous les champs sont vides
        return

    # Requête SQL
    query = "SELECT nom_personne, prenom_personne, photo_personne, genre, qualification_statut FROM personnes NATURAL JOIN genres NATURAL JOIN statut WHERE " + nom_colonne + prenom_colonne + ";"

    #Exécution de la requête SQL
    cursor.execute(query)

    # Récupération des résultats de la requête SQL
    for enregistrement in cursor :
        
        # Vérification si image associée à une personne
        if os.path.exists(photo_path + enregistrement[2]):
            img = Image.open(photo_path + enregistrement[2]) # Ouverture de l'image
        else:
            img = Image.open(photo_path + "no_photo_available.jpg") # Ouverture "image no available" 

        width, height = img.size # Récupérer la taille de l'image
        
        
        # Condition pour le redimenionnage
        if width >= width_canva or height >= height_canva:  # Vérifier si dimension photo supérieure au canevas
            if width > height: # Photo format paysage
                ratio = width/height # Ratio largeur / hauteur
                new_width = width_canva # nouvelle largeur
                new_height = int(new_width//ratio) # nouvelle hauteur
                photo = ImageTk.PhotoImage(img.resize((new_width, new_height))) # Ouverture et redimentionnage de la photo
            else: # Photo format portrait
                ratio = height/width # Ratio hauteur / largeur
                new_height = height_canva # nouvelle hauteur
                new_width = int(new_height//ratio) # nouvelle largeur    
                photo = ImageTk.PhotoImage(img.resize((new_width, new_height))) # Ouverture et redimentionnage de la photo
        else: 
            photo = ImageTk.PhotoImage(img) # Ouverture de l'image

        canva_photo.itemconfig(photo_img, image=photo) # actualisation de l'image sur le canevas
        # Actualisation du label sous la photo 
        label_photo.set(enregistrement[3] + " " + enregistrement[0] + " " + enregistrement[1] + "\n (" + enregistrement[4] + ")")
    
    fenetre.mainloop() # Actualisation de la fenêtre
    
    cursor.close() # Fermeture du curseur
    bdd.close() # Déconnection de la base de données


# Chemin d'accès aux photos
photo_path = "./photos/"

#### Interface graphique ####

fenetre = Tk() # Création de la fenêtre de l'application
fenetre.title('Trombinoscope') # Titre de l'applicatoin

## Info sur la taille de l'écran
screen_width = fenetre.winfo_screenwidth() # Largeur
screen_height = fenetre.winfo_screenheight() # Hauteur

width_factor = 1.6  # Facteur souhaité largeur
height_factor = 1.4 # Facteur souhaité hauteur

# Définition de la taille de l'application selon la taille de l'écran
fenetre.geometry(str(int(screen_width//width_factor))+'x'+str(int(screen_height//height_factor))+'+250+70')

# Création d'un panneau pour placer les widgets
panneau = PanedWindow(fenetre, orient='vertical')

# Widget : champ de saisie de texte
nom_editeur = Entry(panneau)
prenom_editeur = Entry(panneau)

# Widget : canevas pour afficher les photos
width_canva = 1512 // 6 # Largeur
height_canva =  2016 // 6 # Hauteur
canva_photo = Canvas(panneau, width=width_canva, height=height_canva) # Création du canva

# Affichage de l'image principale de l'application
img = ImageTk.PhotoImage(Image.open(photo_path + "simplon.jpg")) # Ouverture de l'image
photo_img = canva_photo.create_image(width_canva/2, height_canva/2, image=img) # création de l'image sur le canva

# Widget : Label pour afficher les informations sur la personne
label_photo = StringVar()

# Ajout des widgets au panneau
panneau.add(Label(panneau, text='Nom', anchor=CENTER)) # Label pour la saisie nom
panneau.add(nom_editeur) # Saisie du nom
panneau.add(Label(panneau, text='Prenom', anchor=CENTER)) # Label pour la saisie prenom
panneau.add(prenom_editeur) # Saisi du prenom
panneau.add(Button(text='Chercher', command=recherche_db)) # Bouton recherche appelant la fonction de recherche sur la base de données
panneau.add(canva_photo) # Canevas photo
panneau.add(Label(textvariable=label_photo, height=2)) # Label d'information de la personne

panneau.pack() # Affichage du panneau sur l'application

fenetre.mainloop() # Affichage de l'application
