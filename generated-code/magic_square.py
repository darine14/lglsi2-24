def carre_magique(n):
    if n % 2 == 0:
        raise ValueError("L'ordre du carré magique doit être impair")

    carre_magique = [[0] * n for _ in range(n)]

    i, j = 0, n // 2

    for num in range(1, n**2 + 1):
        carre_magique[i][j] = num
        i -= 1
        j += 1

        
    return carre_magique

def afficher_carre_magique(carre_magique):
    for ligne in carre_magique:
      
        print(" ".join(map(str, ligne)))

# Exemple d'utilisation avec un carré magique d'ordre 3
ordre = 3
carre_magique = carre_magique(ordre)
afficher_carre_magique(carre_magique)

