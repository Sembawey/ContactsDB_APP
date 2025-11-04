#------------------- Define DB_F Path -------------------
path = "/home/ahmed/python/DB_file.txt"
################################################################################
#------------------- Start Main Menu -------------------
def main_menu():
    global mmSelection
    print("Select \'i\' to add contact")        #---------------------- Done
    print("Select \'v\' to view contacts")      #---------------------- Done
    print("Select \'s\' to search contacts")    #---------------------- Done
    print("Select \'d\' to delete contact")     #---------------------- Done
    print("Select \'e\' to erase contacts")     #---------------------- Done
    print("Select \'q\' to Close Application")  #---------------------- Pending
    mmSelection = input("Please enter your Selection: ")
    if mmSelection.lower() == "i":
        addContact()
        
    elif mmSelection.lower() == "v":
        view()
        
    elif mmSelection.lower() == "s":
        search()
        
    elif mmSelection.lower() == "d":
        deleteOne()
        
    elif mmSelection.lower() == "e":
        deleteAll()

    elif mmSelection.lower() == "q":
        return False
        
    else:
        print("Wrong Selection !")
        
    myQuit()

#------------------- End Main Menu -------------------
################################################################################
#------------------- Start Quit Function -------------------
def myQuit():
    global quitOption
    quitOption = input("Enter \'q\' to exit or \'m\' for Main Menu: ")
    if quitOption.lower() == "q":
        exit()
    elif quitOption.lower() == "m":
        pass
    else:
        myQuit()
#------------------- End Quit Function -------------------
################################################################################
#------------------- Start View Contacts -------------------
def view():
    with open (path , "r") as file:
        content = file.read()
        print("\n" + "   Welcome to Contact List DB Application   ".center(90,"=") + "\n")
        print( "Name".center(30 , " ") + "Contact ID".center(30 , " ") + "Phone Number".center(30 , " ") )
        print("".center(90,"-"))
        print(content)
#------------------- End View Contacts -------------------
################################################################################
#------------------- Start Add Contact -------------------
def addContact ():
    fName = input("Please Enter The First Name of your Contact:" + "\n")
    lName = input("Please Enter The Last Name of your Contact:" + "\n")
    contactID = input("Please Enter The ID of your Contact:" + "\n")
    phoneNum = input("Please Enter The phone Num of you Contact:" + "\n")
    with open(path , "a") as file:
        file.write( f"{fName} {lName}".center(30," ") + f"{contactID}".center(30," ") + f"{phoneNum}".center(30," ")  + "\n")
#------------------- End Add Contact -------------------
################################################################################
#------------------- Start Delete All Contacts -------------------
def deleteAll ():
    with open(path , "w") as file:
        file.write("")
#------------------- End Delete All Contacts -------------------

################################################################################
#------------------- Start Search Function -------------------
def search():
    findContact = input("Please Enter Any Contact Detail:\n")
    with open(path , "r") as file:
        lines = file.readlines()
        print("\n" + "   Required Contact Details   ".center(90,"=") + "\n")
        print( "Name".center(30 , " ") + "Contact ID".center(30 , " ") + "Phone Number".center(30 , " ") )
        print("".center(90,"-"))
        for line in lines:
            if findContact.lower() in line.lower():
                print (line)
#------------------- End Search Function -------------------
################################################################################
#------------------- Start Delete One Contact --------------
def deleteOne():
    deleteOneContact = input("Please Enter Contact Need to Delete:\n")
    with open(path , "r") as file:
        lines = file.readlines()
        for line in lines:
            if deleteOneContact.lower() in line.lower():
                indexToDelete = lines.index(line)
                del lines[indexToDelete]
    with open(path , "w") as file:
        for line in lines:
            file.write(line)
#------------------- End Delete Function -------------------
################################################################################
#------------------- Start  ---------------------------------

while True:
    if main_menu() ==  False:
        break
