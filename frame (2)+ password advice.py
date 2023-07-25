#importing our pop up window from tkinter
import tkinter
from tkinter import messagebox #pop up box appears outside our window
#import packages for dictionary attack - for hashing and reading urls
import hashlib
import urllib.request

#Function to read url text file of the 10,000 most common passwords
#which will be used a dictionary
#Define function and variable being parsed (the url address)
def read_dictionary(url):
     #Declare and make variable global to be used throughout the program
     global common_passwords
     #Variable 'common_passwords' turned into an empty list
     common_passwords = []
     #Open url text file and run through each line
     for line in urllib.request.urlopen(url):
          #Decode each line of text using Unicode
          #so each line becomes a separate string
          url_line = line.decode('utf-8')
          #Use strip to remove \n in each line
          #Add the each word to the common_passwords list
          common_passwords.append(url_line.strip())
    
#Function for dictionary attack (hash password and list then compare values)
def compare_passwords():
    #assign user's entered password from window input to a variable
    password = password_entry.get()
    #hash user password
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    #For loop passing through each entry in the common_passwords list
    for word in common_passwords:
        #hash each value in the list as it passes through the loop
        hashed_word = hashlib.sha256(word.encode('utf-8')).hexdigest()
        #compare each hashed list value with the hashed user password
        if hashed_password == hashed_word:
            #If a match is find, send a message box notifying the user
             cracked_message = f"Your password '{password} was cracked. \n \n Try to not use complete words," +\
                               "\n include lower and upper case letters \n and use numbers and symbols"
             messagebox.showinfo(title="Password was cracked", message=cracked_message)
            #Break the for loop as there's no need to iterate through again
             break
    #If all items in the dictionary list have been iterated through and no match has been found,
    #Follow this path
    else:
        #Notify user the dictionary attack was unsuccessful
         #pop up box which shows invalid login needs to change to password cracker 
        messagebox.showerror(title="Crack unsuccessful", message="Finding another way..") 


#The url leading the to the list of 10,000 words for the dictionary attack
url ='https://lucidar.me/en/security/files/10000-most-common-passwords.txt'
#Call the function to load the dictionary
read_dictionary(url)



window = tkinter.Tk()
window.title("password cracker")
#popup window size in width and height
window.geometry('600x450')
#main frame bg color dark slate gray
window.configure(bg='#2F2F4F')

#inner frame color dark slate, placing all our widgets inside a frame for better UI exterience
#frame is our tkinter container inside window for responsivness on larger screen size
frame = tkinter.Frame(bg='#2F2F4F') 

# Creating widgets using grid (login created using pack above grid)
#Parent is window and text is username followed by another parent window and text password 
#x3 labels as static text on our password cracker screen 
#multiple attributes used to style our pop up window bg(background) fg(foreground)
login_label = tkinter.Label(frame, text="Check if a password can be cracked: ", bg='#52528B', fg="#FFFF14", font=("Arial", 19))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 18))
password_label = tkinter.Label(frame, text="Password", bg='#52528B', fg="#FFFF14", font=("Arial", 18))
#command used to execute when button is clicked
login_button = tkinter.Button( frame, text="Enter", bg='#FFFFEF', fg="#272740", font=("Arial", 18), command=compare_passwords)

# Placing widgets on the screen using grid which has 4 rows and 2 columns, starting at zero, 1, 2  & 3
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)#Pad(y) adding spaceing on y axis
password_label.grid(row=2, column=0,)
password_entry.grid(row=2, column=1, pady=20, padx=(100, 10))
login_button.grid(row=3, column=0, columnspan=2, pady=30) #spacing of login button on y axis

#using pack to make our pop up window responsive when you change the sizing to larger screen to look centralised
frame.pack()

#window.mainloop allows Tkinter to run and display our pop up window. 
window.mainloop()
