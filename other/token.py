class Token:
    def __init__(self):
        self._type = ""  # Type of token
        self._val = ""   # Value of token

    def set_type(self, type_str):
        self._type = type_str

    def set_val(self, val_str):
        self._val = val_str

    def get_type(self):
        return self._type

    def get_val(self):
        return self._val

    def __ne__(self, other):
        return self._type != other._type or self._val != other._val