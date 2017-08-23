
def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BasetdIn','Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = input('Enter your username: ')
    if username in usernames:
        print("Access Granted")
    else:
        print("Access Denied")

main()