# Configuration and Test Report
# Hamza Asaad 231450993

## Objective
Our objective is to test selenium functionality and test browser API calls using ```selenium```.

## Configuration 
- ```selenium``` installed using the command ```pip install selenium```
- ```selenium wire``` an extension on selenium which enables us to catch browser API requests ```pip install selenium-wire```
- ```webdriver_manager``` a dependency which automatcially installs the browser driver in our case the ```Chrome``` web driver at runtime ```pip install webdriver_manager```.

## Test Cases
There are two test cases:
1. ```test_google_search``` the code opens google finds the search box element and types in: ```selenium wire``` and submits the value.<br>With ```self.assertNotIn("No results found.", driver.page_source)``` assertion we check whether google successfully found a result.
3. ```test_api_calls``` runs the browser and opens www.google.com and prints out all the requests made by the site.

## Output Screenshots

### Test Case 1
<img width="1312" alt="Screen Shot 2022-08-16 at 11 00 18 PM" src="https://user-images.githubusercontent.com/66818162/184947718-2e0b14e7-82c6-4dc1-90d3-cecf129261d5.png">
<img width="1312" alt="Screen Shot 2022-08-16 at 11 00 22 PM" src="https://user-images.githubusercontent.com/66818162/184947690-3521c2f7-53b8-4d8a-90aa-470830d76eab.png">

### Test Case 2
<img width="1423" alt="Screen Shot 2022-08-16 at 10 57 53 PM" src="https://user-images.githubusercontent.com/66818162/184947185-4e49f573-1f2a-4fd0-ae03-4c678929b64e.png">

### Test Result
   <img width="807" alt="Screen Shot 2022-08-16 at 10 58 46 PM" src="https://user-images.githubusercontent.com/66818162/184947352-2cab4b49-8f2d-4bbf-aa46-de12a66009a8.png">
