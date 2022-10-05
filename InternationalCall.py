from Call import *


class InternationalCall(Call):
    def __init__(self):
        Call.__init__(self)
        self.country=input('Choose an country:\n 1- Uruguay\n 2- Brasil \n 3- Chile \n ---->')
        #It simulates an list of countries to choose
    
    def calculate_amount(self):
        #calculate the amount of an international call
        if (self.country=='1'):
            self.amount=(float(self.minutes)*0.2)
        elif (self.country=='2'):
            self.amount=(float(self.minutes)*0.5)
        elif (self.country=='3'):
            self.amount=(float(self.minutes)*0.4)
        else:
            print('Wrong option, try again.')
            exit()