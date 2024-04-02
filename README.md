# Password-Generator

## Purpose:
As a new and learning Python developer, I wanted to gain more experience
generating random strings, importing CSV files, and saving CSV files. In this project,
I have also learned about using the customTkinter module to create a simple UI for
this program. 

## What does it do:
This program does exactly what the name says it does: generate passwords. When ran, 
the user inputs a username, what website this password is for, and how long they want
the password string to be. 

If you have an existing CSV file with passwords and want to import it, you can do so 
by pressing the "Import CSV" button. If it follows the correct format, the file will 
be successfully imported. If it does not, you will get a message that says it is 
incorrect. 

In the repository, there are two provided csv files, "correct.csv" and "incorrect.csv".
These files show the correct formatting, and how the columns should be named. 

There are 3 spaces for user entry: Username, Website, and How Many Characters.

For example: <br />
Username: bob <br />
Website: github <br />
How many characters?: 8 <br />

When the "Generate" password is pressed, these events may occur: <br />
1. It will create a new CSV file in the working directory named "passwords.csv" if a
   file is not imported. The generated password will save in this file.
2. If a CSV file is imported, generated passwords will save in this file.
3. If a "passwords.csv" file is already in the working directory, the generated
   passwords will save there.

I hope you enjoy my first Python project with a UI using customtkinter. If there are any
recommendations for this project, please let me know as I am open to learning new things.
