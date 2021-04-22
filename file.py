#create record 
#update record
#read record 
#delete record
import os
import userval

user_db_path = "data/user_record/"

def create(user_acc_no,first,last,email, pin,password):

    user_data = first + "," + last + "," + email + "," + pin + "," + password + "," + str(0) 
    if does_account_number_exist(user_acc_no):
        return False
    if does_email_exist(email):
        print("user already exist")

        return False

    
    completion_state = False
    try:
            f=open(user_db_path + str(user_acc_no) + ".txt", "x")
    except FileExistsError:
            data_exist=read(user_db_path, str(user_acc_no) + ".txt")
            if not data_exist:
                delete(user_acc_no)
    else:
            f.write(str(user_data))
            completion_state=True
    finally:
            f.close()
            return completion_state
            # create a file
            # name of file should be account.txt
            # add the user details to the file
            # return true
            # if saving to file fails delete created file

def read(user_acc_no):
    is_valid = userval.acc_number_validation(user_acc_no)
    try:
        if is_valid:
            f=open(user_db_path + str(user_acc_no) + ".txt", "r")
        else:
            f=open(user_db_path + user_acc_no, "r")
       
    except FileNotFoundError:
        print("user not found")
        return False
    except FileExistsError:
        print("user does not exist")
        return False
    except TypeError:
        print("invalid account format")
        return False
    else:
         return f.readline()
    return False


def update(user_acc_no,pos,newval):
    print("update user record")
    if does_account_number_exist:
        try:
            f=open(user_db_path + str(user_acc_no) + ".txt", "r+")

        except FileNotFoundError:
                return False
        except FileExistsError:
                delete(str(user_acc_no) + ".txt")
                return False
        else:
            user= str.split(read(str(user_acc_no)), ",")
            user[pos]=newval
            user= user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + user[4] + "," + user[5]
            f.write(str(user))
            f.close()
            return True
    return False
                  
            

    # find user with the account number
    # fetch the context of the file
    # update the details of the record
    # save the file



def delete(user_acc_no):
    completion_state= False
    if os.path.exists(user_db_path + str(user_acc_no) + ".txt"):
        try:
            os.remove(user_db_path + str(user_acc_no) + ".txt")
            completion_state = True
        except FileNotFoundError:
            print("user not in records")
        finally:
            return completion_state
        # find the account number
        # delete the user record


def does_email_exist(email):
    all_user= os.listdir(user_db_path)

    for user in all_user:
        user_list=str.split(read(user), ',')
        if email in user_list:
            return True
    return False

def does_account_number_exist(user_acc_no):
    all_user= os.listdir(user_db_path)

    for user_acc in all_user:
        if user_acc == str(user_acc_no) + ".txt":
            return True
    return False

 
def authentication(user_acc_no, password):
    if does_account_number_exist(user_acc_no):
        
        user= str.split(read(user_acc_no), ",")
        if password == user[-2]:
            return user
            return True

    
    return False
       
       
       
       
       
       # find the user record in the data

#create(3034567892, 'wesley', 'mike', 'mike@zuri.team','1234','danny')

#print(read(['one','two']))
#print(does_email_exist("dan@zuri.team"))
#print(does_account_number_exist(3036582485))
#update(3034567892,-1,"mypassword")