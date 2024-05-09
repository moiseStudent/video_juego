"""
Juego para practicar los temas visto de poo y solid
"""
import time
from abc import ABC, abstractclassmethod

class Weapon(ABC):

    def __init__(self, name, damage):

        self.__name = name
        self.__damage = damage

    @abstractclassmethod
    def name(self):
        return self.__name
    
    @abstractclassmethod
    def get_damage(self):
        return self.__damage
    
    @abstractclassmethod
    def describe(self) -> str:
        return f'Nombre: {self.__name}, daño: {self.__damage}'

### Golpear con el punio ###
class Fist(Weapon):

    def __init__(self, name='puño', damage=3):
        super().__init__(name, damage)
    
    @property
    def name(self):
        return self._Weapon__name
    
    def get_damage(self) -> int:
        print(self._Weapon__damage)
        return self._Weapon__damage
    
    def describe(self) -> str:
        return f'Nombre: {self.name}, daño: {self.get_damage()}%'

    # Golpear con los puños #
    def hit_with_fist(self):
        pass

### Espada ###
class Sword(Weapon):

    def __init__(self, name, damage):
        super().__init__(name, damage)

    @property
    def name(self):
        return self._Weapon__name
    
    def get_damage(self):
        return self._Weapon__damage
    
    def describe(self) -> str:
        return f'Nombre: {self.name}, daño: {self.get_damage()}%'
    
    

### Personajes ###
class Character:

    def __init__(self, name, stroke):

        self.__name = name
        self.__stroke = stroke
        self.__life = 100
        self.__weapon = None
    
    @property
    def name(self):
        return self.__name
    
    ### Representacion str del obj ###
    def __repr__(self) -> str:
        ### Comprobar que el decimal sea distinto de cero ###
        if self.__life % 1 == 0:
            return f'{self.__name}(daño: {self.__stroke}, vida: {self.__life})'
        
        else:
            return f'{self.__name}(daño: {self.__stroke}, vida: {self.__life:.1f})'
    
    ### Equipar arma ###
    def equip_weapon(self, weapon):
        self.__weapon = weapon

    """
    Encapsulada para no ser usada fuera de la clase, sera usada por un
    metodo interno en la clase.
    """
    def __attack(self):
        if self.__weapon:
            return self.__stroke + self.__weapon.get_damage()
        else:
            return self.__stroke
    
    """
    Funcion: Recibir el danio, parametro damage se resta a la vida de
    la victima.
    """
    def take_damage(self, damage):
        self.__life -= damage

        if self.__life <= 0 :
            return f'El peleador: {self.__name} ha muerto.'
        
        elif self.__life > 0:
            return f'Vida restante de {self.name}: {self.__life}'
    
    ### Hacer ataque ###
    def perform_attack(self, victim):
        damage_dealt = self.__attack() ### daño causado ###

        print(f"""El peleador: {self.__name} ha atacado a {victim.name} con un/a 
              {self.__weapon.name} ataque: {damage_dealt}pts""")
        print(victim.take_damage(damage_dealt))


### Crear Espada ###
sword = Sword('Espada', 5)

### Default weapong ###
hand = Fist()
### Personajes ###
mitnik = Character('Mitnik', stroke = 100.1)
moises = Character('Moises', stroke = 10.2)


mitnik.equip_weapon(hand)
moises.equip_weapon(hand)

moises.take_damage(34)

mitnik.perform_attack(moises)
moises.perform_attack(mitnik)




print(mitnik) # Estados #
print(moises) # Estados #
 
# Equipar armas, parametro: el arma a equipar#
#mitnik.equip_weapon(sword)

# Ejecutar el ataque
#mitnik.perform_attack(moises)

print(mitnik) # Estados #
print(moises) # Estados #
"""
while True:
    
    print(""'
          .: Simulator fight:.
1. Jugar vs pc
2. jugar vs amigo
3. salir
""')
    
    try:
        option = int(input('select option -> '))

        if option == 1:
            print('Jugando con pc')
            time.sleep(2)
        
        elif option == 2:
            print('Jugando con amigo')
            time.sleep(2)
        
        elif option == 3:
            print('Saliendo del juego, gracias por jugar...')
            time.sleep(1)
            break
    
    except ValueError:
        print('Error: Opcion invalida !')

"""
"""
Implentaciones: 

Añadir Funciones de Personajes:

Implementa funciones específicas para cada personaje, como habilidades especiales o movimientos únicos.
Más Interacción de Usuario:

Mejora la interfaz de usuario permitiendo a los usuarios elegir acciones y ver resultados de manera más interactiva.
Clases de Armas Adicionales:

Crea más clases de armas con diferentes estadísticas y efectos para proporcionar variedad en el juego.
Sistema de Niveles:

Implementa un sistema de niveles para los personajes, donde ganan experiencia y mejoran sus habilidades con el tiempo.
Combates en Turnos:

Cambia el sistema de combate a un formato por turnos, donde los jugadores eligen acciones para cada turno.
Persistencia de Datos:

Permite a los jugadores guardar y cargar partidas, manteniendo la progresión de sus personajes.
Pantalla de Estado:

Crea una pantalla de estado que muestre la información clave de cada personaje, como vida, poder y nivel.
Mejora la Lógica de Combate:

Implementa una lógica de combate más avanzada que tenga en cuenta las estadísticas y habilidades de los personajes.
Efectos de Sonido y Gráficos:

Agrega efectos de sonido y gráficos para mejorar la experiencia del juego.
Menús de Opciones:

Crea menús de opciones que permitan a los jugadores personalizar su experiencia, como ajustar la dificultad o cambiar configuraciones.
Historia y Misiones:

Introduce una trama y misiones para darle un contexto narrativo al juego.

PODER HACER QUE CIERTOS PERSONAJE SE FUSIONEN PARA HACER UNO MAS PODEROSO
"""
s