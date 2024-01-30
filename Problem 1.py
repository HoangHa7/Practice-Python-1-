Pi = 22/7
choose = None


# function to invert radian to degree
def invert_degree(y):
    degree = y * (180/Pi)
    print("Degree:", round(degree, 0))
    return 0


# function to invert degree to radian
def invert_radian(y):
    radian = y * (Pi/180)
    print("Radian:", round(radian, 2))
    return 0


# function to check
def rerun(x):
    inputs = None
    if x == "radian to degree":
        # Check to see if the inout is a number or not
        while inputs is None:
            try:
                inputs = float(input("Radian? "))
            except ValueError:
                print("Not a number, try again!")
        invert_degree(inputs)
    elif x == "degree to radian":
        # Check to see if the inout is a number or not
        while inputs is None:
            try:
                inputs = float(input("Degree? "))
            except ValueError:
                print("Not a number, try again!")
        invert_radian(inputs)


# while loop to check the answer base on 2 choices
while choose is None:
    choose = input("Which one do you want to convert 'radian to degree' or 'degree to radian'? ")
    while choose != "degree to radian" or choose != "radian to degree":
        if choose == "degree to radian" or choose == "radian to degree":
            rerun(choose)
            break
        choose = input("Which one do you want to convert 'radian to degree' or 'degree to radian'? ")
