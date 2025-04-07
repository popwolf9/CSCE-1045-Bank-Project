def encrypt(pw):
    blank = ""
    for i in pw:
        if i.isupper():
            b = ord('A')
            change = (ord(i) + 3 - b) % 26 + b
            blank += chr(change)
        elif i.islower():
            b = ord('a')
            change = (ord(i) + 3 - b) % 26 + b
            blank += chr(change)
        elif i.isdigit():
            b = ord('0')
            change = (ord(i) + 3 - b) % 10 + b
            blank += chr(change)
        else:
            blank += i
    return blank

class User:
    def __init__(self, user, pw, balance=0.0):
        self.name = user
        self.pw = encrypt(pw)
        self.balance = float(balance)

    def check_pw(self, pw):
        return self.pw == encrypt(pw)

    def new_pw(self, pw_new):
        self.pw = encrypt(pw_new)

    def deposit(self, money):
        if money < 0:
            print("Error: Please use positive numbers.")
        else:
            self.balance += money
            print(f"Thank you for your patronage. New balance: ${self.balance:.2f}")

    def withdraw(self, money):
        if money < 0:
            print("Error: Please use positive numbers.")
        elif money > self.balance:
            print("You do not have enough funds to withdraw. Please check your balance.")
        else:
            self.balance -= money
            print(f"Thank you for your patronage. New balance: ${self.balance:.2f}")

    def print_total(self):
        print(f"We appreciate your continued patronage. Your balance: ${self.balance:.2f}")



class Bank:
    def __init__(self):
        self.user = None
        self.login_user = None

    def registration(self):
        print("=== Thank you for choosing Superior Banking. Open your account here: ===")
        count_name = 0
        while count_name == 0:
            name = input("Username: ")
            if name == "":
                print("Error: Please input a username.")
            else:
                count_name += 5
        count_pw = 0
        while count_pw == 0:
            pw = input("Password: ")
            if pw == "":
                print("Error: Please input a password.")
            else:
                count_pw += 5
        while self.user is None:
            temp = False
            try:
                deposit = float(input("Give your new account a starting balance: "))
                if deposit < 0:
                     print("Error: Please use positive numbers. Type 0 if you do not have initial funds.")
                else:
                    temp = True
            except ValueError:
                print("Error: Not a real number.")
            if temp is True:
                self.user = User(name, pw, deposit)
                print(f"Account '{name}' has been registered. When you are ready, please login to access bank systems. Enjoy Superior Banking!")

    def login(self):
        print("\n=== Logging in... ===")
        if self.user is None:
            print("There is no user.")
            return False

        name = input("Username: ")
        pw = input("Password: ")

        if name != self.user.name:
            print("Invalid login.")
            return False
        if not self.user.check_pw(pw):
            print("Invalid login.")
            return False

        self.login_user = self.user
        print("Thank you for using Superior Banking. You may now access your funds.")
        return True

    def pw_change(self):
        if not self.login_user:
            print("Please login first in order to access funds. For help, call our office.")
            return
        pw = input("Enter your current password: ")
        if not self.login_user.check_pw(pw):
            print("Invalid password. Please try again...")
            return
        count_pw_new = 0 
        while count_pw_new == 0:
            pw_new = input("Enter your new password: ")
            if pw_new == "":
                print("Error: New password cannot be blank.")
            else:
                count_pw_new += 5
        self.login_user.new_pw(pw_new)
        print("You have changed your password. Please make a note of it somewhere secure.")

    def main_menu(self):
        print("\n==== Superior Banking Main Menu: ====")
        print("1. Login\n2. Deposit\n3. Withdraw\n4. Show Total Balance\n5. Change Password\n6. Exit Bank")

    def run(self):
        temp = 1
        print("\n***** Greetings and welcome to Superior Banking ****")
        print("*   Computer Science and Enginnering         *\n*   CSCE 1035.001 - Computer Programming I   *\n*   Prajesh Gohel EUID pg0783@my.unt.edu     *")
        self.registration()
        while temp != 0:
            self.main_menu()
            option = input("\nChoose an option: ")

            if option == "1":
                self.login()

            elif option == "2":
                if not self.login_user:
                    print("Please login to your Superior Banking account.")
                else:
                    try:
                        money = float(input("How much money do you want to put in? "))
                        self.login_user.deposit(money)
                    except ValueError:
                        print("Error: Use a real number.")

            elif option == "3":
                if not self.login_user:
                    print("Please login to your Superior Banking account.")
                else:
                    try:
                        money = float(input("How much money do you want to take out? "))
                        self.login_user.withdraw(money)
                    except ValueError:
                        print("Error: Use a real number.")

            elif option == "4":
                if not self.login_user:
                    print("Please login to your Superior Banking account.")
                else:
                    self.login_user.print_total()

            elif option == "5":
                if not self.login_user:
                    print("Please login to your Superior Banking account.")
                else:
                    self.pw_change()

            elif option == "6":
                print("We appreciate your continued patronage at Superior Banking! Have a good da- aaaaand we just lost the account...")
                temp -= 1

            elif option == "9":
                print("\n=== USER DICTIONARY ===")
                print(f"Username: {self.user.name}\nEncrypted Password: {self.user.pw}\nTotal Money: ${self.user.balance:.2f}")
            
            else:
                print("This option is not valid, please try again.")


b = Bank()
b.run()
