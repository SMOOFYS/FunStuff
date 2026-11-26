print("Welcome to MyFace")
username = "Simbaiscool"
password = "Verycool"

user_name = input("Username: ")
user_pass = input("Password: ")

if user_name in ["Simbaiscool", "simbaiscool"] and user_pass in ["Verycool", "verycool"]:
    print(f"Welcome back {username}.")
elif user_name not in ["Simbaiscool", "simbaiscool"] and user_pass not in ["Verycool", "verycool"]:
    print("Your username or password is incorrect. Refresh the page to try again.")
   
    
    

    