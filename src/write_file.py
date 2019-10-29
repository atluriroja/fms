def new():
    # asks user for filename
    newfile = input("Insert 'newfile.txt' >>> ")
    #clear_files=[]
 
    # opens user inputted filename ".txt" and (w+) makes new and writes
    with open(newfile, 'w') as f:
        # asks for user input to enter into the file
        user_input = input("user input >>> ")
        # writes user input to the file and adds new line
        if user_input==[]:
            f.write("")
            #return(clear_files)
    
        elif user_input!=[]:
           f.write(user_input)
        
        f.write("\n")
    return new

new()
