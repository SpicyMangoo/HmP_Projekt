import time

def addition(x,y):
    print("<>addition")
    return x + y

def subtraction(x,y):
    print("<>subtraktion")
    return x - y

# func() = Pointer meiner Funktion als Parameter
def decorate_print(func):
    def inner(*args, **kwargs):
        print(f"->decorate_print")
        val = func(*args, **kwargs)
        print(f"<-decorate_print")
        return val
    
    return inner


def decorate_time(func):
    def inner(*args, **kwargs):
        print(f"->decorate_time")
        start = time.time()
        val = func(*args, **kwargs)
        end = time.time()
        print(f"<-decorate_time: {end - start}")
        return val
    
    return inner


add1 = decorate_time(addition)
theAdd = decorate_print(add1)

sub1 = decorate_time(subtraction)
theSub = decorate_print(sub1)

print(theAdd(*args:3,3))
print(theSub(*args:3,3))