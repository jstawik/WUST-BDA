from nltk.book import text1, text2, text3, text4, text5, text6, text7, text8, text9
from nltk import sent_tokenize


def eleven(a: list):
    return list(filter(lambda x: x > 0, a))


def twelve(a):
    return list(filter(lambda x: len(x) < 5, a))


def thirteen(a):
    idx, _ = max([(i, len(x)) for (i, x) in enumerate(a)], key=lambda x: x[1])
    return a[idx]


def fourteen(a, b):
    ret = []
    while a or b:
        if a:
            ret.append(a.pop(0))
        if b:
            ret.append(b.pop(0))
    return ret


def fifteen(a):
    n = [x for x in a if isinstance(x, int)]
    s = [x for x in a if isinstance(x, str)]
    return sorted(s) + sorted(n)


def sixteen(a):
    return sorted({x[0]: x[1] for x in a}.items(), key=lambda i: i[1])


def seventeen(a):
    return f'Monty Python: {text6.count(a)}, WSJ: {text7.count(a)}'


def eighteen(a, b):
    return set(a.vocab())-set(b.vocab())


def nineteen():
    vocab = set()
    texts = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
    for text in texts:
        vocab.update(text.vocab())
    return vocab


def twenty(a):
    sents = sent_tokenize(' '.join(a))
    idx, _ = max([(i, len(x)) for (i, x) in enumerate(sents)], key=lambda x: x[1])
    return sents[idx]


if __name__ == "__main__":
    print(eleven([1, -1, 2, 3, -4, -5, 6]))
    print(twelve(['test', 'badtest', 'foo', 'foobar']))
    print(thirteen(['a', 'aa', 'aaaa', 'aa', 'aaaa', 'a']))
    print(fourteen(['a', 'b', 'c'], [1, 2, 3]))
    print(fifteen(['a', 'ba', 0, 'c', 12, 123, 3, 'ca']))
    print(sixteen([('Bartek', 'Babiarska'), ('Adam', 'Abelska'), ('Celina', 'Centrum')]))
    print(seventeen('knight'))
    print(eighteen(text6, text7))
    print(nineteen())
    print(twenty(text2))

