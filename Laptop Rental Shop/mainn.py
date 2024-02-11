from operations import *
from read import *
from write import *



print("\n")
print("\n")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\n")
print("\t \t \t \t \t\t\t\t\t  The Large Laptop")
print("\t \t \t \t \t\t\t\tTeku, Kathmandu | Phone No: 987624368")
print("\n")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t \t \t \t \t\t\t     Hello admin! I hope you have a good day ahead!")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\n")

laptop_dictionary_stock= get_data_from_textfile()
loop_execution = True

while loop_execution == True:
    
    print("Press the dedicated number from 1-3 for the required task")
    print("\n")
    print("1. To sale laptops           ||      2. To purchase laptops           ||       3. To exit the system")
    print("\n")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    
#asking user to input
    user_input=user_input_option()
    
    
#1 Pressed
    if user_input == 1:
        print("\t\t\tKey 1 PRESSED")
        #asking user to input name, contact number
        name_of_customer, phone_number = buyer_information()
        
        
        items_sold=[]
        sell_more = True

        while sell_more == True:
            
            #displaying stocks 
            laptop_stock()
            
            print("\n")
            
            cont=False
            while cont==False:
            #taking serial number from user and validating serial number
            
                serial_number=id_validation_sales(laptop_dictionary_stock)
                
                quantity=quantity_validation_sales(laptop_dictionary_stock,serial_number)
                
                if int(laptop_dictionary_stock[serial_number][3])>0 :
                    
                    
                    
                #updating stocks
                    update_stocks_sale(laptop_dictionary_stock,serial_number,quantity)
                    
                #appending into array
                    laptop_sales(laptop_dictionary_stock,serial_number,quantity,items_sold)
                    
                 #asking customer if wants 
                    customer_request_message=input("Do you want to buy more (Y/N)? ")
                    print("\n")
                    if customer_request_message=="Y" or customer_request_message=="y":
                        sell_more=True
                        
                    else:
                        
                        laptop_name=laptop_dictionary_stock[serial_number][0]
                        brand_name=laptop_dictionary_stock[serial_number][1]
                        print("\n")
                        print("The Bill is displayed below:")
                        print("\n")
                        
                        #Writing Bill in text file
                        sales_invoice1(name_of_customer,phone_number,items_sold)
                        
                        #Writing Bill in terminal
                        sales_invoice2(name_of_customer,phone_number,items_sold)
                                        
                        
                        cont=True 
                        sell_more=False
                        success=False
                        
                else:
                    print("Sorry, The selected laptop is currently out of stock...")
                    print("\n")
                    print("Please select any other laptop.")
                    cont=False
                    print("\n")    
              
                

#2 Pressed   
    elif user_input == 2:
        print("\t\t\t2 PRESSED")
        print("\n")
        distributor_name = input("Enter name of the distributor/company: ")
        print("\n")
        
        #list to store data for bill generation
        items_bought=[]
        buy_more = True
            
        while buy_more==True:
            print("We want to order some laptops")
            print("\n")  
            
            #displaying stocks 
            laptop_stock()
            
            print("\n")  
            
            #taking serial no. adn validating it
            serial_number1= id_validation_purchase(laptop_dictionary_stock)
            
            
            print("\n")
            
            laptop_name = laptop_dictionary_stock[serial_number1][0]
            
            
            # taking order quantity and validating it
            order_quantity=quantity_validation_purchase()
        
            
            #updating stocks
            update_stocks_purchase(laptop_dictionary_stock,serial_number1,order_quantity)
                
            #appending into array
            laptop_purchase(laptop_dictionary_stock,serial_number1,order_quantity,items_bought,laptop_name)
            
            
            #asking owner he/she wants to purchase more
            owner_request_message=input("Do you want to purchase more (Y/N)? ")
            print("\n")
            if owner_request_message=="Y" or owner_request_message=="y":
                buy_more=True
            else:
                print("\n")
                print("The Bill is displayed below:")
                print("\n")
                laptop_name=laptop_dictionary_stock[serial_number1][0]
                unit_net_price = laptop_dictionary_stock[serial_number1][2]
                selected_item_net_price = laptop_dictionary_stock[serial_number1][2].replace("$", "")
                total_net_price = int(selected_item_net_price)*int(order_quantity)
                
                #Display Purchase invoice in terminal
                purchase_invoice2(distributor_name,items_bought) 
                
                #Writing Purchase invoice in text file
                purchase_invoice1(distributor_name,items_bought)
              
                buy_more=False
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
#3 Pressed               
    elif user_input == 3:
        print("\t\t\t3 PRESSED")
        loop_execution = False
        print("You exit the system.")




