import requests #lets me make requests to pastebin to check
from random import *  #lets me generate the random codes
import string #works with random
import os #this lets me do the title
from colorama import init, Fore, Back, Style #allows me to do nice colors - only Fore should be needed but I like to copy them all anyways aha
init(convert=True) #makes colorama work
characters = string.ascii_letters + string.digits #defines what characters we're using
os.system(f"title Pastebin Finder!") #titles the project



while True:
	code =  "".join(choice(characters) for x in range(8))	#Made so this can be adaptable and do a randomised string count although pastebin seems to always be 8 so this will generate 8 random letters+digits which is perfect
	response = requests.get("https://pastebin.com/raw/"+code) #gets response from pastebin with pastebin.com/raw
	if "404" in response.text: #if response has 404 in - like the invalid codes will - it calls it invalid.
		print(Fore.RED+"[Invalid] - https://pastebin.com/"+code) #Prints in red and the pastebin link that is invalid
	else: #if its not 404 - aka valid itll do this:
		print(Fore.GREEN+"[Valid] - https://pastebin.com/"+code) #prints in green that it is valid and the pastebin link,
		f = open("valid.txt","a")#opens a file for all valid links 
		f.write("https://pastebin.com/" + code +"\n")#writes the link and a new line so the links arent all next to each other 
		f.close #closes the file  
		f = open(code+".txt","w") #makes a file with the end of the pastebin link name , if it was pastebin.com/test - this would be test
		f.write("Contents:\n\n" + response.text + "\n") #writes contents from the pastebin.com/test link into the newly made file
		f.close #closes the file  
		#as its a while true loop itll go on forever and repeat the process!
