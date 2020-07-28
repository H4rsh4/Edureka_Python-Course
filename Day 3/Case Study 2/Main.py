#No fields of data of customers who are ineligible for loan in the data source


import pandas as pd

bank_data = 'E:\Edureka_Python-Course\Day 3\Case Study 2\\bank-data.csv'
df_raw = pd.read_csv(bank_data, low_memory=False)

jobs = {str(j).lower() for j in df_raw.job}
print(jobs)

eligible_jobs = []
#print(jobs)

max_age = max(df_raw.age)
min_age = min(df_raw.age)


print(df_raw.head())

def check_eligibility(profession:str):
    return True if profession.lower() in eligible_jobs else False

while True:
    print('If you want to exit, type "exit" in the profession')
    profession = str(input('Profession of the client: ')).strip()
    
    if check_eligibility(profession):
        print('Client is eligible')
    else:
        print("Not eligible")