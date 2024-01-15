import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

LINK = "https://formy-project.herokuapp.com/form"

"""
########### pytest ###########

pip install pytest
pip install pytest-xdist (pentru teste in paralel)

Pytest este un framework de testare care poate fi folosit atat pentru Unit Testing cat si pentru Integration Testing sau 
Functional Testing.

Pentru a rula toate testele dintr-un fisier, se va folosi terminalul

### Teste rulate in mod secvential (unul dupa celalalt):
Pentru a rula testele unul dupa altul, se foloseste comanda:

 pytest calea_catre_fisier/fisier.py     

-> in cazul nostru:     pytest w2/c10_firefox_si_pytest.py

### Teste rulate in paralel (mai multe deodata):
Pentru a rula teste in paralel, se foloseste comanda:

    pytest calea_catre_fisier/fisier.py -n x  (unde x este nr-ul de teste care merg in paralel)  
     
    -> in cazul nostru:     pytest w2/c10_firefox_si_pytest.py -n 2
"""


def test_chrome():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(LINK)
    expected_url = "https://formy-project.herokuapp.com/form"
    actual_url = driver.current_url
    time.sleep(10)
    assert expected_url == actual_url, f"Invalid URL, expected {expected_url}, but found {actual_url}"
    driver.quit()


def test_firefox():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get(LINK)
    expected_url = "https://formy-project.herokuapp.com/form"
    actual_url = driver.current_url
    time.sleep(10)
    assert expected_url == actual_url, f"Invalid URL, expected {expected_url}, but found {actual_url}"
    driver.quit()

