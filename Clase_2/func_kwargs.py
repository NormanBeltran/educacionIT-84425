def f(**kwargs):
    #print(type(kwargs))
    #print(kwargs)
    for k, v in kwargs.items():
        print(f"La clave {k} tiene como valor {v}")


f(a=1, b=2, c=3)    