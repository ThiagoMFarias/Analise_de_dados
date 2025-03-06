import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options = Options()
options.headless = True 
driver = webdriver.Firefox(options=options)

url = "https://www.uece.br/uece/noticias/"
driver.get(url)
driver.implicitly_wait(5)  

def carregar_noticias_ate_limite(limite=50):
    noticias = []
    
    while len(noticias) < limite:
        time.sleep(2) 
        
        try:
            posts = driver.find_element(By.CLASS_NAME, "cc-posts")
            posts_html = posts.get_attribute('innerHTML')
            soup = BeautifulSoup(posts_html, 'html.parser')
            
            posts_title = soup.find_all("h3")
            posts_description = soup.find_all(class_="cc-post-excerpt")
            
            for title, desc in zip(posts_title, posts_description):
                noticia = {
                    "title": title.text.strip(),
                    "description": desc.text.strip()
                }
                if noticia not in noticias:
                    noticias.append(noticia)
                    if len(noticias) >= limite:
                        break
        except Exception as e:
            print(f"Erro ao obter notícias: {e}")
            break
        
        try:
            botao_veja_mais = driver.find_element(By.CLASS_NAME, "cc-button")
            driver.execute_script("arguments[0].scrollIntoView();", botao_veja_mais)
            time.sleep(1)  
            botao_veja_mais.click()
        except Exception:
            print("Botão 'Veja Mais' não encontrado ou fim das notícias.")
            break
    
    return noticias

noticias_extraidas = carregar_noticias_ate_limite(limite=50)

if noticias_extraidas:
    df = pd.DataFrame(noticias_extraidas)
    df.to_json('results.json', orient="records", force_ascii=False, indent=4)
    print("Arquivo 'results.json' gerado com sucesso!")
    print("Success in Web Scraping! 50 notícias extraídas.")
else:
    print("Nenhuma notícia foi extraída.")
    
driver.quit()