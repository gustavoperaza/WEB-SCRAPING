from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://resultados.as.com/resultados/futbol/primera/clasificacion/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
# Equipos
eq = soup.find_all("span", class_="nombre-equipo") #de la isnpeccion de la pagina

equipos=list() #creo una lista vacia para guardar los equipos

count=0
for i in eq:
    if count<20: # establesco un contador para tener solo 20 equipos
       equipos.append(i.text)
    else:
        break

    count+=1
#puntos

pt = soup.find_all("td", class_="destacado") #de la inspeccion de la pagina

puntos=list() #creo una lista vacia para guardar los equipos

count=0
for i in pt:
    if count<20: # establesco un contador para tener solo 20 equipos
       puntos.append(i.text)
    else:
        break
    count+=1


df=pd.DataFrame({"Nombre":equipos,"Puntos":puntos}, index=list(range(1,21)))
print(df)

df.to_csv("Clasificacion.csv", index=False)


