import mysql.connector as msc

# Fonction de requête SQL
def requete_sql(nom_colonne, prenom_colonne, genre_colonne, statut_colonne, photo_path):
    # Connection à la db
    bdd = msc.connect(user='ISEN', password='ISEN', host='127.0.0.1', port='8081', database='trombinoscope')
    cursor = bdd.cursor()

    query = "SELECT nom_personne, prenom_personne, photo_personne, genre, qualification_statut FROM personnes NATURAL JOIN genres NATURAL JOIN statut WHERE " + nom_colonne + prenom_colonne + genre_colonne + statut_colonne + ";"

    cursor.execute(query)

    resultat = []
    cnt = 0

    for enregistrement in cursor :
        resultat.append(list(enregistrement))
        resultat[cnt][2] = photo_path+resultat[cnt][2]
        cnt += 1
    
    cursor.close()
    bdd.close()

    return resultat