

try:    
    num1 = int(input('Please enter an integer: '))
    print(num1*10)
except:    
    print('Woops! That\'s not an integer, try again!')    
    num1 = int(input('Please enter an integer: '))