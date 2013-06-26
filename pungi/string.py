import re


def pp(*args, **kwargs):
    args_list = [repr(s) for s in args]
    kwargs_list = ["{0}={1}".format(key, repr(value))
                   for key, value in kwargs.items()]
    return ", ".join(args_list + kwargs_list)


def humanize(word):
    s = re.sub('(.)(()[A-Z][a-z]+)', r'\1 \2', word)
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s).lower()
