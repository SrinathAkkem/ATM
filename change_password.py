import time
from read_file import read_file
def gate_x(t_password):
    wrong_flag = True  
    print("\nIf you wish to return to the previous page, type\"Exit\"\n")
    for i in range(3):
        entered_password = input('\nEnter The Old Password : ')
        if entered_password == "Exit": 
            return '-1'
        if entered_password == t_password: 
            wrong_flag = False
            break
    if wrong_flag: 
        return '1'
    else:
        return '0'
def change_password(ls):
    old_password = ls[2]
    flag = gate_x(old_password)
    if flag == '0':
        new_password = input("\nEnter the new password: ")
        '''Get the new password'''
        file_name = ls[0] + '.txt'
        process_list = read_file(file_name)
        id_file = open(file_name, 'a')

        if len(process_list) == 0:
            last_id = 1
        else:
            last_id = int(process_list[len(process_list) - 1][0]) + 1
        id_file.write('{0}\tchange_password\t\t{1}\t{2}\t{3}\n'.format(str(last_id), str(time.ctime()), old_password, str(new_password)))
        id_file.close()
        ls[2] = new_password
    elif flag == '1':
        input("You're outside of the range of try... press Enter.")
