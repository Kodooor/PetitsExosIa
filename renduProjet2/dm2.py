# Algo de recherche non informée = sans notion de coût (= sans notion d'heuristique)
import random
from math import sqrt


def ecrireLesTaquin(m, n):
    fichier = open("data.txt", "a")
    fichier.write(str(n*n) + "\n")
    nombresDejaAssignees = []
    j = 0
    for i in range(m):
        while j < n*n:
            x = random.randrange(0, n*n)
            if x not in nombresDejaAssignees:
                nombresDejaAssignees.append(x)
                if j == n*n-1:
                    fichier.write(str(x))
                else:
                    fichier.write(str(x) + ",")
                j = j + 1
        fichier.write("\n")
        nombresDejaAssignees = []
        j = 0
    fichier.close()

ecrireLesTaquin(1000, 3)

def initial():
    fichier = open("data.txt", "r")
    x = random.randrange(1, 1000)
    i=1
    ligneFic = ""
    valeurRes = ""
    resultat = []
    for ligne in fichier.readlines():
        if i==x:
            ligneFic = ligne
        else:
            i = i + 1
    ligneFic = ligneFic.replace("\n", "" )
    print(ligneFic)
    for j in range(0, len(ligneFic)):
        if ligneFic[j] != ",":
            valeurRes += ligneFic[j]
        else:
            resultat.append(int(valeurRes))
            valeurRes = ""
    resultat.append((int(valeurRes)))
    return resultat

print(initial())

def final(etat):

    valIndice = -1
    for i in range(len(etat)):
       if etat[i] == 0:
           if i == len(etat) - 1:
               return True
           else:
               return False
       elif etat[i] > valIndice:
           valIndice = etat[i]
       else:
           return False

#Retourne le chemin d'un noeud
def getChemin(noeud):
    return noeud[1]

#Retourne l'état correspondant à un noeud
def getEtat(noeud):
    return noeud[0]

def getCout(noeud):
    return noeud[2]

def getH(noeud):
    return noeud[3]

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
        print(getEtat(i),getCout(i))
    print(getEtat(noeud))
    print(len(chemin))


#nombre de chiffre total - nb chiffre à la bonne place
def h1(etat):
    nbBonneplace = 0
    for i in range(0, len(etat)):
        if(etat[i] == i+1):
            nbBonneplace = nbBonneplace + 1

    return len(etat) - nbBonneplace

print("heuristique :")
print(h1(initial()))

def h2(etat):
    #la distance de manhattan totale(distance de chaque pièce entre sa pos actuelle et sa pos finale)
    tabResultat = []
    subTab = []
    tabFinal = []
    res = 0
    n = sqrt(len(etat))
    n = int(n)

    for a in range(1, n*n):
        if a % n == 1 and a!=1:
            tabFinal.append(subTab)
            subTab = []
            subTab.append(a)
        else:
            subTab.append(a)
    subTab.append(0)
    tabFinal.append(subTab)
    subTab = []

    for i in range(0, len(etat)):
        if i%n == 0 and i!=0:
            tabResultat.append(subTab)
            subTab = []
            subTab.append(etat[i])
        else:
            subTab.append(etat[i])
    tabResultat.append(subTab)

    for j in range(0, len(tabResultat)):
        for k in range(0, len(tabResultat[j])):
            val = tabResultat[j][k]
            for l in range(0, len(tabFinal)):
                for m in range(0, len(tabFinal[l])):
                    if tabFinal[l][m] == val:
                        vallm = (l,m)
            res += abs(j - vallm[0]) + abs(k - vallm[1])
    return res

print(h2(initial()))

def actions():
    return [deplacerValeur]

def deplacerValeur(etat):
    tabResultat = []
    subTab = []
    tabFinal = []
    n = sqrt(len(etat))
    tabInter0 = []
    tabInter1 = []
    tabInter2 = []
    tabInter3 = []

    for i in range(0, len(etat)):
        if i % n == 0 and i != 0:
            tabResultat.append(subTab)
            subTab = []
            subTab.append(etat[i])
        else:
            subTab.append(etat[i])
    tabResultat.append(subTab)
    tabI = []

    for a in range(0, len(tabResultat)):
        tabInter0.append(tabI)
        for b in range(0, len(tabResultat[a])):
            tabI.append(tabResultat[a][b])
        tabI = []

    tabI = []
    for a in range(0, len(tabResultat)):
        tabInter1.append(tabI)
        for b in range(0, len(tabResultat[a])):
            tabI.append(tabResultat[a][b])
        tabI = []

    tabI = []
    for a in range(0, len(tabResultat)):
        tabInter2.append(tabI)
        for b in range(0, len(tabResultat[a])):
            tabI.append(tabResultat[a][b])
        tabI = []

    tabI = []
    for a in range(0, len(tabResultat)):
        tabInter3.append(tabI)
        for b in range(0, len(tabResultat[a])):
            tabI.append(tabResultat[a][b])
        tabI = []

    for j in range(0, len(tabResultat)):
        for k in range(0, len(tabResultat[j])):
            if tabResultat[j][k] == 0:
                try:
                    tabInter0[j][k] = tabInter0[j][k+1]
                    tabInter0[j][k+1] = 0
                    tabFinal.append(tabInter0)
                except:
                    pass
                try:
                    tabInter1[j][k] = tabInter1[j][k-1]
                    tabInter1[j][k-1] = 0
                    tabFinal.append(tabInter1)
                except:
                    pass
                try:
                    tabInter2[j][k] = tabInter2[j+1][k]
                    tabInter2[j+1][k] = 0
                    tabFinal.append(tabInter2)
                except:
                    pass
                try:
                    tabInter3[j][k] = tabInter3[j-1][k]
                    tabInter3[j-1][k] = 0
                    tabFinal.append(tabInter3)
                except:
                    pass
    tabFinal2 = []
    for z in range(0,len(tabFinal)):
        tabII = []
        for y in range(0,len(tabFinal[z])):
            for x in range(0,len(tabFinal[z][y])):
                tabII.append(tabFinal[z][y][x])
        tabIII = (tabII,1)
        tabFinal2.append(tabIII)


    return tabFinal2

print("deplacer valeur")
print(deplacerValeur(initial()))


#Fonction noeudFils en recherche informée
def noeudFils(noeud, heuristic):
    ls = []
    for action in actions():
        listeSuivant = action(getEtat(noeud))
        for elt in listeSuivant:
            etatSuiv = elt[0]
            coutAction = elt[1]
            if not dejavu(etatSuiv, getChemin(noeud)):
                cheminSuivant = list(getChemin(noeud))
                cheminSuivant.append(noeud)
                ls.append((etatSuiv, cheminSuivant, coutAction+getCout(noeud), heuristic(etatSuiv)))
    return ls


def algoHeuristique(listAtt, choix):
    while listAtt:
        noeud = listAtt.pop()
        if final(getEtat(noeud)):
            afficher_sol(noeud)
            return True
        listeSuivant = noeudFils(noeud, h1)
        listAtt.extend(listeSuivant)
        if choix == "glouton":
            listAtt.sort(key=lambda elt:elt[3], reverse=True)
        else:
            listAtt.sort(key=lambda elt:elt[2] + elt[3], reverse=True)

#print(algoHeuristique([initial(), [], 0, 2], "glouton"))

def main(choixAlgo, heuristic):
    init = (initial(), [], 0, heuristic(initial()))
    algoHeuristique([init], choixAlgo)

main("glouton", h1)
