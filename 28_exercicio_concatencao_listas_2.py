import random


def debug(func):
    def _debug(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}(args: {args}, kwargs: {kwargs}) -> {result}')
        return result
    return _debug


l1 = [i for i in range(10)]
l2 = [i for i in range(5)]


@debug
def soma_listas(l1, l2):
    interval = min(len(l1), len(l2))
    return [l1[i] + l2[i] for i in range(interval)]


soma_listas(l1, l2)
