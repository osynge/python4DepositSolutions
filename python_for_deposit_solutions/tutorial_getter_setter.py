import logging


log = logging.getLogger(__name__)


def Property(func):
    return property(**func())


class setter_example_obj:
    """
    setter_example_obj example
    """
    def __init__(self):
        self._alwaysint = None

    @Property
    def alwaysint():
        doc = "this variable will always be an int"

        def fset(self, value):
            self._alwaysint = int(value)

        def fget(self):
            if self._alwaysint is None:
                raise Exception
            return self._alwaysint

        def fdel(self):
            self._alwaysint = None

        return locals()
