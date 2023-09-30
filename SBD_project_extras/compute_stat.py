from tabulate import tabulate
import csv
import os
import statistics
import matplotlib.pyplot as plt

def stat(config: str): #create statistics tables
    files = read_exports(config)
    infos_vu  = [['', 'Mean', 'Median', 'Standard deviation', 'Variance', 'Time']]
    infos_qps = [['', 'Mean', 'Median', 'Standard deviation', 'Variance', 'Time']]

    for key in files:
        row = ""
        if key[-6:] == "vu.csv":   
            row = str(key[:-6]) + " virtual users"
            values_int = [int(value) for value in files[key]['Valeur']]
            mean = int(statistics.mean(values_int))
            median = int(statistics.median(values_int))
            std = int(statistics.stdev(values_int))
            var = int(statistics.variance(values_int))
            time = files[key]['Heure'][-1]
            infos_vu.append([row, mean, median, std, var, time])

        elif key[-7:] == "qps.csv":
            row = str(key[:-7]) + " queries per set"
            values_int = [int(value) for value in files[key]['Valeur']]
            mean = int(statistics.mean(values_int))
            median = int(statistics.median(values_int))
            std = int(statistics.stdev(values_int))
            var = int(statistics.variance(values_int))
            time = files[key]['Heure'][-1]
            infos_qps.append([row, mean, median, std, var, time])

    # tableaux en images pour report
    infos_vu.sort(key=lambda x: int(x[0].split()[0]) if len(x[0].split()) > 0 else 0) # order by nb of user
    fig_vu, ax_vu = plt.subplots()
    ax_vu.axis("off")
    table_vu = ax_vu.table(cellText=infos_vu, loc="center")
    table_vu.auto_set_font_size(False)
    table_vu.set_fontsize(12)
    table_vu.scale(1.4, 1.4)
    table_vu.auto_set_column_width(range(len(infos_vu)+1))
    fig_vu.savefig("SBD/tables/" + config + "_infos_vu.png", bbox_inches='tight')
    plt.show()
    plt.close(fig_vu) 
    
    infos_qps.sort(key=lambda x: int(x[0].split()[0]) if len(x[0].split()) > 0 else 0) # order by query per set
    fig_qps, ax_qps = plt.subplots()
    ax_qps.axis("off")
    table_qps = ax_qps.table(cellText=infos_qps, loc="center")
    table_qps.auto_set_font_size(False)
    table_qps.set_fontsize(12)
    table_qps.scale(1.4, 1.4)
    table_qps.auto_set_column_width(range(len(infos_qps)+1))
    fig_qps.savefig("SBD/tables/" + config + "_infos_qps.png", bbox_inches='tight')
    plt.show()
    plt.close(fig_qps)
    return


def read_exports(config): # create dictionnaire avec cahque fichier en key et en value un matrice avec les colomnes
    repertoire = 'exports/' + config + '/'
    files_retour = {}
    for fichier in os.listdir(repertoire):
        if fichier.endswith('.csv'):
            chemin_fichier = os.path.join(repertoire, fichier)
            with open (chemin_fichier, "r") as fichier_csv:
                lecteur_csv = csv.DictReader(fichier_csv)

                dictionnaire = {}

                for ligne in lecteur_csv:
                    for colonne, valeur in ligne.items():
                        if colonne not in dictionnaire:
                            dictionnaire[colonne] = []
                        dictionnaire[colonne].append(valeur)

            files_retour[fichier] = (dictionnaire)
    return files_retour
    