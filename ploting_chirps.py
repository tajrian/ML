# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 07:15:08 2019

@author: Tajri
"""

import seaborn as sns; sns.set(color_codes=True)
import pandas as pd
import matplotlib.pyplot as plt

chirp_data = pd.read_csv("chirps.csv")

g = sns.lmplot(x="Chirps_15s",y="Temp_C",data = chirp_data)

plt.title('Cricket Chirp and Temperature')

plt.show()
