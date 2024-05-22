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

class MonoState(StringReprMixin):
    _state = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, nome=None, sobrenome=None):
        if nome is not None:
            self.nome = nome
        
        if sobrenome is not None:
            self.sobrenome = sobrenome


if __name__ == '__main__':
    ms1 = MonoStateSimple()
    ms2 = MonoStateSimple()


    print(ms1)
    print(ms2)

    ms1.x = 30

    print(ms1)
    print(ms2)

    m1 = MonoState(nome="William")
    m2 = MonoState(sobrenome="Mezzina")

    print(m1)