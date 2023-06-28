# import random
    
    
# num = random.randint(1,20) 

# while True:
#     guess = int(input("Guess A Number Between 1 to 20: "))
    
#     if guess==num:
#         print("You Gueseed A Correct Number")
#         break
    
#     if guess>20 or guess<0:
#         print("Your guessed is out of range")
#         break  
      
#     elif guess>num:
#         print("You guessed A Greater number") 
          
#     elif guess<num:
#         print("You Guessed A Smaller number")  
        
        

# Oops conceps project-------------------------------Bankdemo--------------------------------------

# class Bank:
    
#     def openaccount(self, cname, acno, balance):
#         self.c = cname
#         self.a = acno
#         self.b = balance
#         print("Hello", self.c, ", Your Account number ", self.a, "Is Opened With ", self.b)            

#     def deposit(self,amount):
#         self.b = self.b + amount
        
#     def withdraw(self, amount):
#         if amount<self.b:
#             self.b=self.b-amount
#         else:
#             print("Sorry You Need Another ", amount-self.b)            

#     def checkBalance(self):
#         print("Current Balance: ", self.b)        


# b1 = Bank()   
# # b2 = Bank()  
# print("*"*75)   
# cname = input("Enter Customer Name: ")
# print("*"*75)
# acno = int(input("Enter Account Number: "))
# print("*"*75)
# balance = int(input("Enter Initial Balance: "))
# print("*"*75)

# b1.openaccount(cname, acno, balance)
# print("*"*75)
# # b2.openaccount(cname, acno, balance)

# while True:
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Check Balance")
#     print("4. Exit")
#     print("*"*75)
#     choice=int(input("Enter Your choice: "))
    
#     if choice==1:
#         amount=int(input("Enter Deposit Amount: "))
#         b1.deposit(amount)
#         print("*"*75)

#     elif choice==2:
#         amount=int(input("Enter Withdraw Amount: "))
#         b1.withdraw(amount)
#         print("*"*75)

#     elif choice==3:
#         b1.checkBalance()
#         print("*"*75)

#     else:
#         print("Thank You For Using Our Services. Have a great day")            
#         break



#---------------------Bike Rental System-------------------------#

# class Bikeshop:
    
#     def __init__(self,stock):
#         self.stock = stock
#     def displayBike(self):
#         print("Total Bikes", self.stock)
#     def rentForBike(self,q):
        
#         if q<0:
#             print("Enter the positive value or greater than zero")        
#         elif q>self.stock:
#             print("Enter the Value (less then stock)")    
#         else:
#             self.stock = self.stock-q
#             print("Total Prices", q*100)    
#             print("Total Bikes", self.stock)
            
            
# while True:
#     obj = Bikeshop(100)
#     uc = int(input('''
#       1 Display Stocks
#       2 Rent a Bike
#       3 Exit             
#                    ''')) 
    
#     if uc == 1:
#         obj.displayBike()           
#     elif uc==2:
#         n = int(input("Enter The Quantity:  "))    
#         obj.rentForBike(n)
#     else:
#         break    


#-------------------------Library Demo-----------------------------------#

# class Library:
    
#     def __init__(self, list, name):
#         self.bookList = list
#         self.name = name
#         self.lendDict = {}
        
#     def displayBooks(self):
#         print(f'We have following books inn our library: {self.name}')     
#         for book in self.bookList:
#             print(book)
    
#     def lendBook(self,user, book):
#              if book not in self.lendDict.keys():
#                  self.lendDict.update({book:user})
#                  print("Lender-book database has been updated. You can take the book now")   
#              else:
#                  print(f'Book is already being used by {self.lendDict[book]}') 
                 
#     def addbook(self,book):
#         self.bookList.append(book)
#         print("Book has been added to the book list")                 
    
#     def returnBook(self, book):
#         self.lendDict.pop(book)    
     
     
# if __name__ == '__main__':
#     harry = Library(['Python', "Rich Daddy Poor Daddy", "Harry Potter", "C++ Basics", 'Algorithms by CLRS'], "Sector_4_Library")        

#     while(True):
#         print(f'Welcome to the {harry.name} library. Enter Your choice to continue')
#         print("1. Display Books")
#         print("2. Lend a Book")
#         print("3. Add a Book")
#         print("4. Return a Book")
#         user_choice = input("Enter your choice1: ")
#         if user_choice not in ["1", "2", "3", "4"]:
#             print("Please enter a valid option")
#             continue
#         else:
#             user_choice = int(user_choice) 
            
#         if user_choice == 1:
#             harry.displayBooks()
            
#         elif user_choice == 2:
#             book = input("Enter the name of the book your want to lend: ")
#             user = input("Enter your name")        
#             harry.lendBook(user,book)
            
#         elif user_choice == 3:
#             book = input("Enter the name of the book youn want to add: ")    
#             harry.addbook(book)
            
#         elif user_choice == 4:
#             book = input("Enter the name of the book you want to return: ")
#             harry.returnBook(book)
            
#         else: 
#             print("Not a valid option")    

#         print("Press q to quit and c to continue") 
#         user_choice2 = input("Enter your choice2: ")   
#         while(user_choice2!="c" and user_choice2!="q"):
#         # while(user_choice2=="c" or user_choice2=="q"):
#             # user_choice2 = input("Enter your choice1: ")
#             if user_choice2 == "q":
#                 exit()
#             elif user_choice2 == "c":
#                 continue    
                                                        
                
            
        



    


         
        
        
        
    
