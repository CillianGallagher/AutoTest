
def main_menu():

    print ("""                   _     _______        _
        /\        | |   |__   __|      | |
       /  \  _   _| |_ ___ | | ___  ___| |
      / /\ \| | | | __/ _ \| |/ _ \/ __| __|
     / ____ \ |_| | || (_) | |  __/\__ \ |_ 
    /_/    \_\__,_|\__\___/|_|\___||___/\__|\n""") 
    
    

    print ("\nWelcome to AutoTest!")
    print ("""\nAutoTest is an Automated GUI Test Tool, used during the regression testing 
    stage of Software Testing, increasing testing accuracy whilst reducing the time requiring human input to a minimum. """)
    
    print ("\nPlease select a option:\n")

    print ("1 - Start Test")
    print ("2 - Start Section")
    print ("3 - User Manual")
    print ("4 - Test Report")

    check = input ("Please slect your option and press ENTER > ")

    if check == "1":
        S1()
    elif check == "2":
        section()
    elif check == "3":
        user_manual()
    elif check == "4":
        report()
        
def section():
    print 

def user_manual():
    print

def report ():
    print

class S1():

    def __init__():
        print ("")


main_menu()