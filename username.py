username=input("enter your username: ")

#result=username.find(" ")

username.isalpha()

if len(username)>12:
    print("username should have 12 characters or less")
elif not username.find(" ") ==-1:
    print("your username cant contain spaces")
elif not username.isalpha():
    print("your username cant contain numbers ")
else:
    print(f"welcome {username}")


