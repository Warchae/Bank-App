'''
A Bank App Which is Just Register and Login Withdraw and Deposit Money To Your Account.
We need Bank Account, Money Trace, Account Credits.
'''
#Creating userCredits List Because I Don't Know SQL
userCredits = []

# Register Function to the Bank with using in-Python list (which is the worst and not even logical decision).
def registerfunc():
    regNationalID = str(input("Enter Your National ID For REGISTER: "))
    while len(regNationalID) != 11:
        regNationalID = str(input("Please Enter Your 11 Digit National ID: "))
        
    regPassword = str(input("Enter Your 6 Digit Password For REGISTER: "))
    while len(regPassword) < 5 or len(regPassword) >7:
        regPassword = str(input("Please Enter Your 6 Digit Password: "))
    
    userCredits.append([regNationalID,regPassword])
    return main()

#Login Function To the BANK with registered ID and Password
def loginfunc():
    loginID = input("Please Enter Your ID For Login: ")
    while len(loginID) != 11:
        loginID = input("Your ID Must Be 11 Digit! Please Try Again: ")
    
    loginPass = input("Please Enter Your Password: ")
    while len(loginPass) != 6:
        loginPass = input("Your Password must be 6 Digit! Please Try Again: ")
        
    #Control For List In List Or Not
    if [loginID,loginPass] in userCredits:
        loggedIn = 1
        print("Welcome to Our Bank.")
    else:
        print("Your Informations Doesn't Match Or You Are Not Registered Yet.\nDirecting To The Main Menu")
        return main()

#Creating Main Menu For The Bank App Login Page
def main():
    command = input("1) Register\n2) Login\n3) Exit\nPlease Enter Your Command: ")
#Change if commands to "switch-case" module
    if command == "1":
        registerfunc()
    elif command == "2":
        loginfunc()
    else:
        exit()

main()