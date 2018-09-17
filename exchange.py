import unittest #Testing module...
from typing import Dict #Type system
from dataclasses import dataclass, field #Data classes

@dataclass(order = True)
class Money:
    amount: int

    def times(self, times: int):
        return self.amount * times

@dataclass(order = True)
class Dollar(Money):
    type: str = "USD"

    def DollarToFranc(self):
        return self.amount / 2

@dataclass(order = True)
class Franc(Money):
    type: str = "CFH"

    def FrancToDollar(self):
        return self.amount * 2

class test():
    '''
    Money being a general placeholder for any money class...
    '''
    def assertInitialValue(self, Money,amount: int):
        '''Does 5 equal 5, or does amount not randomly change...'''
        money = Money(amount)
        print(money.amount == amount)

    def testMulti(self, Money, amount: int, times: int, result: int):
        '''
        Amount being amount in dollar class, times being how many times 
        one is multiply, and result being the expected result of multiplication
        '''
        money = Dollar(amount)
        money.amount = money.times(times)
        print(result == money.amount) #Add unnit test module later... But this is a crude workaround


testA = test()
testA.testMulti(Dollar,5,2,10)

francA = Franc(5)
print(francA.FrancToDollar())

dollarA = Dollar(50)
print(dollarA.DollarToFranc())

'''
testA = test()
testA.testMulti(Dollar, 5, 2, 10) 

testB = test()
testB.testMulti(Dollar,5, 3, 15)

testC = test()
testC.assertInitialValue(Dollar,5)

testD = test()
testD.assertInitialValue(Franc, 5)


class test(unittest.TestCase):
    def testMulti(self):
        dollarFive = Dollar(5)
        dollarFive.amount = dollarFive.times(2)
    self.assertEqual(10, dollarFive.amount) # print(10 == DollarFive.amount)

testExample = test()
print(testExample.testMulti())
'''



