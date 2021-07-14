def sub(x,y):
    z= x-y
    return print(z)

a= int(input("enter the value: "))
b= int(input("enter the value: "))34

sub(a,b)

# convertors using the function
def temp(c):
    f=(9/5)+c + 32
    return print(f)

c = int (input("enter the temperature"))
temp(c)

def hour(m,s):
    h = m/60 + s/3600
    return print(h)

m = int(input("enter the minutes"))
n = int(input("enter the seconds"))

hour(m,n)