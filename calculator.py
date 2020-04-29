def add(x,y):
    return (x+y)

def subtract(x,y):
    return(x-y)

def multiply(x,y):
    return(x*y)

def divide(x,y):
    return(x/y)

print('CALCULATOR')
print('1 = ADD')
print('2 = SUBTRACT')
print('3 = MULTIPLY')
print('4 = DIVIDE')

choice = input('Please select function: 1/2/3/4')

num1 = float(input('Please input first number:'))
num2 = float(input('Please input second number'))

if choice == '1':
    print(num1, '+', num2, '=', add(num1,num2))
elif choice == '2':
    print(num1, '-', num2, '=', subtract(num1,num2),)
elif choice == '3':
    print(num1, '*', num2, '=', multiply(num1,num2))
elif choice == '4':
    print(num1, '/', num2, '=', divide(num1,num2))
else:
    print('INVALID INPUT')


########################################
# Calculator function sort of
########################################

'''
MAKE IT LOOK LIKE THIS...

calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"

'''

def calculate(**kwargs):
'''
define a dictionary called operation_lookup  that maps a string like "add"
to an actual mathematical operation involving the values of 'first' and 'second'
'''
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }


# create a boolean variable called is_float, which is True if kwargs contains 'make_float', otherwise it's false

    is_float = kwargs.get('make_float', False)

'''
Then I lookup the correct value from the operation_lookup dict using the operation that was specified in kwargs
Basically, turning something like "subtract" into: kwargs.get('first', 0) - kwargs.get('second', 0)

I store the result in a variable called operation_value

'''
    operation_value = operation_lookup[kwargs.get('operation', '')]

'''
I return a string containing either the specified message or the default 'The result is' string.

Whether operation_value  is interpolated as a float or int is determined by the is_float  variable.

'''

    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final
