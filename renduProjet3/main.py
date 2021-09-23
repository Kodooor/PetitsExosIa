#Base de regles cuisine
connaissances = {"pate" : ["farine", "oeuf", "beurre", "sel"],
                 "pommes_sucrees" : ["pomme","sucre"],
                 "tarte_aux_pommes": ["pommes_sucrees", "pate"],
                 "tarte_aux_abricots" : ["pate", "abricot"],
                 "tarte_aux_poires" : ["pate", "poire"],
                 "tarte_aux_cerises" : ["pate", "cerise"]
                 }
#Base de regles vitesse
connaissancesVitesse = { "50": ["ville", "leger", "non_proximite_etablissement", "non_limitation_vitesse", "non_danger"],
                         "45": ["ville", "lourd", "non_proximite_etablissement", "non_limitation_vitesse", "non_danger"],
                         "30": ["ville", "leger", "proximite_etablissement", "non_limitation_vitesse"],
                         "90_departementale": ["non_ville", "departementale", "non_limitation_vitesse", "non_danger", "non_proximite_etablissement"],
                         "90_nationale" : ["non_ville", "nationale", "non_4_voies", "non_muret_central", "non_limitation_vitesse", "non_danger", "non_proximite_etablissement"],
                         "110_nationale": ["non_ville", "nationale", "4_voies", "muret_central", "non_limitation_vitesse", "non_danger", "non_proximite_etablissement"],
                         "130" : ["non_ville", "autoroute", "non_limitation_vitesse", "non_danger", "non_proximite_etablissement"],
                         "30_panneau" : ["panneau_30"],
                         "45_panneau" : ["panneau_45"],
                         "60_panneau" : ["panneau_60"],
                         "80_panneau" : ["panneau_80"],
                         "90_panneau" : ["panneau_90"],
                         "110_panneau" : ["panneau_110"],
                         "130_panneau" : ["panneau_130"],
                         "40_pb" : ["ville" ,"mauvaise_visibilite", "danger", "non_proximite_etablissement", "non_limitation_vitesse"],
                         "80" : ["non_ville" ,"mauvaise_visibilite", "danger", "non_proximite_etablissement", "non_limitation_vitesse"],
                         "40_vn" : ["chaussee_glissante","non_limitation_vitesse"]
                         }

faits = []
for c,v in connaissancesVitesse.items():
    for elem in v:
        if elem not in faits:
            faits.append(elem)

#Base de faits cuisine = ["poire", "pomme", "abricot", "farine", "beurre", "oeuf", "sel"]
#Base de faits vitesse = []


def chainageAvant(connaissances ,baseDeFaits):
    ajout = False
    while True:
        change = False
        for cle, valeur in connaissances.items():
            if cle not in baseDeFaits:
                possible = True
                for i in range(len(valeur)):
                    if valeur[i] not in baseDeFaits:
                        possible = False

                if possible:
                    print(cle)
                    baseDeFaits.append(cle)
                    change = True
                    ajout = True
        if change == False:
            print("Aucun élement trouvé")
        return baseDeFaits

# print(connaissances ,chainageAvant(["poire", "pomme", "abricot", "farine", "beurre", "oeuf", "sel"]))


def chainageAvantAvecBut(connaissances, baseDeFaits, fait):

    while True:
        if fait in baseDeFaits:
            print(fait)
            return baseDeFaits
        else:
            change = False
            for cle, valeur in connaissances.items():
                if cle not in baseDeFaits:
                    possible = True
                    for i in range(len(valeur)):
                        if valeur[i] not in baseDeFaits:
                            possible = False

                    if possible:
                        baseDeFaits.append(cle)

                        if cle == fait:
                            print(cle)
                            return baseDeFaits
            if change == False:
                print("Aucun élement trouvé")
                return baseDeFaits

# print(chainageAvantAvecBut(connaissances ,["poire", "pomme", "abricot", "farine", "beurre", "oeuf", "sel"], "oeuf"))
# print(chainageAvantAvecBut(connaissances ,["poire", "pomme", "abricot", "farine", "beurre", "oeuf", "sel"], "tarte_aux_abricots"))
# print(chainageAvantAvecBut(connaissances ,["poire", "pomme", "abricot", "farine", "beurre", "oeuf", "sel"], "pate"))

def chainageArriere(connaissances, baseDeFaits, fait):
    if fait in baseDeFaits:
        return baseDeFaits
    else:
        if fait not in connaissances.keys():
            return False
        ok = False
        for regle in connaissances[fait]:
            print(regle)
            p = True
            for f in regle:
                p = p and chainageArriere(connaissances,baseDeFaits,f)
            if p :
                return True

# print(chainageArriere(connaissances, ["poire", "pomme", "abricot", "farine", "beurre", "oeuf", "sel"], "pate"))

def tell(connaissances, cle, valeur):
    connaissances[cle] = valeur

# tell(connaissances, "chausson_aux_pommes", ["pate_feuilleté", "compote_de_pomme"])
# print(connaissances)

def main():
    faitsVitesse = []
    while True:
        print("Voici les faits possibles : ")
        fts = ""
        for elm in faits:
            fts += elm + " || "
        print(fts)
        f = input("Entrez les caractéristiques de la route (\"continuer\" si vous avez fini et que vous voulez passer au choix de l'algo) : ")
        if f in faits:
            if f not in faitsVitesse:
                faitsVitesse.append(f)
                print("Fait "+ f +" ajouté")
            else:
                print("Fait déja existant")
            print("=======================================================================================")
        elif f == "continuer":
            a = input(
                "Voici les algos possibles : 1 = Chainage avant || 2 = Chainage avant avec but || 3 = Chainage arriere : ")
            if a == "1":
                print("Vitesse conseillée")
                chainageAvant(connaissancesVitesse, faitsVitesse)
                print("=======================================================================================")

            elif a == "2":
                b = input("Entrez votre but : ")
                chainageAvantAvecBut(connaissancesVitesse, faitsVitesse, b)
                print("=======================================================================================")

            elif a == "3":
                b = input("Entrez votre but : ")
                print(chainageArriere(connaissancesVitesse,faitsVitesse,b))
                print("=======================================================================================")

            else:
                print("Chiffre non disponible !")

        else:
            print("/!\\ Fait pas dans la base de faits /!\\")
            print("=======================================================================================")


    print(faitsVitesse)

main()
