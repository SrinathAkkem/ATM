import read_file
import os
def print_process(process):
    date = '{}'.format(process[2:7])
    print('{0}\t{1}\t{2}{3: ^10} {4: ^10}'.format(process[0],process[1].center(len('change_password')),date.center(len(date)),process[7],process[8])
    )
def show_history(ls):
    choice = int(input('1) show deposit processes\n2) show withdraw processes\n3) show change password process\n4) show all processes\n5) clear processes\n\nchoice>> '))
    file_name = ls[0] + '.txt'   
    id_list = read_file.read_file(file_name)
    os.system('clear')
    top_line = '\nID\t' + 'Type'.center(len('change_password')) + 'Date and Time'.center(40) + 'before'.center(10) + 'after'.center(15)
    print(top_line)
    print('-' * len(top_line))
    if choice == 1:
        for line in id_list:
            if line[1] == 'deposit':
                print_process(line)
    elif choice == 2:
        for line in id_list:
            if line[1] == 'withdraw':
                print_process(line)
    elif choice == 3:
        for line in id_list:
            if line[1] == 'change_password':
                print_process(line)
    elif choice == 4:
        for line in id_list:
            print_process(line)
    elif choice == 5:
        new_file = open(file_name, 'w')
        new_file.close()
    else:
        print('ERROR: Wrong choice')
    input('\nPress Enter to go back..')
    os.system('clear')
