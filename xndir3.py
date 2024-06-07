#xndir_3 (Write a function that prompts the user to enter a number and tries to convert it to an integer. Handle the TypeError exception by printing a message indicating that the input is not a valid number. Use a finally block to print "Type conversion process completed.")
def prompt():
    x = input("enter number ")
    try:
        x = int(x)
    except ValueError as e:
        print("you entered an invalid number",{e})
    finally:
        print("Type conversion process completed.")

prompt()