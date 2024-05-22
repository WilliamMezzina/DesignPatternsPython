from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass

class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro de luxo buscando cliente")

class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro popular buscando cliente")

class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Moto popular buscando cliente")

class VeiculoFactory(ABC):
    def __init__(self, tipo) -> None:
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo:str) -> Veiculo:
        pass
    
    def buscar_cliente(self):
        self.carro.buscar_cliente()

class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo:str) -> Veiculo:
        if tipo == "luxo":
            return CarroLuxo()
        elif tipo == "popular":
            return CarroPopular()
        elif tipo == "moto":
            return MotoPopular()
        assert 0, "Veiculo não existe"

class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo:str) -> Veiculo:
        if tipo == "popular":
            return CarroPopular()
        assert 0, "Veiculo não existe"

if __name__ == '__main__':
    carro1 = ZonaSulVeiculoFactory.get_carro("luxo")
    carro2 = ZonaNorteVeiculoFactory.get_carro("popular")
    carro1.buscar_cliente()
    carro2.buscar_cliente()