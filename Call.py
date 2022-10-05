from datetime import date
import time

class Call():
    minutes=0
    def __init__(self):
        self.minutes=input("Enter the call's duration in minutes: ")
        self.date = date.today()
        self.amount=0
        self.current_time = time.strftime("%H:%M:%S", time.localtime())
    
    def show_amount(self):
        #Returns the amount of the call
        self.calculate_amount()
        return self.amount

    def calculate_amount(self):
        pass