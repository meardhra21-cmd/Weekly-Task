employees = []


def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    employee = {
        "id": emp_id,
        "name": name,
        "basic": basic
    }

    employees.append(employee)


def calculate_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    gross = basic + hra + da
    return gross


def apply_bonus_deduction(gross):
    bonus = gross * 0.05
    deduction = gross * 0.08
    net_salary = gross + bonus - deduction
    return net_salary


def generate_payroll_report():
    print("\n--- Payroll Report ---")
    for emp in employees:
        gross = calculate_salary(emp["basic"])
        net = apply_bonus_deduction(gross)

        print("\nEmployee ID:", emp["id"])
        print("Employee Name:", emp["name"])
        print("Net Salary:", net)


add_employee()
add_employee()

generate_payroll_report()
