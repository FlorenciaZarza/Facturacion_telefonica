
from Call import *
from LocalCall import *
from NationalCall import *
from InternationalCall import *
from Invoice import *

def print_menu(options):
    #Prints the console menu
    print('Choose an option:')
    for clave in sorted(options):
        print(f' {clave}) {options[clave][0]}')
    print ('-------------------------\n')

def input_option(options):
    #Input the selected option
    while (a := input('Selected option: ')) not in options:
        print('Wrong option, try again.')
    return a

def run_option(option, options):
    #Executes the action corresponding to the selected option
    options[option][1]()

def menu(nombre,options, option_salida):
    #Implements menu's actions
    option = None
    while option != option_salida:
        print_menu(options)
        option = input_option(options)
        run_option(option, options)
        print()

def exit_program():
    print('*Leaving*')
    exit()

def principal_menu():
    options = { #Defines a data dictionary and what action each option performs
        '1': ('Modify Basic Monthly Suscription', action1),
        '2': ('Add new call', submenu),
        '3': ('Print invoice and exit', action3),
        '4': ('Exit', exit_program)
    }

    menu('Menu Principal',options, '4')

def action1():
    new_cost= input('Enter new Basic Monthly Suscription: ')
    invoice.modifyMonthlyCost(float(new_cost))
    print ("*Modification completed*")

def submenu():
    optionsS = { #Defines a data dictionary and what action each option performs
        'a': ('Local call', functionA),
        'b': ('National call', functionB),
        'c': ('International call', functionC),
        'd': ('Return to principal menu', submenu_exit),
        'e': ('Exit', exit_program)
    }

    menu('Submenu',optionsS, 5)

def functionA():
    local_call = LocalCall()
    print('Amount: ', local_call.show_amount())
    invoice.addLocalCall(local_call)

def functionB():
    national_call = NationalCall()
    print('Amount: ', national_call.show_amount() )
    invoice.addNationalCall(national_call)

def functionC():
    international_call = InternationalCall()
    print('Amount: ', international_call.show_amount())
    invoice.addInternationalCall(international_call)
   
def action3():
    invoice.printInvoice()

def submenu_exit():
    print('\n*Leaving*\n')
    print ('__________________________________________')
    principal_menu()

if __name__ == '__main__': 
    invoice=Invoice()
    principal_menu()

