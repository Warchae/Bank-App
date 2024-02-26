from bank_class import *
exc = exchangeRate()
main = True
while main:

    main = 1
    if main:

        print("""
    *****Welcome To Bank*****
    A. Join Our Bank
    B. Login To Your Bank Account
    C. Exchange Rates
    R. Reload Menu
    Q. Exit
            """)
        
        choice = input("Choice: ").upper()

        if choice not in ("ABCQR"):
            print("Invalid choice, please enter correctly.")

        elif choice == "A":
            print("*****Register*****")
            name = input("Name: ")
            lastName = input("Last Name: ")
            address = input("Address: ")
            id = input("National ID: ")
            password = input("Password: ")
            customer_id = str(uuid.uuid4().fields[-1])[:8]
            customer = Customer(name,lastName,address,id,password)
            customers[customer_id] = customer
            accounts[customer_id] = BankAccount(customer_id)
            print("Account Created Succesfully, Your Customer ID is {}.".format(customer_id))

        elif choice == "B":
            print("*****Login*****")
            id = input("Customer ID: ")
            password = input("Password: ")
            try:
                if customer_id in customers and customers[customer_id].password == password:
                    logged_in = True
                    while logged_in:
                        print(f"""
                *****Have A Great Day, {customers[customer_id].name}*****
                1. Money Deposit
                2. Money Withdraw
                3. Money Transfer
                4. Take Credit
                5. Return Credit
                6. Show Balance
                7. Log Out                                       
                                """)
                        select = input("Select Your Operation: ")
                        if select == "1":
                            amount = int(input("How much money would you want to deposit: "))
                            accounts[customer_id].moneyDeposit(amount)
                            logged_in = True
                        elif select == "2":
                            amount = int(input("How much money would you want to withdraw: "))
                            accounts[customer_id].moneyWithdraw(amount)
                            logged_in = True
                        elif select == "3":
                            yourID = id
                            toID = input("Enter Account Number For Transfer: ")
                            amount = int(input("Enter Amount for Transfer: "))
                            accounts[customer_id].moneyTransfer(amount, yourID, toID)
                            logged_in = True
                        elif select == "4":
                            accounts[customer_id].takeCredit()
                            logged_in = True
                        elif select == "5":
                            accounts[customer_id].returnCredit()
                            logged_in = True
                        elif select == "6":
                            accounts[customer_id].getMoney()
                            logged_in = True
                        elif select == "7":
                            logged_in = False
                            
                else:
                    print("Invalid Inputs")

            except NameError:
                print("You Must Be Create Account First!")
                logged_in = False
                
        elif choice == "C":
            exc.showExcRate()
            choice = input("Press R For Return To Main Menu, Press Q For Exit: ")

        elif choice == "R":
            main = True

        elif choice == "Q":
            print("Thank You For Your Visit. Have A Great Day.")
            main = False
