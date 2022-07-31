# Test Report
# Hamza Asaad 231450993

## Test Objective

The objective of the test is functional testing of the 5 functions.

## Test cases, test coverage and execution details.

### Test Cases
- ```add``` takes two numbers ```x,y``` as input and returns the addition of the two numbers.
- ```sub``` takes two numbers ```x,y``` as input and returns the subtraction of the two numbers.
- ```square``` takes a number ```x``` as input and returns the square of that number.
- ```findArea``` takes two numbers ```x,y``` and applies the ```l * b``` formula and returns the area of a rectangle.
- ```findPerimeter``` takes two numbers ```x,y``` and applies the ```2 * ( l + b )``` formula and returns the perimeter of a rectangle.

### Test Coverage
- ```add``` we have three edge case tests adding positive numbers, negative nubers and postive and negative numbers together.
- ```sub``` we have three edge case tests subtracting positive numbers, negative numbers and postive and negative numbers from each other.
- ```square```we have two edge case tests squaring positive number and negative numbers.
- ```find Area``` and  ```findPerimeter``` tests cover similar cases using positive numbers, negative nubers and positive and negative numbers.

## Defects counts

No defects were found in any function.

## Platform and test environment configuration details

```PyUnit``` is the module used on the the code is in ```Python```. Only the  ```test.py``` file has to be run and it offers all options to run specific unit tests or the entire testing suite.
