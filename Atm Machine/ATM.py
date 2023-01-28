#######################################
# GUI-Author: Esraa Mohamed Ahmed
# Date: 23/1/2023
#######################################
# importing Libraries
#######################################
from tkinter import* 
from tkinter import ttk
import tkinter.messagebox
import time
import math   
'''**************************************************_Window _**********************************************************'''
cash=1000
loan =0
Get_cash=0
class atm:
    def __init__(self,window_1):
        self.window_1=window_1
        self.window_1.title("ITI ATM MACHINE")
        blank_space= " "
        #used to set main window size 
        self.window_1.geometry("800x760+280+0")
        #Back Ground of the Window
        self. window_1.configure(bg="black")
        #========================================FRAMES====================================================#
        #Main Frame
        MainFrame=Frame(self.window_1,bd=20,width=784,height=700,relief=RIDGE)
        MainFrame.configure(bg="gray")
        MainFrame.grid()
        
        TopFrame1=Frame(MainFrame,bd=7,width=740,height=300,relief=RIDGE)
        TopFrame1.configure(bg="black")
        TopFrame1.grid(row=1,column=0,padx=12)
        
        TopFrame2=Frame(MainFrame,bd=7,width=740,height=300,relief=RIDGE)
        TopFrame2.configure(bg="black")
        TopFrame2.grid(row=0,column=0,padx=8)
        
        TopFrame2Left=Frame(TopFrame2,bd=5,width=177,height=300,relief=RIDGE)
        TopFrame2Left.configure(bg="black")
        TopFrame2Left.grid(row=0,column=0,padx=8)
        
        localtime=time.asctime(time.localtime(time.time()))
        labl2=Label(TopFrame2,font=('aria',11,'bold'),text=localtime,fg="Powder Blue",bg="Black",bd=10,anchor='w')
        labl2.grid(row=1,column=1)
        
        TopFrame2Mid=Frame(TopFrame2,bd=5,width=500,height=290,relief=RIDGE)
        TopFrame2Mid.configure(bg="Powder Blue")
        TopFrame2Mid.grid(row=0,column=1,padx=8)
        
        TopFrame2Right=Frame(TopFrame2,bd=5,width=177,height=300,relief=RIDGE)
        TopFrame2Right.configure(bg="black")
        TopFrame2Right.grid(row=0,column=2,padx=8)
                
        #************************************************Functions************************************************************#
        def Done():
            pinNo=self.txtReceipt.get("3.0","end-1c")
            if(pinNo==str("3456")):            
                self.txtReceipt.focus_set()
                self.txtReceipt.delete("1.0",END) 
                self.txtReceipt.insert(END,'\t\tITI_ATM'+ "\n\n")
                self.txtReceipt.insert(END,'50\t\t\t\t      250' + "\n\n\n\n")
                self.txtReceipt.insert(END,'100\t\t\t\t     300' + "\n\n\n\n\n")
                self.txtReceipt.insert(END,'150\t\t\t\t     350' + "\n\n\n\n\n")
                self.txtReceipt.insert(END,'200\t\t\t\t     400' + "\n\n")            
                #-----------------------ENABLE_LEFT_ARROWS--------------------------#            
                self.btnArrowL1=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Fifty,
                image=self.img_arrow_Left).grid(row=0,column=0,padx=2,pady=10)
                
                self.btnArrowL2=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Hundred,
                image=self.img_arrow_Left).grid(row=1,column=0,padx=2,pady=10)
                
                self.btnArrowL3=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Hundred_Fifty,
                image=self.img_arrow_Left).grid(row=2,column=0,padx=2,pady=10)
                
                self.btnArrowL4=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Two_Hundred,
                image=self.img_arrow_Left).grid(row=3,column=0,padx=2,pady=10)
                #-----------------------ENABLE_RIGHT_ARROWS--------------------------#   
                self.btnArrowR1=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=Two_Hundred_Fifty,
                image=self.img_arrow_Right).grid(row=0,column=0,padx=2,pady=10)
                
                self.btnArrowR2=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=Three_Hundred,
                image=self.img_arrow_Right).grid(row=1,column=0,padx=2,pady=10)
                
                self.btnArrowR3=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=Three_Hundred_fifity,
                image=self.img_arrow_Right).grid(row=2,column=0,padx=2,pady=10)
                
                self.btnArrowR4=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=Four_Hundred,
                image=self.img_arrow_Right).grid(row=3,column=0,padx=2,pady=10)
            else:
                self.txtReceipt.focus_set()
                self.txtReceipt.delete("1.0",END) 
                self.txtReceipt.insert(END,'Invalid Bank ID Account.'+ "\n\n")
                
                #=========================================Enter_Button====================================================#  
        def enter_pin():
            pinNo=self.txtReceipt.get("3.0","end-1c")
            if((pinNo==str("1234")) or (pinNo==str("4343")) or (pinNo==str("9876"))):
                self.txtReceipt.delete("1.0",END) 
                self.txtReceipt.insert(END,'\t\tITI_ATM'+ "\n\n")
                self.txtReceipt.insert(END,'Withdraw Cash\t\t\t\t     Loan' + "\n\n\n\n")
                self.txtReceipt.insert(END,'Cash With Receipt\t\t\t\t  Deposite' + "\n\n\n\n\n")
                self.txtReceipt.insert(END,'Balance\t\t\t     Request New Pin' + "\n\n\n\n\n")
                self.txtReceipt.insert(END,'Transaction\t\t\t     Print Statement' + "\n\n")
                
                #-----------------------ENABLE_LEFT_ARROWS--------------------------#            
                self.btnArrowL1=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=withdrawcash,
                image=self.img_arrow_Left).grid(row=0,column=0,padx=2,pady=10)
                
                self.btnArrowL2=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Cash_with_Receipt,
                image=self.img_arrow_Left).grid(row=1,column=0,padx=2,pady=10)
                
                self.btnArrowL3=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=balance,
                image=self.img_arrow_Left).grid(row=2,column=0,padx=2,pady=10)
                
                self.btnArrowL4=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Transaction,
                image=self.img_arrow_Left).grid(row=3,column=0,padx=2,pady=10)
                #-----------------------ENABLE_RIGHT_ARROWS--------------------------#   
                self.btnArrowR1=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=Loan,
                image=self.img_arrow_Right).grid(row=0,column=0,padx=2,pady=10)
                
                self.btnArrowR2=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=deposite,
                image=self.img_arrow_Right).grid(row=1,column=0,padx=2,pady=10)
                
                self.btnArrowR3=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=request_new_pin,
                image=self.img_arrow_Right).grid(row=2,column=0,padx=2,pady=10)
                
                self.btnArrowR4=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=statement,
                image=self.img_arrow_Right).grid(row=3,column=0,padx=2,pady=10)
            else :
                self.txtReceipt.delete("1.0",END)
                self.txtReceipt.insert(END,'Invalid Pin Number'+ "\n\n")  
        #=========================================Clear_Button====================================================#  
        def clear_pin():
        
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'\t\tITI_ATM'+ "\n")
            self.txtReceipt.insert(END,'Please Enter Your Password:'+ "\n")
            #-----------------------ENABLE_LEFT_ARROWS--------------------------#            
            self.btnArrowL1=Button(TopFrame2Left,width=80,height=50,state=DISABLED,
            image=self.img_arrow_Left).grid(row=0,column=0,padx=2,pady=10)
            
            self.btnArrowL2=Button(TopFrame2Left,width=80,height=50,state=DISABLED,
            image=self.img_arrow_Left).grid(row=1,column=0,padx=2,pady=10)
            
            self.btnArrowL3=Button(TopFrame2Left,width=80,height=50,state=DISABLED,
            image=self.img_arrow_Left).grid(row=2,column=0,padx=2,pady=10)
            
            self.btnArrowL4=Button(TopFrame2Left,width=80,height=50,state=DISABLED,
            image=self.img_arrow_Left).grid(row=3,column=0,padx=2,pady=10)
            #-----------------------ENABLE_RIGHT_ARROWS--------------------------#   
            self.btnArrowR1=Button(TopFrame2Right,width=80,height=50,state=DISABLED,
            image=self.img_arrow_Right).grid(row=0,column=0,padx=2,pady=10)
            
            self.btnArrowR2=Button(TopFrame2Right,width=80,height=50,state=DISABLED,
            image=self.img_arrow_Right).grid(row=1,column=0,padx=2,pady=10)
            
            self.btnArrowR3=Button(TopFrame2Right,width=80,height=50,state=DISABLED,
            image=self.img_arrow_Right).grid(row=2,column=0,padx=2,pady=10)
            
            self.btnArrowR4=Button(TopFrame2Right,width=80,height=50,state=DISABLED,
            image=self.img_arrow_Right).grid(row=3,column=0,padx=2,pady=10)
        #====================================Return_Button=================================================# 
        def Return_Pin():
            self.txtReceipt.delete("1.0",END)              
            
            self.txtReceipt.insert(END,'\t\tITI_ATM'+ "\n\n")
            self.txtReceipt.insert(END,'Withdraw Cash\t\t\t\t     Loan' + "\n\n\n\n")
            self.txtReceipt.insert(END,'Cash With Receipt\t\t\t\t  Deposite' + "\n\n\n\n\n")
            self.txtReceipt.insert(END,'Balance\t\t\t     Request New Pin' + "\n\n\n\n\n")
            self.txtReceipt.insert(END,'Transaction\t\t\t     Print Statement' + "\n\n")
            
            #-----------------------ENABLE_LEFT_ARROWS--------------------------#            
            self.btnArrowL1=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=withdrawcash,
            image=self.img_arrow_Left).grid(row=0,column=0,padx=2,pady=10)
            
            self.btnArrowL2=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Cash_with_Receipt,
            image=self.img_arrow_Left).grid(row=1,column=0,padx=2,pady=10)
            
            self.btnArrowL3=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=balance,
            image=self.img_arrow_Left).grid(row=2,column=0,padx=2,pady=10)
            
            self.btnArrowL4=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Transaction,
            image=self.img_arrow_Left).grid(row=3,column=0,padx=2,pady=10)
            #-----------------------ENABLE_RIGHT_ARROWS--------------------------#   
            self.btnArrowR1=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=Loan,
            image=self.img_arrow_Right).grid(row=0,column=0,padx=2,pady=10)
            
            self.btnArrowR2=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=deposite,
            image=self.img_arrow_Right).grid(row=1,column=0,padx=2,pady=10)
            
            self.btnArrowR3=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=request_new_pin,
            image=self.img_arrow_Right).grid(row=2,column=0,padx=2,pady=10)
            
            self.btnArrowR4=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=statement,
            image=self.img_arrow_Right).grid(row=3,column=0,padx=2,pady=10)
        #=====================================================================================================#
        #============================================Numbers=================================================#
        def insert0():
            Value0=0
            self.txtReceipt.insert(END,Value0)
            
        def insert1():
            Value1=1
            self.txtReceipt.insert(END,Value1)

        def insert2():
            Value2=2
            self.txtReceipt.insert(END,Value2)

        def insert3():
            Value3=3
            self.txtReceipt.insert(END,Value3)
            
        def insert4():
            Value4=4
            self.txtReceipt.insert(END,Value4)   

        def insert5():
            Value5=5
            self.txtReceipt.insert(END,Value5) 

        def insert6():
            Value6=6
            self.txtReceipt.insert(END,Value6)

        def insert7():
            Value7=7
            self.txtReceipt.insert(END,Value7)
            
        def insert8():
            Value8=8
            self.txtReceipt.insert(END,Value8)
            
        def insert9():
            Value9=9
            self.txtReceipt.insert(END,Value9)
        #----------------------------------Distroy_Window-----------------------------------------#
        def cancel():
            Cancel=tkinter.messagebox.askyesno("ATM","Confirm if you want to cancel")
            if Cancel>0:
                self.window_1.destroy()
                return                      
        #-----------------------------------------------------------------------------------------#
        def withdrawcash():
            enter_pin()
            self.txtReceipt.delete("1.0",END)              
            self.txtReceipt.focus_set()
            self.txtReceipt.delete("1.0",END) 
            self.txtReceipt.insert(END,'\t\tITI_ATM'+ "\n\n")
            self.txtReceipt.insert(END,'50\t\t\t\t      250' + "\n\n\n\n")
            self.txtReceipt.insert(END,'100\t\t\t\t     300' + "\n\n\n\n\n")
            self.txtReceipt.insert(END,'150\t\t\t\t     350' + "\n\n\n\n\n")
            self.txtReceipt.insert(END,'200\t\t\t\t     400' + "\n\n")            
            #----------------------------ENABLE_LEFT_ARROWS--------------------------#            
            self.btnArrowL1=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Fifty,
            image=self.img_arrow_Left).grid(row=0,column=0,padx=2,pady=10)
            
            self.btnArrowL2=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Hundred,
            image=self.img_arrow_Left).grid(row=1,column=0,padx=2,pady=10)
            
            self.btnArrowL3=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Hundred_Fifty,
            image=self.img_arrow_Left).grid(row=2,column=0,padx=2,pady=10)
            
            self.btnArrowL4=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Two_Hundred,
            image=self.img_arrow_Left).grid(row=3,column=0,padx=2,pady=10)
            #---------------------------ENABLE_RIGHT_ARROWS---------------------------#   
            self.btnArrowR1=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=Two_Hundred_Fifty,
            image=self.img_arrow_Right).grid(row=0,column=0,padx=2,pady=10)
            
            self.btnArrowR2=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=Three_Hundred,
            image=self.img_arrow_Right).grid(row=1,column=0,padx=2,pady=10)
            
            self.btnArrowR3=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=Three_Hundred_fifity,
            image=self.img_arrow_Right).grid(row=2,column=0,padx=2,pady=10)
            
            self.btnArrowR4=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=Four_Hundred,
            image=self.img_arrow_Right).grid(row=3,column=0,padx=2,pady=10)
            #==============================================================================================================#
        def Cash_with_Receipt():
            enter_pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'\t\tITI_ATM'+ "\n\n")
            self.txtReceipt.insert(END,'\t  Welcome To Our Bank sir. \n\n\n')
            self.txtReceipt.insert(END,'-Your Current Status is : ACTIVE \n\n')
            self.txtReceipt.insert(END,'-Account Balance:')
            self.txtReceipt.insert(END,cash)
            self.txtReceipt.insert(END,'\n-Withdraw Cash:')
            self.txtReceipt.insert(END,Get_cash)
            self.txtReceipt.insert(END,'\n-Your Loan To the Bank is :')
            self.txtReceipt.insert(END,loan)
            self.txtReceipt.insert(END,'\n\n\n\n\t '+localtime)
            self.txtReceipt.insert(END,'\n\n\t  Thanks For Using ITI Bank\n')
             #==============================================================================================================#       
        def Loan():
            enter_pin()
            self.txtReceipt.delete("1.0",END)              
            self.txtReceipt.focus_set()
            self.txtReceipt.delete("1.0",END) 
            self.txtReceipt.insert(END,'\t\tITI_ATM'+ "\n\n")
            self.txtReceipt.insert(END,'500\t\t\t\t     2500' + "\n\n\n\n")
            self.txtReceipt.insert(END,'1000\t\t\t\t    3000' + "\n\n\n\n\n")
            self.txtReceipt.insert(END,'1500\t\t\t\t    3500' + "\n\n\n\n\n")
            self.txtReceipt.insert(END,'2000\t\t\t\t    4000' + "\n\n")            
            #-------------------------ENABLE_LEFT_ARROWS----------------------------#            
            self.btnArrowL1=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Five_Hundred,
            image=self.img_arrow_Left).grid(row=0,column=0,padx=2,pady=10)
            
            self.btnArrowL2=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Thousand,
            image=self.img_arrow_Left).grid(row=1,column=0,padx=2,pady=10)
            
            self.btnArrowL3=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Thousand_Five_Hundred,
            image=self.img_arrow_Left).grid(row=2,column=0,padx=2,pady=10)
            
            self.btnArrowL4=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Two_Thousand,
            image=self.img_arrow_Left).grid(row=3,column=0,padx=2,pady=10)
            #-------------------------ENABLE_RIGHT_ARROWS----------------------------#   
            self.btnArrowR1=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=Two_Thousand_Five_Hundred,
            image=self.img_arrow_Right).grid(row=0,column=0,padx=2,pady=10)
            
            self.btnArrowR2=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=Three_Thousand,
            image=self.img_arrow_Right).grid(row=1,column=0,padx=2,pady=10)
            
            self.btnArrowR3=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=Three_Thousand_Five_Hundred,
            image=self.img_arrow_Right).grid(row=2,column=0,padx=2,pady=10)
            
            self.btnArrowR4=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=Four_Thousand,
            image=self.img_arrow_Right).grid(row=3,column=0,padx=2,pady=10)
            #==============================================================================================================#
        def deposite():
            enter_pin()
            self.txtReceipt.delete("1.0",END)              
            self.txtReceipt.focus_set()
            self.txtReceipt.delete("1.0",END) 
            self.txtReceipt.insert(END,'\t\tITI_ATM'+ "\n\n")
            self.txtReceipt.insert(END,'500\t\t\t\t     2500' + "\n\n\n\n")
            self.txtReceipt.insert(END,'1000\t\t\t\t    3000' + "\n\n\n\n\n")
            self.txtReceipt.insert(END,'1500\t\t\t\t    3500' + "\n\n\n\n\n")
            self.txtReceipt.insert(END,'2000\t\t\t\t    4000' + "\n\n")            
            #-----------------------ENABLE_LEFT_ARROWS--------------------------#            
            self.btnArrowL1=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Five_Hundred,
            image=self.img_arrow_Left).grid(row=0,column=0,padx=2,pady=10)
            
            self.btnArrowL2=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Thousand,
            image=self.img_arrow_Left).grid(row=1,column=0,padx=2,pady=10)
            
            self.btnArrowL3=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Thousand_Five_Hundred,
            image=self.img_arrow_Left).grid(row=2,column=0,padx=2,pady=10)
            
            self.btnArrowL4=Button(TopFrame2Left,width=80,height=50,state=NORMAL,command=Two_Thousand,
            image=self.img_arrow_Left).grid(row=3,column=0,padx=2,pady=10)
            #-----------------------ENABLE_RIGHT_ARROWS--------------------------#   
            self.btnArrowR1=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=Two_Thousand_Five_Hundred,
            image=self.img_arrow_Right).grid(row=0,column=0,padx=2,pady=10)
            
            self.btnArrowR2=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=Three_Thousand,
            image=self.img_arrow_Right).grid(row=1,column=0,padx=2,pady=10)
            
            self.btnArrowR3=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=Three_Thousand_Five_Hundred,
            image=self.img_arrow_Right).grid(row=2,column=0,padx=2,pady=10)
            
            self.btnArrowR4=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=Four_Thousand,
            image=self.img_arrow_Right).grid(row=3,column=0,padx=2,pady=10)
                
            #==============================================================================================================#     
        def request_new_pin():
            enter_pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'\t   Welcome to ITI Bank\n\n\n')
            self.txtReceipt.insert(END,' New Pin Will Be Sent to Yout Home Address\n')
            self.txtReceipt.insert(END,'\n\n\n\n\n\n\n\n\n\n\tThanks For Using ITI Bank\n')
            #==============================================================================================================#
        def balance():
            enter_pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'\tWelcome to ITI Bank\n\n')
            self.txtReceipt.insert(END,' Your Current Balance is :')
            self.txtReceipt.insert(END,cash)
            self.txtReceipt.insert(END,'$')
            self.txtReceipt.insert(END,'\n Your Loan To the Bank is :')
            self.txtReceipt.insert(END,loan)
            self.txtReceipt.insert(END,'\n\n\n\n\n\n\n\n\t '+localtime)
            self.txtReceipt.insert(END,'\n\n\tThanks For Using ITI Bank\n')
            #==============================================================================================================#
        def statement():
            enter_pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'\t     ITI ATM MACHINE.\n')
            self.txtReceipt.insert(END,'\t  Welcome To Our Bank sir. \n\n\n')
            self.txtReceipt.insert(END,'-Your Current Status is : ACTIVE \n')
            self.txtReceipt.insert(END,'-Account Balance:')
            self.txtReceipt.insert(END,cash)
            self.txtReceipt.insert(END,'\n-Your Loan To the Bank is :')
            self.txtReceipt.insert(END,loan)
            self.txtReceipt.insert(END,'\n\n\n\n\n\n\n\t'+localtime)
            self.txtReceipt.insert(END,'\n\n\t  Thanks For Using ITI Bank\n')
            #==============================================================================================================#
        def Transaction():
            enter_pin()
            self.txtReceipt.delete("1.0",END) 
            self.txtReceipt.insert(END,'\tWelcome to ITI Bank\n')
            self.txtReceipt.insert(END,'Please Enter The Transaction Account ID:\n') 
                       
            #-----------------------ENABLE_LEFT_ARROWS--------------------------#            
            self.btnArrowL1=Button(TopFrame2Left,width=80,height=50,state=DISABLED,
            image=self.img_arrow_Left).grid(row=0,column=0,padx=2,pady=10)
            
            self.btnArrowL2=Button(TopFrame2Left,width=80,height=50,state=DISABLED,
            image=self.img_arrow_Left).grid(row=1,column=0,padx=2,pady=10)
            
            self.btnArrowL3=Button(TopFrame2Left,width=80,height=50,state=DISABLED,
            image=self.img_arrow_Left).grid(row=2,column=0,padx=2,pady=10)
            
            self.btnArrowL4=Button(TopFrame2Left,width=80,height=50,state=DISABLED,
            image=self.img_arrow_Left).grid(row=3,column=0,padx=2,pady=10)
            #-----------------------ENABLE_RIGHT_ARROWS--------------------------#   
            self.btnArrowR1=Button(TopFrame2Right,width=80,height=50,state=DISABLED,
            image=self.img_arrow_Right).grid(row=0,column=0,padx=2,pady=10)
            
            self.btnArrowR2=Button(TopFrame2Right,width=80,height=50,state=DISABLED,
            image=self.img_arrow_Right).grid(row=1,column=0,padx=2,pady=10)
            
            self.btnArrowR3=Button(TopFrame2Right,width=80,height=50,state=DISABLED,
            image=self.img_arrow_Right).grid(row=2,column=0,padx=2,pady=10)
            
            self.btnArrowR4=Button(TopFrame2Right,width=80,height=50,state=NORMAL,command=Done,
            image=self.img_arrow_Right).grid(row=3,column=0,padx=2,pady=10)
        #======================================Lift_Widget====================================================#
        self.txtReceipt=Text(TopFrame2Mid,height=19,width=42,bd=12,font=('arial',9,'bold'))
        self.txtReceipt.grid(row=0,column=0)
        
        self.img_arrow_Left=PhotoImage(file="lArrow.png")
        
        self.btnArrowL1=Button(TopFrame2Left,width=80,height=50,state=DISABLED,command=withdrawcash,
        image=self.img_arrow_Left).grid(row=0,column=0,padx=2,pady=10)
        
        self.btnArrowL2=Button(TopFrame2Left,width=80,height=50,state=DISABLED,
        image=self.img_arrow_Left).grid(row=1,column=0,padx=2,pady=10)
        
        self.btnArrowL3=Button(TopFrame2Left,width=80,height=50,state=DISABLED,command=balance,
        image=self.img_arrow_Left).grid(row=2,column=0,padx=2,pady=10)
        
        self.btnArrowL4=Button(TopFrame2Left,width=80,height=50,state=DISABLED,
        image=self.img_arrow_Left).grid(row=3,column=0,padx=2,pady=10)
        
        #======================================RIGHT_Widget====================================================#   
        self.img_arrow_Right=PhotoImage(file="rArrow.png")
        
        self.btnArrowR1=Button(TopFrame2Right,width=80,height=50,state=DISABLED,command=Loan,
        image=self.img_arrow_Right).grid(row=0,column=0,padx=2,pady=10)
        
        self.btnArrowR2=Button(TopFrame2Right,width=80,height=50,state=DISABLED,command=deposite,
        image=self.img_arrow_Right).grid(row=1,column=0,padx=2,pady=10)
        
        self.btnArrowR3=Button(TopFrame2Right,width=80,height=50,state=DISABLED,command=request_new_pin,
        image=self.img_arrow_Right).grid(row=2,column=0,padx=2,pady=10)
        
        self.btnArrowR4=Button(TopFrame2Right,width=80,height=50,state=DISABLED,command=Transaction,
        image=self.img_arrow_Right).grid(row=3,column=0,padx=2,pady=10)
        
        #======================================Pin_numbers_buttons====================================================#  
        self.img1=PhotoImage(file="one.png")
        self.btn1=Button(TopFrame1,width=100,height=50,state=NORMAL,command=insert1,bg='dark gray',
        image=self.img1).grid(row=2,column=0,padx=2,pady=3)
        
        self.img2=PhotoImage(file="two.png")
        self.btn2=Button(TopFrame1,width=100,height=50,state=NORMAL,command=insert2,bg='dark gray',
        image=self.img2).grid(row=2,column=1,padx=2,pady=3)
        
        self.img3=PhotoImage(file="three.png")
        self.btn3=Button(TopFrame1,width=100,height=50,state=NORMAL,command=insert3,bg='dark gray',
        image=self.img3).grid(row=2,column=2,padx=2,pady=3)
        
        self.imgCE=PhotoImage(file="cancel.png")
        self.btnCanvel=Button(TopFrame1,width=100,height=50,state=NORMAL,command=cancel,bg='dark gray',
        image=self.imgCE).grid(row=2,column=3,padx=2,pady=3)
        
        #===========================================================================================================# 
        self.img4=PhotoImage(file="four.png")
        self.btn4=Button(TopFrame1,width=100,height=50,state=NORMAL,command=insert4,bg='dark gray',
        image=self.img4).grid(row=3,column=0,padx=2,pady=3)
        
        self.img5=PhotoImage(file="five.png")
        self.btn5=Button(TopFrame1,width=100,height=50,state=NORMAL,command=insert5,bg='dark gray',
        image=self.img5).grid(row=3,column=1,padx=2,pady=3)
        
        self.img6=PhotoImage(file="six.png")
        self.btn6=Button(TopFrame1,width=100,height=50,state=NORMAL,command=insert6,bg='dark gray',
        image=self.img6).grid(row=3,column=2,padx=2,pady=3) 
        
        self.imgCLR=PhotoImage(file="clear.png")
        self.btnCLR=Button(TopFrame1,width=100,height=50,state=NORMAL,command=clear_pin,bg='dark gray',
        image=self.imgCLR).grid(row=3,column=3,padx=2,pady=3)
        #===========================================================================================================# 
        self.img7=PhotoImage(file="seven.png")
        self.btn7=Button(TopFrame1,width=100,height=50,state=NORMAL,command=insert7,bg='dark gray',
        image=self.img7).grid(row=4,column=0,padx=2,pady=3)
         
        self.img8=PhotoImage(file="eight.png")
        self.btn8=Button(TopFrame1,width=100,height=50,state=NORMAL,command=insert8,bg='dark gray',
        image=self.img8).grid(row=4,column=1,padx=2,pady=3)
        
        self.img9=PhotoImage(file="nine.png")
        self.btn9=Button(TopFrame1,width=100,height=50,state=NORMAL,command=insert9,bg='dark gray',
        image=self.img9).grid(row=4,column=2,padx=2,pady=3)          

        self.imgEN=PhotoImage(file="enter.png")
        self.btnEN=Button(TopFrame1,width=100,height=50,state=NORMAL,command=enter_pin,bg='dark gray',
        image=self.imgEN).grid(row=4,column=3,padx=2,pady=3)
        #===========================================================================================================# 
        self.imgsp1=PhotoImage(file="empty.png")
        self.btnsp1=Button(TopFrame1,width=100,height=50,state=NORMAL,bg='dark gray',
        image=self.imgsp1).grid(row=5,column=0,padx=2,pady=3)
         
        self.img0=PhotoImage(file="zero.png")
        self.btn0=Button(TopFrame1,width=100,height=50,state=NORMAL,command=insert0,bg='dark gray',
        image=self.img0).grid(row=5,column=1,padx=2,pady=3)
        
        self.imgsp2=PhotoImage(file="empty.png")
        self.btnsp2=Button(TopFrame1,width=100,height=50,state=NORMAL,bg='dark gray',
        image=self.imgsp2).grid(row=5,column=2,padx=2,pady=3)          

        self.imgsp3=PhotoImage(file="Return.png")
        self.btnsp3=Button(TopFrame1,width=100,height=50,state=NORMAL,command=Return_Pin,bg='gainsboro',
        image=self.imgsp3,text='Return').grid(row=5,column=3,padx=2,pady=3) 
        #===========================================================================================================# 
        def Fifty():
            global cash
            global Get_cash
            Value0=50
            Get_cash+=Value0
            cash-=Value0
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,Value0)
            self.txtReceipt.insert(END,"\nYou Balance Has Become: ")
            self.txtReceipt.insert(END,cash)

        def Hundred():
            global cash
            global Get_cash
            Value1=100
            Get_cash+=Value1
            cash-=Value1
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,Value1)
            self.txtReceipt.insert(END,"\nYou Balance Has Become: ")
            self.txtReceipt.insert(END,cash)
        def Hundred_Fifty():
            global cash
            global Get_cash
            Value2=150
            Get_cash+=Value2
            cash-=Value2
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,Value2)
            self.txtReceipt.insert(END,"\nYou Balance Has Become: ")
            self.txtReceipt.insert(END,cash)
        def Two_Hundred():
            global cash
            global Get_cash
            Value3=200
            Get_cash+=Value3
            cash-=Value3
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,Value3)
            self.txtReceipt.insert(END,"\nYou Balance Has Become: ")
            self.txtReceipt.insert(END,cash)
        def Two_Hundred_Fifty():
            global cash
            global Get_cash
            Value4=250
            Get_cash+=Value4
            cash-=Value4
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,Value4)
            self.txtReceipt.insert(END,"\nYou Balance Has Become: ")
            self.txtReceipt.insert(END,cash)
        def Three_Hundred():
            global cash
            global Get_cash
            Value5=300
            Get_cash+=Value5
            cash-=Value5
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,Value5)
            self.txtReceipt.insert(END,"\nYou Balance Has Become: ")
            self.txtReceipt.insert(END,cash)

        def Three_Hundred_fifity():
            global cash
            global Get_cash
            Value6=350
            Get_cash+=Value6
            cash-=Value6
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,Value6)
            self.txtReceipt.insert(END,"\nYou Balance Has Become: ")
            self.txtReceipt.insert(END,cash)
        def Four_Hundred():
            global cash
            global Get_cash
            Value7=400
            Get_cash+=Value4
            cash-=Value7
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,Value7)
            self.txtReceipt.insert(END,"\nYou Balance Has Become: ")
            self.txtReceipt.insert(END,cash)
        #-------------------------For_Loan------------------------------#
        def Five_Hundred():
            global cash
            global loan
            Value8=500
            loan+=Value8
            cash+=Value8
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,Value8)
            self.txtReceipt.insert(END,"\nYou Balance Has Become: ")
            self.txtReceipt.insert(END,cash)  
            
        def Thousand():
            global cash
            global loan
            Value9=1000
            loan+=Value9
            cash+=Value9
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,Value9)
            self.txtReceipt.insert(END,"\nYou Balance Has Become: ")
            self.txtReceipt.insert(END,cash)   
            
        def Thousand_Five_Hundred():
            global cash
            global loan
            Value10=1500
            loan+=Value10
            cash+=Value10
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,Value10)
            self.txtReceipt.insert(END,"\nYou Balance Has Become: ")
            self.txtReceipt.insert(END,cash)   

        def Two_Thousand():
            global cash
            global loan
            Value11=2000
            loan+=Value11
            cash+=Value11
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,Value11)
            self.txtReceipt.insert(END,"\nYou Balance Has Become: ")
            self.txtReceipt.insert(END,cash) 
            
        def Two_Thousand_Five_Hundred():
            global cash
            global loan
            Value12=2500
            loan+=Value12
            cash+=Value12
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,Value12)
            self.txtReceipt.insert(END,"\nYou Balance Has Become: ")
            self.txtReceipt.insert(END,cash)             

        def Three_Thousand():
            global cash
            global loan
            Value13=3000
            loan+=Value13
            cash+=Value13
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,Value13)
            self.txtReceipt.insert(END,"\nYou Balance Has Become: ")
            self.txtReceipt.insert(END,cash)               
            
        def Three_Thousand_Five_Hundred():
            global cash
            global loan
            Value14=3500
            loan+=Value14
            cash+=Value14
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,Value14)
            self.txtReceipt.insert(END,"\nYou Balance Has Become: ")
            self.txtReceipt.insert(END,cash)          

        def Four_Thousand():
            global cash
            global loan
            Value15=4000
            loan+=Value15
            cash+=Value15
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,Value15)
            self.txtReceipt.insert(END,"\nYou Balance Has Become: ")
            self.txtReceipt.insert(END,cash)   

                 
if __name__=='__main__' :      
    window_1=Tk()
    application=atm(window_1)
    window_1.mainloop()

