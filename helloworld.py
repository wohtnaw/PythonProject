# python reserved word
import keyword
print(keyword.kwlist)


# string
str="hello"
print(str)                 # output string
print(str[0:-1])           # output the first to second last characters
print(str[0])              # output first character
print(str[2:5])            # output secnod to fourth characters
print(str[2:])             # output all characters behind the second character(no contain)
print(str[1:5:2])          # output every 2 words between the 1st and 5th
print(str * 2)             # output the characters for 2 times
print(str + 'world')         # contact string
 
print('------------------------------')
 
print('hello\nrunoob')      # use "\" and "n" declare special character
print(r'hello\nrunoob')     # insert "r" before string will able to prevent escape


# show multi rows in 1 row
import sys; x = 'runoob'; sys.stdout.write(x + '\n')


# output without new a line
print( x, end=" " )


# implicit type conversion
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("num_int value type is:",type(num_int))
print("num_flo value type is:",type(num_flo))

print("num_new value is:",num_new)
print("num_new value type is:",type(num_new)) 

