# #jeu de devinette

# import random
# # random.randint(a, b)

# def jeu_devinette():
#     print("Bienvenue au jeu du Devinette!")
#     print("Je pense à un nombre entre 1 et 100.")

#     nombre_aleatoire = random.randint(1, 100)
#     # print(nombre_aleatoire)
#     tentative=0
#     devine=False


#     while not devine :
#         try:
#             proposition = int(input('entrer le nombre de votre choix'))
#             print(proposition)
#             tentative =+1

#             if(nombre_aleatoire > proposition):
#                 print("trop grand")
#             elif(nombre_aleatoire < proposition):
#                 print("trop petit")
#             else:
#                 print("exact ")
#                 print(f"Bravo! Vous avez deviné en {tentative} tentatives.")
#                 devine = True
#         except valueError:
#             print('Veuillez entrer un nombre valide')

# # Lancer le jeu
# jeu_devinette()


import random

def jeu_devinette():
    print("Bienvenue au jeu du Devinette!")
    print("Je pense à un nombre entre 1 et 100.")

    # Générer un nombre aléatoire
    nombre_aleatoire = random.randint(1, 100)
    tentative = 0
    devine = False

    while not devine:
        try:
            # Demander une proposition à l'utilisateur
            proposition = int(input('Entrez le nombre de votre choix : '))
            tentative += 1  # Incrémentation correcte du compteur de tentatives

            if nombre_aleatoire > proposition:
                print("C'est trop petit!")
            elif nombre_aleatoire < proposition:
                print("C'est trop grand!")
            else:
                print("Exact!")
                print(f"Bravo! Vous avez deviné en {tentative} tentatives.")
                devine = True
        except ValueError:  # Correction de la capitalisation de ValueError
            print("Veuillez entrer un nombre valide.")

# Lancer le jeu
jeu_devinette()
