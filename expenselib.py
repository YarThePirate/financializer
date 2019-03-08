from expense import Expense

def monthly_total(expenses):
    total = 0
    for expense in expenses:
        total += expense.to_monthly()

    return total

def amortize_for_pay_period(expenses, pay_periods_per_month=2):
    return monthly_total(expenses) / pay_periods_per_month
