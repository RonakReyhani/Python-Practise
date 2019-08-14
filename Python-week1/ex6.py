name = input ('What is you name? ')
age = int(input ('How old are you? '))

def fun(name,age):
        if age>30:
               
                print("{name} is at level {age}".format(name=name,age=age) )   
        elif age<30:
                print("{name} is {age} years old".format(name=name ,age=age) )
                    
        else:
                print("{name} is {age}!!!".format(name=name ,age=age) )
        return        

fun(name,age)    