# taking input from user and validating it
def user_input_option():
    success=False
    while success==False:
        #Exception handling
        try:
            #taking input from the user
            user_input = int(input("Enter the option to continue: "))
            if user_input> 3 or user_input<0:
                print("ERROR!! Enter numbers only from 1-3")
                success=False
            else:
                success=True
                
            
            print("\n")
        except ValueError as e: 
            print("\n")
            print("ERROR!! Enter only numbers")
            print("\n")
    
    print("\n")
    
    return user_input


# taking name and phone number of customer and validating them
def buyer_information():
    
    print("\n")
    name_of_customer=input("Please provide us your name: ")
    print("\n")
    
    check= False
    while check==False:
        try:
            phone_number=int(input("Enter your phone number: "))
            if  phone_number<0:
                    print("ERROR!! Enter valid phone number only")
                    check=False
            else:
                    check=True
                    
                
            print("\n")
        except ValueError as e:
            print("\n")
            print("ERROR!! Enter valid phone number only")
            print("\n")
    
    print("\n")
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    
    return name_of_customer, phone_number


# displaying the laptops available in the shop
def laptop_stock():
    
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print("S.No. \t\t Laptop Name            Company Name            Price\t        Quantity        Processor             Graphics Card")
    print("-------------------------------------------------------------------------------------------------------------------------------------------")

    file = open("laptop.txt", "r")
    i = 1
    for line in file:
           print(i, "\t    " + line.replace(",","\t"))
           i = i+1
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")

    print("\t\t\t\t\t\tDear admin, Choose from the above stock which laptop you wish to sale/purchase.")
    print("\n")
  
    
# take serial number as input and validate it    
def id_validation_sales(laptop_dictionary_stock): 
    
    while True:
        serial_number = input("Enter the id of laptop you want to purchase: ")
        print("\n")
        if serial_number.isdigit():
            serial_number = int(serial_number)
            if serial_number==0:
                print("Invalid!! please provide valid input")
                print("\n")
                continue
            if serial_number <= 0 or serial_number > len(laptop_dictionary_stock):
                print("Laptop not found")
                print("\n")
                print("Please enter a valid laptop ID !!")
                print("\n")
                continue
            if int(laptop_dictionary_stock[int(serial_number)][3])==0:
                print("Sorry, The selected laptop is currently out of stock...")
                print("\n")
                print("Please select any other laptop.")
                print("\n")
                continue
          
            # serial_number = int(serial_number)
                               
            serial_number = int(serial_number)
            break
        else:
            print("Error! Please enter appropriate input.")
            print("\n") 
    return serial_number


# take quantity as input and validate it
def quantity_validation_sales(laptop_dictionary_stock,serial_number):
    
    quantity_selected= laptop_dictionary_stock[serial_number][3]
    
    quantity = input("Enter how many you want: ")
    
    while quantity.isdigit()==False :
        print("Inappropriate input for quantity!!")
        print("\n")
        quantity = input("Enter how many you want: ")
        print("\n")
        
    quantity=int(quantity)
    
    while  quantity>int(quantity_selected):
        print("Dear Customer, the number of laptop you are looking for is not available in our shop.")
        print("\n")

        quantity=int(input("Enter how many you want: "))
    print("\n")
    
    while quantity<=0 :
        print("Invalid input")
        print("Please enter a valid quantity")
        
        quantity = int(input("Enter how many you want: "))
      
    return quantity

#Updating stocks in text file
def update_stocks_sale(laptop_dictionary_stock,serial_number,quantity):
    
    laptop_dictionary_stock[serial_number][3] = int(laptop_dictionary_stock[serial_number][3])-int(quantity)

    file = open("laptop.txt", "w")
    for values in laptop_dictionary_stock.values():
        file.write(str(values[0])+","+str(values[1])+",$"+str(values[2])+",\t"+str(values[3])+",\t"+str(values[4])+",\t"+str(values[5]))
        file.write("\n")
    file.close()
    
    
# adding the elements required for bill to a new list    
def laptop_sales(laptop_dictionary_stock,serial_number,quantity,items_sold):
    
    name_of_product = laptop_dictionary_stock[serial_number][0]
    brand_name=laptop_dictionary_stock[serial_number][1]
    user_quantity = quantity
    unit_price = laptop_dictionary_stock[serial_number][2]
    selected_item_price = laptop_dictionary_stock[serial_number][2].replace("$", "")
    total_price = int(selected_item_price)*int(user_quantity)

    items_sold.append([name_of_product, brand_name, user_quantity, unit_price, total_price])
    
    return items_sold




# When 2 Pressed

# take serial number as input and validate it
def id_validation_purchase(laptop_dictionary_stock):
    
    serial_number1 = input("Enter the id of laptop you want. ")
    
    while serial_number1.isdigit()==False :
        print("Inappropriate  serial number!!")
        print("\n")
        serial_number1 = input("Enter the id of laptop you want to buy. ")
        print("\n")
        
    serial_number1=int(serial_number1)
    
    
    while serial_number1 <= 0 or serial_number1 > len(laptop_dictionary_stock) :
        print("INVALID!! You have entered an id out of our list of stocks please re-enter a valid one!!")
        print("\n")
        serial_number1 = input("Enter the id of laptop you want. ")
        while serial_number1.isdigit()==False :
            print("Inappropriate  serial number!!")
            serial_number1 = input("Enter the id of laptop you want. ")
        
        serial_number1=int(serial_number1)
    
        print("\n")
    
    return serial_number1


# take order_quantity as input and validate it
def quantity_validation_purchase():
    order_quantity = input("Enter how many you want. ")
    
    
    while order_quantity.isdigit()==False :
        print("Inappropriate input for quantity!!")
        print("\n")
        order_quantity = input("Enter how many you want. ")
        print("\n")
        
    order_quantity=int(order_quantity)
    
    while order_quantity<=0 :
        print("Dear Customer, the number of laptop you are looking for is not available in our shop.")
        print("\n")

        order_quantity=int(input("Enter how many you want: "))
    print("\n")
    
    return order_quantity



#Updating stocks in text file
def update_stocks_purchase(laptop_dictionary_stock,serial_number1,order_quantity):   
    laptop_dictionary_stock[serial_number1][3] = int(laptop_dictionary_stock[serial_number1][3])+int(order_quantity)

    file = open("laptop.txt", "w")

    for values in laptop_dictionary_stock.values():
        file.write(str(values[0])+","+str(values[1])+",$"+str(values[2])+",\t"+str(values[3])+",\t"+str(values[4])+",\t"+str(values[5]))
        file.write("\n")
    file.close()


# adding the elements required for bill to a new list
def laptop_purchase(laptop_dictionary_stock,serial_number1,order_quantity,items_bought,laptop_name):   
    
    brand_name = laptop_dictionary_stock[serial_number1][1]
    unit_net_price = laptop_dictionary_stock[serial_number1][2]
    selected_item_net_price = laptop_dictionary_stock[serial_number1][2].replace("$", "")
    total_net_price = int(selected_item_net_price)*int(order_quantity)
    
    items_bought.append([laptop_name, brand_name, order_quantity,unit_net_price,total_net_price])

    return items_bought



 