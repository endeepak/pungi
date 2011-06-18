import re


def pp(*args):
    return ", ".join([repr(s) for s in args])


def humanize(word):
    s = re.sub('(.)(()[A-Z][a-z]+)', r'\1 \2', word)
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s).lower()
