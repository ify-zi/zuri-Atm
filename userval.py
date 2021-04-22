
def acc_number_validation(accNo):
    #check if accounnt number is not empty
    #if account number is 10 digit
    #if the account number is an integer


    if accNo:
            try:
                int(accNo)
                if len(str(accNo)) == 10:
                    return True
            except ValueError:
                #print("invalid account number")
                return False
            except TypeError:
                #print("invalid account type")
                return False
        
   
    return False
        


