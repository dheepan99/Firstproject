# Dictionary to store employee details
employees = {}

# function to add employee

def add_employee(emp_id,name,age,salary,department):
    
    employees[emp_id]={
        "Name":name,
        "Age":age,
        "Salary":salary,
        "Department":department
    }
    print(f"Employee {name} added successfully !")

# function to view aii employees
def view_employee():

    if employees:
        for emp_id,emp_details in employees.items():
            print(f"ID : {emp_id}, Details : {emp_details}")
    else:
        print("\nNo Employees added yet !\n")

# function to update employee details
def update_employee(emp_id,name=None,age=None,salary=None,department=None):
    try:
        if emp_id in employees:
            if name:
                employees[emp_id]["Name"] = name
            if age:
                employees[emp_id]["Age"] = age
            if salary:
                employees[emp_id]["Salary"] = salary
            if department:
                employees[emp_id]["Department"] = department
            
            print(f"Employee {emp_id} updated successfully!")
        else:
            print(f"Employee with ID {emp_id} Not Found")
    except keyError as e:
        print(f"Error updating Employee details : {e}")

# function to remove Employee
def remove_employee(emp_id):

    try:
        emp =employees.pop(emp_id)

        print(f"Employee {emp['Name']} Remove successfully..!")
    except keyError :
        print(f"Employee with ID {emp_id} not Found")

# function to save employee data to a without JSON
def save_to_file(filename):
    try:
        with open(filename,'w') as file:
            for emp_id,details in employees.items():
                line = f"{emp_id} :-> {details['Name']},{details['Age']},{details['Salary']},{details['Department']}\n"
                file.write(line)
        print("Employee data saved successfully..!")
    except Exception as e:
        print(f"Error : {e}")

# function to upload employee data from a file without JSON
def load_from_file(filename):
    try:
        with open(filename,'r') as file:
            global employees
            employees = {}  #clear the existing dictionary before loading
            for line in file:
                emp_data = line.strip().split(',')
                emp_id,name,age,salary,department = emp_data

                employees[emp_id]={
                    "Name":name,
                    "Age":age,
                    "Salary":salary,
                    "Department":department
                }
        print("Employee data Loaded successfully..!")        

    except FileNotFoundError:
        print(f"File {filename} not Found")
    except Exception as e:
        print(f"Error :{e}")

# main menu function
def menu():

    while True:
        print("\nWelcom to the employee management system : ")

        print("1. Add Eployee")
        print("2. View Eployee")
        print("3. Update Eployee")
        print("4. Delete Eployee")
        print("5. save to file")
        print("6. Load from file")
        print("7. Exit")

        choice = input("Enter your choice :")
        if choice == "1":
            emp_id = input("Enter Employee ID : ")
            name = input("Enter Employee Name : ")
            age = input("Enter Employee Age : ")
            salary = input("Enter Employee Salary : ")
            department = input("Enter Employee department : ")
            
            add_employee(emp_id,name,age,salary,department)
            
        elif choice == "2":
            view_employee()
            
        elif choice == "3":
            emp_id = input("Enter employee ID to Update : ")
            name = input("Enter New Name (leave blank to skip) : ")or None
            age = input("Enter New Age (leave blank to skip) : ")or None
            salary = input("Enter New Salary (leave blank to skip) : ")or None
            department = input("Enter New Department (leave blank to skip) : ")or None
            
            update_employee(emp_id,name,age,salary,department)
            
        elif choice == "4":
            emp_id = input("Enter Employee ID to Remove : ")
            remove_employee(emp_id)
            
        elif choice == "5":
            filename = input("Enter file Name to save : ")
            save_to_file(filename)
            
        elif choice == "6":
            filename = input("Enter filename to load from : ")
            load_from_file(filename)
            
        elif choice == "7":
            break  

menu()