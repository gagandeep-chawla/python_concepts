#decorators with the arguments

def decorators_with_arguments(arg1,arg2):
    def real_decorators(function):
        def inner_decorator(*args,**kwargs):
            print('Here we are going to print the decorators args') 
            print(f'The args1 of the decorators with argsment are -{arg1}')
            print(f'The args2 of the decorators of the arguements are -{arg2}')
            function(*args)
        return inner_decorator
    return real_decorators

@decorators_with_arguments('argument1','argument2')
def real_function(*args):
    for arg in args:
        print(f'The function of the {args}')

real_function(1,2,3,4,5)