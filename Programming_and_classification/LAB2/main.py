def eleven(a:list):
    return list(filter(lambda x: x > 0, a))


def twelve(a):
    return list(filter(lambda x: len(x) < 5, a))


if __name__ == "__main__":
    print(eleven([1, -1, 2, 3, -4, -5, 6]))
    print(twelve(['test', 'badtest', 'foo', 'foobar']))
    