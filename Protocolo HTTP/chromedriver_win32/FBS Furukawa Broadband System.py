import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import  Options


listaProdutos = []
listaObs = []
cont = 0

while cont != 1:
    cont +=1
    
    url = (f'https://www.furukawalatam.com/pt-br/catalogo-de-produtos-categoria/FBS?page={cont}')

# Pegar conteudo HTML a partir da URL

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=r'C:\xampp\htdocs\diretorio\Web-Scraping\Protocolo HTTP\chromedriver_win32\chromedriver.exe')
    driver.get(url)

    time.sleep(15)

    element = driver.find_element_by_xpath("//div[@class='container d-flex mt-2']")
    html_content = element.get_attribute("outerHTML")

    #Parsear o conteudo HTML  - BeautifulSoup

    soup = BeautifulSoup(html_content, "html.parser")
    descricao = soup.find_all('p', attrs={'product-name title break-all'})
    observacao = soup.find_all('p', attrs={'pb-3 fillterBy'}) 

    for descri in descricao:
        descricao = descri.get_text()
        listaProdutos.append(descricao)
        
    for obser in observacao:
        obs = obser.get_text()
        listaObs.append(obs)
        
driver.quit()

with open('C:/xampp/htdocs/diretorio/Web-Scraping/Relatorios.csv/Scraping-Furukawa-FBS_DESCRI.csv', 'a', encoding='utf=8') as file:
    file.writelines('\n'.join(listaProdutos))
    file.close()

with open('C:/xampp/htdocs/diretorio/Web-Scraping/Relatorios.csv/Scraping-Furukawa-FBS_OBS.csv', 'a', encoding='utf=8') as file:
    file.writelines('\n'.join(listaObs))
    file.close()