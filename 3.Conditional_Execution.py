# type
a = type(True)
print(a)
s = str(a) # <class 'bool'>
print ('Now s is:',s)
print(s[0]) # <> parts of string

# Quotient and Remainder
division = 7/3 # gives actual float result
quotient = 7 // 3 # gives floor
remainder = 7%3 # gives remainder
# power
power = 3 ** 4 # 3 raised to power 4 (has high precedence)

print(quotient,remainder, division, power)

# using as calculator
#comparators have higher priority than boolean

# if/else
x =  9
if x > 0 :
    print('x is positive')
else:
    pass # pass simply does nothing
    print ('hh')

# elif

x = 5
y = 7

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

# nested

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

# try and  except

inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')
