from datetime import date
from Call import *


class LocalCall(Call):
    def __init__(self):
        Call.__init__(self)
        self.day=self.date.weekday()

    def calculate_amount(self):
        #calculate the amount of an local call
        if (0 <= self.day <= 4):
            if ('08:00:00' <= self.current_time <= '20:00:00'):
                self.amount=(float(self.minutes)*0.2)
            else:
                self.amount=(float(self.minutes)*0.1)
        else:
            self.amount=(float(self.minutes)*0.3)
