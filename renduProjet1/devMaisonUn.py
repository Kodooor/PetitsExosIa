def initial():
    return (5,5,2,0)

print(initial())
# contenance max pichet1, contenance actuelle pichet1
# contenance max pichet2, contenance actuelle pichet2

# Si notre pichet 2 a une contenance de 1 on a notre état final
def final(etat):
    if etat[3] == 1:
        return True;
    else:
        return False

#false
print(final((5,5,2,0)))
#true
print(final((5,5,2,1)))

#La liste de nos actions possibles
def actions():
    return [jeterCompletementPichet, viderCompletementPichetAutre, viderPartiellementPichetAutre]

#Retourne le chemin d'un noeud
def getChemin(noeud):
    return noeud[1]

#Retourne l'état correspondant à un noeud
def getEtat(noeud):
    return noeud[0]

#Si on a déja vu un état dans un chemin, on return true
def dejavu(etat,chemin):
    for noeud in chemin:
        if etat == getEtat(noeud):
            return True
    return False

#Afficher la solution
def afficher_sol(noeud):
    print("Solution :")
    chemin=getChemin(noeud)
    for i in chemin:
        print(getEtat(i))
    print(getEtat(noeud))
    print("Longueur : "+str(len(chemin)+1))

#Fonction qui vide le contenu d'un pichet
def jeterCompletementPichet(etat):
    #cm1 = contenance max pichet 1
    #ca1 = contenance actuelle pichet 1
    #cm2 = contenance max pichet 2
    #ca2 = contenance actuelle pichet 2

    (cm1, ca1, cm2, ca2) = etat
    listeSuivant = []
    if ca1 != 0:
        listeSuivant.append((cm1, 0, cm2, ca2))
    if ca2 != 0:
        listeSuivant.append((cm1, ca1, cm2, 0))
    return listeSuivant


# Fonction qui vide complètement un pichet dans un autre
def viderCompletementPichetAutre(etat):
    (cm1, ca1, cm2, ca2) = etat
    listeSuivant = []
    #Si la contenance du pichet dans lequel on veut vider l'autre pichet permet d'acceuillir tout le contenu
    if ca1 < (cm2 - ca2) and ca1 != 0:
        ca2 += ca1
        ca1 = 0
        listeSuivant.append((cm1, ca1, cm2, ca2))
    elif ca2 < (cm1 - ca1) and ca2 != 0:
        ca1 += ca2
        ca2 = 0
        listeSuivant.append((cm1, ca1, cm2, ca2))
    return listeSuivant

print(viderCompletementPichetAutre(initial()))

#Fonction qui remplit un pichet avec une partie de l'autre
def viderPartiellementPichetAutre(etat):
    (cm1, ca1, cm2, ca2) = etat
    listeSuivant = []
    if ca1 >= cm2 - ca2:
        while ca2 != cm2:
            ca2 += 1
            ca1 -= 1
        listeSuivant.append((cm1, ca1, cm2, ca2))
    elif ca1 < cm2 - ca2:
        print("On ne peut pas remplir l'autre pichet entièrement")
    elif ca2 >= cm1 - ca1:
        while ca1 != cm1:
            ca1 += 1
            ca2 -= 1
        listeSuivant.append((cm1, ca1, cm2, ca2))
    elif ca2 < cm1 - ca1:
        print("On ne peut pas remplir l'autre pichet entièrement")
    return listeSuivant


print(viderPartiellementPichetAutre(initial()))

#Fonction noeudFils
def noeudFils(noeud):
    listeFils=[]
    etatCourant=getEtat(noeud)
    cheminCourant = getChemin(noeud)
    for action in actions():
        listeEtatSuivant = action(etatCourant)
        for etat in listeEtatSuivant:
            if not dejavu(etat,cheminCourant):
                chemin = list(cheminCourant)
                chemin.append(noeud)
                listeFils.append((etat,chemin))
    return listeFils

print(noeudFils((initial(),[])))

#Fonction de recherche
def rp_rec(noeud):
    if final(getEtat(noeud)):
        afficher_sol(noeud)
        return True
    else:
        listeSuivant = noeudFils(noeud)
        for suiv in listeSuivant:
            if rp_rec(suiv):
                return True
        return False

initNode = (initial(),[])
rp_rec(initNode)