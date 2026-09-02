try:
    a=int(input('enter your first number'))
    b=int(input('enter your second number'))

    print(a+b)
    print(a*b)
    print(a/b)

except ZeroDivisionError as error:
    print(error)


except  ValueError as error:
    print(error)



print('gm')
print('gn')               
