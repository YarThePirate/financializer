from time import sleep

from constants import msgs, freqs 
from expense import Expense

def build_expense():
    amnt = float(input("How much is the expense? "))
    
    while True:
        raw_freq = input(msgs.freq)

        if raw_freq in freqs.keys():
            freq = freqs[raw_freq]
            break
        print("\n Invalid value!\n")
        sleep(1)

    print(f'You entered an expense of amount')


def main():
    
    while True:
        choice = input(msgs.main)

        if choice == "Q":
            break
        elif choice == "1":
            build_expense()

        print(f'\nYour choice was {choice}')

    print("loop complete")


if __name__ == "__main__":
    main()
    
