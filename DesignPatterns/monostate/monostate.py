class StringReprMixin:
    def __str__(self) -> str:
        param = ', '.join(
            [f'{k}={v}' for k,v in self.__dict__.items()]
            )
        return f'{self.__class__.__name__}({param})'
    
    def __repr__(self):
        return self.__str__()


class MonoStateSimple(StringReprMixin):
    _state = {'x': 10, 'y':20}

    def __init__(self):
        self.__dict__ = self._state




if __name__ == '__main__':
    m1 = MonoStateSimple()
    m2 = MonoStateSimple()


    print(m1)
    print(m2)

    m1.x = 30

    print(m1)
    print(m2)