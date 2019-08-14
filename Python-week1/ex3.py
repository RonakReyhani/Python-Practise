num1=int(input('hello user please give me a number :'))
num2=int(input('me agin,I need another number from you :'))

def pickGreater(num1,num2):
    if num1 > num2:
        print( str(num1) + ' is' + ' greater' + ' than ' + str(num2))  
    elif num2>num1:
        print( str(num2)+ ' is' + ' greater' + ' than ' + str(num1))   
        
    else:
        print("The numbers you entered are the same.")
    return

pickGreater(num1,num2)   