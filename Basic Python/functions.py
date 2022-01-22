#***********#
# FUNCTIONS #
#***********#
# def stands for define
# folloed by the function name
# the by ():
# put anything you want insde(should by valid python code)
def say_hello():
    print("helllllloooooooooooooooo")
# call function:
def say_hello():
    print("helllllloooooooooooooooo")
# call function:
say_hello()

#************#
# PARAMETERS #
#************#
#           PARAMETERS
def say_bye(name, emoji):
    print(f"Bye, {name}{emoji}")
# call function:
say_bye("Arjun ", ":)")
# Default paramenters
def say_feeling(feeling="happy"):
    print(f"I am {feeling} today")
say_feeling()