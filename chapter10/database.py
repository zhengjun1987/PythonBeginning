# FileName: /Users/zhengjun/Desktop/PythonBeginning/chapter10/database.py
# Author:Zheng Jun
# Date:2018/9/17 18:48
# E-mail:zhengjun1987@outlook.com

import shelve


def store_person(db):
    """
    让用户输入数据并将其保存到shelf对象中
    :param db:
    :return:
    """
    pid = input("Enter unique ID number:")
    person = {'name': input("Enter name:"), 'age': input("Enter age:"), 'phone': input("Enter phone:")}
    db[pid] = person


def lookup_person(db):
    """
    用户输入id和需查找字段，并从shelf中获取相应数据
    :param db:
    :return:
    """
    pid = input("Enter id number:")
    field = input("What would you like to know?(name, age, phone)")
    field = field.strip().lower()
    print(f"{field.capitalize()}: " + db[pid][field])


def print_help():
    print("The available commands are:")
    print("store: Stores information about a person.")
    print("lookup: Looks up a person from ID number")
    print("quit: Save changes and exit.")
    print('?: Print this message.')


def enter_command():
    cmd = input("Enter command(? for help):")
    cmd = cmd.strip().lower()
    return cmd


def main():
    database = shelve.open('database.dat')
    print(f"main :  = {database}")
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()


if __name__ == '__main__': main()

# /usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/bin/python3.9 /Users/zhengjun/Desktop/PythonBeginning/chapter10/database.py
# main :  = <shelve.DbfilenameShelf object at 0x10ea42340>
# Enter command(? for help):?
# The available commands are:
# store: Stores information about a person.
# lookup: Looks up a person from ID number
# quit: Save changes and exit.
# ?: Print this message.
# Enter command(? for help):store
# Enter unique ID number:001
# Enter name:Mr.Zheng
# Enter age:23
# Enter phone:+86 1713 1420 668
# Enter command(? for help):lookup
# Enter id number:001
# What would you like to know?(name, age, phone)phone
# Phone: +86 1713 1420 668
# Enter command(? for help):quit
#
# Process finished with exit code 0


# /usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/bin/python3.9 /Users/zhengjun/Desktop/PythonBeginning/chapter10/database.py
# main :  = <shelve.DbfilenameShelf object at 0x10a0e4340>
# Enter command(? for help):lookup
# Enter id number:001
# What would you like to know?(name, age, phone)name
# Name: Mr.Zheng
# Enter command(? for help):lookup
# Enter id number:001
# What would you like to know?(name, age, phone)age
# Age: 23
# Enter command(? for help):quit
#
# Process finished with exit code 0