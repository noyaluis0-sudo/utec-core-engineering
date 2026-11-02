El polimorfismo en Python es la capacidad de que diferentes objetos respondan a la misma
Polimorfismo con herencia (sobrescritura de métodos):
Las clases hijas heredan de una clase padre y pueden redefinir (sobrescribir) un método con el mismo nombre, adaptándolo a su propia lógica.python
class Perro:
    def hablar(self):
        print("Guau!")

class Gato:
    def hablar(self):
        print("Miau!")

def hacer_hablar(animal):
    animal.hablar()

hacer_hablar(Perro())  # Imprime: Guau!
hacer_hablar(Gato())   # Imprime: Miau!
