#!/usr/bin/env python
# coding: utf-8

# # TASK 01

# In[1]:


todo_list = []

def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added successfully!")

def view_tasks():
    if todo_list:
        print("Tasks in your to-do list:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty!")

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_index = int(input("Enter the number of the task to remove: ")) - 1
            if 0 <= task_index < len(todo_list):
                removed_task = todo_list.pop(task_index)
                print(f"'{removed_task}' has been removed from your to-do list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Your to-do list is empty!")

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")


# # TASK 02
# 

# In[8]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    return x / y

def calculator():

    print("Options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4):")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

# Run the calculator
calculator()


# # TASK 03

# In[11]:


import random
import string


# In[12]:


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Invalid input. Please enter a positive integer for password length.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")
        return

    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()


# # TASK 04

# In[14]:


import random


# In[15]:


def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == "rock" and computer_choice == "scissors") or        (user_choice == "scissors" and computer_choice == "paper") or        (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    return "Computer wins!"

# Main game loop
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}. Computer chose {computer_choice}.")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Your Score: {user_score}, Computer Score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors Game!")
    play_game()


# # TASK 05

# In[17]:


contacts = {}


# In[18]:


def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
    address = input("Enter the address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print("Contact added successfully!")
    
def view_contacts():
    if not contacts:
        print("Your contact book is empty.")
    else:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("-" * 20)



# In[19]:


def search_contact():
    query = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if query in [name, details['phone']]:
            found = True
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            break
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"Current Details for {name}:")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")
        contacts[name]['phone'] = input("Enter the new phone number: ")
        contacts[name]['email'] = input("Enter the new email: ")
        contacts[name]['address'] = input("Enter the new address: ")
        print("Contact details updated successfully!")
    else:
        print("Contact not found.")


# In[20]:


def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


# In[21]:


while True:
    print("\nOptions:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4/5/6).")


# In[ ]:




