import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


"""
1. Intrati pe site-ul https://www.elefant.ro/
"""

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

LINK = "https://www.elefant.ro/"
driver.get(LINK)
driver.maximize_window()
time.sleep(1)

cookie_cancel = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
cookie_cancel.click()
time.sleep(1)


"""
2. Cautati un produs la alegere (iphone 14) si verificati ca s-au returnat
cel putin 10 rezultate ([class="product-title"])
"""

search_button = driver.find_element(By.CLASS_NAME, "js-has-overlay")
search_button.click()
search_button.send_keys("iphone 14")
search_button.send_keys(Keys.ENTER)
time.sleep(1)

iphone14_items = driver.find_elements(By.CSS_SELECTOR, '[class="product-title"]')
print(len(iphone14_items))
assert len(iphone14_items) > 10

"""
3. Extrageti din lista produsul cu pretul cel mai mic [class="current-price "]
din primele 10 produse gasite
(puteti sa va folositi de find_elements)
"""

# v1
# iphone14_items = driver.find_elements(By.CSS_SELECTOR, '[class="current-price "]')
# print(iphone14_items)
# new_list =[]
# for elem in iphone14_items:
#     print(elem.text)
#     print(elem.get_property('current-price'))
#     new_list.append(elem)
#


# V2
dropdown_button = Select(driver.find_element(By.CLASS_NAME, "js-sortSelection"))
dropdown_button.select_by_visible_text('Pret crescator')
time.sleep(2)

lowest_price_product = driver.find_element(By.CSS_SELECTOR, "[class='product-tile js-product-tile js-product-tile-0f68804d-7ceb-44ab-af4a-4060f9be1b7d']")
print(lowest_price_product.text)
lowest_price_product.click()
time.sleep(3)

"""
4. Extrageti titlul paginii si verificati ca este corect
"""
driver.get(LINK)
expected_title = "elefant.ro - mallul online al familiei tale! • Branduri de top, preturi excelente • Peste 500.000 de produse pentru tine!"
actual_title = driver.title
assert expected_title == actual_title

"""
5. Intrati pe site, accesati butonul cont si click pe conectare.
Identificati elementele de tip user si parola si inserati valori incorecte
(valori incorecte inseamna oricare valori care nu sunt recunoscute drept cont valid)
- Dati click pe butonul "conectare" si verificati urmatoarele:
             1. Faptul ca nu s-a facut logarea in cont
            2. Faptul ca se returneaza eroarea corecta
"""

LINK = "https://www.elefant.ro/"
driver.get(LINK)
driver.maximize_window()
cont_button = driver.find_element(By.XPATH, "(//*[@class='material-icons'])[4]")
cont_button.click()
time.sleep(2)
connect_button = driver.find_element(By.XPATH, "//*[@class='my-account-login btn btn-primary btn-block']")
connect_button.click()

email_button = driver.find_element(By.XPATH, "(//*[@class='form-control'])[1]")
password_button = driver.find_element(By.XPATH, "(//*[@class='form-control'])[2]")
email_button.send_keys("flaviu@gmail.abc")
password_button.send_keys("flaviu")
time.sleep(2)

conectare_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']")
conectare_button.click()

error_alert = driver.find_element(By.XPATH, "//*[@class='alert alert-danger']")
current_error = error_alert.text
expected_error = "Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou."
assert current_error == expected_error
time.sleep(2)

"""
6. Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@")
si verificati faptul ca butonul "conectare" este dezactivat
"""

email_button = driver.find_element(By.XPATH, "(//*[@class='form-control'])[1]")
email_button.clear()
email_button.send_keys("flaviu")
time.sleep(2)
conectare_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']")
actual = conectare_button.get_property("disabled")
print(actual)
expected = True
assert expected == actual


