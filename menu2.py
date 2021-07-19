import os
import withdraw
import deposit
import show_history
import change_password
def clear_screen():
    os.system('clear')
    print()
def menu2(account):
    print("\n---------Hello, {0}--------- ".format(account[1]))
    ch = int(input("\n1) show info \n2) show process history\n3) deposit\n4) withdraw\n5) change password \n6) logout\n\nchoice>>"))
    clear_screen()
    if ch == 1:
        print("ID: {}\nName: {}\nBalance: {}\n".format(account[0], account[1], account[3]))
    elif ch == 2:
        show_history.show_history(account)
    elif ch == 3:
        deposit.deposit(account)
    elif ch == 4:
        withdraw.withdraw(account)
    elif ch == 5:
        change_password.change_password(account)
    elif ch == 6:
        return
    else:
        print("ERROR: Wrong choice\n")

    menu2(account)
