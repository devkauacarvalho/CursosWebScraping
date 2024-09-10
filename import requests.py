import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.kabum.com.br'  
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# para encontrar os produtos (ajuste os seletores conforme necessário)
produtos = []
for item in soup.select('.produto'):  
    nome = item.select_one('.nome-produto').text.strip()
    preco = item.select_one('.preco-produto').text.strip()
    produtos.append({'Nome': nome, 'Preço': preco})


df = pd.DataFrame(produtos)
df.to_excel('produtos_intelbras.xlsx', index=False)    
