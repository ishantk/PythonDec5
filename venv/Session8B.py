# Amazon eCommerce
"""
class LedTV:

    def __init__(self, pid, name, brand, price, screenSize, technology):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price
        self.screenSize = screenSize
        self.technology = technology

    def showLedTvDetails(self):
        print("=====",self.name,"=====")
        print("Brand\t",self.brand)
        print("Price\t", self.price)
        print("Tech\t", self.technology)
        print("=======================")

class Shoe:

    def __init__(self, pid, name, brand, price, shoeSize, color):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price
        self.shoeSize = shoeSize
        self.color = color

    def showShoeDetails(self):
        print("=====",self.name,"=====")
        print("Brand\t",self.brand)
        print("Price\t", self.price)
        print("Color\t", self.color)
        print("=======================")

class MobilePhone:

    def __init__(self, pid, name, brand, price, ram, memory, os):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price
        self.ram = ram
        self.memory = memory
        self.os = os

    def showPhoneDetails(self):
        print("=====",self.name,"=====")
        print("Brand\t",self.brand)
        print("Price\t", self.price)
        print("OS\t", self.os)
        print("=======================")

"""

class Product:
    def __init__(self, pid, name, brand, price):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price

    def showProductDetails(self):
        print("=====",self.pid," | ",self.name, "=====")
        print("Brand\t", self.brand)
        print("Price\t", self.price)
        print("================================")


class LedTV(Product): # IS-A Relationship

    def __init__(self, pid, name, brand, price, screenSize, technology):
        Product.__init__(self,pid, name, brand, price)
        self.screenSize = screenSize
        self.technology = technology

    def showLEDTvDetails(self):
        Product.showProductDetails(self)
        print("Size\t", self.screenSize)
        print("Tech\t", self.technology)


"""
print(Product.__dict__)
print(LedTV.__dict__)

# Object Construction Statement
ledRef = LedTV(101,"OLED","Samsung",60000)
print(ledRef.__dict__)
ledRef.showProductDetails()
"""

# print(LedTV.__dict__)


ledRef = LedTV(101,"OLED","Samsung",60000,50,"QLED")
ledRef.showLEDTvDetails()



"""
    Inheritance Types:
        1. Single Level
            A
            |
            B
        
        class A:
            pass
            
        class B(A):
            pass
        
        --------------    
        2. Multi Level
            A
            |
            B
            |
            C
        
        class A:
            pass
            
        class B(A):
            pass  
        
        class C(B):
            pass 
            
        --------------    
        3. Hierarchy
            A
            |
         B     C
        
        class A:
            pass
            
        class B(A):
            pass  
        
        class C(A):
            pass  
                  
        --------------    
        4. Multiple
            A   B
              |
              C
            
        
        class A:
            pass
            
        class B:
            pass  
        
        class C(A,B):
            pass 
            
        --------------    
        4. Hybrid
            A
            |
            B
            |
            C
            |
            D   
            |
        E        F
            |
            G
    
    Assignment : Write Code Snippets for above use cases 
                 Explore what happens when attributes becomes protected or private during inheriance
"""
