"""
This file is created as part of lecture 126
"""
# Constants:
FILEPATH = "todos.txt"


# Functions:

def get_todos(filepath=FILEPATH):
    # This is a doc string - Document string that is displayed in the help()
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the txt file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


# If you want to run a print statement within functions.py,
# then a conditional statement is needed
# Without the conditional the print statements would print when main.py is run
# --name-- is type str, and when run in functions is name = main

# print(__name__) print __main__ to the console
# print(__name__) this will sow the name to be functions when the main.py file is run

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
