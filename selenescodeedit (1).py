#Importing tqdm to create like a progress bar that shows how long it takes to finish the Brute Force
from tqdm import tqdm
import itertools, random, string, time
#allow us to do loops in an arbitrary way so we dont have to modify the number of loops
from itertools import product 

# declare this function with an out string which will be blank
def passwordBR(charLength, password):
    #connect the password that wasn't guessed by the dictionary attack to the brute force try-out
    while len(password) < charLength:
        password = password(alphabet)
    return password

#we are going to need our password to be a tuple creating an immutable list
def bruteForce(pwBrute):
    #we add the estimated_time in order to shorten the time that Brute Force takes to guess the password
    estimated_time = int((alphabet.index(pwBrute[0]) / len(alphabet)) * (len(alphabet) ** charLength))
    pwTuple = tuple(pwBrute)
    #we create a list with all the items of the alphabet within a list, it repeats the time it is shown in (charLenght)
    charlist = [[x for x in alphabet]]* len(pwBrute)
    arguments = [char for char in charlist]

    #create the big previous list using itertools, iterate through that and then print everything which will have tons of permutations
    for combination in tqdm(itertools.product(*arguments), total = estimated_time):
        if combination == pwTuple:
            return combination

#if messagebox.showerror:
password = input("Enter a password: ")
start = time.time()
#we need the alphabet so the brute force can try all the characters from numbers to lower/upper case letters and special characters
alphabet= string.printable[:95]
#to check all the possibilities is to take the lenght of the alphabet and raise it to the character lenght
charLength = len(password)
passwordBR = passwordBR(charLength, password)
print(f"attempting to brute force {passwordBR}")
result = bruteForce(passwordBR)
end = time.time()
res = end - start
print(f"Bruteforced password {result} in {res} seconds")
#have the print statement at the end of the execution that calculates how long it took
