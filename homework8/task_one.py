def up_str(func):
    def wrap(some_str):
        res = func(some_str)
        return res
    return wrap


@up_str
def test_func(some_str):
    some_str = ['Hello', ' world!']
    new_list = [word.upper() for word in some_str]
    return new_list


print(test_func(['Hello', ' world!']))
