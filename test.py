class Calculator(object):
     def __init__(self, first, second):
         self.first = first 
         self.second = second

     @staticmethod
     def add(first, second):
         return (first + second)

     def addWithoutStatic(self):
         return (self.first +  self.second)

if __name__ == "__main__" :
     addResult = Calculator.add(2, 3)
     obj = Calculator(2,3)
     addWithoutStaticResult = obj.addWithoutStatic()
     print (addResult)
     print (addWithoutStaticResult)
    

