import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# accesam un link
LINK = 'https://carturesti.ro/'
driver.get(LINK)
# time.sleep(1)

# maximizam fereastra
driver.maximize_window()
time.sleep(1)

# cookie cancel
cookie_cancel = driver.find_element(By.XPATH, "//div[@class='cookieInfo container']//button")
cookie_cancel.click()

"""
1. XPATH - Gaseste butonul "COMANDA-L AICI", incepand de la elementul div cu clasa homePage
Verifica ca tag-ul acestuia este a.
Da click pe buton si verifica ca link-ul curent este cel asteptat.
"""

#//div[@class="homePage"]/div[2]/div/div[3]/a
#//div[@class="homePage"]//a[@href="/coupon-checkout"]
btn = driver.find_element(By.XPATH, '//div[@class="homePage"]//a[@href="/coupon-checkout"]')
time.sleep(1)
btn.click()
time.sleep(1)

expected_url = "https://carturesti.ro/coupon-checkout"
actual_url = driver.current_url
assert expected_url == actual_url

"""
2. XPATH - Gaseste elementul cu textul 'Împachetare gratuită'
Verifica ca tag-ul acestuia este h4.
"""
driver.back()
time.sleep(1)

h4_element = driver.find_element(By.XPATH, '(//div[@class="homePage"]//h4)[1]')
actual = h4_element.tag_name
expected = 'h4'
assert actual == expected

"""
3. XPATH - cauta elementul div care se afla imediat dupa
elementul de tip i cu clasa 'cartu-icons-giftbox'
"""

div_element = driver.find_element(By.XPATH,'//*[@class="cartu-icons-giftbox"]/following-sibling::div')
actual = div_element.tag_name
expected = 'div'
assert actual == expected

"""
4. XPATH - cauta elementul h4 care se afla exact ianintea elementului
span cu textul 'peste 120.000 de produse! '
"""
preceding_element = driver.find_element(By.XPATH, "(//span[@class='hidden-xs'])[1]/preceding-sibling::h4")
actual = preceding_element.tag_name
expected = 'h4'
assert actual == expected

