#FyntraCustomerData.csv


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, confusion_matrix

import matplotlib.pyplot as plt
from seaborn import jointplot, pairplot


DATA_PATH = 'E:/Edureka_Python-Course/Data Sources/Day_6/'
df_raw = pd.read_csv(DATA_PATH+'FyntraCustomerData.csv', low_memory=False)


df_raw.info()


df_raw.head().transpose()


df_raw.corr()


jointplot(df_raw.Time_on_Website, df_raw.Yearly_Amount_Spent, data=df_raw, kind='kde')


jointplot(df_raw.Time_on_App, df_raw.Yearly_Amount_Spent, data=df_raw, kind='kde')


pairplot(df_raw)


plt.scatter(df_raw.Length_of_Membership, df_raw.Yearly_Amount_Spent)


"""
Sourced from GeeksforGeeks
"""
def estimate_coef(x, y): 
    # number of observations/points 
    n = np.size(x) 
  
    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 
  
def plot_regression_line(x, y, b): 
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
  
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
  
    # plotting the regression line 
    plt.plot(x, y_pred, color = "g") 
  
    # putting labels 
    plt.xlabel('x') 
    plt.ylabel('y') 
  
    # function to show plot 
    plt.show() 


coef = estimate_coef(df_raw.Length_of_Membership, df_raw.Yearly_Amount_Spent)

plot_regression_line(df_raw.Length_of_Membership, df_raw.Yearly_Amount_Spent, coef)



train_x, test_x, train_y, test_y = train_test_split(df_raw.drop(['Yearly_Amount_Spent',
                                                                 'Email',
                                                                 'Address',
                                                                 'Avatar']
                                                                , axis=1),
                                                    df_raw.Yearly_Amount_Spent,
                                                    test_size=0.2,
                                                    random_state=85)
train_x


model_linreg = LinearRegression()
model_linreg.fit(train_x, train_y)


y_pred = model_linreg.predict(test_x)


 == len()


plt.scatter(x=test_x.Length_of_Membership , y=y_pred)
plt.scatter(x=test_x.Length_of_Membership , y=test_y)



def RMSE(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))


print(f'Root Mean Squared Error: {RMSE(test_y, y_pred)}')
