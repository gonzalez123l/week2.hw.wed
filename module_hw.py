from IPython.display import clear_output

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

groccery_cart= {}
deleted_items={}
    
def groccery_item(item, amount):
    groccery_cart[item]= amount

def main():
    while True:
        item = input('Enter gorrcery item:')
        
        amount = input('How many would you like to add?:')
        groccery_item(item, amount)
        
        quant = input('See item in cart?(y/n):')
        if quant == 'y':
            print(groccery_cart)
        
        delete = input('Do you want to delete items?(y/n):')
        if delete == 'y':
            print(groccery_cart)
            
            deleted_item = input('Select item to delete')
            
            del groccery_item[deleted_items]
        
        cont = input('Would you like to continue adding to your cart?(y/n):')
        if cont == 'n':
            break
        print(groccery_cart)
        
main() 



#functions

#1st Funtion
#A is eqaul to length and B is equal to width
def footage_house(A, B):
    print("Area is", A * B)


#2nd Function
#A is equal to PI and B is equal to radius
def circumf_circle(A, B)
    print("Area of Circle is", 2*A * B)