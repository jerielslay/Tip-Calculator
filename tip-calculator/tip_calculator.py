'''  
# First I'm defining a function to handle the process
'''  

def calculate_tab(): 
    '''
    Here I'm creating a try and except function so that if the user enters a value other than a float, the except 
    part of the function will catch the ValueError
    '''
    bill = False
    while type(bill) != float:
        try:
            bill = float(input('Enter your bill amount: $'))
        except ValueError:
                print('Please enter numbers only.')
    
    '''
    Next, I'm doing the same thing below but using a try and except function within a while loop. So if the user inputs an
   incorrect value, it will restart just this one function, as opposed to the whole "calculate_tab" function. I've used the
   "round operator" so that the floats can round to the nearest second decimal number.
    '''  
    tip = False
    while type(tip) != float:
        try: 
            tip = float(input('What percentage would you like to tip?: '))
            tip = (bill * (tip/100))
            total = tip + bill
            print(f"Your tip is: ${round(tip, 2)}")
            print(f"Bill total: ${round(total, 2)}")
        except ValueError:
            print('Please enter numbers only.(Decimal allowed)')
        break
            
    '''
    Here is the same as above...Except is catching the value error in advance.
    '''
    people = False
    while type(people) != int:
        try:
            people = int(input('How many people will split the bill?: '))
            people = total/people
        except ValueError:
            print('Please enter numbers only.')
        
        print(f'Each person will pay: ${round(people)}')
        break

    '''
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Above is where the results are being printed. I chose to use the "round" operator so that I could round the decimal to
    the nearest 2. I did this just in case, hypothetically speaking, the user has like 200 guests on a $50 tab and tipping
    a random decimal number.
    ===========================================================================================
    Below, this is the progam looping itself to see if the user wants to calculate another bill.
    vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    '''
    def quest():
        while True:
            question = str(input('Would you like to calculate another bill?: [Y]es or [N]o'))
            if question.lower() == 'y':
                calculate_tab()
            elif question.lower() == 'n':
                print("Thank You For Dining At 'Toney's Steakhouse'. Come Again Soon!")
            else:
                print('Y or N only.')
                quest()
            break
    quest()

print("Welcome to 'Toney's Steakhouse'")
calculate_tab()