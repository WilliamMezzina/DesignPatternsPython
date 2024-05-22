"""
Esse modelo chama o __init__ sempre que a classe é "instanciada"
"""

class AppSettings:
    _instance = None

    def  __new__(cls, *arg, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *arg, **kwargs)
        
        return cls._instance
    
    def __init__(self):
        print("OI")

if __name__ == '__main__':
    as1 = AppSettings()
    as2 = AppSettings()

    print(as1)
    print(as2)