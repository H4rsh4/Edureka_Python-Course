#[UNCLEAR OBJECTIVE]


import pandas as pd

bank_data = 'E:\Edureka_Python-Course\Day 3\Case Study 2\\bank-data.csv'
df_raw = pd.read_csv(bank_data, low_memory=False)

jobs = {j for j in df_raw.job}
print(jobs)

eligibility = {job:(True if elig) for }
#print(jobs)

''''''
print(df_raw.head())

def check_eligibility(profession:str):
    return True if profession in eligible_jobs else False

while True:
    print('If you want to exit, type "exit" in the profession')
    profession = str(input('Profession of the client: ')).strip()
    
    if check_eligibility(profession):
        print('Client is eligible')