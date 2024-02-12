def est_palindrome(mot)
    mot = mot.lower()
    return mot == mot[::-1]

# Liste de mots à vérifier
mots = ["radar", "python", "stats", "level", "deified"]

# Vérifier si chaque mot est un palindrome
for mot in mots:
    if est_palindrome(mot)
        print(f" est un palindrome !")
    else
        print(f" n'est pas un palindrome.")
