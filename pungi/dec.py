import pungi


def spied(function):

    def decorator(self):
        function(self)
        pungi.stopSpying()
    return decorator
