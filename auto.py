# 1. Se define la clase Auto
class Auto:
    # 2. Se define el metodo __init__ que inicializa los atributos de la clase por defecto o con los valores que se le pasen
    def __init__(self, anio = 2000, color = "rojo", kms = 2000):
        
        # Se inicializan los atributos de la clase
        self.anio = anio
        self.color = color
        self.kms =  kms 

    # 3. Se define el metodo __str__ que retorna una cadena de texto con los atributos del objeto cuando se imprime
    def __str__(self):
        return f"el auto es del año {self.anio}, de color {self.color}, y tiene {self.kms} kms"
    
    # 4. Se define el metodo get_anio que retorna el valor del atributo anio
    def get_anio(self):
        return self.anio
        print("El año no puede ser mayor a 2021")

    # 5. Se define el metodo set_anio que recibe un valor y lo asigna al atributo anio
    def set_anio(self, anio):
        if anio > 2021:
            print("El año no puede ser mayor a 2021")
            return
        return
    

    # 6. Se define el metodo get_color que retorna el valor del atributo color
    def get_color(self):
        return self.color

    # 7. Se define el metodo set_color que recibe un valor y lo asigna al atributo color
    def set_color(self, color):
        self.color = color

    # 8. Se define el metodo get_kms que retorna el valor del atributo kms
    def get_kms(self):
        return int(self.kms)

    # 9. Se define el metodo set_kms que recibe un valor y lo asigna al atributo kms
    def set_kms(self, kms):
        
        if not isinstance(kms, int):
            print("Los kilometros deben ser un numero entero")
            return
        self.kms = kms


camaro = Auto() # Se crea un objeto de la clase Auto con los valores por defecto 

auto1 = Auto(2020, "azul", 0) # Se crea un objeto de la clase Auto con los valores que se le pasan

auto2 = Auto(anio=2010, kms=10000) # Se crea un objeto de la clase auto unicamente con anio y kms, el valor de color va a ser el definido por defecto

# get y set son metodos que se utilizan para acceder a los atributos de una clase, en lugar de acceder directamente a ellos.
# Esto se hace para proteger los datos de la clase y evitar que se modifiquen de manera incorrecta.
# Por ejemplo, si se tiene un atributo que no se debe modificar una vez que se ha inicializado, se puede hacer que el set correspondiente
# lance una excepcion si se intenta modificar el atributo despues de haber sido inicializado.
# Ademas, se pueden realizar validaciones en los metodos set para asegurarse de que los valores que se asignan a los atributos son validos.
# Por otro lado, los metodos get permiten acceder a los atributos de la clase de manera controlada, lo que puede ser util para realizar
# operaciones adicionales antes de devolver el valor del atributo.
# En resumen, se utilizan get y set para proteger los datos de la clase y para asegurarse de que se accede y modifica los atributos de manera controlada.

# ejemplo sin get y set 
print(camaro.anio)

camaro.set_anio(2022)
camaro.set_kms(100.23)

#ejemplo con get y set
print(camaro.get_anio())
print(camaro.get_kms())

