import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# ######################### Intro HTML, DOM, CSS #########################

"""
Pagina HTML = orice pagina web scrisa in limbajul HTML

Forma generala a unui fisier html:

<html>      - Nodu HTML, primul nod din document. Marcheaza inceputul paginii.

    <head>
            .... - aici vine metadata neafisata in browser (ex: titlul paginii, fisiere pt stilizare, etc)
    </head

    <body>
            .... - aici vin elementele din pagina (div-uri, butoane, input-uri, etc)
    </body>

</html>     

Nodul <head> - este un container pentru metadata (date despre date) si poate contine titlul paginii, 
referinte catre fisiere cu scripturi, stiluri si alte

Nodul <body> - contine elementele propriu-zise din pagina care sunt afisate in browser

- Fiecare element din pagina are un tip 
- Aceste tipuri sunt indicate printr-un <tag> HTML
- Orice element care se deschide cu un <tag> trebuie sa se si inchida cu un alt </tag> curespunzator 

Cele mai intalnite tag-uri HTML sunt:

<div> - division = marcheaza inceputul unei diviziuni 
<input> - input = o zona in care se poate introduce un text
<textarea> - text area = asemanator cu inputul, dar mai mare ca dimensiune 
<label> - label = reprezinta o eticheta text care descrie un element sau un grup de elemente
<button> - buton = buton HTML
<td> - tabel = tabel HTML 
<th> - tabel head = cap de tabel tabel 
<tr> - tabel row = rand dintr-un tabel 
<td> - tabel data = o celula dintr-un tabel
<select> - dropdown = lista din care se poate selecta un item dorit
<form> - formular = un formular alcatuit din mai multe elemente 

DOM = Document Object Model - modelul de reprezentare a unei pagini web 
DOM-ul are structura unui tree (copac) si contine toate elementele care se afla intr-o pagina HTML. 

Fiecare element poate avea atribute (proprietati) precum id, class, name, etc. 
- id: de regula este unic pentru fiecare element
- name: este de regula folosit pentru a identifica elementele mai usor in javascript
- class: este folosita de fisierele css care ajuta la stilizarea elementelor

Fisierele javascript sunt incluse de regula in <head> si definesc comportamentul elementelor dintr-o pagina
Fisierele css sunt incluse si ele in <head> ajuta la stilizare 

Pentru a simula navigarea pe internet in cod, avem nevoie si de un browser.
"""

# ######################### INSTALARE SELENIUM SI WEBDRIVE MANAGER #########################

# In terminal scriem urmatoarele randuri, unul cate unul, apasand Enter si asteptand sa se instaleze fiecare

"""
pip install selenium
pip install webdriver-manager
"""

# Documentatiile oficiale ale librariilor:
# Selenium: https://pypi.org/project/selenium/
# webdriver-manager: https://pypi.org/project/webdriver-manager/

"""
NOTA: 

Daca nu merge instalatul package-urilor prin pip install, 

1. Deschideti un terminal powershell (Start-ul din Windows-> tastati powershell -> click dreapta -> Run as Administrator)
si tastati urmatoarea comanda urmata de enter:   Set-ExecutionPolicy Unrestricted 

Sau in PyCharm intram in meniul File -> Settings -> Tools -> Terminal si schimbam Shell path din powershell in CMD

"""

# ######################### CREARE WEBDRIVER SI NAVIGARE CATRE UN LINK #########################

# Vom crea o instanta de WebDriver (tip Chrome) pentru a putea naviga si interactiona cu elemente intr-un browser Chrome
# Browserul se deschide in momentul in care initializam variabila driver

# creare driver - varianta simpla:
# driver = webdriver.Chrome()

# creare driver - varianta cu webdriver manager (recomandat):
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Declaram o constanta de tip string cu linkul pe care il vom deschide in browser
LINK = "https://formy-project.herokuapp.com/"

# instructiune pentru a deschide un URL
driver.get(LINK)

# instructiune pentru a maximiza fereastra
driver.maximize_window()

# ######################### TIPURI DE SELECTORI + EXEMPLE #########################

"""
Pentru a putea interactiona cu elementele dintr-o pagina HTML, libraria Selenium vine in ajutorul nostru, oferindu-ne 
posibilitatea de a identifica elementele folosindu-ne de locatorii care acestia ii pot avea

Selector (sau locator) = o modalitate <abstracta> prin care definim cum poate fi identificat un element in DOM

Modalitati prin care putem identifica un WebElement:

- LINK TEXT: un text (exact) care are un link ancorat -> un element cu tag-ul HTML <a> 

- PARTIAL LINK TEXT: un text (parte dintr-un text) care are un link ancorat -> un element cu tag-ul HTML <a> 

- TAG NAME: tag-ul html

- ID: dupa id-ul elementului

- CLASS NAME: atributul class al unui element

- XPATH: calea relativa sau absoluta catre un element in DOM

- CSS SELECTOR: selectorul css
"""

# ################ 1. LINK TEXT
link_autocomplete = driver.find_element(By.LINK_TEXT, "Autocomplete")
link_autocomplete.click()
time.sleep(1)

# navigam inapoi la pagina anterioara
driver.back()

# ################ 2. PARTIAL LINK TEXT
# link_partial_elements = driver.find_element(By.PARTIAL_LINK_TEXT, "Enabled and disabled")
# link_partial_elements.click()
# time.sleep(2)

# driver.back()


# ################ 3. TAG NAME
# element_a = driver.find_element(By.TAG_NAME, "a")
# driver.find_element(By.TAG_NAME, "a").click()
time.sleep(1)
lista_elemente = driver.find_elements(By.TAG_NAME, "a")

# lista_elemente[18].click()
# time.sleep(3)

# contor = 1
#
# for element in lista_elemente:
#
#     print(f"Text element nr {contor}: {element.text}")
#
#     if element.text == "Buttons":
#         element.click()
#         break
#     contor += 1
#
# time.sleep(2)


# ################ 4. ID

driver.get("https://formy-project.herokuapp.com/form")

first_name_input = driver.find_element(By.ID, "first-name")
first_name_input.send_keys("Alina")
time.sleep(2)

# ################ 5. CLASS NAME

elemente_form_control = driver.find_elements(By.CLASS_NAME, "form-control")
print(f"Avem {len(elemente_form_control)} elemente cu clasa form-control")

# ################ 6. XPATH

# #### XPATH ABSOLUT - calea absoluta catre element, incepand cu nodul <html>

# simbolul / (forward-slash) indica faptul ca ne referim la primul copil al elementului parinte cu tag-ul pe care
# urmeaza sa-l specificam dupa el

# in cazul in care un parinte are mai multi copii cu acelasi <tag>, putem specifica copilul la care ne referim
# indicandu-i ordinea intre paranteze drepte, de exemplu primul div va fi marcat astfel: div[1]

driver.find_element(By.XPATH, "/html/body/div/form/div/div[2]/input").send_keys("Pop")

# ##### XPATH RELATIV - o cale relativa in care ne putem folosi de atributele elementului/elementelor la care ne referim

# putem avea un numar variabil de cai relative care sa bata catre acelasi element, depinde de ce vrem sa ne folosim
# caile relative incep cu // si indica faptul ca nu pornim de la primul element din document (adica nodul <html>)
# simbolul " * " indica faptul ca ne referim la toate tipurile de element, indiferent de tag
# dupa specificarea tag-ului html, intre paranteze drepte indicam atributele dupa care vrem sa identificam elementul
# cu @ marcam atributul, apoi ii indicam valoarea EXACTA intre ghilimele

driver.find_element(By.XPATH, "//input[@id='job-title']").send_keys("Programator")

# acelasi element cu XPATH-uri diferite

# xpath relativ care selecteaza toate elementele cu id-ul first-name
first_name_relativ_fara_tag_cu_id = driver.find_element(By.XPATH, '//*[@id="first-name"]')

# xpath relativ care selecteaza toate elementele de tip input si cu id-ul first-name
first_name_relativ_cu_tag_cu_id = driver.find_element(By.XPATH, '//input[@id="first-name"]')

# xpath relativ care selecteaza toate elementele (indiferent de tag)
# si cu atributul @placeholder avand valoarea "Enter first name"
first_name_relativ_fara_tag_cu_placeholder = driver.find_element(By.XPATH, '//*[@placeholder="Enter first name"]')

# xpath relativ care selecteaza toate elementele de tip input
# si cu atributul @placeholder avand valoarea "Enter first name"
first_name_relativ_cu_tag_cu_placeholder = driver.find_element(By.XPATH, '//input[@placeholder="Enter first name"]')

# ################ CSS SELECTOR
"""
 simbolul   *  - selecteaza toate elementele
 sintaxa    #idElement  - selecteaza elementul cu id-ul "idElement"
 .button - selecteaza elementele care au clasa "button" 
 .button.primary - selecteaza elementele care au atat clasa "button" cat si clasa "primary"
 input  - selecteaza toate elementele de tip input
 div input -  selecteaza toate elementele de tip input care se afla intr-un div
 div > input - selecteaza toate elementele de tip input unde parintele e un div
 div + input - selecteaza primul element input care e dupa un element div
 div ~ input - selecteaza toate elementele de tip input precedate de un element div
 input [class] - selecteaza elementele de tip input care au atributul class
 input [class='value'] - selecteaza elementele de tip input care au atributul class = 'value'
 input [class~='value'] - selecteaza elementele de tip input ale caror atribut class contine textul 'value' 
 [id|="radio-button"] - selecteaza toate elementele ale caror id e egal cu sau incepe cu radio-button
"""

driver.find_element(By.CSS_SELECTOR, "#first-name").clear()
driver.find_element(By.CSS_SELECTOR, "html>body>div>form>div>div:nth-of-type(2)>input").clear()
driver.find_element(By.CSS_SELECTOR, "input[id='job-title']").clear()

# ##### acelasi element cu CSS-uri diferite

# doar cu #ID
first_name_cu_id_css = driver.find_element(By.CSS_SELECTOR, '#first-name')
# tag si #ID
first_name_cu_tag_si_id_css = driver.find_element(By.CSS_SELECTOR, 'input#first-name')
# tag si ID, de data asta ca id-ul e mentionat la fel ca orice alt atribut si fara #
first_name_cu_tag_si_atribut_id_css = driver.find_element(By.CSS_SELECTOR, 'input[id="first-name"]')
# tag si atributul placeholder
first_name_cu_tag_si_atribut_placeholder_css = driver.find_element(By.CSS_SELECTOR,
                                                                   'input[placeholder="Enter first name"]')
# tag cu clasa si atributul id
first_name_cu_tag_clasa_si_id = driver.find_element(By.CSS_SELECTOR, 'input.form-control[id="first-name"]')

# element cu tag-ul input si atributul type = radio
radio_cu_atribut_type_radio = driver.find_element(By.CSS_SELECTOR, "input[type='radio']")

time.sleep(3)

driver.quit()

driver.get("https://formy-project.herokuapp.com/form")

# Cauta primul element de tip input
driver.find_element(By.XPATH, "(//input)[1]").send_keys("Andrei")

# Cauta al doilea element de tip input
driver.find_element(By.XPATH, "(//input)[2]").send_keys("Pop")

# Ultimul element copil cu tag-ul <option> al unui element parinte <select>
text_element = driver.find_element(By.XPATH, "//select//option[last()]").text
print(text_element)

# Penultimul element copil cu tag-ul <option> al unui element parinte <select>
text_element_2 = driver.find_element(By.XPATH, "//select//option[last()-1]").text
print(text_element_2)

# Simbolul | (pipe) se foloseste intre 2 xpathuri
driver.find_element(By.XPATH, "//input[@id='id-inexistent'] | //input[@id='first-name']").clear()

# Operatorul or este un OR logic si returneaza elementele care respecta regula data
driver.find_element(By.XPATH, "//input[@id='last-name' or @id='id-inexistent']").clear()

# Operatorul logic not - neaga o conditie data
driver.find_element(By.XPATH, "//input[not(@type='text')]").click()

tag_element = driver.find_element(By.XPATH, "//label[text()='First name']/parent::*").tag_name
print(tag_element)

# cauta toti fratii de dupa elementul //option[2] care sunt de tipul <option>
print(len(driver.find_elements(By.XPATH, "//option[2]/following-sibling::option")))

# CSS doar cu ID
first_name_cu_id_css = driver.find_element(By.CSS_SELECTOR, "#first-name")

# CSS cu tag si ID
first_name_cu_tag_si_id = driver.find_element(By.CSS_SELECTOR, "input#first-name")

# CSS cu tag si atribut-valoare
first_name_cu_tag_si_atribut = driver.find_element(By.CSS_SELECTOR, "input[id='first-name']")

# selector_element_inexistent = driver.find_element(By.CSS_SELECTOR, "input[id='inexistent']")

# CSS cu clasa care contine o parte din valoarea data
buton_submit = driver.find_element(By.CSS_SELECTOR, "a[class~='btn-primary']")
