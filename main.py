import os

while True:
    print("1 = To add password")
    print("2 = Veiw a password")
    print("3 = Exit")
    

    choice = input("1 or 2 or 3:")

    if choice == '1':
        x = input("What is the account or website?:")

        # Username
        y = input("What is the username:")
        y = ("Username: " + y)

        # Password
        p = input("What is the password:")
        p = (" Password: " + p)
        
        # Setting A custom name for the file.       
        x = (x + "Credentials.txt")
         
      
        # The things we add to the file.
        f = open(x, "w")
        f.write(y)
        f.write(p)
        f.close()

    elif choice == '2':
        x = input("What is the account or website you would to veiw case sensitive ")
        x = (x + "Credentials.txt")
        f = open(x)
        print(f.read()) 

    elif choice == '3':
        print("Goodbye!")
        break
    
    
