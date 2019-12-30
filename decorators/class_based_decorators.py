#class based decorators

class ClassBasedDecorators(object):
    
    def __init__(self,fun_to_decorators):
        print('inside the class decorators')
        self.fun_to_decorators = fun_to_decorators
        
    def __call__(self,*args,**kwargs):
        print('inside the call method')
        print('print the *args -{}'.format(args))
        print('print the kwargs - {}'.format(kwargs))
        return self.fun_to_decorators(*args,**kwargs)
    

@ClassBasedDecorators
def print_mor_args(*args,**kwargs):
    for arg in args:
        print(arg)

print_mor_args(1,2,3,4,dicts = {'key':'value','key1':'value2'})