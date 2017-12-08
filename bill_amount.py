cost_A = 10
cost_B = 20
cost_C = 30

#Below is a function defintion 
def apply_discount(amount,discount):
    #amount and discount are he parameters to the function
    final_amount = amount - (amount*discount)/100
    #final_amount is the return value from function, if there is nothing you can say return None
    return final_amount

#To take input from users
product_name  = input("Enter the product Name, A, B, C: ")
no_of_prods = input("Enter the number of products: ")
if(product_name == "A"):
    bill_amount = int(no_of_prods)*cost_A
elif(product_name == "B"):
    bill_amount = int(no_of_prods)*cost_B
elif(product_name == "C"):
    bill_amount = int(no_of_prods)*cost_C
else:
    bill_amount = int(no_of_prods)*30


print("Your bill before discount - ",bill_amount)
#This is how the function call with arguments or parameters will work  
final_bill_amount = apply_discount(bill_amount,20)
print("Your Final bill after discount - ",final_bill_amount)
print("you saved - ",bill_amount - final_bill_amount)
