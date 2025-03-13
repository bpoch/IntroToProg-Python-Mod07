# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Brian Pochert, 03/09/2025 add set of data classes with inheritance
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

# TODO Create a Person Class (DONE)
class Person:
    """
    A Class representing person data
    Properties:
    - student_first_name (str): The students first name
    - student_last_name (str): The students last name
    - course_name (str): The students course name
    ChangeLog:
    -Brian Pochert 03/09/2025 create the class
    """
    def __init__(self, student_first_name:str ="", student_last_name:str = "", course_name:str = ""):
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name
        self.course_name = course_name

# TODO Add first_name and last_name properties to the constructor (DONE)
    def __int__(self, student_first_name: str ="", student_last_name: str =""):
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name

# TODO Create a getter and setter for the first_name property (Done)
    @property
    def student_first_name(self):
        return self.__student_first_name.title()
    @student_first_name.setter
    def student_first_name(self, value:str):
        if value.isalpha() or value =="":
            self.__student_first_name = value
        else:
            raise ValueError("The First name should not contain numbers ")

# TODO Create a getter and setter for the last_name property (Done)
    @property
    def student_last_name(self):
        return self.__student_last_name.title()
    @student_last_name.setter
    def student_last_name(self, value:str):
        if value.isalpha() or value =="":
            self.__student_last_name = value
        else:
            raise ValueError("The Last name should not contain numbers ")

# TODO Override the __str__() method to return Person data (DONE)
    def __str__(self):
        return f"{self.student_first_name}, {self.student_last_name}"

# TODO Create a Student class that inherits from the Person class (DONE)
class Student(Person):
    """
    A collection data about students

    ChangeLog: (Who, When, What)
    Brian Pochert 03/09/2025 created the class
    """

# TODO call to the Person constructor and pass it the first_name and last_name data (DONE)
    def __init__(self, student_first_name: str ="", student_last_name: str =""):
        super().__init__(student_first_name=student_first_name, student_last_name=student_last_name)

# TODO add a assignment to the course_name property using the course_name parameter (DONE)
    def __init__(self, course_name):
        self.course_name = course_name

# TODO add the getter for course_name
    @property
    def course_name(self):
        return self.__course_name.title()

# TODO add the setter for course_name
    @course_name.setter
    def course_name(self, value: str):
        if value.isalpha() or value == "":
            self.__course_name = value
        else:
            raise ValueError("The course name should have a name and number")

# TODO Override the __str__() method to return the Student data
    def __str__(self):
        return f"{self.student_first_name},{self.student_last_name}, {self.course_name}"


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows to be filled with file data

        :return: list
        """

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        Brian Pochert, 03/09/2025 changed the custom error message to reflect first name for student_first_name
        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            student_first_name = input("Enter the student's First name: ")
            if not student_first_name.isalpha():
                raise ValueError("The First name should not contain numbers.")
            student_last_name = input("Enter the student's Last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The Last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("-"*40)
print("Program Ended")
print("Thank You")
