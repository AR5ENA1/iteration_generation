list_of_lists_2 = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
]


def flattenlist(nestedlist):
    if len(nestedlist) == 0:
        return nestedlist
    if isinstance(nestedlist[0], list):
        return flattenlist(nestedlist[0]) + flattenlist(nestedlist[1:])
    return nestedlist[:1] + flattenlist(nestedlist[1:])


print(flattenlist(list_of_lists_2))
