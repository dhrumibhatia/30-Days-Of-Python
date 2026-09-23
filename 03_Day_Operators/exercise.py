age=25
height = 6.3
var_comp = 2+5j

def area_triangle():
    base = int(input('Enter base: '))
    height = int(input('Enter the height: '))
    return 0.5*height*base
print(area_triangle())

def peri_triangle():
    side1 = int(input('Enter the side: '))
    side2 = int(input('Enter the side: '))
    side3 = int(input('Enter the side: '))
    return side1+side2+side3
print(peri_triangle())

def rec():
    length = int(input('Enter the length: '))
    width = int(input('Enter the width: '))
    print('Area of rectangle is: ', length*width)
    print('Perimeter of rectangle is: ', 2*(length+width))  
print(rec())

def circle():
    radius = int(input('Enter the radius: '))
    print('Area of circle is: ', 3.14*radius*radius)
    print('Perimeter of circle is: ', 2*3.14*radius)
print(circle())

line_slope = 2
x_intercept = 2 / line_slope
y_intercept = -2
print('Slope of y = 2x - 2:', line_slope)
print('x-intercept:', x_intercept)
print('y-intercept:', y_intercept)

point_slope = (10 - 2) / (6 - 2)
distance = ((6 - 2) ** 2 + (10 - 2) ** 2) ** 0.5
print('Slope between (2, 2) and (6, 10):', point_slope)
print('Euclidean distance:', distance)
print('The slopes are equal:', line_slope == point_slope)

# 11
for x_value in [-5, -4, -3, -2, 0]:
    y_value = x_value ** 2 + 6 * x_value + 9
    print(f'x = {x_value}, y = {y_value}')
print('y is 0 when x = -3:', (-3) ** 2 + 6 * (-3) + 9 == 0)


print('Lengths are different:', len('python') != len('dragon'))


print("'on' is in both words:", 'on' in 'python' and 'on' in 'dragon')


sentence = 'I hope this course is not full of jargon'
print("jargon' is in the sentence:", 'jargon' in sentence)


print("There is no 'on' in both words:", not ('on' in 'python' and 'on' in 'dragon'))


python_length = len('python')
print('Python length as a float:', float(python_length))
print('Python length as a string:', str(python_length))


number = 12
print('12 is even:', number % 2 == 0)


print('7 // 3 equals int(2.7):', 7 // 3 == int(2.7))


print("type('10') equals type(10):", type('10') == type(10))


print("int(float('9.8')) equals 10:", int(float('9.8')) == 10)

def workdone():
    hours = int(input('Enter hours: '))
    rate = int(input('Enter rate per hour: '))
    return hours * rate
print('Work done:', workdone())

def live():
    years = int(input('Enter number of years you have lived: '))
    return years * 365 * 24 * 60 * 60
print('You have lived for', live(), 'seconds.')

def table():
    num = int(input('Enter a number: '))
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
table()
