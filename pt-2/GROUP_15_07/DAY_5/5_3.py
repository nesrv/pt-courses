

def h1(func):
    def wrapper(string, tag):
        return f'<{tag}> {func(string)} </{tag}>'
    return wrapper


def div(func):
    def wrapper(*args, **kwargs):
        return f'<div>\n\t {func(*args, **kwargs)} \n</div>'
    return wrapper

@div
@h1
def some_func(string, tag="h1"):
    return string


res = some_func("привет", tag="span")

print(res)


