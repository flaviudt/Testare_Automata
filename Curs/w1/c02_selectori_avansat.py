import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
LINK = "https://formy-project.herokuapp.com/form"

driver.get(LINK)
time.sleep(1)

driver.maximize_window()

# ################ Relatii parinte-copil #################

# Cauta primul element de tip input - practic parantezele indica faptul ca ceea ce este intre ele este o lista cu
# mai multe elemente, iar [1] este indexul elementului pe care il cautam. Daca nu erau parantezele, xpath-ul returna mai
# multe elemente. Spre deosebire de Python, Java, C, in HTML indexarea incepe de la 1
driver.find_element(By.XPATH, "(//input)[1]").send_keys("Andrei")

#Cauta al doilea element de tip input
driver.find_element(By.XPATH, "(//input)[2]").send_keys("Pop")

# al doilea copil cu tag-ul <div> al unui element parinte oarecare - observam ca parintele nu e specificat
driver.find_element(By.XPATH, "//div[2]")

# Al doilea copil cu tag-ul ORICARE (*) al unui element parinte oarecare, cu clasa 'form-control'
driver.find_element(By.XPATH, "//*[2][@class='form-control']").clear()
time.sleep(1)

# Primul element copil cu tag-ul <input> cu id='last-name' al unui element parinte <div>
driver.find_element(By.XPATH, "//div/input[1][@id='last-name']").send_keys("Test")
time.sleep(1)

# Ultimul element copil cu tag-ul <option> al unui element parinte <select>
driver.find_element(By.XPATH, "//select/option[last()]")

# Penultimul element copil cu tag-ul <option> al unui element parinte <select>
driver.find_element(By.XPATH, "//select/option[last()-1]")

# Parintele elementului <input> cu id-ul first-name
driver.find_element(By.XPATH, "//input[@id='first-name']/..")

# ################ XPATH-uri cu operatori logici (and, or, |, not) si atribute cu continut specific (contains) #################

# SIMBOLUL | (pipe) - se foloseste intre 2 xpath-uri
# Input cu id='id-inexistent' sau Input cu id='first-name'
# simbolul pipe | semnifica un SAU logic intre 2 xpath-uri
driver.find_element(By.XPATH, "//input[@id='id-inexistent'] | //input[@id='first-name']").send_keys("Test")
time.sleep(1)

# OPERATORUL or - sau logic
# Input cu id='id-inexistent' sau id='last-name'
# "or" este un SAU logic si se foloseste intre 2 atribute sau doua conditii dintr-un xpath
driver.find_element(By.XPATH, "//input[@id='id-inexistent' or @id='last-name']").clear()
time.sleep(1)

# Input al carui id contine cuvantul "first" SAU cuvantul "last"
driver.find_element(By.XPATH, "//input[contains(@id,'first') or contains(@id,'last')]").clear()
time.sleep(1)

# OPERATORUL and - si logic
# "and" este un SI logic si se foloseste intre 2 atribute sau doua conditii dintr-un xpath
# Input al carui id contine "last" SI cuvantul "name"
driver.find_element(By.XPATH, "//input[contains(@id,'last') and contains(@id,'name')]").send_keys("Test")
time.sleep(1)

# OPERATORUL not - negare logica
# "not" este o negare logica si se foloseste intre 2 atribute sau doua conditii dintr-un xpath
# Input al carui atribut type NU este egal cu 'text'
driver.find_element(By.XPATH, "//input[not(@type='text')]").send_keys("Test")
time.sleep(1)

# ################# XPATH-uri cu "axis navigation" sau "rudenii" intre elemente #################

"""
Sintaxa generala:
//tag-din-care-pornim/axis::tag-la-care-ne-referim
"""

# ancestor	        - selecteaza toti stramosii elementului din care pornim (parinti, parintii parintilor, etc) - IN SUS
# ancestor-or-self	- selecteaza toti stramosii elementului din care pornim + elementul din care pornim - IN SUS
# parent	        - selecteaza STRICT parintele elementului din care pornim - IN SUS
# descendant	    - selecteaza toti descendentii (copiii, copiii copiilor) elementului din care pornim - IN JOS
# descendant-or-self- selecteaza toti descendentii elementului din care pornim + elementul din care pornim - IN JOS
# child	            - selecteaza toti copii nodului (elementului) din care pornim - IN JOS
# following-sibling	- selecteaza "fratii" urmatori ai elementului din care pornim - ACELASI NIVEL
# preceding-sibling	- selecteaza "fratii" precedenti ai elementului din care pornim - ACELASI NIVEL

# EXEMPLE:

# ############################## ancestor

# Stramosii <div> al elementului <label> cu textul ='First name'
driver.find_element(By.XPATH, "//label[text()='First name']/ancestor::div")

# TOTI stramosii elementului <label> cu textul ='First name'
driver.find_element(By.XPATH, "//label[text()='First name']/ancestor::*")

#  ############################## ancestor-or-self

# TOTI stramosii elementului <label> cu textul ='First name' inclusiv <label>
driver.find_element(By.XPATH, "//label[text()='First name']/ancestor::*")

#  ############################## parent

# parintele elementului <label> cu textul ='First name' (cu sau fara tag specificiat)
driver.find_element(By.XPATH, "//label[text()='First name']/parent::strong")
driver.find_element(By.XPATH, "//label[text()='First name']/parent::*")

#  ############################## descendant

# toti descendentii elementului <div> avand clasa 'input-group', indiferent de tip
driver.find_element(By.XPATH, "//div[@class='input-group']/descendant::*")

# toti descendentii elementului <div> avand clasa 'input-group' care unt de tip <input>
driver.find_element(By.XPATH, "//div[@class='input-group']/descendant::input")

#  ############################## descendant-or-self

# toti descendentii elementului <div> cu clasa 'input-group' indiferent de tip, inclusiv div-ul din care pornim
driver.find_element(By.XPATH, "//div[@class='input-group']/descendant-or-self::*")

#  ############################## child

# toti copiii elementului <div> cu clasa 'input-group' care sunt si ei de tipul <div>
driver.find_element(By.XPATH, "//div[@class='input-group']/child::div")

#  ############################## following-sibling

# toti fratii dupa elementul <option> cu atributul value=2 care sunt si ei de tipul <option>
driver.find_element(By.XPATH, "//option[@value='2']/following-sibling::option")

#  ############################## preceding-sibling

# toti fratii inaintea elementului <option> cu atributul value=2 care sunt si ei de tipul <option>
driver.find_element(By.XPATH, "//option[@value='2']/preceding-sibling::option")

driver.quit()
