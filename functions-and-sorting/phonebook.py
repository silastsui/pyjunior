#!/usr/bin/python
#phonebook

#add a person to the phone database (a)
#remove a person from the phone database r
#edit (overwrite) e
#search (s)
 
def menu():
    while True:
        action = raw_input("""What would you like to do?
search (s), add (a), remove (r), edit (e), quit (q), view (v)   
""")
        if action in ('s','a','r','e','q','v'):
            return action
        else:
            print "Sorry, your command wasn't recognized"
            continue

def add():
    global phonebook
    name = raw_input('Enter your contact name: ')
    if phonebook.has_key(name) == True:
        return "A contact under this name already exists. Edit it instead."
    phone = raw_input('Enter your phone number: ')
    phonebook[name] = phone
    return name, phonebook[name]

def search():
    global phonebook
    name = raw_input('Enter the name of the contact you want to find: ')
    if phonebook.has_key(name) == False:
        return "That contact doesn't exist!"
    return name, phonebook[name]

def remove():
    global phonebook
    name = raw_input('Enter the name of the contact you want to delete: ')
    if phonebook.has_key(name) == False:
        return "That contact doesn't exist!"
    del phonebook[name]
    return name, "has been deleted"

def edit():
    global phonebook
    name = raw_input('Enter the name of the contact you want to find: ')
    if phonebook.has_key(name) == False:
        return "That contact doesn't exist!"
    phone = raw_input("Enter the contact's new phone number")
    phonebook[name] = phone
    return name, phonebook[name]

phonebook = {}

print "Welcome to to your phonebook!"

while True:
    action = menu()
    if action == 'q':
        break
    elif action == 'v':
        print phonebook
    elif action == 'a':
        print add()
    elif action == 's':
        print search()
    elif action == 'r':
        print remove()
    elif action == 'e':
        print edit()
    
print 'Thank you for using the phonebook!'
