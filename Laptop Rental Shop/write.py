import datetime

# During sale
# generation of sales bill in text file   
def sales_invoice1(name_of_customer,phone_number,items_sold):
    now = datetime.datetime.now()
    date_time_of_purchase =now.strftime("%d-%B-%Y %H-%M-%S")
    total = 0
    shipping_cost = 750
    
    for j in items_sold:
        total += int(j[4])
    grand_total = total+shipping_cost
    
    file=open(str(name_of_customer)+"-"+str(date_time_of_purchase)+".txt","w")
    file.write("-------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\t \t \t \t \t\t\t\tThe Large Laptop")
    file.write("\n")
    file.write("\t \t \t \t \t\t\tTeku, Kathmandu | Phone No: 987624368")
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t--------------")
    file.write("\n")
    file.write("\t \t \t \t \t\t\t\tSales Invoice")
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t--------------")
    file.write("\n")
    file.write("------------------------------------------------------------------------")
    file.write("\n")
    file.write("Customer name:      Contact number         Date Time Of Purchase")
    file.write("\n")
    file.write("------------------------------------------------------------------------")
    file.write("\n")
    file.write(str(name_of_customer)+"\t\t\t"+str(phone_number)+"\t\t\t  "+str(date_time_of_purchase))
    file.write("\n")
    file.write("------------------------------------------------------------------------")
    file.write("\n")
    file.write("\n")
    file.write("-----------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("Name of Laptop   |       Name of Brand        |       Unit Amount     |       Total  Amount  |        Quantity     |")
    file.write("\n")
    file.write("------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    
   
    for i in items_sold:
        file.write(str(i[0])+"\t\t"+str(i[1])+ "\t\t"+"$"+str(i[3]) +"\t\t    "+"$"+str(i[4])+"\t\t\t\t"+str(i[2])+"\n")
        
    file.write("\n")
    file.write("------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\n")
    file.write("The Shipping cost: "+"$"+str(shipping_cost))
    file.write("\n")
    file.write("\n")
    file.write("Overall Total Amount:"+"$"+str(grand_total))
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------------------------")          
    file.write("\n")
    file.write("*****Note: Shipping cost is added to the grand total*****"+"\n")
    file.write("\n")
    file.write("\t\t\t\t\t \t\t\t\tThank You for shopping with us :)")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    file.close()
 
 
# generation of sales bill in terminal   
def sales_invoice2(name_of_customer,phone_number,items_sold):
    now = datetime.datetime.now()
    date_time_of_purchase =now.strftime("%d-%B-%Y %H-%M-%S")
    total = 0
    shipping_cost = 750
    
    for j in items_sold:
        total += int(j[4])
    grand_total = total+shipping_cost
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t \t \t \t \t\t\t\t  The Large Laptop")
    print("\t \t \t \t \t\t\tTeku, Kathmandu | Phone No: 987624368")
    print("\n")
    print("\t\t\t\t\t\t\t\t--------------")
    print("\t \t \t \t \t\t\t\tSales Invoice")
    print("\t\t\t\t\t\t\t\t--------------")
    print("\n")
    print("------------------------------------------------------------------------")
    print("Customer name:      Contact number         Date Time")
    print("------------------------------------------------------------------------")
    print(str(name_of_customer)+"\t\t\t"+str(phone_number)+"\t\t  "+str(date_time_of_purchase))
    print("------------------------------------------------------------------------")
    print("\n")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("Name of Laptop     |        Name of Brand   |         Unit Amount     |       Total Amount   |      Quantity         |")
    print("--------------------------------------------------------------------------------------------------------------------")
    
    
    for i in items_sold:
        print(str(i[0])+"\t"+str(i[1])+ "\t"+"$"+str(i[3]) +"\t          "+"$"+str(i[4])+"\t\t        "+str(i[2]))
    print("\n")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("\n")

    print("The Shipping cost: "+"$"+str(shipping_cost))
    print("\n")
    print("Overall Total Amount is : "+"$"+str(grand_total))
    print("\n")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")          
    
    print("*****Note: Shipping cost is added to the grand total*****"+"\n")
    print("\t\t\t\t\t \t\t\t\tThank You for shopping with us :)")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")




#During purchase
# generation of purchase bill in text file
def purchase_invoice1(distributor_name,items_bought):
    now = datetime.datetime.now()
    date_time_of_purchase_owner = now.strftime("%d-%B-%Y %H-%M-%S")        
    total=0
    for i in items_bought:
        total+=int(i[4])
    vat_amount= 0.13 * total
    gross_amount= total+vat_amount
            
    file=open(str(distributor_name)+"-" +str(date_time_of_purchase_owner)+".txt","w")
    file.write("-------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\t \t \t \t \t\t\t\t \t   The Large Laptop")
    file.write("\n")
    file.write("\t \t \t \t \t\t\t\t\tTeku, Kathmandu | Phone No: 987624368")
    file.write("\n")
    file.write("-------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t\t\t--------------")
    file.write("\n")
    file.write("\t \t \t \t \t\t\t\t\t\tOrder Invoice")
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t\t\t--------------")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("Distributor Name: "+str(distributor_name))
    file.write("\n")
    file.write("\n")
    file.write("Date Time: "+str(date_time_of_purchase_owner))
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("Name of Laptop     |  Name of Brand     |       Unit Net Amount      |     Quantity                           ")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")

    for i in items_bought:
        file.write(str(i[0])+"\t   "+str(i[1])+ "              "+"$"+str(i[4])+"                "+str(i[2]))
        file.write("\n")
        
    file.write("---------------------------------------------------------------------------------------------------------------------------------------------------------")   
    file.write("\n")
    file.write("\n")
    file.write("VAT Amount: "+ "$"+str(vat_amount))
    file.write("\n")
    file.write("\n")
    file.write("Overall total amount: "+"$"+str(gross_amount))
    file.write("\n")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\t\t\t\t\t \t\t\t\t\t\t\tThank You")
    file.write("\n")
    file.write("\n")
    file.close()
    

# generation of purchase bill in text file
def purchase_invoice2(distributor_name,items_bought):
    now = datetime.datetime.now()
    date_time_of_purchase_owner = now.strftime("%d")+"-"+now.strftime("%B")+"-"+now.strftime("%Y")+"  "+now.strftime("%H")+"-"+now.strftime("%M")+"-"+now.strftime("%S")     
   
    total=0
    for i in items_bought:
        total+=int(i[4])
    vat_amount= 0.13 * total
    gross_amount= total+vat_amount
            
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t \t \t \t \t\t\t\t \t  The Large Laptop")
    print("\t \t \t \t \t\t\t\tTeku, Kathmandu | Phone No: 987624368")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("\t\t\t\t\t\t\t\t\t--------------")
    print("\t \t \t \t \t\t\t\t\tOrder Invoice")
    print("\t\t\t\t\t\t\t\t\t--------------")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Distributor Name: "+str(distributor_name))
    print("\n")
    print("Date Time: "+str(date_time_of_purchase_owner))
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Name of Laptop     |      Name of Brand        |          Unit Net Amount     |       Quantity                           ")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
   

    for i in items_bought:
        print(str(i[0])+"   "+str(i[1])+ "               "+"$"+str(i[4])+"                      "+str(i[2]))
            
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("\n")
    print("VAT Amount: "+ "$"+str(vat_amount))
    print("\n")
    print("Overall Total amount: "+"$"+str(gross_amount))
    print("\n")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("\t\t\t\t\t \t\t\t\t-----Thank You-----")
    print("\n")
    print("\n")

    
    


