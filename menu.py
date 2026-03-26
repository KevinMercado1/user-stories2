from add_product import add_product as adp
from Show_inventory import show_inventory as show
from calculate_total import calculate_total as Cal 
m = True

def menu ():
     option = ""
     while m:
        print('\n --- Menu Options ---\n')
        print('1.Add Products.')
        print('2. Show Inventory.')
        print('3.Calculate Total')
        print('4. Exit')

        if option == 1:
            print('Please enter a product: ')