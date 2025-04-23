# Define three functions
def fun():
    print("This is fun()")

def disp():
    print("This is disp()")

def msg():
    print("This is msg()")

# Store functions in a list
functions_list = [fun, disp, msg]

# Loop through the list and call each function
for func in functions_list:
    func()

