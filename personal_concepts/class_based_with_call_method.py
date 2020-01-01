#In this condition we are calling the __call__ of the class

class HelloClass(object):
    def __init__(self,name):
        print('inside init method')
        self.name = name
    
    def __call__(self):
        print('inside the __call__ method')
        print(f'the name of the user are -{self.name}')


HelloClass('tesing')
print('--------------')
hello = HelloClass('hello world')
hello()
