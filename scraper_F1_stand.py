import requests
from bs4 import BeautifulSoup
import pandas as pd 

pagina = requests.get('https://www.formule1.nl/wk-standen-coureurs/')
#print(pagina.status_code)

soup = BeautifulSoup(pagina.content, 'html.parser')

# hieronder is om posities van een coureur te grabben
positions = []
table_rows = soup.find_all(id="f1-calendar-gp-info-tab-drivers")
for tr in table_rows:
    for i in tr.find_all(class_='f1-calendar__gp-table-position'):
        pos = i.text
        positions.append(pos)

# hieronder is om een naam van een coureur te grabben
namen = []
for x in table_rows:
    for n in x.find_all('a'):
        naam = n.text
        namen.append(naam)

# hieronder is om aantal gescoorde punten van een coureur te grabben
punten = []
for y in table_rows:
    for p in y.find_all(class_='col-xs-12 col-sm-2 f1-last-table-col', text=True):
        punt = p.get_text()
        punten.append(punt)

punten_zonder_tab = []
for item in punten:
    a = item.strip(' \t\n\r ')
    punten_zonder_tab.append(a)

# de data omzetten in csv
tabel_coureurs_punten = pd.DataFrame(
    {
        'Positie': positions,
        'Namen': namen,
        'punten': punten_zonder_tab
    }
)
tabel_coureurs_punten.to_csv('stand_coureurs.csv')
print('Het wegschrijven van data naar een csv bestand is gelukt!! Open dit bestand!')
