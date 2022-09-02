#Aeron's BANK project

from re import A
import useful_tools
from useful_tools import users
import random
#print(useful_tools.date_validated)

#1. branch
user_iterations = 0
user_accounts = []
initial_balance = 0

while True:
    print("------------------------------------------------------------------------")
    what_branch = (int(input("\nHELLO BANK USER\nTHIS IS AERON's BANK\n\nWhat branch your'e going?\n(1) Main Branch\n(2) ATM Branch\n(3) Near Branch\n(4) Admin\n(5) Exit\n\nPress: ")))

    while True:
        chosen = "Not Yet"                                               # variable for choosing in

        if what_branch == 1:                                             # Main Branch (Can Create Account, Can Withdraw, Can Check Account)
            print("------------------------------------------------------------------------")
            M_tasks = (int(input("\n WELCOME TO MAIN BRANCH!\n\n 1. Create Account\n 2. Withdraw or Deposit\n 3. Check Account\n 4. Go Back\n 5. Exit\n\nHello USER please choose on the following: ")))

            if M_tasks == 1:
                chosen = "CA"
            elif M_tasks == 2:
                chosen = "WOD"
            elif M_tasks == 3:
                chosen = "CB"
            elif M_tasks == 4:
                break
            elif M_tasks == 5:
                print("Thank you! Keep safe!")
                exit()
            else:
                print("Invalid Choice")
                continue

        elif what_branch == 2:                                             # ATM Branch (Can Withdraw, Can Check Account)
            print("------------------------------------------------------------------------")
            A_tasks = (int(input("\n WELCOME TO ATM BRANCH!\n\n 1. Withdraw or Deposit\n 2. Check Account\n 3. Go Back\n 4. Exit\n\nHello USER please choose on the following: ")))

            if A_tasks == 1:
                chosen = "WOD"
            elif A_tasks == 2:
                chosen = "CB"
            elif A_tasks == 3:
                break
            elif A_tasks == 4:
                print("Thank you! Keep safe!")
                exit()
            else:
                print("Invalid Choice")
                continue

        elif what_branch == 3:                                             # Near Branch (Can Check Account)
            print("------------------------------------------------------------------------")
            N_tasks = (int(input("\n WELCOME TO NEAR BRANCH!\n\n 1. Check Account\n 2. Go Back\n 3. Exit\n\nHello USER please choose on the following: ")))

            if N_tasks == 1:
                chosen = "CB"
            elif N_tasks == 2:
                break
            elif N_tasks == 3:
                print("Thank you! Keep safe!")
                exit()
            else:
                print("Invalid Choice")
                continue
        elif what_branch == 4:
            admin_passcode = input("Enter admin passcode: ")            # PASSCODE for ADMIN : admin_passcode

            if admin_passcode == "admin_passcode":
                print("Good Day, Admins! Here's the lists of Users in this bank!")
                
                user_lists = 0
                user_write_lists = 0
                #printing all accounts

                print("\nID        USERNAME      PASSWORD      BALANCE")

                while user_lists != len(user_accounts):
                    print(str(user_accounts[user_lists].user_id) + "   " + str(user_accounts[user_lists].user_username) + "      " + str(user_accounts[user_lists].user_password) + "        " + str(user_accounts[user_lists].user_balance))
                    user_lists += 1
                
                admin_print = input("\nDo you want to Print Accounts? Press 'y' to Print and press any key if No: ")

                if admin_print.lower() == "y":

                    print("\nPrinting in 'Accounts.txt ....")
                    ad_print = open("Accounts.txt", "w")

                    ad_print.write("ID        USERNAME      PASSWORD      BALANCE\n")
                    
                    while user_write_lists != len(user_accounts):
                        ad_print.write(str(user_accounts[user_write_lists].user_id) + "   " + str(user_accounts[user_write_lists].user_username) + "       " + str(user_accounts[user_write_lists].user_password) + "       " + str(user_accounts[user_write_lists].user_balance) + " php\n")
                        user_write_lists += 1

                    ad_print.close()
                    break
                else:
                    print("Thank you Admins!")
                    break

            else:
                print("Invalid Passcode! It is exclusive only for bank's Admin")
                break

        elif what_branch == 5:
            print("Thank you! Keep safe!")
            exit()
        else:
            print("Invalid Branch! Try Again!")
            break
            

    #2. Ask if what to do

        # a. Create or Add Account
        if chosen == "CA":

            username = input("\nEnter your Userame: ")           # username
            password = input("Enter your Password: ")          # password

            confirmation = input("\nPress 'Y' if Confirm, Press any 'key' if dont't save: ")

            if confirmation.lower() == "y":
                random_ID = int(random.uniform(10000000, 99999999)) # random id of user
                user_accounts.append(users(random_ID, username, password, initial_balance))      # id, username, password and balance of iterate user
                print("Hello " + user_accounts[user_iterations].user_username + "! Welcome to Aeron's Bank!")
                user_iterations += 1
            else:                                               # did not iterate if n/N was clicked
                print("Your input details was't saved!")

        # b. Log IN
        elif chosen == "WOD":
            
            break_out_loop = True
            username_counter = 0
            it = len(user_accounts)

            if it > 0:

                while break_out_loop:

                    while username_counter <= 2:

                        print("\nPlease Log in First!\nInput 'x' in username and password to exit.")

                        username_check = input("\nEnter a Username: ")     # Insert Username
                        password_check = input("Enter your Password: ")    # Insert password
                    
                        for ctr_username in range(it):                                        # for loop for the length of array/lists (username) 
                            # checking if there is exists an account username and password in iteration (scanning)
                            if username_check == user_accounts[ctr_username].user_username and password_check == user_accounts[ctr_username].user_password:

                                dep_with = 0

                                while dep_with <= 2:
                                
                                    user_action = int(input("\nHello " + user_accounts[ctr_username].user_username + "! What will you want to do!\n(1) Deposit\n(2) Withdraw\n(3) Log Out\nPress: "))

                                    if user_action == 1:        # deposit ammounnt
                                        deposit_amount = float(input("\nInsert Deposit Ammount: "))   # Deposit Money
                                        user_accounts[ctr_username].user_balance += deposit_amount  # adding deposit money in current balance
                                        print("Succesfully Withdraw "+ str(deposit_amount) + "php in your Balance!\nYou have currently "+ str(user_accounts[ctr_username].user_balance) + "php")
                                        
                                        deposit_reciept = input("\nDo you want to Print deposit Reciept 'y' if Yes and click any key if No: " )

                                        if deposit_reciept.lower() == "y":
                                            print("Printing your Reciept ... \nLook in deposit_reciept.txt")

                                            # Writng a Reciept for Depositing
                                            r_reciept = open("deposit_reciept.txt", "w")

                                            r_reciept.write("\nGood Day and Thank you for Depositing in Aeron's Bank")
                                            r_reciept.write("\n\nDate & Time: " + str((useful_tools.date_validated)))
                                            r_reciept.write("\n\nID: "+ str(user_accounts[ctr_username].user_id))
                                            r_reciept.write("\nUsername: "+ str(user_accounts[ctr_username].user_username))
                                            r_reciept.write("\nBalance: "+ str(user_accounts[ctr_username].user_balance))

                                            r_reciept.close()
                                            continue
                                        else:
                                            print("Thank you for Depositing Money!\nPlease Come Back")

                                        #print reciept

                                    elif user_action == 2:       # withdraw
                                        withdraw_ammount = float(input("\nInsert Withdraw Ammount: "))  # Withdraw Money
                                        
                                        # counter check if the balance is below 300 (co'z 300 php is maintaning balance)
                                        if user_accounts[ctr_username].user_balance - withdraw_ammount < 300:
                                            print("Unssucesfully withdrawal! Your account must have a 300php maintaining balance\nYour current balance is " + str(user_accounts[ctr_username].user_balance))
                                            break
                                        else:
                                            # succesful withrawal, withdraw money is deducted to balance
                                            user_accounts[ctr_username].user_balance -= withdraw_ammount
                                            print("Succsesfully withdraw " + str(withdraw_ammount) + "php in your current balance\nYour current balance is " + str(user_accounts[ctr_username].user_balance))
                                            
                                            withdraw_reciept = input("\nDo you want to Print withdraw Reciept 'y' if Yes and click any key if No: " )
                                            #print reciept
                                            if withdraw_reciept.lower() == "y":
                                                print("Printing your Reciept ... \nLook in withraw_reciept.txt ")

                                                # Writng a Reciept for Depositing
                                                w_reciept = open("withdraw_reciept.txt", "w")

                                                w_reciept.write("\nGood Day and Thank you for Withdrawing in Aeron's Bank")
                                                w_reciept.write("\n\nDate & Time: " + str((useful_tools.date_validated)))
                                                w_reciept.write("\n\nID: "+ str(user_accounts[ctr_username].user_id))
                                                w_reciept.write("\nUsername: "+ str(user_accounts[ctr_username].user_username))
                                                w_reciept.write("\nBalance: "+ str(user_accounts[ctr_username].user_balance))

                                                w_reciept.close()
                                                continue
                                            else:
                                                print("Thank you for Wihthrawing Money!\nPlease Come Back")
                                                username_counter = 3
                                                break_out_loop = False
                                                break

                                    elif user_action == 3:
                                        print("The Account " + user_accounts[ctr_username].user_username + " has been log out!")
                                        dep_with = 2
                                        username_counter = 2
                                        break_out_loop = False
                                        break
        
                                    else:
                                        dep_with += 1
                                        print("Invalid Input!")


                            elif username_check.lower() == "x" or password_check.lower() == "x":
                                username_counter = 3


                            else:
                                username_counter += 1
                                print("Username or Password doesn't exists, Try Again (" + str(username_counter)+ "x)")   # outer break loop (username and password)

                        break_out_loop = False

            else:
                print("No account in this Bank")

        # c. Check Account                  
        elif chosen == "CB":
            it2 = len(user_accounts)
            isCheck_Acc = True

            if it2 > 0:

                while isCheck_Acc:

                    print("\nCheck Account! Input 'x' in Username and Password to exit.")
                    # Release (Bank_UserID, name, username, password)
                    username1 = input("\nEnter Username: ")
                    password1 = input("Enter Password: ")

                    for username_iter in range(it2):
                        if username1 == user_accounts[username_iter].user_username:

                            for password_iter in range(it2):
                                if password1 == user_accounts[password_iter].user_password:
                                    print("Good Day, Welcome to Aeron's Bank (Checking Account)")
                                    print("\nID: " + str(user_accounts[password_iter].user_id))
                                    print("Username: " + str(user_accounts[password_iter].user_username))
                                    print("Password: " + str(user_accounts[password_iter].user_password))
                                    print("Balance: " + str(user_accounts[password_iter].user_balance))

                                    break
                                else:
                                    print("Username doesn't match Password!")
                                    break

                        elif username1.lower() == "x":
                            isCheck_Acc = False
                            break
                            
                        else:
                            print("Not registered Username!")
                            break
            else:
                print("No Account in this bank!")
                
        else:
            exit()



                
