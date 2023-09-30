from compute_stat import stat
from vu import txt_values_to_plot_and_csv
# bogdan lukasz moi sebastiao 

tested_vu = [1, 5, 10, 20, 50] # select only perfomed  1, 5, 10, 20, 50 
tested_qps = [2, 5 , 10, 20] # select only performed 2, 5 , 10, 20

for config in ["sebastiao"]:

    txt_values_to_plot_and_csv(config, tested_vu, "vu")
    txt_values_to_plot_and_csv(config, tested_qps, "qps")
    stat(config)

