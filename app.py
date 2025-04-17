import math

def menu():
    print("Choisissez une figure géométrique :")
    print("1. Carré")
    print("2. Rectangle")
    print("3. Triangle rectangle")
    print("4. Cercle")
    choix = input("Votre choix (1-4) : ")
    return choix

def carre():
    côté = float(input("Longueur du côté : "))
    périmètre = 4 * côté
    surface = côté ** 2
    return périmètre, surface

def rectangle():
    longueur = float(input("Longueur : "))
    largeur = float(input("Largeur : "))
    périmètre = 2 * (longueur + largeur)
    surface = longueur * largeur
    return périmètre, surface

def triangle_rectangle():
    base = float(input("Base : "))
    hauteur = float(input("Hauteur : "))
    hypotenuse = math.sqrt(base**2 + hauteur**2)
    périmètre = base + hauteur + hypotenuse
    surface = (base * hauteur) / 2
    return périmètre, surface

def cercle():
    rayon = float(input("Rayon : "))
    périmètre = 2 * math.pi * rayon
    surface = math.pi * rayon ** 2
    return périmètre, surface

def main():
    choix = menu()
    if choix == "1":
        p, s = carre()
    elif choix == "2":
        p, s = rectangle()
    elif choix == "3":
        p, s = triangle_rectangle()
    elif choix == "4":
        p, s = cercle()
    else:
        print("Choix invalide.")
        return
    print(f"Périmètre : {p:.2f}")
    print(f"Surface : {s:.2f}")

if __name__ == "__main__":
    main()

