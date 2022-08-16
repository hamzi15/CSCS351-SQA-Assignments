# install the following packaages 
# 'pip install selenium' selenium for python
# 'pip install selenium-wire' an extension for selenium to intercept browser api calls
# 'pip install webdriver_manager' webdriver_manager to automatically install chrome driver at run time
import time 
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# installs the chrome driver automatically at run time using webdriver_manager
driver = webdriver.Chrome(ChromeDriverManager().install())

# opens google on the browser
driver.get("https://www.google.com")

# finds the google search form and enters "selenium wire" into it
search = driver.find_elements(By.CLASS_NAME,'gLFyf')
search = search[0]
search.send_keys('selenium wire')
search.submit()

# waits for the page to load by one second
time.sleep(1)

# finds the first few results and outputs them to the console
# results = driver.find_elements(By.XPATH, ".//*[@id='rso']//div//h3/a")
# for result in results:
#     print(result.get_attribute("href"))

# time.sleep(1)

# prints all API calls made by the browser
print("-------------------API Testing-------------------")
for request in driver.requests:
     if request.response:
        print(
            request.method,
            request.host,
            request.response.status_code,
            request.response.date
        )
time.sleep(1)
driver.close()


