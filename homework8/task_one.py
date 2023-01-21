my_list = ['Hello', ' world']


def text_up(func):
    def wrap(values):
        global my_list
        my_list = list(map(str.upper, my_list))
        res = func(values)
        return res
    return wrap


@text_up
def get_text(values):
    res = ' '.join(my_list)
    return res


print(get_text(my_list))
