import random
import datetime 
import userval
import file
from getpass import getpass
#SORRY FOR THE REDUNDANT CODE, I RAN OUT OF OPTIONS


def register():
        global first,last,email,pin,password,accountName #prepared_user_details
        first=input("input firstname:")
        last=input("input lastname:")
        email=input("input email:")
        pin=input("input a four digit pin:")
        password=input("Input Password:")
        accountName = "{} {}".format(last,first)
        #prepared_user_details= first + "," + last + "," + email + "," + str(pin) + "," + password + "," + str(0)
       
    #---------------------Account number generator-------------------------

def genAcc():
        num= 1
        y=[3,0] #all account numbers generated must start with three zero to make it unique
        while num <= 8:
            x = random.randint(0,9)
            y.append(x)
            num = num +1
            accountNo=''.join([str(i)for i in y])
        return accountNo
            
    #-----------------Transfer function---------------------

def transfer(tName, tNo, amount, tBankName):
        user[-1]= int(user[-1]) + amount
        newval=user[-1]
        newval=str(newval)
        try:
            file.update(user_acc_no,-1,newval)
        except FileNotFoundError:
            print("an issues occured due to network, try again later")
            return False
        print("Tranfer successful! \Account name {} \nAccount number : {} \nAmount transferred : {} \nBank : {}".format(tName, tNo, amount, tBankName))
        print("Balance : ${}".format(user[-1]))
        tym =datetime.datetime.now()
        print(tym)
        
    #-----------------deposit function-----------------------

def deposit(amount):
        user[-1] = int(user[-1]) + amount
        newval=user[-1]
        newval=str(newval)
        try:
            file.update(user_acc_no,-1,newval)
        except FileNotFoundError:
            print("an issues occured due to network, try again later")
            return False
        print("{} successful deposited".format(amount))
        print("your balance is ${}".format(user[-1]))
        tym =datetime.datetime.now()
        print(tym)
    #------------------withdraw function---------------------------

def withdraw(amount):
        user[-1]=int(user[-1])
        if user[-1] > amount:
            user[-1] -= amount
            print("successful")
            print("your balance is ${}".format(user[-1]))
        else:
            print("Sorry, not enough funds!")
        newval = user[-1]
        str(newval)
        try:
            file.update(user_acc_no,-1,newval)
        except FileNotFoundError:
            print("an issues occured due to network, try again later")
            return False
        tym =datetime.datetime.now()
        print(tym)
   
   
    #---------------------balance check function------------------------


def statement():
        print("hi {} your balance is ${}.".format(user[1],user[-1]))
    
    
    #---------------------pin validation function------------------------


def pinval(val):
        if val == user[-3]:
            return True
        else:
            return False
   
   
    #---------------------pin reset function---------------------------
def pinReset(val,val2):
        if val == val2:
            user[-3] = val
            print("Pin change successful")
            newval = user[-3]
            try:
                file.update(user_acc_no,-3,newval)
            except FileNotFoundError:
                print("an issues occured due to network, try again later")
                return False
        else:
            print("oops!! The two pin are not the same")
        tym =datetime.datetime.now()
        print(tym)
    
    
     #-----------------password reset function-------------------------       
def passReset(val, val2):
        if val == val2:
            user[-2]= val
            print("Password change successful")
            newval = user[-2]
            try:
                file.update(user_acc_no,-2,newval)
            except FileNotFoundError:
                print("an issues occured due to network, try again later")
                return False
        else:
            print("Passwords not Matched")
        tym =datetime.datetime.now()
        print(tym)
    
    
    #----------------------login function---------------------

def login():
        global user_acc_no, user_password,user
        print("===================LOGIN PAGE=================") 
        print("Enter your login details")
        user_acc_no = int(input("Enter username:"))
        user_password = getpass("Enter password:")

        user= file.authentication(user_acc_no, user_password)
        
        if user:
            operation(user)
        else:
            print("invalid account and password")
            login()
    
   



def welcome():            
    #---------------------------------main prompt---------------
    opt= input("Hello!, Welcome to Zuri Bank \n1. Register\n2.Login \n==>")
    #-----------------------------Registration Prompt--------------------------
    if opt == '1':
        print("============================ZURI BANK========================")
        print("Welcome please carefully follow the prompt and register your details\n Note please only input 1 or 2 ")
        
        register()
        accountNo = ""
        accountNo=genAcc()
        is_user_created = file.create(accountNo,first,last,email,pin,password)
        if is_user_created:
            try:
                print("Registration Successful!!!\n your details are:\n Account name  is {} \n Account number is {}".format(accountName,accountNo))
                login()
                
                tym =datetime.datetime.now()
                print(tym)
            except FileExistsError:
                    print("sorry there was a issue in network connection, please try again")
                    register()

            except ValueError:
                    print("sorry there was a issue in network connection, please try again")
                    register()
                    


    elif opt == '2':
        
         login()
         



    else:
        print("Wrong input. Note: enter 1 or 2 to select")

         
def operation(user):    
    
    print("==========================ZURI BANK===================")
    print("welcome {}".format(user[1] + ' ' + user[0]))
    print("Balance : ${}".format(user[-1]))
    print("Please input only 1,2,3,4,5,6, or 7")
    mainOpt=input("select an option: \n1. Transfer \n2. Withdrawal \n3. Deposit \n4. Change Pin \n5. Reset Password \n6. Account Statment\n7. Complaint\n8. Logout\n0. Exit \n==>")
    
    
    if mainOpt == '1':
        print("Balance = ${}".format(user[-1]))
        amount=int(input("Enter amount:"))
        tName=input("Enter account name:")
        tNo=input("Enter account Number:")
        tBankName=input("Enter Bank:")
        val=input("Enter PIN")
        if (pinval(val) == True):
            if len(tNo) != 10:
                print("wrong account number, Note Account number must be 10 digit")
            else:
                transfer(tName,tNo,amount,tBankName)
                operation(user)
        else:
            print("wrong pin")
    
    elif mainOpt == '2':
        print("Balance = ${}".format(user[-1]))
        amount=int(input("Enter Amount:"))
        val=int(input("Enter transaction Pin:"))
        pinval(val)
        if pinval(val) == True:
                     withdraw(amount)
                     operation(user)
        else:
                     print("oop!! wrong pin")
    
    elif mainOpt == '3':
        print("Balance = ${}".format(user[-1]))
        amount=int(input("Enter Amount:"))
        deposit(amount)
        operation(user)
    
    
    elif mainOpt == '4':
        val=input("Enter new pin:")
        val2=input("Confirm new pin:")
        pinReset(val,val2)
        operation(user)
    
    elif mainOpt == '5':
        val=input("Enter new password:")
        val2=input("Confirm  new password:")
        passReset(val,val2)
        operation(user)
    
    elif mainOpt == '6':
        statement()
        operation(user)
    
    elif mainOpt == '7':
        comp=input("Enter complaint:")
        print("Thanks {} for reaching to us, we will get back to you shortly via your email:{}".format(user[1],user[3]))
        operation(user)
    
    elif mainOpt == '8':
        login()
    
    else:
        print("Thank you for banking with us!!!")
        exit()
    


welcome()