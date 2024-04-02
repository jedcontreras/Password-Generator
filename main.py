import customtkinter as ctk
from tkinter import filedialog, ttk
import pandas as pd
import csv
import os
import string
import random

allCharacters = string.ascii_letters + string.punctuation + string.digits
#variables being used
random_string = ''
global userpass
i = 0
website_input = None
username_input = None
password_length = ''
file_path = None
###### FUNCTIONS

#IMPORTING AN EXISTING CSV
def importCsv():
    global userpass
    global file_path
    global username_aliases
    global password_aliases
    global website_aliases
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        userpass = pd.read_csv(file_path)
        
        #possible column names
        username_aliases = ['username']
        password_aliases = ['password']
        website_aliases = ['website']
        
        #check if columns exist
        user_column = any(alias.lower() in map(str.lower, userpass.columns) for alias in username_aliases)
        pass_column = any(alias.lower() in map(str.lower, userpass.columns) for alias in password_aliases)
        website_column = any(alias.lower() in map(str.lower, userpass.columns) for alias in website_aliases)
        #both columns exist
        if user_column and pass_column and website_column:
            success = ctk.CTkToplevel()
            success.title("Success")
            success.geometry("300x200")
            
            label = ctk.CTkLabel(success, text="Import Successful!")
            label.pack(pady=20)
            close_button = ctk.CTkButton(success, text="Close", command=success.destroy)
            close_button.pack(pady=10)
            
            success.mainloop()
            return userpass
        else:
            noColumn = ctk.CTkToplevel()
            noColumn.title("Error")
            noColumn.geometry("500x200")
            
            label = ctk.CTkLabel(noColumn, text="This file is missing: Website and/or Username and/or Password columns.")
            label.pack(pady=20)
            close_button = ctk.CTkButton(noColumn, text="Close", command=noColumn.destroy)
            close_button.pack(pady=10)
            userpass = None
            noColumn.mainloop()
            return userpass
    else:
        noFile = ctk.CTkToplevel()
        noFile.title("No File Selected")
        noFile.geometry("300x200")
            
        label = ctk.CTkLabel(noFile, text="No file has been selected")
        label.pack(pady=20)
        close_button = ctk.CTkButton(noFile, text="Close", command=noFile.destroy)
        close_button.pack(pady=10)
        userpass = None
        noFile.mainloop()
        return userpass
#PASSWORD LENGTH
def passwordInput():
    global password_length
    password_length = digitEntry.get()
    return password_length
#USERNAME INPUT
def usernameInput():
    global username_input
    username_input = usernameEntry.get()
    return username_input
#WHAT WEBSITE?
def websiteInput():
    global website_input
    website_input = websiteEntry.get()
    return website_input
#PASSWORD BEING GENERATED
def generateRandomString():
    length_str = password_length #.get gets the input from the user putting in digit in textbox
    if length_str.isdigit():
        length = int(length_str)
        return ''.join(random.choice(allCharacters) for _ in range(length))
    else:
        print("Please input a valid number.")
        return None
#GENERATE BUTTON AND ADDING TO THE CSV     
def generatePassword():
    global password_length, website_input, username_input, random_string, userpass
    global i, csv_file, file, userpassCreated
    passwordInput()
    websiteInput()
    usernameInput()
    file = 'passwords.csv'
    if os.path.exists(file):
        fileExists = True
    else:
        fileExists = False
    
    random_string = generateRandomString()  # Generate random string after getting user input
    password_label.configure(text="Generated Password: " + random_string)
    # Create a dictionary with the new row data
    if 'userpass' not in globals() or userpass is None:
        if fileExists == False:
            while i < 1:
                createFile = pd.DataFrame(
                    {
                        'Website': [],
                        'Username': [],
                        'Password': []
                    }
                )        
                csv_file = 'passwords.csv'
                createFile.to_csv(csv_file, index=False)
                i = i+1
        readFile = pd.read_csv('passwords.csv')
        if random_string:
            new_row = {'Website': website_input, 'Username': username_input, 'Password': random_string}
        # Append the new row to the original DataFrame
            updated_df = pd.concat([readFile, pd.DataFrame([new_row])], ignore_index=True)
            updated_df.to_csv('passwords.csv', index=False)
            userpassCreated = pd.read_csv('passwords.csv')
            print(updated_df)
    else:
        if random_string:
            new_row = {'Website': website_input, 'Username': username_input, 'Password': random_string}
        # Append the new row to the original DataFrame
            updated_df = pd.concat([userpass, pd.DataFrame([new_row])], ignore_index=True)
            updated_df.to_csv(file_path, index=False)
            userpass = pd.read_csv(file_path)
            print(updated_df)


#////////////////////////

############ USER INTERFACE
main = ctk.CTk()
main.title("Password Generator")
main.geometry("800x400")

label = ctk.CTkLabel(master=main, text="Password Generator", font=("Roboto",24))
label.pack(pady=12, padx=10)

# Set the x and y coordinates where the first entry will be placed
x_coordinate = 100  # You can adjust this as needed
y_coordinate = 50   # You can adjust this as needed

# Set the width for the entries
entry_width = 200  # You can adjust this as needed


spacing = 20  # Space between the entries; adjust as needed

# username entry box
usernameEntry = ctk.CTkEntry(master=main, placeholder_text="Username?", width=entry_width)
usernameEntry.place(x=x_coordinate + entry_width + spacing, y=y_coordinate)
usernameEntry.pack(pady=12)

# website box
websiteEntry = ctk.CTkEntry(master=main, placeholder_text="What website?", width=entry_width)
websiteEntry.place(x=x_coordinate + entry_width + spacing, y=y_coordinate)
websiteEntry.pack(pady=12, padx=10)

# how many digits box
digitEntry = ctk.CTkEntry(master=main, placeholder_text="How many characters?", width=entry_width)
digitEntry.place(x=x_coordinate, y=y_coordinate)
digitEntry.pack(pady=12, padx=10)

# generate button
generate_button = ctk.CTkButton(master=main, text="Generate", command=generatePassword)
generate_button.pack(pady=12, padx=10)

# IMPORT CSV BUTTON
import_button = ctk.CTkButton(master=main, text="Import CSV", command=importCsv)
import_button.pack(pady=12, padx=10)

# DISPLAY PASSWORD
password_label = ctk.CTkLabel(master=main, text="", font=("Roboto", 12))
password_label.pack(pady=12)

main.mainloop()