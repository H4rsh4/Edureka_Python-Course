import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


DATA_PATH = '/home/h4rsh4/learn/Edureka_Python-Course/Data Sources/Day_5/'


#hw = hollywood movies csv
hw_df_raw = pd.read_csv(DATA_PATH+'HollywoodMovies.csv',low_memory=False)
hw_df_raw


hw_df_raw.columns


#Question 1
quest_movies = hw_df_raw[hw_df_raw['Story'] == 'Quest']
quest_movies[quest_movies['RottenTomatoes'] == max(quest_movies['RottenTomatoes'])].Movie


#Question 2
hw_df_raw[hw_df_raw.TheatersOpenWeek == max(hw_df_raw.TheatersOpenWeek)].Genre


#Question 3
hw_df_raw.sort_values(by = 'Budget', ascending=False).Movie[:5]


#Question 4
fig, ax = plt.subplots(figsize=(20,5))
ax.set_title("World Gross vs RottenTomatoes's score (sorted by rating)")
ax.set_ylabel('Rating')
ax.set_xlabel('World Gross')
ax.scatter( hw_df_raw.sort_values(by='RottenTomatoes').WorldGross, hw_df_raw.sort_values(by='RottenTomatoes').RottenTomatoes)


#Question 5
#5.1
q5_df_raw = pd.DataFrame(data={'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'], 
'age': [42, 52, 36, 24, 73], 
'preTestScore': [4, 24, 31, ".", "."],
'postTestScore': ["25,000", "94,000", 57, 62, 70]})
#5.2
q5_df_raw.to_csv('example.csv', sep=',', index=False)
#5.3
q5_df_raw = pd.read_csv('example.csv', low_memory=False)
q5_df_raw.columns


#5.4
q54_df = pd.read_csv('example.csv', header=None)
q54_df


#5.5
q55_df = pd.read_csv('example.csv', index_col=['first_name', 'last_name'])
q55_df


#5.6
q55_df == np.nan


#5.7
q57_df_raw = pd.read_csv('example.csv', skiprows=3)
q57_df_raw


#5.8
q58_df_raw = pd.read_csv('example.csv', sep=None, thousands=',')
q58_df_raw


#Part 6
q6_series = pd.Series(data=['Amit','Bob', 'Kate', 'A', 'b', np.nan, 'Car' 'dog', 'cat'])
q6_series


#6a
q6_series.str.lower()


#6b
q6_series.str.upper()


q6_series.str.len()


#6.2
q62_series = pd.Series(data=[' Atul', 'John ', ' jack ', 'Sam'])


#6a
q62_series.str.strip()


#6b
q62_series.str.lstrip()


#6c
q62_series.str.rstrip()


#6.3
q63_series = pd.Series(data=['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'])
q63_series


#6.3a
q63_series.str.split('_')


#6.3 b
q63_series.str.split('_')[0][0]


q633 = q63_series.str.split('_')
def ret_str(st):
    if type(st) get_ipython().getoutput("= list:")
        return st
    return ','.join(st)
q633.apply(ret_str)


#6.4
q64_series = pd.Series(data=['A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat'])
def replace_X_dog(var):
    if type(var) == str:
        if 'X' in var:
            return var.replace('X', 'XX-XX')
        if 'dog' in var:
            return var.replace('dog', 'XX-XX')
    return var
q64_series.apply(replace_X_dog)


#6.5
q65_series = pd.Series(data=['12', '-$10', '$10,000']).str.replace('$', '')
q65_series


#6.6
q66_series = pd.Series(data=['india 1998', 'big country', 'Ab bA',np.nan])
for var in q66_series:
    if type(var) == str:
        if var.islower():
            print(var[::-1])
            continue
    print(var)
q66_series



#6.7
q67_series = pd.Series(data=['1', '2', '1a', '2b', '2003c'])
print('\n'.join([str(str(i).isalnum()) for i in q67_series]))


#6.8
q68_series = pd.Series(data=['1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'])
for val in q68_series:
    print('A' in val)


#6.9
#unclear objective
q69_series = pd.Series(data=['a', 'a|b', np.nan, 'a|c'])
chars = ['a', 'b', 'c']
for val in q69_series:
    if type(val) == str:
        print(any(
                    [
                        (i in chars) for i in val
                    ]
                ),
              end='\t'
             )
    else:
        print(False, end='\t')


q610_df_l = pd.DataFrame(data={'key': ['One', 'Two'], 'ltable': [1,2] })
q610_df_r = pd.DataFrame(data={'key': ['One', 'Two'], 'rtable': [4,5] })

merged_df = pd.merge(q610_df_l, q610_df_r, on='key') # inner merge
merged_df



