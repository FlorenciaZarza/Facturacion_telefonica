import datetime 
import calendar


class Invoice():
    list_of_calls_loc=[]
    list_of_calls_nac=[]
    list_of_calls_int=[]
    def __init__(self):
        self.current_time = datetime.datetime.now()
        self.month=calendar.month_name[self.current_time.month]
        self.monthly_cost=30
        self.totalGlobal=0
        
    def printInvoice(self):
        print("Invoice of: ",  self.month)
        print('Basic Monthly Suscription:', self.monthly_cost)
        print("Local calls:")
        self.viewCalls(self.list_of_calls_loc)
        print(f'Total local calls: {self.viewTotal(self.list_of_calls_loc)}' )
        print ("National calls:")
        self.viewCalls(self.list_of_calls_nac)
        print(f'Total national calls: {self.viewTotal(self.list_of_calls_nac)}')
        print ("International calls:")
        self.viewCalls(self.list_of_calls_int)
        print(f'Total international calls: {self.viewTotal(self.list_of_calls_int)}' )
        self.add_monthly_cost()
        print(f"Total: {self.totalGlobal}")
        exit()
        
    def addLocalCall(self,call):
        self.list_of_calls_loc.append(call)
        
    def addNationalCall(self,call):
        self.list_of_calls_nac.append(call)
        
    def addInternationalCall(self,call):
        self.list_of_calls_int.append(call)
        
    def viewCalls(self,list):
        if (len(list)==0):
            print('No calls made')
        else:
            print("Date      | Amount")
            for obj in list:
                print(obj.date, "|" ,obj.amount)
    
    def modifyMonthlyCost(self,new_cost):
        self.monthly_cost=new_cost

    def calculate_subtotal(self,list):
        self.subtotal=0
        for i in list:
            self.subtotal+=i.amount

    def viewTotal(self,list):
        self.calculate_subtotal(list)
        self.totalGlobal+= self.subtotal
        return self.subtotal

    def add_monthly_cost(self):
        self.totalGlobal+=self.monthly_cost
