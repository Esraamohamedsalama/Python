'''
Author Name :Esraa Mohamed Ahmed
Date:11/7/2022
File Name:Grocery store 
'''

#Variables
product_list=["Potato","Tomato","Apple","Strawbary"]
Cost_list=[6,10,15,20]
Amount_List=[60,50,30,60]
customar_List=[]
Customar_amount=[]
customar_cost=[]
cost=0

print("_________Welcome ITI Shop :)__________")
while True:
    print("1-For Customar Mode\n2-For Owner Mode\n0-To Exit")
    Mode = input("Please Enter Your Mode--> ")
    if Mode == "0" :
        print("_____________GOODBYE :)_____________")
        break  
    elif Mode == "1":
        print("----------------------------------------------------")
        ch=input("1-To See Products List\n2-To Buy from the List\n3-To Print The Bill\nPlease Enter Your choice:")
        if ch == '1':
            print("***********Items Available in Our Store****************")
            print(product_list)
            print(Cost_list)
            print("-------------------------------------------------------")
        elif ch=='2':
            print("1-For ",product_list[0],"\n2-For ",product_list[1],"\n3-For ",product_list[2],"\n4-For ",product_list[3])
            Type=input("\nEnter your order:")
            amount=0
            cost =0
            if(Type=='1'):
                customar_List.append(product_list[0])
                amount=input("Enter the amount:")
                Customar_amount.append(amount)
                customar_cost.append(int (Cost_list[0]*int (amount)))
                Amount_List[0]-=float(amount)
                amount =0
            elif(Type=='2'):
                customar_List.append(product_list[1])
                amount=input("Enter the amount:")
                Customar_amount.append(amount)
                customar_cost.append(int (Cost_list[1]* int(amount)))
                Amount_List[1]-=float(amount) 
                amount =0
            elif(Type=='3'):
                customar_List.append(product_list[2])
                amount=input("Enter the amount:")
                Customar_amount.append(amount)
                customar_cost.append(int (Cost_list[3]* int(amount)))
                Amount_List[2]-=float(amount) 
                amount =0
            elif(Type=='4'):
                customar_List.append(product_list[3])
                amount=input("Enter the amount:")
                Customar_amount.append(amount)
                customar_cost.append(int (Cost_list[3]* int(amount)))
                Amount_List[3]-=float(amount) 
                amount =0
            else:
                print("Out of range\n")
            print("\n")
            
        elif ch=='3':
            print("******WELCOME TO OUR STORE******")
            for i in range(len(customar_List)):
                print(customar_List[i],"\t",Customar_amount[i])
            for i in range(len(customar_cost)):        
                cost+=int(customar_cost[i])
            print(customar_cost)
           
            print("Total Cost------>",cost)
            print("***********Thank You************")
            print("Hope to see you back soon :)")
            print("-----------------------\n")
            
    elif Mode == "2":
        print("----------------------------------------------------")
        print("1-Add Product\n2-Show product\n3-Change Cost\n4-To Clear the list\n0-To Exit")
        choice =(input("\nPlease Enter Your Choice->"))
        if choice == '0' :
            break
        elif choice == '1':
            add=input("Enter your New Product :")
            price=float(input("Enter the price of this product :"))
            Amount=float(input("Enter The Amount of the New product :"))
            product_list.append(add)
            Cost_list.append(price)
            Amount_List.append(Amount)
            print(product_list,"\n",Cost_list,"\n",Amount_List)
        elif choice == '2' :
            print(product_list[::1])
            print(Cost_list[::1])
            print(Amount_List[::1])
        elif choice == '3':
            index=int (input("Enter the item number you Want to Edit: "))
            Edit=input ("Please Enter Your New cost:")
            Cost_list[index]=Edit
        elif choice== '4':
            product_list.clear
            Cost_list.clear
            Amount_List.clear
        else :
            print("out of range")
        print("__________________________________________________________")
    else :
        print("Out Of Range")
    