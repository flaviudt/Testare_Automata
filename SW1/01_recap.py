from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

"""
1.
- Instantiaza un un browser de Chrome.
- Acceseaza pagina https://the-internet.herokuapp.com/
- Maximizeaza fereastra
"""

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
time.sleep(1)

LINK = "https://the-internet.herokuapp.com/"
driver.get(LINK)
# time.sleep(2)
driver.maximize_window()
# time.sleep(2)

"""
2. Acceseaza link-ul Form Authentication, folosind un selector potrivit.
Incearca mai multe variante posibile.
"""

#dupa XPATH
login_link = driver.find_element(By.XPATH, "//a[@href='/login']")
login_link.click()
time.sleep(1)

# # dupa LINK-TEXT
# driver.find_element(By.LINK_TEXT, "Form Authentication").click()
# time.sleep(2)

# # dupa PARTIAL LINK TEXT
# driver.find_element(By.PARTIAL_LINK_TEXT, "Form ").click()
# time.sleep(2)
#
# dupa TAG NAME
# driver.find_element(By.TAG_NAME, "(//a)[22]")
# driver.find_elements(By.TAG_NAME, 'a')[21]

"""
3. Identifica elementul ce contine textul "Login Page"
si verifica, folosind un assert, ca acest element are textul asteptat
"""
#
# login_page = driver.find_element(By.XPATH, "//h2")
# actual = login_page.text
# expected = "Login Page"
# assert expected == actual

"""
4. Identifica input-urile username si password,
introdu valori valide, si da click pe butonul login
"""

username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPas")
time.sleep(1)

login_btn = driver.find_element(By.CLASS_NAME, "radius")
login_btn.click()
time.sleep(1)

"""
5. Verifica, folosind un assert ca ai ajuns pe pagina
https://the-internet.herokuapp.com/secure
"""

# expected_url = "https://the-internet.herokuapp.com/secure"
# actual_url = driver.current_url
# assert expected_url == actual_url

"""
6. Da click pe butonul logout
"""

# logout_btn = driver.find_element(By.XPATH, '//a[@href="/logout"]')
# logout_btn.click()
# time.sleep(1)

"""
7. Introdu un username corect si o parola incorecta.
Identifica mesajul care apare si verifica in cod ca acela este mesajul asteptat.
"""

# username = driver.find_element(By.ID, "username")
# username.send_keys("tomsmith")
# password = driver.find_element(By.ID, "password")
# password.send_keys("incorect pass")
time.sleep(4)
msg = driver.find_element(By.XPATH, '//*[@id="flash"]')
acc = msg.text
#exp = "Your password is invalid!\n×"
#assert acc == exp, f'{acc}'
expected_text = 'Your password is invalid!'
assert expected_text in acc

time.sleep(1)
"""
8. Introdu un username corect.
Gaseste elementul cu tag-ul h4.
Ia textul de pe el si fa split dupa spatiu. Considera fiecare cuvant ca o potentiala parola.
Foloseste o structura iterativa prin care sa introduci rand pe rand parolele si sa apesi login
La final, testul trebuie sa printeze fie "Nu am reusit sa gasesc parola", fie "Parola secreta este [parola]"
"""
h4 = driver.find_element(By.CLASS_NAME,"subheader")
possible_pass = h4.text.split()

for elem in possible_pass:
    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")
    password = driver.find_element(By.ID, "password")
    password.send_keys(elem)
    login_btn = driver.find_element(By.CLASS_NAME, "radius")
    login_btn.click()

    expected_url = "https://the-internet.herokuapp.com/secure"
    actual_url = driver.current_url
    if expected_url == actual_url:
        print(f"Parola secreta este {elem}")
        break
else:
    print("Nu am reusit sa gasesc parola")


