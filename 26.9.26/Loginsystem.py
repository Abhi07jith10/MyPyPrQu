#Store a fixed username and password in variables. 
# Ask the user to enter both. 
# If both match, display "Login successful". 
# If username is correct but password is wrong, display "Incorrect password". 
# If username itself is wrong, display "User not found".

username="Abhi2004"
password="123456"

user_name=input("Enter the username : ")
pass_word=input("Enter the password : ")

if user_name==username and password==pass_word:
    print("Login successfull")

elif user_name!=username :
    print("User not found ")

elif user_name==username and password!=pass_word:
    print("Incorrect password ")
else:
    print("Invalid output")
