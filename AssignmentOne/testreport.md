# Test Report
# Hamza Asaad 231450993

## Test Objective

The objective of the test is functional testing of the 5 functions.

## Test cases, test coverage and execution details.

### Test Cases 🧪
- ```add``` takes two numbers ```x,y``` as input and returns the addition of the two numbers.
- ```sub``` takes two numbers ```x,y``` as input and returns the subtraction of the two numbers.
- ```square``` takes a number ```x``` as input and returns the square of that number.
- ```findArea``` takes two numbers ```x,y``` and applies the ```l * b``` formula and returns the area of a rectangle.
- ```findPerimeter``` takes two numbers ```x,y``` and applies the ```2 * ( l + b )``` formula and returns the perimeter of a rectangle.

### Test Coverage 🛠️
- ```add``` we have three edge case tests adding positive numbers, negative nubers and postive and negative numbers together.
- ```sub``` we have three edge case tests subtracting positive numbers, negative numbers and postive and negative numbers from each other.
- ```square```we have two edge case tests squaring positive number and negative numbers.
- ```find Area``` and  ```findPerimeter``` tests cover similar cases using positive numbers, negative nubers and positive and negative numbers.

## Defects counts 🔎

### Add unit test cases: All Passed ✅
<img width="515" alt="Screen Shot 2022-07-31 at 11 45 49 PM" src="https://user-images.githubusercontent.com/66818162/182040935-e54605d2-693c-41a7-a8b9-34d04c9cc335.png">
### Sub unit test cases: All Passed ✅
<img width="515" alt="Screen Shot 2022-07-31 at 11 45 55 PM" src="https://user-images.githubusercontent.com/66818162/182040939-d3f7df60-bfab-49d7-a80a-8bcfece62501.png">
### Square unit test cases: All Passed ✅
<img width="515" alt="Screen Shot 2022-07-31 at 11 46 00 PM" src="https://user-images.githubusercontent.com/66818162/182040953-e88d608b-c512-43b5-b32a-3fcbe9f4227c.png">
### Rectangular Area test cases: All Passed ✅
<img width="515" alt="Screen Shot 2022-07-31 at 11 46 23 PM" src="https://user-images.githubusercontent.com/66818162/182040955-ee9f1afb-66b5-4a1a-9fe0-56e5dfd7ce4c.png">
### Rectangular Perimeter test cases: All Passed ✅
<img width="515" alt="Screen Shot 2022-07-31 at 11 46 34 PM" src="https://user-images.githubusercontent.com/66818162/182040957-25f60fad-a2bc-436e-979d-12492b2a96d8.png">
<img width="515" alt="Screen Shot 2022-07-31 at 11 46 46 PM" src="https://user-images.githubusercontent.com/66818162/182040962-ed670d18-18e8-41e0-b234-b11bdee21ffc.png">

No defects were found in any function.

## Platform and test environment configuration details 💻

```PyUnit``` is the module used on the the code is in ```Python```. Only the  ```test.py``` file has to be run and it offers all options to run specific unit tests or the entire testing suite.
