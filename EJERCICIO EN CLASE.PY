

#FUNCION USADA PARA CONVERTIR 

def convertir_temperaturas(grados_celsius):
    fahrenheit = (9/5) * grados_celsius + 32 #Convierte la temperatura de Celsius a Fahrenheit usando la fórmula estándar.
    kelvin = grados_celsius + 273.15
    return fahrenheit, kelvin

# PEDIMOS POR CONSOLA 
grados_celsius = float(input("Por favor, ingresa la temperatura en grados Celsius: "))#ALMACENAMOS EN LA VARIABLE  FLOTANTE  LOS DATOS INGRESADOS POR EL USUARIO
fahrenheit, kelvin = convertir_temperaturas(grados_celsius)

print(f"{grados_celsius} grados Celsius son {fahrenheit} grados Fahrenheit y {kelvin} grados Kelvin.")#IMPRIMIMOS LOS 2

