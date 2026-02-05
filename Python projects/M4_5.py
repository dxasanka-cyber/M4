correct_username = "python"
correct_password = "rules"
attempts = 0
while attempts <5:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == correct_username and password == correct_password:
        print("Welcome !")
        break
    else :
        attempts += 1
        print(f" Incorrect. Attempt remaining: {5- attempts}")
        if attempts == 5:
            print ("Access Denied")
