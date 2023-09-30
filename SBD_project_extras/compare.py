from tabulate import tabulate
import csv
import os
import matplotlib.pyplot as plt

results5, results1 = {}, {}
maxs = []

for config in ["bogdan", "lukasz", "moi", "sebastiao"]:
    repertoire = 'exports/' + config + '/'
    chemin_fichier = os.path.join(repertoire, "5vu.csv")
    with open (chemin_fichier, "r") as fichier_csv:
        lecteur_csv = csv.DictReader(fichier_csv)

        dictionnaire = {}

        for ligne in lecteur_csv:
            for colonne, valeur in ligne.items():
                if colonne not in dictionnaire:
                    dictionnaire[colonne] = []
                dictionnaire[colonne].append(int(valeur))

    results5[config] = (dictionnaire)

    chemin_fichier = os.path.join(repertoire, "1vu.csv")
    with open (chemin_fichier, "r") as fichier_csv:
        lecteur_csv = csv.DictReader(fichier_csv)

        dictionnaire = {}

        for ligne in lecteur_csv:
            for colonne, valeur in ligne.items():
                if colonne not in dictionnaire:
                    dictionnaire[colonne] = []
                dictionnaire[colonne].append(int(valeur))

    results1[config] = (dictionnaire)


for config in ["bogdan", "lukasz", "moi", "sebastiao"]:
    plt.plot(results1[config]['Heure'], results1[config]['Valeur'], '-', label= config + " results: " + str(results1[config]['Heure'][-1]) + "s")
    maxs.append(max(results1[config]['Valeur']))

plt.xlabel('Elasped time')
plt.ylim(0, max(maxs))
plt.ylabel('Number of query per hours')
plt.title('Comparaison of our configurations with 1 virtual user')
plt.legend()
plt.grid(True)
plt.savefig("SBD/images/all_1vu.png")  
plt.show()
plt.close()

for config in ["bogdan", "lukasz", "moi", "sebastiao"]:
    plt.plot(results5[config]['Heure'], results5[config]['Valeur'], '-', label= config + " results: " + str(results5[config]['Heure'][-1]) + "s")
    maxs.append(max(results5[config]['Valeur']))

plt.xlabel('Elasped time')
plt.ylim(0, max(maxs))
plt.ylabel('Number of query per hours')
plt.title('Comparaison of our configurations with 5 virtual users')
plt.legend()
plt.grid(True)
plt.savefig("SBD/images/all_5vu.png")  
plt.show()
plt.close()


