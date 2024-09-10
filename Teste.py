import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://cursos.intelbras.com.br/'
cursos = []  
def scrape_page(url): 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

   
    for item in soup.select('.curso-item'):  # Procurar o cam
        nome = item.select_one('.curso-nome').text.strip()  
        link = item.select_one('a')['href']  
        
       
        if not link.startswith('http'):
            link = base_url + link
        
        
        cursos.append({'Nome': nome, 'Link': link})

def get_next_page_url(soup):
    next_button = soup.select_one('.pagina-seguinte') 
    if next_button and 'href' in next_button.attrs:
        return next_button['href']
    return None


next_page_url = base_url
scrape_page(next_page_url)

while next_page_url:
    response = requests.get(next_page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    next_page_url = get_next_page_url(soup) 
    if next_page_url and not next_page_url.startswith('http'):
        next_page_url = base_url + next_page_url  
    if next_page_url:
        scrape_page(next_page_url)  

df = pd.DataFrame(cursos)
df.to_excel('Cursos_Intelbras.xlsx', index=False)
