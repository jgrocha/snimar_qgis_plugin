import re
import urllib



class EmailValidator(object):
    def __init__(self):
        self.regex = re.compile(r'^.+@([^.@][^@]+)$', re.IGNORECASE)

    def is_valid(self, string):
        match = self.regex.match(string or '')
        if not match:
            return False
        else:
            return True
class URLValidator:
    def __init__(self):
        pass
    def is_valid(string):
        pass
