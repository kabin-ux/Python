# reading the data in laptop.txt text file and adding them into a dictionary(laptop_dictionary_stock)
def get_data_from_textfile():
    file = open("laptop.txt", "r")
    laptop_dictionary_stock = {}
    laptop_id = 1
    for line in file:
        line = line.replace("\n", "")
        line = line.replace("$", "")
        laptop_dictionary_stock.update({laptop_id: line.split(",")})
        laptop_id = laptop_id + 1
    file.close()

    return laptop_dictionary_stock
    



