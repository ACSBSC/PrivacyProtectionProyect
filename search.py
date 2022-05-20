import pandas as pd
import numpy as np


'''
2003 Survey

We search for:
-Woman
-between 43 and 46 years old at the time of the survey
-Is an Architect
-Worked as an independent architect at the time of the survey
-borned in Barcelona
-lives in Barelona
-has 2-3 children

'''

#We know that her level of studies is of University and had at least 2 times sex and at least with one partner
'''
Having these pieces of information, we decided to get form the survey the results of 
"Personas de 18 a 49 que han tenido relaciones sexuales alguna vez en  la vida por sexo, 
estudios y número de parejas sexuales en la vida."

AND

"Personas de 18 a 49 que han tenido relaciones sexuales alguna vez en  la vida por sexo, 
grupo de edad, estudios y edad de inicio de las  relaciones."

'''
df = pd.read_csv('./CSV/EdadySexo/Estudios/02008.csv', sep=';')
nr_partners = df.loc[(df['Sexo'] == 'Mujeres') & (df['Estudios']=='Universitarios')]
df = pd.read_csv('./CSV/EdadySexo/Estudios/02006.csv', sep=';')
women_had_sex = df.loc[(df['Sexo'] == 'Mujeres') & (df['Estudios']=='Universitarios') & (df['Grupo de edad']=='De 40 a 49 años')]

print(nr_partners)
print(women_had_sex)


'''

'''

