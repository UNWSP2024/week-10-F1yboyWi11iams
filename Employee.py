# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.



# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.


class Employee:
    def __init__(self, name, ID_number, department, job_title):
        self.__name = name
        self.__ID_number = ID_number
        self.__department = department
        self.__job_title = job_title

    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def set_department(self, department):
        self.__department = department

    def set_job_title(self):
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

employee1 = Employee(name, id_number, department, job_title)
employee1.name = "Susan Meyers"
employee1.id_number = "47899"
employee1.department = "Accounting"
employee1.job_title = "Vice President"

print(employee1)

employee2 = Employee(name, id_number, department, job_title)
employee2.name = "Mark Jones"
employee2.id_number = "39119"
employee2.department = "IT"
employee2.job_title = "Programmer"

print(employee2)

employee3 = Employee(name, id_number, department, job_title)
employee3.name = "Joy Rogers"
employee3.id_number = "81774"
employee3.department = "Manufacturing"
employee3.job_title = "Engineer"

print(employee3)
