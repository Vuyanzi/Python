pound_weight = input ('What is your weight in pounds ')
kilograms = int(pound_weight) * 0.45
g = 'Your weight in kilograms is '
v = kilograms
print(g + str(v))
course = "python's course for beginners"
print(course)
course = "python course for 'beginners'"
print(course[0])
print(course[-3])
print(course[0:6])
print(course[0:])
print(course[1:])
print(course[:6])
print(course[:])
message = '''Hey everyone 
its never too late to start 
sooooo take the first step always and stick to it'''
print(message)
# conditions
answer= input("Does it ever get easy")
while answer == 'No':
    print("That's how life is")
if answer == 'Yes':
    print("Good for you, not everyone gets it easy in life")
else:
    print("Don't worry, you'll figure it out soon")
print("But we all keep going either way")
'''string formatting
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)
You will need to write a format string which prints out the data using the following syntax: 
Hello John Doe. Your current balance is $53.44.'''
fname = 'Glorious'
sname = 'Vuyanzi'
data = 34.5
print('Hello %s %s.Your current balance is $%.2f' % (fname, sname, data))
# given solution
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)
root = "sample"
here = "output"
path = f"{root}/{here}"
print(path)
# string operations
course = 'Python for beginners'
print(course.title())
print(course.upper())
print(course.lower())
print(course.find('beginners'))
print(course.replace('beginners', 'everyone'))
print('Python' in course)
