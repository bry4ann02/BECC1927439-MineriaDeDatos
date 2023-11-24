import pandas as pd #importamos pandas 
url = "https://raw.githubusercontent.com/GabeAvinaz/Proj_1_MLS_Player_Salary_-Projections/main/data/mls_salaries_masterlist.csv" #escribimos la url de nuestro csv


df = pd.read_csv(url) #creamos un dataframe con pandas para ver nuestro url
df.to_csv('mls_salaries_masterlist.csv', index = False) #lo descargamos en forma de df con index falsos para que no tenga formato y listo
