from datetime import datetime
from datetime import date
import random

now = datetime.now()
current_date = date.today()
current_time = now.strftime("%H:%M:%S")

# register
# username,password,email
# generate user id

# login
# (username or email) and password


# bank operations

# initializing the system
import random

database = {}  # dictionary


def front_menu():
    print("Welcome to your friendly neighborhood bank (FNB)")

    have_account = int(input('Do you have account with us:\nPlease choose 1 for Yes and 2 for No \n'))

    if (have_account == 1):
        login()
    elif (have_account == 2):
        register()
    else:
        print('You have selected an invalid option')
        front_menu()


def login():
    print('********** Welcome, please login to your account **********')

    account_num = int(input('What is your account number \n'))
    password = input('What is your password \n')

    for account_number, user_details in database.items():
        if account_number == account_num:
            if user_details[3] == password:
                bank_operations(user_details)


def register():
    print('********** Please Register **********')
    email = input('What is your email address? \n')
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    password = input('Create a password for yourself \n')

    account_number = generate_account_number()

    database[account_number] = [first_name, last_name, email, password]

    print('Your account has been created')
    print('Your account number is: %d' % account_number)
    print('-------------------------------------------')

    login()


def bank_operations(user):
    print('Welecome %s %s' % (user[0], user[1]))
    print('Date:', current_date)
    print('Current time: ', current_time)
    print('What would you like to do?')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Logout')
    selected_option = int(input('4. Exit Menu \n'))

    if (selected_option == 1):
        print('You selected %s' % selected_option)
        withdrawal_operation()
        bank_operations(user)
    elif (selected_option == 2):
        print('You selected %s' % selected_option)
        deposit_operation()
        bank_operations(user)
    elif (selected_option == 3):
        login()
    elif (selected_option == 4):
        exit()
    else:
        print('Invalid option selected')
        bank_operations(user)


def withdrawal_operation():
    withdraw_amount = input('How much would you like to withdraw? \n')
    print('Take your cash \n')
    print('Amount withdrawn was $% \n' % withdraw_amount)


def deposit_operation():
    deposit_amount = input('How much would you like to deposit? \n')
    print('Your current balance is $%s \n' % deposit_amount)


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


front_menu()