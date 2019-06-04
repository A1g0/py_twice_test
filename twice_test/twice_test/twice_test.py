


def twice(func):
    def wrapper(*args, **kwargs):
        res = func(func(*args, **kwargs))
        return res
    return wrapper

@twice
def test(X):
    return X * X


print(test(2.0));