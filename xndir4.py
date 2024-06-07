#xndir_4 (Write a simple login system where the user enters a username and password. Handle the KeyError by raising a custom exception if the username is not found in the users database(dictionary).)
database = {"karen":123,"armine":456}
username = input("username ")
password = input("password ")
if username in database and database[username] == password:
    print("you have entered")
else:
    raise KeyError("you enter wrong username or password")