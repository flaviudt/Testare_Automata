import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import calendar
import datetime

"""
########### ASSERT ###########

assert este sintaxa care evalueaza o conditie si returneaza o eroare in cazul in care conditia nu este adevarata

Practic, in testare automata, un assert este cel care decide daca testul e "trecut" sau "picat" (passed sau failed) 
"""

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://formy-project.herokuapp.com/datepicker")

id_date_picker = "datepicker"


# Definim o functie pentru deschiderea date picker-ului pe care o vom refolosi
def open_date_picker():
    driver.find_element(By.ID, id_date_picker).click()


# Ex1 - Deschidem date picker-ul si dam click pe ziua curenta
# Ce observam?
# Cum putem sa facem programul sa ruleze corect indiferent data în care suntem?
# Care este diferenta dintre ziua de astazi si celelalte zile ale calendarului? -> clasa elementelor <td>

open_date_picker()
time.sleep(1)

# verificam faptul ca inputul corespunzator datepickerului nu afiseaza nicio data
assert len(driver.find_element(By.ID, id_date_picker).get_attribute("value")) == 0

driver.find_element(By.CSS_SELECTOR, ".today.day").click()

# verificam faptul ca dupa click pe ziua curenta inputul afiseaza un text cu lungimea mai mare ca 0
assert len(driver.find_element(By.ID, id_date_picker).get_attribute("value")) > 0
time.sleep(1)

# Ex2 - Deschidem date picker-ul si afisam cate zile are luna curenta.
# Trebuie sa mearga corect indiferent de data in care rulam scriptul

open_date_picker()

# Salvam elementele intr-o lista, apoi afisam marimea listei
lista_zile = driver.find_elements(By.XPATH, "//td[@class='day' or contains(@class, 'today')]")

print(f"Luna curenta are {len(lista_zile)} zile")

# cod pentru a lua dinamic numarul de zile din luna in care ne aflam
now = datetime.datetime.now()
numar_zile_luna_curenta = calendar.monthrange(now.year, now.month)[1]

assert numar_zile_luna_curenta == len(lista_zile)


# Ex 3 - Navigam in calendar folosind butonul » (Next) pana cand ajungem in anul 2024

def get_calendar_month_and_year_text():
    return driver.find_element(By.CLASS_NAME, "datepicker-switch").text


next_button = driver.find_element(By.CLASS_NAME, "next")

print(get_calendar_month_and_year_text())

while "2024" not in get_calendar_month_and_year_text():
    next_button.click()
    time.sleep(1)

# Assert cu mesaj de eroare
assert "2024" in get_calendar_month_and_year_text(), "Eroare. Textul cautat nu este afisat"


