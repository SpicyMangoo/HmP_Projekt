import time

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

@decorate_print
@decorate_time
def addition(x,y):
    print("<>addition")
    return x + y


@decorate_print
@decorate_time
def subtraction(x,y):
    print("<>subtraktion")
    return x - y



print(addition(*args:3,3))
print(subtraction(*args:5,3))