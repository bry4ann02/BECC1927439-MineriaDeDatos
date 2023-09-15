import pandas as pd #importamos pandas 
url = "https://raw.githubusercontent.com/erikgregorywebb/data/main/data/spotify-charts-daily-2020-10-07.csv" #escribimos la url de nuestro csv


df = pd.read_csv(url) #creamos un dataframe con pandas para ver nuestro url
df.to_csv('spotify-charts-daily-2020-10-07.csv', index =False) #lo descargamos en forma de df con index falsos para que no tenga formato y listo
