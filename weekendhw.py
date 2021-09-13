class Cart:
    def __init__(self):
        self.cart=[] 
    
    def display(self):
        print(f"Here is your cart {self.cart}, Would you like to continue?")
        
    def additem(self, newitem):
        self.cart.append(newitem)
        
    def deleteitem(self, delete_item):
        self.cart.remove(delete_item)
        

class Userinterface:
    def __init__(self,cart):
        self.cart = cart
        
    def go_shopping(self):
        while True:
            response = input(f'Please type a number 1 to add 2 to del 3 show 4 quit ')
            while response not in ["1","2","3","4"]:
                response = input(f'Please enter a valid response ')
            if response == "1":
                item = input('Please enter the item you wish to add ')
                self.cart.additem(item)
            if response == "2":
                item = input('Please enter the item you wish to remove ')
                self.cart.deleteitem(item)
            if response == "3":
                self.cart.display()
            if response == "4":
                print(f'Goodbye')
                break
                
cart=Cart()

ui = Userinterface(cart)
ui.go_shopping()