# Standard Library Imports
from time import sleep

# External Python Library Imports
from pymongo import MongoClient

# App Libraries
from constants import msgs, freqs 
from expense import Expense

MONGO_HOST = "localhost"
MONGO_PORT = 27017
DB_NAME = "financializer"
EXPENSE_COLLECTION = "expenses"

client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client[DB_NAME]
expenses = db[EXPENSE_COLLECTION]

def build_expense():
    """Builds an expense using input from the command line"""
    name = input("What is this expense called?\n> ")
    
    amnt = float(input("How much is the expense?\n> $"))
    
    while True:
        raw_freq = input(msgs.freq)

        if raw_freq in freqs.keys():
            freq = freqs[raw_freq]
            break
        print("\n Invalid value!\n")
        sleep(1)

    expense = Expense(name, amnt, freq)

    print(f'Your expense summary: {expense}')
    return expense

def build_expense_loop():
    """Wraps the CLI expense builder in a confirmation loop"""
    while True:
        e = build_expense()
        confirm = input(msgs.confirm)
        if confirm == 'Y':
            break
    return e

def main():
    
    while True:
        choice = input(msgs.main)

        if choice == "Q":
            break
        elif choice == "1":
            expense = build_expense_loop()

        print(f'\nYour choice was {choice}')

    print("loop complete")


if __name__ == "__main__":
    main()
    
