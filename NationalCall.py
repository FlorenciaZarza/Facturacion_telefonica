from Call import *


class NationalCall(Call):
    def __init__(self):
        Call.__init__(self)
        self.locality=input('Choose an locality:\n 1- Berazategui\n 2- Quilmes \n 3- La Plata \n ---->')
        #It simulates an list of localities to choose
      
    def calculate_amount(self):
        #Calculate the amount of an national call
        if (self.locality=='1'):
            self.amount=(float(self.minutes)*0.2)
        elif (self.locality=='2'):
            self.amount=(float(self.minutes)*0.5)
        elif (self.locality=='3'):
            self.amount=(float(self.minutes)*0.4)
        else:
            print('Wrong option, try again')
            exit()