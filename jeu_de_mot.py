import random
import pyperclip

while True:
    word = input("Entrez le mot : ")
    print("Recherche de mot en cours...")

    with open("D:\Desktop\Python_Project\Jeu De Mot\ods6.txt","r") as file:
        data = file.readlines()

    correct_word = []

    for i in data:
        if word.upper() in i:
            correct_word.append(i)   
    if correct_word == []:
        print("Votre mot n'est pas dans la liste !")
        
    result = random.choice(correct_word)  
    print("\n Votre mot est : "+result)
    
    cop = input("Voulez vous copier votre mot ? {O/N} : ")
    while cop not in ("O","N"):
        cop = input("Vous devez répondre par une valeur correcte ! {O/N} : ")
    if cop == "O":
        up_lo = input("Voulez vous que votre mot soit en miniscule ? {O/N} : ")
        while up_lo not in ("O","N"):
            up_lo = input("Vous devez répondre par une valeur correcte ! {O/N} : ")
        if up_lo == "O":
            pyperclip.copy(result.lower())
            print("Mot copié en miniscule avec succès !")
        elif up_lo == "N":
            pyperclip.copy(result)
            print("Mot copié avec succès !")
        
    elif cop == "N":
        pass
    
    cont = input("Voulez vous continuer ? {O/N} : ")
    while cont not in ("O","N"):
        cont = input("Vous devez répondre par une valeur correcte ! {O/N} : ")
    if cont == "O":
        continue
    if cont == "N":
        print("Bye ! En espérant te revoir prochainement.")
        break