import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


DATA_PATH = 'E:/Edureka_Python-Course/Data Sources/Day_6/'
df_raw = pd.read_csv(DATA_PATH+'cereal.csv', low_memory=False)


df_raw.info()


len(df_raw.mfr.unique())


df_raw.head().transpose()


plt.hist(df_raw.sugars)


plt.hist(df_raw.vitamins)


df_raw.name


dict((v,k) for k,v in di.items())


x = df_raw.mfr.copy()
di = {
    'N': 'Nabisco',
    'Q': 'Quaker Oats',
    'K': 'Kelloggs',
    'R': 'Raslston Purina',
    'G': 'General Mills' ,
    'P' :'Post' ,
    'A':'American Home Foods Products'
}
x.replace(to_replace=di)


bar1_heights = [(mfr,len(df_raw[df.mfr == mfr])) for mfr in df_raw.mfr.unique()]
plt.bar(df_raw.mfr, bar1_heights)


bar1_heights = [(mfr,len(df_raw[df_raw.mfr == mfr])) for mfr in df_raw.mfr.unique()]
bar1_heights


df_raw.mfr.replace(di)


df_raw.mfr



