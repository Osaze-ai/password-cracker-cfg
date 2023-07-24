#importing our pop up window from tkinter
import tkinter
from tkinter import messagebox #pop up box appears outside our window
import hashlib
import urllib.request
import string
from itertools import product
import time


#Function to ready a url text file of the 10,000 most common passwords which will be used a dictionary
#Define the name of the function and the variable being parsed (the url address)
def read_dictionary(url):
     #Declare the variable and make global to be used throughout the program
     global common_passwords
     #The variable 'common_passwords' is turned into an empty list
     common_passwords = []
     #Use a try block in case the url fails
     try:
          #Use the urllib package to open the url parsing each line of text
          for line in urllib.request.urlopen(url):
               #Decode each line of text using Unicode so each line becomes a separate string
               url_line = line.decode('utf-8')
               #Use strip to remove \n in each line
               #Add the each word to the common_passwords list
               common_passwords.append(url_line.strip())
     #Follow this path if there is an error in open the url
     except:
          #Notify the user that the dictionary for the cracker was not opened and quit the program
          print("There was an error with finding the weblink for the dictionary attack")
          quit()
     
for i in range(2):
     url = 'https://lucidar.me/en/security/files/10000-most-common-passwords.txt'
     #Function for the dictionary attack (hash password and list and compare values)
     def compare_passwords():
          #declare user's entered password from window input
          password = password_entry.get()
          #hash user password
          hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
          for word in common_passwords:
            hashed_word = hashlib.sha256(word.encode('utf-8')).hexdigest()
            if hashed_password == hashed_word:
                messagebox.showinfo(title="Password was cracked", message =f"'{password} is a bad password")
                break
            else:
               messagebox.showerror(title="Crack unsuccesful", message="Finding another way...")
               
               st = time.time()
            def product_loop(password, generator):
                for p in generator:
                    if ''.join(p)== password:
                        print('\nPassword:', ''.join(p))
                        return ''.join(p)
                return False
            def BruteForce(password, max_nchar=8):
                """Password brute-force algorithm.
        
                parameters
                ----------
                password: string
                    To-be-found password.
                max_nchar: int
                    maximum numbers of characters of password
        
                return
                ------
                BruteForce_password: string
                    Brute-forced password
                """
                print("1) Digits cartesian product")
                for l in range(0,9):
                    generator = product(string.digits, repeat=int(l))
                    print("\t..%d digit" % l)
                    p = product_loop(password, generator)
                    if p is not False:
                        return p
        
                print("2)Digits + ASCII lowercase")
                for l in range(1,max_nchar + 1):
                    print("\t..%d char" % l)
                    generator = product(string.digits + string.ascii_lowercase,
                                        repeat=int(l))
                    p = product_loop(password,generator)
                    if p is not False:
                        return p
            
                print("4)Digits + ASCII lower/upper + punctuation")
                all_char = string.digits + string.ascii_letters + string.punctuation
                for l in range(1, max_nchar + 1):
                    print("\t..%d char" % 1)
                    generator = product(all_char, repeat=int(l))
                    p = product_loop(password, generator)
                    if p is not False:
                        return p
    
            et = time.time()
            res = et - st
            print("Total time:", res, "seconds")

read_dictionary(url)


window = tkinter.Tk()
window.title("password cracker")
#popup window size in width and height
window.geometry('340x440')
#main frame bg color dark slate gray
window.configure(bg='#2F2F4F')

#inner frame color dark slate, placing all our widgets inside a frame for better UI exterience
frame = tkinter.Frame(bg='#2F2F4F') #frame is our tkinter container inside window for responsivness on larger screen size

# Creating widgets using grid (login created using pack above grid)
#Parent is window and text is username followed by another parent window and text password 
#x3 labels as static text on our password cracker screen 
#multiple attributes used to style our pop up window bg(background) fg(foreground)
login_label = tkinter.Label(frame, text="Check if a password can be cracked: ", bg='#52528B', fg="#FFFF14", font=("Arial", 28))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 18))
password_label = tkinter.Label(frame, text="Password", bg='#52528B', fg="#FFFF14", font=("Arial", 18))
#command used to execute when button is clicked
login_button = tkinter.Button( frame, text="Check password", bg='#FFFFEF', fg="#272740", font=("Arial", 20), command=compare_passwords)

# Placing widgets on the screen using grid which has 4 rows and 2 columns, starting at zero, 1, 2  & 3
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)#Pad(y) adding spaceing on y axis
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30) #spacing of login button on y axis

#using pack to make our pop up window responsive when you change the sizing to larger screen to look centralised
frame.pack()

#window.mainloop allows Tkinter to run and display our pop up window. Placed at the end of our password cracker code
window.mainloop()
