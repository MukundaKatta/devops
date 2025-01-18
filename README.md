Imports
python
Copy
Edit
import csv
This imports Python's built-in csv module, which is used for reading and writing CSV (Comma-Separated Values) files.
csv.DictReader is used later to parse the CSV file into a list of dictionaries.
File Path
python
Copy
Edit
file_path = "employees.csv"
This sets the path to your CSV file.
It assumes the employees.csv file is in the same directory as your Python script.
Load Employees Function
python
Copy
Edit
def load_employees(file_path):
    """
    Load employees from a CSV file into a list of dictionaries.
    """
This defines a reusable function named load_employees that takes the path to a CSV file (file_path) as its argument.
Purpose: To read the CSV file and return the data as a list of dictionaries.
Initialize an Empty List
python
Copy
Edit
    employees = []
This creates an empty list called employees, which will store each row of the CSV as a dictionary.
Open the File
python
Copy
Edit
    try:
        with open(file_path, mode="r") as file:
The try block begins to catch any errors that might occur while opening or reading the file.
open(file_path, mode="r"): Opens the file in read mode (r).
with ensures the file is properly closed after it’s done being read.
Read the CSV as a Dictionary
python
Copy
Edit
            reader = csv.DictReader(file)
csv.DictReader reads the CSV file and treats the header row (first row) as the keys of a dictionary.
Each subsequent row becomes a dictionary where the keys are column headers (e.g., EmployeeID, Name) and the values are the corresponding data in that row.
Append Rows to the List
python
Copy
Edit
            for row in reader:
                employees.append(row)
A loop iterates through each row in the reader.
row is a dictionary representing a single employee (e.g., {"EmployeeID": "101", "Name": "John Doe", ...}).
Each row is added to the employees list using append.
Success Message
python
Copy
Edit
        print(f"Successfully loaded {len(employees)} employees.")
After reading all rows, this prints how many employees were successfully loaded.
len(employees) gives the count of dictionaries (i.e., rows) in the list.
Error Handling
File Not Found Error
python
Copy
Edit
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
If the file doesn’t exist, Python raises a FileNotFoundError. This block catches that error and prints a user-friendly message.
Generic Exception
python
Copy
Edit
    except Exception as e:
        print(f"An error occurred while loading employees: {e}")
Catches any other unexpected errors and prints the error message (e).
Return Employees
python
Copy
Edit
    return employees
At the end of the function, the employees list is returned, which contains all the rows from the CSV file as dictionaries.
Main Block
python
Copy
Edit
if __name__ == "__main__":
This ensures that the following code is only executed if the script is run directly (not imported as a module).
Set File Path
python
Copy
Edit
    file_path = "employees.csv"
Assigns the file path to the variable file_path.
Load Employees
python
Copy
Edit
    employees = load_employees(file_path)
Calls the load_employees function and stores the returned list of dictionaries in the employees variable.
Check and Display Employees
If Data Was Loaded
python
Copy
Edit
    if employees:
        print("\nEmployee Data:")
If the employees list is not empty (i.e., the file was successfully read), it proceeds to display the data.
Print Each Employee
python
Copy
Edit
        for emp in employees:
            print(f"ID: {emp['EmployeeID']}, Name: {emp['Name']}, "
                  f"Department: {emp['Department']}, Position: {emp['Position']}, "
                  f"Salary: {emp['Salary']}")
Loops through each dictionary (emp) in the employees list.
Prints the values of EmployeeID, Name, Department, Position, and Salary for each employee in a formatted string.
If No Employees Were Loaded
python
Copy
Edit
    else:
        print("No employees were loaded. Please check the file and try again.")
If the employees list is empty, it prints an error message asking the user to check the file.
How It Works Together
The script attempts to open and read the file employees.csv.
Each row is converted into a dictionary and added to the employees list.
If the file is successfully loaded:
The script prints a message indicating how many employees were loaded.
It displays the employee data.
If the file is missing or an error occurs, it prints an appropriate error message.
Example Execution
With a Valid CSV (employees.csv):
plaintext
Copy
Edit
Successfully loaded 5 employees.

Employee Data:
ID: 101, Name: John Doe, Department: Engineering, Position: Software Engineer, Salary: 80000
ID: 102, Name: Jane Smith, Department: HR, Position: HR Manager, Salary: 90000
ID: 103, Name: Bob Brown, Department: Finance, Position: Accountant, Salary: 70000
ID: 104, Name: Susan Green, Department: Marketing, Position: Marketing Specialist, Salary: 75000
ID: 105, Name: Tom White, Department: Engineering, Position: DevOps Engineer, Salary: 85000
With a Missing File:
plaintext
Copy
Edit
Error: File 'employees.csv' not found.
No employees were loaded. Please check the file and try again.




