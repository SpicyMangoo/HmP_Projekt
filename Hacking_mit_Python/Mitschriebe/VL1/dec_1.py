def myFunc(*args, **kwargs):

    for arg in args:
        print(arg)

    for key, val in kwargs.items():
        print(key, val)
    
myFunc(*args:1,2,3,4,"Bobias",[9,9,9],name="TAUMANN")