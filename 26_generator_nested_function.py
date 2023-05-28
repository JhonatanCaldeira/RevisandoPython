def debug(func):
    def _debug(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}(args: {args}, kwargs: {kwargs}) -> {result}')
        return result
    return _debug


@debug
def soma(a, b):
    return a + b


def generate_power(expoente):
    def power(func):
        def inner_power(*args, **kwargs):
            base = func(*args, **kwargs)
            return base ** expoente
        return inner_power
    return power


@debug
@generate_power(2)
def raise_two(n):
    return n


@generate_power(3)
def raise_three(n):
    return n


soma(1, 2)
raise_two(100)
