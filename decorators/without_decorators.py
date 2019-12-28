'''
In this file we have discribe the how decoratores working.
'''
def pass_thru(fun_to_decorators):
    def new_func(*original_args, **original_kwargs):
        print("the original_args -{}".format(original_args))
        print("The value of the kwargs-{}".format(original_kwargs))
        fun_to_decorators(*original_args, **original_kwargs)
    return new_func


@pass_thru
def print_args(*args, **kwargs):
    for arg in args:
        print('The value of arg-{}'.format(arg))
    for key, value in kwargs.items():
        print('the value of key-{} and value-{}'.format(key, value))


'''
here pass_thru method called the print_args method and the 
(1, 2, 3, dicts={'key': 'value'}) are the argument of the
print_args methods
'''
pass_thru(print_args)(1, 2, 3, dicts={'key': 'value'})
