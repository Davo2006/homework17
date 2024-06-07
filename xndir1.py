#xndir_1 (Write a function that checks the length of a string provided by the user. Handle the TypeError by raising a custom exception if the input is not a string.)
def check_lenght(m):
    if not type(m) is str:
        raise TypeError("you must give a string")
    x = len(m)
    return x
print(check_lenght(["iuhviuhveiuh"]))



