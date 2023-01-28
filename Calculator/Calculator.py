'''
Author Name :Esraa Mohamed Ahmed
Date:11/7/2022
File Name:Scientific and programable mode Calculator
'''

print("_____________WELCOME :)_____________")
while True :
    print("1-scientific mode\n2-Programming Mode\n3-For EXIT ")
    mode= input("Please Enter Your Mode--> ")
    if mode == "1" :
        Num1,Operation,Num2=input("Entre Your Operation: ").split(" ",3)
        if str(Operation) == "+"  :
            print(Num1,"+",Num2,"=",int (Num1)+int (Num2))
        elif str(Operation) == "-" :
            print(Num1,"-",Num2,"=",int (Num1)-int (Num2))
        elif str(Operation) == "*" :
            print(Num1,"*",Num2,"=",int (Num1)*int (Num2))
        elif str(Operation) == "/" :
            if Num2 != "0" :
                print(Num1,"/",Num2,"=", float(Num1)/float (Num2))
            else :
                print ("Error Cant divid by zero")
        elif str(Operation) == "%" :
            print(Num1,"%",Num2,"=", Num1 % Num2)
    
        print("------------------------------")
    
    elif mode== "2" :
        print("******************************")
        print("1-For binary\n2-For hex\n3-For OCT\n4-For BitWise OPeration\n5-Bit Shift\n")
        choice=input ("Please Enter Your Option-->")
        if choice in ('1','2','3') :
            Num=int(input("Please Enter The Number You Want To Convert :"))
            if choice == '1'   :
                a=bin(Num)
                print(Num," in binary = ",a)
            elif choice == '2' :
                a=hex(Num)
                print(Num ,"in hex =",a)
            elif choice == '3' :
                a=oct(Num)
                print(Num ,"in oct =",a)
            
        elif choice == '4':
            Num1,Operation,Num2=input("Entre Your Operation: ").split(" ",3)
            if str(Operation) == "&" :
                And= int (Num1) & int(Num2)
                print(Num1,"&",Num2,"=","\nDecimal",And,"\nBinary=",bin(And),"\nHex=",hex(And),"\nOctal=",oct(And),"\n")
            elif str(Operation) == "|" :
                Or= int (Num1)|int(Num2)
                print(Num1,"|",Num2,"=","\nDecimal",Or,"\nBinary=",bin(Or),"\nHex=",hex(Or),"\nOctal=",oct(Or),"\n") 
            elif str(Operation) == "^" :
                Xor=int (Num1) ^ int(Num2)
                print(Num1,"^",Num2,"=","\nDecimal",Xor,"\nBinary=",bin(Xor),"\nHex=",hex(Xor),"\nOctal=",oct(Xor),"\n") 
        elif choice == '5':
            Num1,Operation,Num2=input("Entre Your Operation: ").split(" ",3)
            if str(Operation)=='>>' :
                shift_Right=int (Num1)>> int (Num2)
                print(Num1,">>",Num2,"=",shift_Right,"\t Binary-->",bin(shift_Right),"\n")
            elif str(Operation)=='<<':
                shift_left=int(Num1)<<int (Num2)
                print(Num1,"<<",Num2,"=",shift_left,"\t Binary-->",bin(shift_left),"\n")
        else :
            print("Not Found")
                
        print("******************************")    
                
    elif mode == "3" :
        print("_____________GOODBYE :)_____________")
        break
    else :
        print("___________________")
        print("Wrong OPtion Mode:(")

