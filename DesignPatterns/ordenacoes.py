"""
ordem dos chamados de dunder method
"""

class Meta(type):
    def __call__(cls, *args, **kwargs):
        print("Call meta chamado")
        super().__call__(*args, **kwargs)

class Pessoa(metaclass=Meta):    
    def __new__(cls, *args, **kwargs):
        print("NEW")
        return super().__new__(cls)

    def __init__(self, nome):
        print("INIT")
        self.nome = nome

    def __call__(self):
        print("Call chamado")

if __name__ == '__main__':
    p1 = Pessoa("William")