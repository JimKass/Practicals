
menu = """(H)ello
(G)oodbye
(Q)uit"""
name = input('Enter name: ')

print(menu)
choice = input('>>> ').lower()
while choice != 'q':
    if choice == 'h':
        print('Hello, ', name)
    elif choice == 'g':
        print('Goodbye, ', name)
    else:
        print('What are you doing, {}? That was an invalid choice'.format(name))
    print(menu)
    choice = input('>>> ').lower()
print('Finished')
