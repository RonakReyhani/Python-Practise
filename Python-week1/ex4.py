number = int(input('give me a number : '))
def comp(number):
    if number> 5:
        # print('True')
        return True
    elif number<5:
        # print('False')    
        return False
    else:
        return('The integer is exactly 5')

print(comp(number))        