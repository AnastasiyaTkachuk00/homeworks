my_list = ['Hello', ' world']

class text_up:
    def __init__(self, func):
        self._func = func

    def __call__(self, values, func):
        my_list = list(map(str.upper, my_list))
        res = func(values)
        res2 = ' '.join(my_list)
        print(func(my_list)) 
        return res2
           





