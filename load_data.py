import csv

file_path = "employees.csv"

def load_employees(file_path):
    """
    Load employees from a CSV file into a list of dictionaries.

    Args:
        file_path (str): The path to the CSV file containing employee data.

    Returns:
        list: A list of dictionaries where each dictionary represents an employee.
    """
    employees = []
    try:
        with open(file_path, mode="r") as file:
            # Use DictReader to read the CSV file into dictionaries
            reader = csv.DictReader(file)
            for row in reader:
                employees.append(row)
        print(f"Successfully loaded {len(employees)} employees.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred while loading employees: {e}")
    return employees

if __name__ == "__main__":
    # Path to the CSV file in the repository
    file_path = "employees.csv"

    # Load employee data
    employees = load_employees(file_path)

    # Check if employees were loaded successfully
    if employees:
        print("\nEmployee Data:")
        for emp in employees:
            print(f"ID: {emp['EmployeeID']}, Name: {emp['Name']}, "
                  f"Department: {emp['Department']}, Position: {emp['Position']}, "
                  f"Salary: {emp['Salary']}")
    else:
        print("No employees were loaded. Please check the file and try again.")


