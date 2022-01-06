import os.path
from tkinter.constants import ACTIVE, HORIZONTAL
import tkinter as tk
from PIL import Image, ImageTk
from recherche_db import *

photo_path = "./photos/"
root = tk.Tk()
root.title("Trombinoscope")

# Fonction pour retirer les widgets de la frame d'affichage
def rm_widget():
    for widget in frame_affichage.winfo_children():
        widget.destroy()

# Fonction associé au bouton recherche
def recherche():
    global nom_colonne
    global prenom_colonne
    global genre_colonne
    global resultat

    rm_widget() # Suppresion des widgets sur la frame affichage

    nom_saisi = nom_editeur.get() # Récupération du nom saisi
    prenom_saisi = prenom_editeur.get() # Récupération du prénom saisi
    genre_saisi = liste_genre.curselection() # Récupération du genre
    statut_saisi = liste_statut.curselection() # Récupération du statut

    nom_colonne = ""
    prenom_colonne = ""
    genre_colonne = ""
    statut_colonne = ""

    # Vérification des saisies de l'utilisateur pour selectionner la recherhe adapter
    if not nom_saisi and prenom_saisi:
        prenom_colonne = "prenom_personne =\'" + prenom_saisi + "\'" # Recherche par prénom
    elif not prenom_saisi and nom_saisi:
        nom_colonne = "nom_personne =\'" + nom_saisi + "\'" # Recherche par nom
    elif nom_saisi and prenom_saisi:
        nom_colonne = "nom_personne =\'" + nom_saisi + "\'" # Recherche par nom et prénom
        prenom_colonne = " AND prenom_personne =\'" + prenom_saisi + "\'"
    elif len(genre_saisi) > 0:
        genre_colonne = "id_genre =\'" + str(genre_saisi[0]+1) + "\'" # Recherche par genre
    elif len(statut_saisi) > 0:
        statut_colonne = "id_statut =\'" + str(statut_saisi[0]+1) + "\'" # Recherche par statut
    else:
        # Remise de l'image principal si pas de champs sélectionné
        canva_photo = tk.Canvas(frame_affichage, width=width_canva, height=height_canva) 

        img = ImageTk.PhotoImage(Image.open(photo_path + "simplon.jpg"))
        photo_img = canva_photo.create_image(width_canva/2, height_canva/2, image=img)

        canva_photo.pack()

        root.mainloop()
        return


    resultat = requete_sql(nom_colonne, prenom_colonne, genre_colonne, statut_colonne, photo_path) # intérogation db

    affichage_photo = [] # Liste avec les canvas
    photo = [] # Liste avec les photos
    label_photo = [] # Liste avec les labels des photos

    width_image = 100 # Largeur des images
    height_image = 140 # Hauteur des images
    cnt_image = 0 # Compteur pour la boucle
    ligne_image = 0 # Compteur pour l'indice ligne dans pour l'organisation grid des canvas et labels
    colonne_image = 0 # Compteur pour l'indice colonne dans pour l'organisation grid des canvas et labels

    for i in range(len(resultat)):
        # Ouverture de la photo
        # Vérification si image associée à une personne
        if os.path.exists(resultat[i][2]):
            img = Image.open(resultat[i][2]) # Ouverture de l'image
        else:
            img = Image.open(photo_path + "no_photo_available.jpg") # Ouverture "image no available" 

        photo.append(ImageTk.PhotoImage(img.resize((width_image,height_image)))) # Ajout des photos dans listes

        # Ajout des canvas
        affichage_photo.append(tk.Canvas(frame_affichage,width=width_image, height=height_image))
        affichage_photo[i].create_image(width_image/2,height_image/2, image=photo[i])
        affichage_photo[i].grid(row=ligne_image, column=colonne_image)
        
        # Texte photo
        legende_photo = str(resultat[i][3]) + " " + str(resultat[i][0]) + " " + str(resultat[i][1]) + "\n (" + str(resultat[i][4]) + ")"
        label_photo.append(tk.Label(frame_affichage, text=legende_photo))
        label_photo[i].grid(row=ligne_image+1, column=colonne_image)

        cnt_image += 1
        colonne_image += 1

        if cnt_image == 8: # 8 photos par lignes
            cnt_image = 0
            ligne_image += 2
            colonne_image = 0

    root.mainloop()
    


# Taille de l'application
width_app = root.winfo_screenwidth()
height_app = root.winfo_screenheight()-100
root.geometry(str(width_app)+"x"+str(height_app)+"+0+0")

# Interface graphique
panneau_general = tk.PanedWindow(root, orient=tk.HORIZONTAL, width=width_app, height=height_app)
frame_recherche = tk.Frame(root, width=int(width_app//3), height=height_app)
frame_affichage = tk.Frame(root, width=int(width_app//3)*2, height=height_app)

panneau_general.add(frame_recherche)
panneau_general.add(frame_affichage)

# Widget recherche
# nom
label_nom = tk.Label(frame_recherche, text='Nom', anchor=tk.CENTER)
label_nom.pack()

nom_editeur = tk.Entry(frame_recherche)
nom_editeur.pack()

# prenom
label_prenom = tk.Label(frame_recherche, text='Prenom', anchor=tk.CENTER)
label_prenom.pack()

prenom_editeur = tk.Entry(frame_recherche)
prenom_editeur.pack()

# genre
label_genre = tk.Label(frame_recherche, text='Genre', anchor=tk.CENTER)
label_genre.pack()

liste_genre = tk.Listbox(frame_recherche)
liste_genre.insert(1,"M.")
liste_genre.insert(2,"Mme.")
liste_genre.insert(3,"Autre")
liste_genre.pack()

# statut
label_statut = tk.Label(frame_recherche, text='Statut', anchor=tk.CENTER)
label_statut.pack()

liste_statut = tk.Listbox(frame_recherche)
liste_statut.insert(1,"Chargé de projet")
liste_statut.insert(2,"Formateur")
liste_statut.insert(3,"Etudiant P1")
liste_statut.insert(4,"Etudiant P2")
liste_statut.pack()

bouton_recherche = tk.Button(frame_recherche,text='Chercher', command=recherche)
bouton_recherche.pack()

# Canva photo
width_canva = 400
height_canva =  400
canva_photo = tk.Canvas(frame_affichage, width=width_canva, height=height_canva)

img = ImageTk.PhotoImage(Image.open(photo_path + "simplon.jpg"))
photo_img = canva_photo.create_image(width_canva/2, height_canva/2, image=img)

canva_photo.pack()

panneau_general.pack()
root.mainloop()