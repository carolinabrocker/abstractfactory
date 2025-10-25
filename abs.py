from abc import ABC, abstractmethod
import random

# ======== Abstract Products ========

class Herbivoro(ABC):
    @abstractmethod
    def comer_grama(self):
        pass


class Carnivoro(ABC):
    @abstractmethod
    def comer(self, herbivoro: Herbivoro):
        pass


# ======== Concrete Products (África) ========

class Gazela(Herbivoro):
    def comer_grama(self): print("Gazela come grama nas savanas africanas.")

class Zebra(Herbivoro):
    def comer_grama(self): print("Zebra pasta entre os leões atentos.")

class Elefante(Herbivoro):
    def comer_grama(self): print("Elefante arranca folhas das árvores.")

class Girafa(Herbivoro):
    def comer_grama(self): print("Girafa come folhas no alto das acácias.")

class Gnu(Herbivoro):
    def comer_grama(self): print("Gnu corre em manada e come grama seca.")


class Leao(Carnivoro):
    def comer(self, herbivoro: Herbivoro): print(f"Leão caça e come o {herbivoro.__class__.__name__}!")

class Hiena(Carnivoro):
    def comer(self, herbivoro: Herbivoro): print(f"Hiena rouba a presa e come o {herbivoro.__class__.__name__}!")

class Leopardo(Carnivoro):
    def comer(self, herbivoro: Herbivoro): print(f"Leopardo salta das árvores e devora o {herbivoro.__class__.__name__}!")

class Crocodilo(Carnivoro):
    def comer(self, herbivoro: Herbivoro): print(f"Crocodilo puxa o {herbivoro.__class__.__name__} para dentro do rio!")

class Guepardo(Carnivoro):
    def comer(self, herbivoro: Herbivoro): print(f"Guepardo corre mais rápido e pega o {herbivoro.__class__.__name__}!")


# ======== Concrete Products (América do Sul) ========

class Veado(Herbivoro):
    def comer_grama(self): print("Veado pasta nas florestas tropicais.")

class Capivara(Herbivoro):
    def comer_grama(self): print("Capivara come capim perto dos rios.")

class Lhama(Herbivoro):
    def comer_grama(self): print("Lhama se alimenta nas montanhas frias dos Andes.")

class Tatu(Herbivoro):
    def comer_grama(self): print("Tatu procura raízes e folhas no solo.")

class Tapir(Herbivoro):
    def comer_grama(self): print("Anta come frutas e folhas perto dos igarapés.")


class Onca(Carnivoro):
    def comer(self, herbivoro: Herbivoro): print(f"Onça embosca e come o {herbivoro.__class__.__name__}!")

class LoboGuara(Carnivoro):
    def comer(self, herbivoro: Herbivoro): print(f"Lobo-guará caça e come o {herbivoro.__class__.__name__}!")

class Jaguatirica(Carnivoro):
    def comer(self, herbivoro: Herbivoro): print(f"Jaguatirica caça silenciosamente o {herbivoro.__class__.__name__}!")

class Gavião(Carnivoro):
    def comer(self, herbivoro: Herbivoro): print(f"Gavião mergulha e pega o {herbivoro.__class__.__name__}!")

class Piranha(Carnivoro):
    def comer(self, herbivoro: Herbivoro): print(f"Piranha ataca em grupo e devora o {herbivoro.__class__.__name__}!")


# ======== Abstract Factory ========

class ContinenteFactory(ABC):
    @abstractmethod
    def criar_herbivoro(self) -> Herbivoro:
        pass

    @abstractmethod
    def criar_carnivoro(self) -> Carnivoro:
        pass


# ======== Concrete Factories ========

class AfricaFactory(ContinenteFactory):
    def __init__(self):
        self.herbivoros = [Gazela(), Zebra(), Elefante(), Girafa(), Gnu()]
        self.carnivoros = [Leao(), Hiena(), Leopardo(), Crocodilo(), Guepardo()]

    def criar_herbivoro(self) -> Herbivoro:
        return random.choice(self.herbivoros)

    def criar_carnivoro(self) -> Carnivoro:
        return random.choice(self.carnivoros)


class AmericaSulFactory(ContinenteFactory):
    def __init__(self):
        self.herbivoros = [Veado(), Capivara(), Lhama(), Tatu(), Tapir()]
        self.carnivoros = [Onca(), LoboGuara(), Jaguatirica(), Gavião(), Piranha()]

    def criar_herbivoro(self) -> Herbivoro:
        return random.choice(self.herbivoros)

    def criar_carnivoro(self) -> Carnivoro:
        return random.choice(self.carnivoros)


# ======== Client ========

class MundoAnimal:
    def __init__(self, factory: ContinenteFactory):
        self.factory = factory

    def cadeia_alimentar(self):
        herbivoro = self.factory.criar_herbivoro()
        carnivoro = self.factory.criar_carnivoro()
        herbivoro.comer_grama()
        carnivoro.comer(herbivoro)


# ======== Execução ========

if __name__ == "__main__":
    print("=== África ===")
    africa = MundoAnimal(AfricaFactory())
    for _ in range(3):
        africa.cadeia_alimentar()
        print()

    print("=== América do Sul ===")
    america_sul = MundoAnimal(AmericaSulFactory())
    for _ in range(3):
        america_sul.cadeia_alimentar()
        print()
