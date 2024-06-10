




def imprimir_todo(*args, **kwargs): 
     for arg in args: 
        print(arg) 
     for key, value in kwargs.items(): 
        print(f"{key}: {value}")

imprimir_todo(1,2,51,5,3)
        