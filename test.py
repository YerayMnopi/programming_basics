### TABLA MULTIPLICAR ###

# input recibe el número como cadena de textopor eso usamos int para convertirlo a numero
numero = int(input("Dime un número"))

print(f"La tabla de multiplicar del {numero} es:")

# range nos genera una secuencia de números, empezando desde 0,
# y terminando en el numero que pasemos menos 1.
# range(x) = [0, 1, 2, ..., x-1]
for multiplicador in range(11):
    # con for y in range(x) podemos recorrer en bucle la secuencia generada
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")


### FUNCIONES ###
# Las funciones son una forma de reutilizar una lógica.
# Las funciones conviene que sean pequeñas y que tenga un único
# propósito
# Si una función se hace muy grande ( > 40 lineas) la puedes partir en funciones mas
# pequeñas
# Siguiendo el ejemplo anterior, podemos meter en una funcion el codigo
# que genera la tabla de multiplicar, y asi lo podemos reutilizar para varios numeros

print("Dime dos numeros")
numero_1 = int(input("Primer numero"))
numero_2 = int(input("Segundo numero"))


def generar_tabla_multiplicar(numero):
    print(f"La tabla de multiplicar del {numero} es:")
    for multiplicador in range(11):
        print(f"{numero} x {multiplicador} = {numero * multiplicador}")


generar_tabla_multiplicar(numero_1)
generar_tabla_multiplicar(numero_2)

### Scope / entornos ###
# Los ficheros son considerados módulos.
# Dentro de los módulos pueden a su vez haber variables, funciones, clases
# Las funciones y las clases tiene su propio scope.
# Por eso el ejemplo de "cajas" dentro de "cajas".
# Siempre existe un scope o entorno global y otro local
# Si declaras dos variables con el mismo nombre fuera y dentro de un scope
# la del scope más concreto tiene prevalencia


# -> Inicio scope del modulo
nombre = "Adrián"  # variable nombre del scope GLOBAL / modulo


def funcion_con_variable_nombre():
    # -> inicio scope de la funcion con variable nombre
    nombre = "Mari Carmen"
    print(nombre)
    # <- fin scope de la funcion con variable nombre


def funcion_sin_variable_nombre():
    # -> inicio scope de la funcion sin variable nombre
    print(nombre)
    # <- fin scope de la funcion con variable nombre


funcion_con_variable_nombre()  # esta debe imprimir Mari Carmen
funcion_sin_variable_nombre()  # Esta debe imprimir Adrián
# <- fin scope del modulo


### CLASES ###
# Las clases permiten encapsular (crear un scope o entorno) para guardar
# datos y lógica que se usan en conjunto.
# Los datos de una clase se llaman atributos
# La lógica de una clase se escribe en métodos. Se diferencian de las
# funciones normales porque están dentro de una clase y siempre reciben
# como primer parámetro la instancia de la clase mediante el keyword "self"

# Las clases se escriben en CamelCase y las funciones y variables en snake_case


class Persona:
    nombre: str

    def __init__(self, nombre):
        self.nombre = nombre

    def saludo(self):
        print(self.nombre, "dice: Hola!")


adrian_morales = Persona("Adrián")
valle = Persona("Valle")
adrian_morales.saludo()
valle.saludo()
print(nombre)
print("primero")


### TIPOS ###
# Python es un lenguage dinamico que no requiere
# declarar tipos como java. Eso no quiere decir que no los tenga
# Puedes declarar los tipos si quieres. Son útiles para
# que python te chive si te equivocas.


class SalaryCalculator:
    MIN_HOUR_RATE: int = 8
    EXTRA_HOUR_RATE: int = 1.5
    MAX_WORK_HOURS: int = 60
    STANDARD_WORKING_HOURS: int = 40

    def __init__(self, hourly_rate: int):
        assert hourly_rate >= self.MIN_HOUR_RATE
        self.hourly_rate = hourly_rate

    def calculate(self, hours) -> int:
        return hours * self.hourly_rate


### TESTING ###
# Los test unitarios son funciones que comprueban
# que tu codigo funciona.
# Le pasamos muchos casos donde sabemos el resultado esperado
# y comprobamos que el codigo hace lo que debe.


def test_calculator_works():
    calculator = SalaryCalculator(40)
    result = calculator.calculate(40)

    print(result)

    # ASSERT es un comando de python que asegura que una condicion se cumple
    # si no se cumple, levanta una excepcion
    assert result == 1600, "La calculadora no funciona bien"

    print("La calculadora funciona")


def test_calculator_ensures_min_hours():
    try:
        SalaryCalculator(3)
    except Exception:
        print("La comprobacion de precio por hora minimo SÍ funciona bien")
        return
    print("La comprobacion de precio por hora minimo NO funciona bien")


test_calculator_works()
test_calculator_ensures_min_hours()


# DEBUGGING
# Debugear te sirve para entender como se está ejecutando un programa:
# - el orden que sigue
# - los valores de las variables en cada punto de ruptura
# Puedes debuggear con VS Code lanzado el fichero con el simbolo del bicho
# y poniendo puntos de ruptura en las lineas donde quieres que se pare.
# Puedes ir linea por linea viendo como funciona el programa.
