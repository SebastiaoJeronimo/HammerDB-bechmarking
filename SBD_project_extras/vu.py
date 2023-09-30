from ast import List
import matplotlib.pyplot as plt
import numpy as np
import csv

def txt_values_to_plot_and_csv(config: str, tested_values, param: str):
    X, Y = [[] for _ in range(len(tested_values))], [[] for _ in range(len(tested_values))]
    maxs=[]

    for test in range(len(tested_values)):
        file_name = config + "/" + str(tested_values[test]) + param + ".txt"
        with open(file_name, "r") as fichier:
            lignes = fichier.readlines()

        heures = []
        print(test)
        for ligne in lignes:
            valeurs = ligne.split()
            if valeurs != []: 
                heure_str = valeurs[7] 
                heure_int = int(heure_str[:2])*3600 + int(heure_str[3:5])*60 + int(heure_str[6:8])
                heures.append(heure_int) #heures for plot x[test] for csv
                Y[test].append(int(valeurs[0])) 

        time_base = heures[0]
        for heure in heures:
            X[test].append(heure - time_base)

        with open("exports/" + file_name[:-4] + ".csv", 'w', newline='') as fichier_csv:
            writer = csv.writer(fichier_csv)
            writer.writerow(['Heure', 'Valeur'])  # Écrire l'en-tête du fichier .csv
            writer.writerows(np.transpose([X[test], Y[test]]))  
        if param == "vu":
            plt.plot(X[test], Y[test], '-', label= str(tested_values[test])+" virtuals users: " + str(X[test][-1]) + "s")
        if param == "qps":
            plt.plot(X[test], Y[test], '-', label= str(tested_values[test])+" queries per set: " + str(X[test][-1]) + "s")
        maxs.append(max(Y[test]))


    plt.xlabel('Elasped time')
    plt.ylim(0, max(maxs))
    plt.ylabel('Number of query per hours')
    if param == "vu":     
        plt.title('Importance of the number of virtual users')
    if param == "qps":
        plt.title('Importance of the number of queries per set')

    plt.legend()
    plt.grid(True)
    plt.savefig("SBD/images/results_" + config + "/" + param + ".png")  
    plt.show()
    plt.close()

    return

