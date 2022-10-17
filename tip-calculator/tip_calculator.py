print("Welcome to 'Toney's Steakhouse'")

'''  
# First I'm defining a function to handle the process
'''  
def calculate_tab(): 
    '''
    # Here I'm creating a try and except function so that if the user enters a value other than a float, then the original
    function will re-run
    '''  
    try: 
        bill = float(input('Enter your bill amount: $'))
    except:
        print('Please enter numbers only.(Decimal allowed)')
        calculate_tab()
    '''
    Next, I'm doing the same thing below but using a try and except function within a while loop. So if the user inputs an
   incorrect value, it will restart just this one function, as opposed to the whole "calculate_tab" function. I've used the
   "round operator" so that the floats can round to the nearest second decimal number.
    '''  
    tip = False
    while type(tip) != float:
        try: 
            tip = float(input('What percentage would you like to tip?: '))
            tip2 = (bill * (tip/100))
            total = (bill * (tip/100)) + bill
            print(f"Your tip is: ${round(tip2, 2)}")
            print(f"Bill total: ${round(total, 2)}")
        except ValueError:
            print('Please enter numbers only.')
    '''
    Here is the same as adove...Except is catching the value error in advance.
    '''
    people = False
    while type(people) != int:
        try:
            people = int(input('How many people will split the bill?: '))
        except ValueError:
            print('Please enter numbers only.')
    '''
    Next is the math that takes place to calculate all of the inputed data.
    '''
    bill_tip = (bill * (tip/100)) + bill
    calculate_bill = bill_tip / people
    '''
    Here is where the results are being printed. I chose to use the "round" operator so that I could round the decimal to
    the nearest 2. I did this just in case, hypothetically speaking, the user has like 200 guests on a $50 tab and tipping
    a random decimal number.
    '''
    print(f'Each person will pay: ${round(calculate_bill, 2)}')
    print("Thank You For Dining At 'Toney's Steakhouse'")

# Here is where I just called the function.
calculate_tab()