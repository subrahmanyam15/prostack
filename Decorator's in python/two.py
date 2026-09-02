# with decorator

def smart_div(func):
    def inner (a,b):
        if b==0:
            print("can't divided by zero" )
        else:
            return func (a,b)
    return inner




# case 2
@smart_div
def cal_div(a,b):
    print(a/b)

cal_div(10,0)
print('gm')







        