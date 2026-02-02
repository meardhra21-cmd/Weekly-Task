def input_employee_details():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))
    return emp_id, name, basic_salary


def calculate_gross_salary(basic):
    hra = 0.20 * basic
    da = 0.10 * basic
    gross_salary = basic + hra + da
    return gross_salary


def calculate_deductions(basic):
    pf = 0.12 * basic
    tax = 0.05 * basic
    total_deductions = pf + tax
    return total_deductions


def display_salary(emp_id, name, gross, deductions):
    net_salary = gross - deductions
    print("\n------ Salary Details ------")
    print("Employee ID   :", emp_id)
    print("Employee Name :", name)
    print("Gross Salary  : ₹", gross)
    print("Deductions    : ₹", deductions)
    print("Net Salary    : ₹", net_salary)


def main():
    emp_id, name, basic = input_employee_details()
    gross = calculate_gross_salary(basic)
    deductions = calculate_deductions(basic)
    display_salary(emp_id, name, gross, deductions)


main()
