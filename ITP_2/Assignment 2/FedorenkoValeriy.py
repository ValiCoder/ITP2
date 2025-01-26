import csv
import json
import os
import datetime

def find_file(filename="employees.csv", search_path="."):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

def main():
    print("Welcome to the Advanced Employee Management System!")
    employees = []
    file_path = find_file()
    employees = load_csv(file_path)
    while True:
        print("\nMenu:\n1. Add an employee\n2. Search for employees\n3. Remove an employee\n4. Update employee information\n5. Display all employees\n6. Generate analytics\n7. Save data to JSON\n8. Export data to CSV\n9. Delete a file\n10. Exit")
        choice = input("Your choice: ")
        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            search_employee(employees)
        elif choice == "3":
            emp_id = input("Enter ID to remove: ")
            if not emp_id.isdigit():
                print("Invalid ID.")
                continue
            emp_id = int(emp_id)
            employees = [emp for emp in employees if emp["id"] != emp_id]
            print("Employee removed.")
        elif choice == "4":
            update_employee(employees)
        elif choice == "5":
            display_employees(employees)
        elif choice == "6":
            generate_analytics(employees)
        elif choice == "7":
            json_path = input("Enter JSON file path: ")
            save_to_json(employees, json_path)
        elif choice == "8":
            csv_path = input("Enter CSV file path: ")
            save_to_csv(employees, csv_path)
        elif choice == "9":
            file_to_delete = input("Enter file path to delete: ")
            delete_file(file_to_delete)
        elif choice == "10":
            print("Thank you for using the Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def load_csv(file_path):
    employees = []
    if os.path.exists(file_path):
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    emp_id = int(row.get("ID", 0))
                    name = row.get("Name", "")
                    position = row.get("Position", "")
                    salary = int(row.get("Salary", 0))
                    skills = set(row.get("Skills", "").split(","))
                    employment_date = row.get("Employment Date", "")
                    employees.append({
                        "id": emp_id,
                        "name": name,
                        "position": position,
                        "salary": salary,
                        "skills": skills,
                        "employment_date": employment_date
                    })
                except ValueError:
                    print("Error reading a row. Skipping.")
    else:
        print("CSV file not found. Creating a new file...")
        create_new_file(file_path)
    return employees

def create_new_file(file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ["ID", "Name", "Position", "Salary", "Skills", "Employment Date"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
    print(f"New file '{file_path}' created successfully.")

def save_to_json(employees, file_path):
    try:
        data = [
            {
                "id": emp["id"],
                "name": emp["name"],
                "position": emp["position"],
                "salary": emp["salary"],
                "skills": list(emp["skills"]),
                "employment_date": emp["employment_date"]
            }
            for emp in employees
        ]
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print("JSON file saved successfully.")
    except Exception:
        print("Error saving JSON file.")

def save_to_csv(employees, file_path):
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ["ID", "Name", "Position", "Salary", "Skills", "Employment Date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for emp in employees:
                writer.writerow({
                    "ID": emp["id"],
                    "Name": emp["name"],
                    "Position": emp["position"],
                    "Salary": emp["salary"],
                    "Skills": ",".join(emp["skills"]),
                    "Employment Date": emp["employment_date"]
                })
        print("CSV file saved successfully.")
    except Exception:
        print("Error saving CSV file.")

def delete_file(file_path):
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print("File deleted successfully.")
        except Exception:
            print("Error deleting the file.")
    else:
        print("File not found.")


def add_employee(employees):
    print("Add a new employee:")

    # Validate employee ID
    emp_id = input("Enter employee ID: ")
    if not emp_id.isdigit():
        print("Invalid ID. Please enter a number.")
        return
    emp_id = int(emp_id)
    if any(emp["id"] == emp_id for emp in employees):
        print("ID already exists.")
        return
    name = input("Enter employee name: ")
    position = input("Enter employee position: ")
    salary = input("Enter employee salary: ")
    if not salary.isdigit() or int(salary) <= 0:
        print("Invalid salary. Please enter a positive number.")
        return
    salary = int(salary)
    skills = set(skill.strip() for skill in input("Enter skills (comma-separated): ").split(","))
    while True:
        employment_date = input("Enter employment date (YYYY-MM-DD): ")
        try:
            parsed_date = datetime.strptime(employment_date, "%Y-%m-%d")
            employment_date = parsed_date.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

    employees.append({
        "id": emp_id,
        "name": name,
        "position": position,
        "salary": salary,
        "skills": skills,
        "employment_date": employment_date
    })


def search_employee(employees):
    print("Search for an employee:")
    search_by = input("Search by 1. ID, 2. Name, 3. Skills: ")
    if search_by == "1":
        emp_id = input("Enter employee ID: ")
        if not emp_id.isdigit():
            print("Invalid ID.")
            return
        emp_id = int(emp_id)
        result = [emp for emp in employees if emp["id"] == emp_id]
    elif search_by == "2":
        name = input("Enter employee name: ").lower()
        result = [emp for emp in employees if name in emp["name"].lower()]
    elif search_by == "3":
        skill = input("Enter skill: ").lower()
        result = [emp for emp in employees if skill in {s.lower() for s in emp["skills"]}]
    else:
        print("Invalid option.")
        return

    if result:
        for emp in result:
            print(f"ID: {emp['id']}, Name: {emp['name']}, Position: {emp['position']}, Salary: ${emp['salary']}, Skills: {emp['skills']}, Employment Date: {emp['employment_date']}")
    else:
        print("No match found.")

def update_employee(employees):
    print("Update employee information:")
    emp_id = input("Enter employee ID to update: ")
    if not emp_id.isdigit():
        print("Invalid ID.")
        return
    emp_id = int(emp_id)
    employee = next((emp for emp in employees if emp["id"] == emp_id), None)
    if not employee:
        print("Employee not found.")
        return
    update_field = input("Update 1. Salary, 2. Add/Remove Skill: ")
    if update_field == "1":
        new_salary = input("Enter new salary: ")
        if not new_salary.isdigit() or int(new_salary) <= 0:
            print("Invalid salary. Please enter a positive number.")
            return
        employee["salary"] = int(new_salary)
        print("Salary updated successfully.")
    elif update_field == "2":
        action = input("Add or remove skill? (add/remove): ").lower()
        skill = input("Enter skill: ").strip()
        if action == "add":
            employee["skills"].add(skill)
            print("Skill added successfully.")
        elif action == "remove" and skill in employee["skills"]:
            employee["skills"].remove(skill)
            print("Skill removed successfully.")
        else:
            print("Invalid action.")
    else:
        print("Invalid option.")

def display_employees(employees):
    print("Display all employees:")
    filter_position = input("Filter by position (leave blank for all): ")
    filtered_employees = [emp for emp in employees if not filter_position or emp["position"].lower() == filter_position.lower()]

    sort_option = input("Sort by (salary/employment_date/none): ").lower()
    if sort_option == "salary":
        filtered_employees.sort(key=lambda x: x["salary"], reverse=True)
    elif sort_option == "employment_date":
        filtered_employees.sort(key=lambda x: x["employment_date"], reverse=True)

    if not filtered_employees:
        print("No employees to display.")
        return
    for emp in filtered_employees:
        print(f"ID: {emp['id']}, Name: {emp['name']}, Position: {emp['position']}, Salary: ${emp['salary']}, Skills: {', '.join(emp['skills'])}, Employment Date: {emp['employment_date']}")
        print("-" * 50)

def generate_analytics(employees):
    print("Generate analytics:")
    if not employees:
        print("No data for analysis.")
        return
    total_payroll = sum(emp["salary"] for emp in employees)
    average_salary = total_payroll / len(employees)
    highest_salary_emp = max(employees, key=lambda x: x["salary"])
    lowest_salary_emp = min(employees, key=lambda x: x["salary"])
    print(f"- Total Payroll: ${total_payroll:,}")
    print(f"- Average Salary: ${average_salary:,.2f}")
    print(f"- Highest Salary: {highest_salary_emp['name']} (${highest_salary_emp['salary']})")
    print(f"- Lowest Salary: {lowest_salary_emp['name']} (${lowest_salary_emp['salary']})")

if __name__ == "__main__":
    main()