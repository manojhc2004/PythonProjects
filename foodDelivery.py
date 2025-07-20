import time
food = {
    "biryani":100,
    "kabab":120,
    "chilli chicken":80,
    "Grilled Chicken Breast":150,
    "Tandoori Chicken":200,
    "Peri-Peri Chicken":180,
    "Chicken Curry":140,
    "Chicken Sandwich":80,
    "Chicken Shawarma":90

}

cart = {}
total_cart_price = 0

def foods():
    global food
    global cart 
    global total_cart_price
    isrunning = True
    while isrunning:
        print("biryani:100\nkabab:120\nchilli chicken:80\nGrilled Chicken Breast:150\nTandoori Chicken:200\nPeri-Peri Chicken:180\nChicken Curry:140\nChicken Sandwich:80\nChicken Shawarma:90")
        user = input("Enter Your Items (q for quit): ").lower()
        if user in food:
            cart[user]=food[user]
            total_cart_price+=food[user]
        elif user =="q":
            isrunning = False
        else:
            print("Invalid Enter")

'''def deletItem():
    isrun = True
    while isrun:
        print(f"Your Items is {cart} Total Price is {total_cart_price}\n")
        usr4 = input("Enter Your Items To Remove: ")
        delete = cart.pop(usr4)'''
        


def paymentMethod():
    print("1.UPI\n2.CASH ON DELIVERY")
    usr1 = input(":")
    if usr1 == "1":
        print("Your Are Selected UPI")
        upi = time.sleep(3)
        print("\\\\\\\\\n\\\\\\\\\n\\\\\\\\\\")
        print(f"Your Items is {cart} Total Price is {total_cart_price}")
    elif usr1 =="2":
        print("Your Are Selected Cash On Delivery")
        print(f"Your Items is {cart} Total Price is {total_cart_price}")
        
    else:
        print("Invalid Enter")

           
def order():
    usr3 = input("To Press Confirm Your order 1\nTo Cancel Your Order Press 2 :")
    if usr3 == "1":
        passmessage = time.sleep(3)
        print("Your Order Is Confirmed!")
    elif usr3 == "2":
        print("Your Order Is Canceled!\nThank You")
    else:
        print("Invalid Enter")

def checkCart():
    print(f"Your Items is:{cart}\n Total Price is:{total_cart_price}")



def main():
    isruns = True
    while isruns:
        print("*****WELCOME TO FOOD24******")
        customer = input("1.Order food\n2.Payment\n3.Confirm Order\n4.Check Cart\n5.EXIT :")
        if customer == "1":
            foods()
        elif customer == "2":
            if total_cart_price ==0:
                print("You Are Not Ordered AnyThing!")
            else:
                paymentMethod()
        elif customer =="3":
            if total_cart_price == 0:
                print("You Cart Is Empty!")
            else:
                order()
        elif customer == "4":
            if total_cart_price ==0:
                print("Your Cart Is Empty!")
            else:
                checkCart()
        elif customer == "5":
            isruns = False
            print("Thank You")
        
        else:
            print('Invalid Enter!')


main()






                    
    

 
       
            
                
           
            
                         

          
               

                
                   
                      
                    