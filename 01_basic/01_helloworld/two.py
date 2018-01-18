# file two.py
import one

print("top-level in two.py")
one.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")

# all of the code that is at indentation level 0 gets executed.
# Functions and classes that are defined are, well, defined, but none of their code gets run.
# Unlike other languages, there's no main() function that gets run automatically - the main()
# function is implicitly all the code at the top level.

# In this case, the top-level code is an if block.  __
# name__ is a built-in variable which evaluates to the name of the current module.
# However, if a module is being run directly (as in myscript.py above),
# then __name__ instead is set to the string "__main__".
# Thus, you can test whether your script is being run directly or being
# imported by something else by testing