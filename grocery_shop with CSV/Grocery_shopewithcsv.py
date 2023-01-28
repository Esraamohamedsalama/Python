'''
Author Name :Esraa Mohamed Ahmed
Date:11/7/2022
File Name:Grocery store with database 
'''
import csv
import Owner_list
#variables
add=0
price=0
Amount=0
# file=open('Owner_list.py',"w+")
# file.write('product_list=[]\n')
# file.write('cost_list=[]\n')
# file.write('Amount_list=[]\n')
# file.write('cost=0\n')

# file.write('customar_product=[]\n')
# file.write('customar_cost=[]\n')
# file.write('customar_amount=[]\n')

# file.write('def Print_list():\n')
# file.write('\tprint(product_list[::1])\n')
# file.write('\tprint(cost_list[::1])\n')
# file.write('\tprint(Amount_list[::1])\n\n')

# file.write('def print_Bill():\n')
# file.write('\tprint("******WELCOME TO OUR STORE******")\n')
# file.write('\tprint("Product \t Amount")\n')
# file.write('\tfor i in range(len(customar_product)):\n')
# file.write('\t\tprint(customar_product[i],"\t",customar_amount[i])\n\n')
# file.write('\tfor i in range(len(customar_cost)):\n')
# file.write('\t\tcost+=int(customar_cost[i])\n')

# file.write('\n\tprint("Total Cost------>",cost)\n')
# file.write('\tprint("***********Thank You************")\n\tprint("Hope to see you back soon :)")\n\tprint("-----------------------")\n\n')

# file.close()


print("_________Welcome ITI Shop :)__________")
while True:
    print("\n1-For Owner Mode\n2-For Customar Mode\n0-To Exit")
    Mode = input("Please Enter Your Mode--> ")
    if Mode == "0" :
        print("_____________GOODBYE :)_____________")
        break  
    elif Mode=="1":
        
        print("---------------welcome owner:)---------------")
        print("1-Add Product\n2-Show product\n3-Change Cost\n4-To Clear the list\n0-To Exit")
        choice =(input("\nPlease Enter Your Choice->"))
        if choice == '0' :
          break
        elif choice =='1':
          file=open("Owner_list.py","a")
          add=str(input("Enter your New Product :"))
          price=str(input("Enter the price of this product :"))
          Amount=str(input("Enter The Amount of the New product :"))
          file.write('product_list.append("'+add)
          file.write('")\n')
          file.write('cost_list.append('+price)
          file.write(')\n')
          file.write('Amount_list.append('+Amount)
          file.write(')\n')
          file.close()
        elif choice =='2':
          file=open("Owner_list.py","r")
          Owner_list.Print_list()    
        elif choice =='3':
          file=open("Owner_list.py","a")
          index=str (input("Enter the item number you Want to Edit: "))
          Edit=input ("Please Enter Your New cost:")
          file.write('\ncost_list['+index)
          file.write(']='+Edit)
          file.write('\n')
          file.close()
          
        elif choice=='4':
          file=open("Owner_list.py","a")
          file.write('product_list.clear')
          file.write('cost_list.clear')
          file.write('Amount_list.clear')
          file.close()
        else :
          print("out of range")
         
        print("__________________________________________________________")
               
    elif Mode=="2":
        print("----------------------------------------------------")
        ch=input("1-To See Products List\n2-To Buy from the List\n3-To Print The Bill\nPlease Enter Your choice:")
        if ch == '1':
            print("***********Items Available in Our Store****************")
            Owner_list.Print_list() 
            print("-------------------------------------------------------")
        elif ch=='2':
            j=0
            amount=0
            for i in Owner_list.product_list:
                print("-For",i,"press",j,":")
                j+=1
                
            Type=int (input("\nEnter your order:"))
            k=0
            amount=0
            for j in range(len( Owner_list.product_list)): 
                if Type==j:
                    amount=input("Enter the amount:")
                    Owner_list.customar_product.append(Owner_list.product_list[j])
                    Owner_list.customar_amount.append(amount)
                    Owner_list.customar_cost.append(int (Owner_list.cost_list[j]* int(amount)))
                    Owner_list.Amount_list[j]-=float(amount)
                    amount=0
                          
        elif ch=='3':
            print("******WELCOME TO OUR STORE******")
            print("Product    Amount    cost")
            Owner_list.print_Bill() 
            #print("Total Cost------>",Owner_list.cost)
            print("***********Thank You************")
            print("Hope to see you back soon :)")
            print("-----------------------")

              