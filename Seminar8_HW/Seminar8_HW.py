# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных

import os

def show_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file:
        data = file.readlines()

        for contact in data:
            print(contact, end='')

    input("\npress any key ")


def add_contact(file_name):
    os.system('CLS')

    with open(file_name, 'a') as file:
        res = ''
        res += input('Input a surname of contact: ') + ' '
        res += input('Input a name of contact: ') + ' '
        res += input('Input a phone of contact: ')

        file.write('\n' + res)

    input("Contact was successfully added! \nPress any key for return: ")

def search_contact(file_name):
    os.system('CLS')
    target = input("input a name of contact for searching: ")

    with open(file_name, 'r') as file:
        contacts = file.readlines()

        for contact in contacts:
            if target in contact:
                print(contact)
                break

        else:
            print("there is no contacts with this name. ")

    input("\npress any key ")

def change_contact(file_name):
    os.system('CLS')
    target = input("input a name of contact for searching: ")

    with open(file_name, 'r') as file:
        contacts = file.readlines()

        for contact in contacts:
            if target in contact:
                name_c = contact.split()[0]
                print(f"Если оставляем имя {name_c}, то нажмите Enter \nили введите новое имя и нажмите Enter\n")
                temp = name_c
                name_c = input('Ввод: ')
                if name_c == "":
                    name_c = temp

                s_name_c = contact.split()[1]
                print(f"Если оставляем фамилию {s_name_c}, то нажмите Enter \nили введите новую фамилию и нажмите Enter\n")
                temp = s_name_c
                s_name_c = input('Ввод: ')
                if s_name_c == '':
                    s_name_c = temp

                phone_c = contact.split()[2]
                print(f"Если оставляем телефон {phone_c}, то нажмите Enter \nили введите новый телефон и нажмите Enter\n")
                temp = phone_c
                phone_c = input('Ввод: ')
                if phone_c == '':
                    phone_c = temp

                temp = contact

                contact_fresh = name_c + ' ' + s_name_c + ' ' + phone_c + '\n'  # строка на которую меняем

    with open(file_name, 'r') as file:
        old_data = file.read()
        new_data = old_data.replace(temp, contact_fresh)

    with open(file_name, 'w') as file:
        file.write(new_data)

    input("\npress any key ")

def removal_contact(file_name):
    os.system('CLS')
    target = input("input a name of contact for removal: ")

    with open(file_name, 'r') as file:
        contacts = file.readlines()

        for contact in contacts:
            if target in contact:
                temp = contact

                print(f'Вы хотите удалить: {contact}')
                choice = int(input('enter 1 if Yes\nenter 2 if No\nEnter: '))
                if choice == 2:
                    break
                elif choice == 1:
                    with open(file_name, 'r') as file:
                        old_data = file.read()
                        new_data = old_data.replace(temp, '')
                        print(f'information {contact}was deleted')


                    with open(file_name, 'w') as file:
                        file.write(new_data)
                else:
                    print('Input Error')

                input("\npress any key ")

def drawing():
    print("1 - show contacts")
    print("2 - add contacts")
    print("3 - search contacts")
    print("4 - change contacts")
    print("5 - removal contacts")
    print("6 - exit")
    print()

def main(file_name):
    while True:
        os.system('CLS')
        drawing()
        user_choice = int(input("Input a number from 1 to 6: "))

        if user_choice ==1:
            show_contacts(file_name)
        elif user_choice ==2:
            add_contact(file_name)
        elif user_choice == 3:
            search_contact(file_name)
        elif user_choice == 4:
            change_contact(file_name)
        elif user_choice == 5:
            removal_contact(file_name)
        elif user_choice == 6:
            print("Have a nice day!")
        else:
            os.system('CLS')
            print('Input Error\n')
            main(file_name)



main('test.txt')

