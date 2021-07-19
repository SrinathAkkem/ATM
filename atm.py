try:
    f = open('Accounts.txt', 'r')
    f.close()
except FileNotFoundError:
    f = open('Accounts.txt', 'w')
    f.close()
import menu1
import os
os.system('clear')
menu1.menu1()
