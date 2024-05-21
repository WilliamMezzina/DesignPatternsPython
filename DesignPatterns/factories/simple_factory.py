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

class VeiculoFactory:
    @staticmethod
    def get_carro(tipo:str) -> Veiculo:
        if tipo == "luxo":
            return CarroLuxo()
        elif tipo == "popular":
            return CarroPopular()
        assert 0, "Veiculo não existe"


if __name__ == '__main__':
    carro1 = VeiculoFactory.get_carro("luxo")
    carro2 = VeiculoFactory.get_carro("popular")
    carro1.buscar_cliente()
    carro2.buscar_cliente()