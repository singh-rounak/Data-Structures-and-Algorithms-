
"""
                    VARIABLE SCOPE:

In Python, the variables can have different scopes, depending on how they are to be accessed. 
"""



'''
                    LOCAL Variables
'''
#These can be accessed only within the Python Function 
# where they are defined

def greet():
    
    # local variable
    message = 'Hello'
    
    print('Local', message)

greet()

# try to access message variable 
# outside greet() function

print(message)
#You will get - NameError: name 'message' is not defined



'''
                GLOBAL Variables
'''
# In Python, a variable declared outside of 
# the function or in global scope is known as a global variable.
# This means that a global variable can be accessed inside or 
# outside of the function.



'''
                NON-LOCAL Variables
'''
message = 'variable is Global'

def outer_func():
    message = 'variable is local'
    print(message)

    def inner_func():
        message = 'variable is non-local'
        print(message)

outer_func()


'''
                    EXAMPLES
'''
message  = 'Hello!'
def greet():
    #declaring local variable
    message = 'local'
    print(message)

greet() # ---> is called to print the local variable 'message'
print(message) # ---> Prints the global variable 'message'