init_list = [115, 352, 0, 310, 500]
res = []


def get_winners(init_list):
    init_list_sorted = sorted(init_list, reverse=True)[:3]
    for index, element in enumerate(init_list_sorted):
        idx = init_list.index(element)
        res.append(idx + 1)


test = get_winners(init_list)
print(res)
