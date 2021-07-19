from menu2 import clear_screen, menu2
def login(acc_list):
    login_id = input('Please enter your information (to return, click "Ctrl+C"). \n>>ID: ')
    login_password = input('>>Password: ')
    found = False
    for account in acc_list:
        if account[0] == login_id and account[2] == login_password:
            found = True
            clear_screen()
            menu2(account)
            break
        else:
            continue
    if not found:
        clear_screen()
        print('Invalid credentials')
        login(acc_list)
    else:
        acc_file = open('Accounts.txt', 'w')
        print('Saving changes...')
        for acc in acc_list:
            for elements in acc:
                acc_file.write("%s\t" % elements)
            acc_file.write('\n')
