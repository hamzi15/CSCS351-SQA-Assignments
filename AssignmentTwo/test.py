# install the following packaages 
# 'pip install selenium' selenium for python
# 'pip install selenium-wire' an extension for selenium to intercept browser api calls
# 'pip install webdriver_manager' webdriver_manager to automatically install chrome driver at run time
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import unittest

# unittest.TestLoader.sortTestMethodsUsing = None


class SeleniumUnitTest(unittest.TestCase):

    def setUp(self):
        # installs the chrome driver automatically at run time using webdriver_manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_google_search(self):
        driver = self.driver

        # opens google on the browser
        driver.get("https://www.google.com")

        # finds the google search form and enters "selenium wire" into it
        search = driver.find_elements(By.CLASS_NAME,'gLFyf')
        search = search[0]
        search.send_keys('selenium wire')
        search.submit()
        self.assertNotIn("No results found.", driver.page_source)

    def test_api_calls(self):
        driver = self.driver

        # opens google on the browser
        driver.get("https://www.google.com")

        print()
        # prints all API calls made by the browser
        for request in driver.requests:
            if request.response:
                print("Request Method:", request.method)
                print("Request Host:", request.host)
                print("Request Status Code:", request.response.status_code)
                print("Request Time Stamp:", request.response.date)
        print()

           
    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()


