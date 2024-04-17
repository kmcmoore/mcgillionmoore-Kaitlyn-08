import sys #don't use quit() or exit() in production code. use sys.exit

#make program repeat 
while True:

#get user input for file:
    file_variable = input('''
    What file would you like to search for?:
    a) Fortune 500 File 
    b) Zoo Animals File 
    x) Exit
    ''')

# process user input
    if file_variable == 'x':
        sys.exit() # this requires
    elif file_variable == 'a':
        file_variable = 'fortune_fivehun.csv'
    elif file_variable == 'b':
        file_variable = 'zoo_animals.csv'
    else:
        print('Invalid option. Please select a, b, or x.')
        continue

    #enter a search term this // is a global variable 
    search_variable = input(f'Enter the search term for {file_variable} file: ')
    search_variable = search_variable.title() #Make it so that the user can enter lower-case term. 

    #go to 02_search_for_team.py to continue...
    def find(file_variable,search_variable):
        with open(file_variable, 'r') as file:
            content = file.read()

    #now the file is in the memory buffer as content

    #next check to see if the search_variable is in the content buffer:
        if search_variable in content:

        #if the file print that is in the file AND
        #if user wants to see the entries for the term 
            print(f'Your search term {search_variable} exists in the {file_variable} file!')
            see_entries = input('Would you like to see the entries? (y or n)?')

        else:
            print(f'{search_variable} does not exist in {file_variable}')
            sys.exit()

        # if y then run this code to output all the entries:
        if see_entries.lower() == 'y':
            print(f'Here are all of the entries with the term {search_variable}:')
            with open(file_variable, 'r') as file:
                for line in file:
                    if search_variable in line: #
                        print(line.strip())
        

        # if N lowercase (user does not want to) then run this code:
        elif see_entries.lower() == 'n':
            print('Goodbye')
            sys.exit()
        



    #call the function
    find(file_variable, search_variable)