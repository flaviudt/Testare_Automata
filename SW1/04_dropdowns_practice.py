import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
time.sleep(1)

# accesam un link
LINK = 'https://the-internet.herokuapp.com/dropdown'
driver.get(LINK)
time.sleep(1)

# maximizam fereastra
driver.maximize_window()
time.sleep(1)

choices = Select(driver.find_element(By.ID, "dropdown"))
print(choices.options) # reprezinta o lista cu elemente de tip WebElement in care fiecare element,
# este o optiunie din dropdown

for option in choices.options:
    print(option.text)

    if option.text == "Please select an option":
        assert not option.is_enabled()
        break

choices.select_by_visible_text('Option 1')
time.sleep(3)
