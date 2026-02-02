def sales_report():
    print("Generating Sales Report")


def employee_report():
    print("Generating Employee Report")


def finance_report():
    print("Generating Finance Report")


def generate_report(report_function):
    report_function()


generate_report(sales_report)
generate_report(employee_report)
generate_report(finance_report)
