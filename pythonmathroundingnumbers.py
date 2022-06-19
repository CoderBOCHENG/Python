# pyMATH -- rounding off numbers

'''
rounding a number, how do we do it?

the round() function rounds a floating point number (float) to
a specific decimal point.



ExAmPlE:

round(number, ndigits)

[number = the number to be rounded off]
[ndigits = number of decimal places]
'''

# for example, lets take a look at the below example to let us further clarify

pi = 3.1415926535879 # (pynumber)
two_decimals = round(pi,2)
three_decimals = round(pi,3)

print(two_decimals)
print(three_decimals)

'''

above examples we had done are rounding off to 2 / 3 decimal places

we will not experiment with more. lets say 4 decimal points

'''

three_decimals = round(pi,2)
print(three_decimals)
