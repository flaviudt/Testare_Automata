# ######################### PROPRIETATILE SI METODELE UNUI WEBELEMENT #########################

"""
WebElement = un WebElement reprezinta un element dintr-o pagina HTML.

Obiectul (variabila) care reprezinta un Web Element nu e altceva decat o referinta catre acel element.

Daca se face un refresh pe pagina sau daca elementul se reincarca,
referintele pot deveni invalide si primim un StaleElementReferenceException
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

LINK = "https://demoqa.com/login"

USER = "ta41"
PASS = "Iloveautomation41!"

driver.get(LINK)

"""
# ############## METODELE CLASEI WEBELEMENT ##############
"""

# ############ send_keys() - simuleaza tastarea de caractere pe un element
username_input = driver.find_element(By.ID, "userName")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login")
username_input.send_keys(USER)
password_input.send_keys(PASS)

# ############ clear() - sterge atributul "value" al unui element - adica goleste textul de pe input
password_input.clear()

# ############ is_displayed() - returneaza un boolean
# True: daca un element EXISTA si este VIZIBIL
# False: daca un element EXISTA dar e INVIZIBIL

assert username_input.is_displayed(), "Elementul username input nu este vizibil"

element_invizibil = driver.find_element(By.ID, "output")
assert not element_invizibil.is_displayed(), "Elementul este vizibil"

driver.get("https://demoqa.com/automation-practice-form")
time.sleep(2)

# ############ is_selected() - returneaza un boolean
# True: daca un element (checkbox, radio button, dropdown) este selectat
# False: daca un element (checkbox, radio button, dropdown) nu este selectat

radio_button_male = driver.find_element(By.XPATH, "//input[@value='Male']")
radio_button_female = driver.find_element(By.XPATH, "//input[@value='Female']")

# GRESIT: butoanele sunt acoperite de label-uri. Va trebui sa dam click pe text, nu pe buton
# radio_button_male.click()

label_male = driver.find_element(By.XPATH, "//label[text()='Male']")
label_male.click()

assert radio_button_male.is_selected()
assert not radio_button_female.is_selected()

# ############ submit() - se poate folosi cand avem de-a face cu formulare pe care le trimitem la server
# echivalent cu click()
submit_button = driver.find_element(By.ID, "submit")

submit_button.submit()
time.sleep(3)

# ############ is_enabled() - returneaza un boolean
# # True: daca un element este activ
# # False: daca un element este inactiv (are atributul disabled)

select_state_input = driver.find_element(By.ID, "react-select-3-input")
select_city_input = driver.find_element(By.ID, "react-select-4-input")

assert select_state_input.is_enabled()
assert not select_city_input.is_enabled()

# ############ get_attribute() - returneaza valoarea unui atribut specificat
mobile_number_input = driver.find_element(By.ID, "userNumber")

expected_placeholder = "Mobile Number"
actual_placeholder = mobile_number_input.get_attribute("placeholder")
assert expected_placeholder == actual_placeholder, "Placeholder-ul nu are valoarea asteptata"


# ############## PROPRIETATI ALE CLASEI WEBELEMENT ##############

# ############ size - ne da un dict care contine inaltimea si latimea elementului (in pixeli)
dimensiune_element = mobile_number_input.size
print(dimensiune_element)
print(type(dimensiune_element))

# ############ location - ne da un dict care contine pozitia elementului pe ecran (coordonate x,y)
pozitie_element = mobile_number_input.location
print(pozitie_element)
print(type(pozitie_element))


# ############ tag_name - ne da tag-ul HTML al elementului
tag_element = mobile_number_input.tag_name
print(tag_element)

# ############ text - ne da textul dintr-un element
# ATENTIE!!! - pentru a lua textul de pe un input se foloseste get_attribute("value")
titlu = driver.find_element(By.XPATH, "//h5")
text_titlu = titlu.text
assert text_titlu == "Student Registration Form"

driver.quit()
