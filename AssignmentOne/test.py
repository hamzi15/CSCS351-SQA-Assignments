from functions import add, sub, square, findArea, findPerimeter
import unittest

class AddUnitTest(unittest.TestCase):
    def testA(self):
        assert add(1, 2) == 3, "can't add positive numbers"

    def testB(self):
        assert add(-1, -2) ==  -3, "can't add negative numbers"

    def testC(self):
        assert add(-47, 57) ==  10, "can't add positive and negative numbers"

class SubUnitTest(unittest.TestCase):
    def testA(self):
            assert sub(1, 2) == -1, "can't subtract positive numbers"

    def testB(self):
            assert sub(-1, -2) == 1, "can't subtract negative numbers"

    def testC(self):
            assert sub(-47, 57) == -104, "can't subtract negative and positive numbers"

class SquareUnitTest(unittest.TestCase):
    def testA(self):
            assert square(4) == 16, "can't square positive numbers"

    def testB(self):
            assert square(-2) == 4, "can't square negative numbers"

    def testC(self):
            assert square(0) == 0, "can't square zero"

class AreaUnitTest(unittest.TestCase):
    def testA(self):
            assert findArea(2, 3) == 6, "can't find area of rectangle"

    def testB(self):
            assert findArea(3, 3) == 9, "can't find area of square"

    def testC(self):
            assert findArea(-1, 3) == -3, "can't find area of rectangle with negative width"

    def TestD(self):
            assert findArea(0, 3) == 0, "can't find area of rectangle with zero width"


class PerimeterUnitTest(unittest.TestCase):
    def testA(self):
            assert findPerimeter(2, 3) == 10, "can't find perimeter of rectangle"

    def testB(self):
            assert findPerimeter(3, 3) == 12, "can't find perimeter of square"

    def testC(self):
            assert findPerimeter(-1, 3) == 4, "can't find perimeter of rectangle with negative width"

    def TestD(self):
            assert findPerimeter(0, 3) == 6, "can't find perimeter of rectangle with zero width"



def addSuite():
        suite = unittest.TestSuite()
        suite.addTest(AddUnitTest('testA'))
        suite.addTest(AddUnitTest('testB'))
        suite.addTest(AddUnitTest('testC'))
        return suite

def subSuite():
        suite = unittest.TestSuite()
        suite.addTest(SubUnitTest('testA'))
        suite.addTest(SubUnitTest('testB'))
        suite.addTest(SubUnitTest('testC'))
        return suite

def squareSuite():
        suite = unittest.TestSuite()
        suite.addTest(SquareUnitTest('testA'))
        suite.addTest(SquareUnitTest('testB'))
        suite.addTest(SquareUnitTest('testC'))
        return suite

def areaSuite():
        suite = unittest.TestSuite()
        suite.addTest(AreaUnitTest('testA'))
        suite.addTest(AreaUnitTest('testB'))
        suite.addTest(AreaUnitTest('testC'))
        suite.addTest(AreaUnitTest('TestD'))
        return suite

def perimeterSuite():
        suite = unittest.TestSuite()
        suite.addTest(PerimeterUnitTest('testA'))
        suite.addTest(PerimeterUnitTest('testB'))
        suite.addTest(PerimeterUnitTest('testC'))
        suite.addTest(PerimeterUnitTest('TestD'))
        return suite


if __name__ == '__main__':
        print("--- Name: Hamza Asaad --- Roll No: 231450993\n Welcome ")
        while True:
                selection = input("\nPlease select a unit test or suite: \n1. Addition\n2. Subtraction\n3. Square\n4. Area\n5. Perimeter\n6. Entire Test Suite\n7. Exit\n")
                if selection == '1':
                        suite = addSuite()
                        unittest.TextTestRunner(verbosity=2).run(suite)
                elif selection == '2':
                        suite = subSuite()
                        unittest.TextTestRunner(verbosity=2).run(suite)
                elif selection == '3':
                        suite = squareSuite()
                        unittest.TextTestRunner(verbosity=2).run(suite)
                elif selection == '4':
                        suite = areaSuite()
                        unittest.TextTestRunner(verbosity=2).run(suite)
                elif selection == '5':
                        suite = perimeterSuite()
                        unittest.TextTestRunner(verbosity=2).run(suite)
                elif selection == '6':
                        suite = unittest.TestSuite([addSuite(), subSuite(), squareSuite(), areaSuite(), perimeterSuite()])
                        unittest.TextTestRunner(verbosity=2).run(suite)
                elif selection == '7':
                        break
                else:
                        print("---Invalid selection---")

        


