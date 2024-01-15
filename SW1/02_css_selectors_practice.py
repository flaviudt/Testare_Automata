import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
time.sleep(1)

# accesam un link
LINK = 'https://the-internet.herokuapp.com/login'
driver.get(LINK)
time.sleep(1)

# maximizam fereastra
driver.maximize_window()
time.sleep(1)

"""
1. CSS SELECTOR - identificare dupa ID

Identifica inputul username dupa id, folosind CSS SELECTOR
"""
username = driver.find_element(By.CSS_SELECTOR, "#username")
username.send_keys("tomsmith")
time.sleep(1)

"""
2. CSS SELECTOR - identificare dupa clasa

a. Identifica elementul h4 dupa clasa, folosin CSS SELECTOR

b. Identifica primul element cu clasele large-6, small-12, columns, folosind CSS SELECTOR.
Folosind assert, verifica tag-ul acestuia este div.
"""
# a.
h4_element = driver.find_element(By.CSS_SELECTOR, ".subheader")
assert 'secure' in h4_element.text

# b.
element = driver.find_element(By.CSS_SELECTOR, ".large-6.small-12.columns")
actual = element.tag_name
expected = "div"
assert actual, expected

"""
3. CSS SELECTOR - identificare dupa nume tag + id/clasa

a. Identifica elementul form, dupa tag + id, folosind CSS SELECTOR.
Verifica ca atributul method al acestuia are valoarea 'post'

b. Identifica butonul de login dupa tag + clasa, folosind CSS SELECTOR.
Verifica ca textul acestuia este 'Login'
"""
# a.
form_element = driver.find_element(By.CSS_SELECTOR, "form#login")
expected = "post"
actual = form_element.get_attribute('method')
assert expected == actual

# b.
button = driver.find_element(By.CSS_SELECTOR, "button.radius")
expected = "Login"
actual = button.text
assert expected == actual

"""
4. CSS SELECTOR - identificare dupa tip atribut=valoare

Identifica labelul pentru parola dupa atribut=valoare, folosind CSS SELECTOR.
Verifica ca textul acestuia este cel asteptat.
"""
label_pwd = driver.find_element(By.CSS_SELECTOR, "label[for='password']")
expected = "Password"
actual = label_pwd.text

assert expected == actual

"""
5. CSS SELECTOR - identificare element mergand din copil in copil (>)

Identifica link-ul din footer (Elemental Selenium), pornind de la div-ul
cu id-ul "page-footer" folosind CSS SELECTOR, si mergand din copil in copil.
Verifica ca valoarea atributului href este cea asteptata.
"""
link_element = driver.find_element(By.CSS_SELECTOR, 'div[id="page-footer"] > div > div > a')
expected = "http://elementalselenium.com/"
actual = link_element.get_attribute('href')

assert expected == actual


"""
6. CSS SELECTOR - identificare orice copil

Identifica link-ul din footer (Elemental Selenium), pornind de la div-ul
cu id-ul "page-footer" folosind CSS SELECTOR, sarind direct la acesta.

Verifica ca tag-ul acestuia este un tag a
"""
link_element = driver.find_element(By.CSS_SELECTOR, 'div[id="page-footer"] a')
expected = "a"
actual = link_element.tag_name
assert expected == actual

"""
7. CSS SELECTOR - identificarea primului copil (first-of-type)

Identifica primul div ce apartine de tag-ul form si verifica ca are clasa row.
"""

#first_div = driver.find_element(By.CSS_SELECTOR, 'form#login>:first-child')
first_div = driver.find_element(By.CSS_SELECTOR, "form > div:first-of-type")
actual = first_div.get_attribute("class")
expected = "row"
assert actual == expected

"""
8. CSS SELECTOR - identificarea ultimului copil (last-of-type)

Identifica copilul ultimului div ce apartine de tag-ul form
si verifica ca acesta are 3 clase setate.
"""
last_child = driver.find_element(By.CSS_SELECTOR, 'form > div:last-of-type >div')
acctual = len(last_child.get_attribute("class").split())
expected = 3
assert acctual == expected

"""
9. CSS SELECTOR - identificare copil care nu este nici primul, nici ultimul (nth-of-type)

Acceseaza elementul input se apartine de al doilea copil al elementului form
si verifica ca are id-ul setat corespunzator
"""

input_element = driver.find_element(By.CSS_SELECTOR, "form >:nth-of-type(2) input")
input_id = input_element.get_attribute('id')
expected = 'password'

assert expected == input_id

"""
10. CSS SELECTOR - identificare frate ulterior (+)

Cauta elementul input care are ca si frate un label cu atributul for=username.

Verifica ca acesta are atributul type=text

"""
input_element = driver.find_element(By.CSS_SELECTOR,"label[for='username']+input")
actual = input_element.get_attribute("type")
expected = "text"

assert actual == expected

