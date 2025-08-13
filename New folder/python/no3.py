#pop test frame for py:pytest,doctest,unittest(built-in)
import unittest
def addNumbers(x,y):
    return x+y
def subtractNumbers(h,i):
    return h-i
def multiplyNumbers(b,c):
    return b*c
def myfunction():
    print('hello world')
class Testmath(unittest.TestCase):
    def test_addNumbers(test):
        test.assertEqual(addNumbers(1,1),2)  
        #test.assertNotEqual(addNumbers(11,10),3)
        #arrange-what are the things that we need?what are we testing?
        #act-what are we doing? what action are we testing?
        #assert-what is the result?what are we expecting?
        """
        x=1 y=1
        z=x+y
        action= addnumber(x,y)
        expect that addnumbers(x,y) will equal z"""
    def test_subtractNumbers(test):
          test.assertEqual(subtractNumbers(1,1),0)
    def test_multiplyNumbers(test):
         test.assertEqual(multiplyNumbers(5,5),25)     
    def test_myfunction(test):
        test.print myfunction('hello world')
        



if __name__ =="__main__":
    unittest.main()