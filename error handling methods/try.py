# case1


try:
    fp=open('data.txt','r')
    data=fp.read()
    print(data)

except FileNotFoundError:print(FileNotFoundError)


finally:
    print("finally block will excuted ")









