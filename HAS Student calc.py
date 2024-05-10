# Student Mark Calculator
# Purpose: To calculate the a list of students marks
# Author: Hasan Hussain
# Date: 03/04/2025


# Here I have defined the function which calculates the mean of the students marks.
def calc_mean(student_marks):
    return sum(student_marks) / len(student_marks)
    #Returns the value as an integer by dividing the stud.ent marks value by the amount of marks stored in the list.


#Here I have defined the function which calculates the mode of the students marks.
def calc_mode(student_marks):
    frequency_dict = {}
    #frequency_dict is used to initialise a new dictionary which also uses curly brackets.
    #It stores the frequency of each mark in the student_marks list.
    for mark in student_marks:
    #Here is a loop which goes over the list of students marks.
        frequency_dict[mark] = frequency_dict.get(mark, 0) + 1
        #updating the dictionary with the frequency/repetition of any values.
    max_frequency = max(frequency_dict.values())
    #calculates the maximum frequency out of all the frequencies that have been stored in dictionary.
    #Each mark has its own value of frequency depending on how many times it is repeated.
    mode =[mark for mark, frequency in frequency_dict.items() if frequency == max_frequency]
    #at this point a seperate list called mode is created. It contains the marks that are most frequent.
    if max_frequency == 1:
    #if statement to check if the maximum frequency is 0.    
        return "NO MODE - THERE ARE NO NUMBERS REPEATED IN THE LIST"
        #returns an output to the user showing that there is no mode as no single number has a higher frequency than another.
    else:
    #otherwise    
        return mode
        #the value of the mode, whichever numbersare in the(mode list) are returned.
        
    
#Here I have defined the function which calculates the median of the students marks.
def calc_median(student_marks):
    num_students = len(student_marks)
    #calculates the number of students marks stored by checking the length of the list and the amount of values there are.
    if num_students % 2 == 0:
    #checking if the amount of students can be divided by 2 and leave a remainder of 0.
    #if the value of the remainder is 0 then the calculator can proceed to find the  middle number.        
        median = (student_marks[num_students//2 - 1] + student_marks[num_students//2]) / 2
        #if there is an even amount of marks. Then finds the two values in the middle of the list.
        #adds the two indices together and then divides them by two.
    else:
    #otherwise    
        median = student_marks[num_students//2]
        #it will calculate the median in another way by finding the exact middle value in the list.
        #e.g if there is a list from 1,2,3,4,5,6,7,8 - the median would be 4.5
        
    return median
    #the new value of median is returned

#Here I have defined the function which calculates the skewness.
#skewness is the degree of asymmetry found in a probability distribution.
def calc_skewness(student_marks):
    mean = calc_mean(student_marks)
    #using the previous defined function (calc_mean)
    median = calc_median(student_marks)
    #using the previous defined function (calc_median)
    squared_distance_of_data_point = [(mark - mean) ** 2 for mark in student_marks]
    #a new list is created whcih calculates the square distance of all data points from the mean.
    sum_squared = sum(squared_distance_of_data_point)
    #this calculates the entire addition of the "squared_distance_of_data_point list and gives that result to sum_squared"
    variation = sum_squared / len(student_marks)
    #calculates the variance of the student marks and divides the sum_squared value by the amount of student marks in the list.
    standard_deviation = variation ** 0.5
    #Takes the value of the variation and finds the square root of it. Hense the use of **0.5
    actual_skewness = (3 * (mean - median) / standard_deviation)
    #the skewness is calculated using all the calculations within the function.
    #it finds the difference between the mean and median which is multiplied by 3 and divided by the Standard deviation.
    return actual_skewness
    #returns the value of the skewness


#Here I have defined the function which give the user the option to add more students to the list and there marks.
def add_students(student_marks):
    additional_students = int(input("Enter the number of additional students: "))
    #User inputs the amount of students which they would like to add. This input is taken as an integer value and stored in the already used list.
    for mark in range(additional_students):
    # initiating a loop which repeatedly goes over the additional_marks for as many times as the user adds the students marks.
    # the loop works in accordance to the amount of students the user added(additional students).
        student_mark = float(input("Enter the student mark: "))
        # whilst the loop is running, the user is prompted to add the marks of the students.
        # this is converted into a float data type/ floating point number.
        student_marks.append(student_mark)
        # the students marks list is then altered as the new data which the user entered is added to the list.
    calc_opt(student_marks)
    #the calc-opt function is called. which gives the user an option to display certain calculations.

#Here I created another function which ties in with the add_students function
# It is the part which gives the user options to choose from.
def calc_opt(student_marks):
    while True:
    # while loop is created which is not broken until the break keyword is used.
        print("1. Calculate Mean")
        print("2. Calculate Mode")
        print("3. Calculate Median")
        print("4. Calculate Skewness")
        print("5. Add more students")
        print("6. Exit")
        #list of options are displayed to the user.

        choice = input("Enter your choices from 1-5")
        # user is asked to select which calculation they would like to choose from.
        # there is no limit to this.
        
        if choice == '1':
            print("Mean:", calc_mean(student_marks))
        #if the user inputs the string 1, the program will calculate and output the mean.

        elif choice == '2':    
            mode_result = calc_mode(student_marks)
        #otherwise if the user inputs the string 2, the program will calculate and output the mode.
           
            if mode_result == "No Mode":
            #if there is no result for more display that.
                print("No Mode")
            else:
                print("Mode(s):", mode_result)
            #otherwise the value of mode is displayed.    
        elif choice == '3':
            print("Median:", calc_median(student_marks))
        #otherwise if the user inputs the string 3, the program will calculate and output the median.
        elif choice == '4':
            print("Skewness:", calc_skewness(student_marks))
        #otherwise if the user inputs the string 4, the program will calculate and output the skewness.
        elif choice == '5':
            print("Exiting Calculator!")
            exit()
        elif choice == '6':
            print("All student scores separated by commas:")
            print(", ".join(map(str, student_marks)))
        #if the user selects option 5 it will exit the calculator.
        else:
            print("Invalid choice. Please enter a valid option.")
        #when a user selects a value that is not provided they are shown a promt to re enter the value.

# Here I have created a function which allows the user to save the list (students and marks) into a file so that they can re use it next time.
def save_student_marks_to_file(file_path, student_marks):
# there are two arguments which are taken into this function.    
    with open(file_path, 'w') as file:
    #opens the file path in write mode. "with" ensures that the file is closed properly.
        for mark in student_marks:            
        #loop which iterates over each and every mark stored in the list.
            file.write(str(mark) + '\n')
            #each mark is written to the file and coverted to string data type.

# This is the main part of the program which uses all the functions that have been created above.
while True:
#loop created and will not be broken until the break statement is used.

    try:
    #use of try block which allows you to test a block of code for errors.
             
        print ("Welcome to the Student Mark Calculator")
        #welcomes the user
        source = input("enter 1 to input and 2 to retrieve from file ")
        # user is prompted with 2 options. this effects how the program will run and what data it will use.
        if source == '2':
        # if the user selects the second option and  they are trying to retrieve the file.    
            file_path = input("Enter the file path: ")
            #they will be prompted to enter the name of the file.
            try:    
                with open(file_path, 'r') as file:
                #opens the specific file which the user entered so that it can retrieve the data from it.
                # "r" is used to specify it will open in read mode    
                    student_marks = [float(mark.strip()) for mark in file.readlines()]
                    # converts the line (mark) to float data type and creates a list containing all the marks from that which is stored already.
                    print("Student marks retrieved successfully.")
                    #prints out a message showing the marks have been taken from a stored file and will be used.
            except FileNotFoundError:
            #if the file which the user inputed is not available or does not exist they are shown an error message.    
                print("File not found. Please try again.")
                continue
                #this keyword allows the loop to skip and re start the prompt for the file.
        elif source == '1':
        #if the users input is 1.
            num_students = int(input("Enter the number of students: "))
            # requests the user to input the number of students manually as there is no file to be retrieved.
            if num_students < 2:
            # checks if the amount of students that have been inputed is less than 2
                print("Calculator requires at least two students to make calculations.")
                # if there are less than two students. the user is informed that more than two students are required. 
                continue
                #this keyword allows the loop to skip and re start the prompt for the file.
                
            student_marks = []
            #empty list is initialised
            for number in range(num_students):
            # this loop is created which iterates "num_students" 
                student_mark = float(input("Enter the students mark: "))
                #user is prompted to input the mark and this is converted into float data type.
                student_marks.append(student_mark)
                #the student marks list is then altered according to the users inputs.
                print("You have entered", number + 1, "numbers")
                # user is shown with the amount of numbers they have entered so far so that they can keep track.

        else:
            print("Invalid input. Please enter '1' or '2'.")
            # otherwise if the input is neither 1 or 2 then the user is show that they should re enter correctly.
            continue
            #this keyword allows the loop to skip and re start the prompt for the file.

        # the calc_mean function is called and used here
        calculate_mean = input("To Calculate Mean - Select option 1: ")
        if calculate_mean == "1":
            new_mean = calc_mean(student_marks)
            print("The mean of the student marks: ", new_mean)

        # the calc_mode function is called and used at this point in the program.
        calculate_mode = input("To Calculate Mode - Select option 2: ")
        if calculate_mode == "2":
            new_mode = calc_mode(student_marks)
            print("The mode of the student marks: ", new_mode)

        # the calc_median function is called and used at this point in the program.
        calculate_median = input("To Calculate Median - Select option 3: ")
        if calculate_median == "3":
            new_median = calc_median(student_marks)
            print("The median of the student marks: ", new_median)

        # the calc_skewness function is called and used at this point in the program.
        calculate_skewness = input("To Calculate Skewness - Select option 4: ")
        if calculate_skewness == "4":
            new_skewness = calc_skewness(student_marks)
            print ("the skewness value is :", new_skewness)

        read_file = input("TO READ CURRENT CONTENTS OF FILE SELECT 5")
        # Allows the user to read all the current values of the student marks stored in the list as strings seperated by commas.
        if read_file == "5":
            print(", ".join(map(str, student_marks)))
            #.join takes all the parts in the list created by map and joins them all as strings.

        # the add_students function is called and used at this point in the program.
        add_more = input("Do you want to add more students? (1 -yes/ 2 -no): ")
        if add_more == "1":
            add_students(student_marks)

    
        save_option = input("Do you want to save these student marks to a file? (y/n): ")
        # user is shown a prompt to save or to not save the student marks
        if save_option.lower() == 'y':
        #if the user selects the string y...
            save_file_path = input("Enter the file path to save the student marks: ")
            # requesting the user to name the file which they would like to save the marks to.
            save_student_marks_to_file(save_file_path, student_marks)
            # function to save the student marks is called using the student marks and save file path.
            print("Student marks saved to: ", save_file_path)
            # informs the user that the path is saved and shows where it has been saved to.
        else:
            print("EXITING CALCULATOR")
            #otherwise if they select no as their option then it will exit the program
        
        break
        # here the loop is broken and the program ends.

    except ValueError:
        print("INVALID INPUT - PLEASE RE-ENTER A NUMBER")
    #if there are any errors in the values then the user is asked to re enter at any point throughout the program.
            



    
