def elementos_distintos(numeros):
    diff_num = set()
    
    for num in numeros:
        # we return false in case of the set already contains the current element
        if num in diff_num:
            return False
        diff_num.add(num)
        
    return True


def convertir_celsius_a_fahrenheit(temperatura_celsius):
    # Se realiza la conversion de la temperatura
    temperatura_fahrenheit = (temperatura_celsius* 9 / 5) + 32
    
    # Luego ya se devuelve el valor recien calculado
    return temperatura_fahrenheit



def sumar_elementos(lista_numeros):

    return sum(lista_numeros)

def leer_archivo():
    archivo =  open("texto_ejemplo.txt", 'rt')
    datos = archivo.read()
    if 'AppExample583' in datos:
        print("El archivo contiene la cadena 'AppExample583'")
        open("texto_ejemplo2.txt", 'wt').write("AppExample583 Running")
    archivo.close()


class Pelicula:
    def __init__(self, titulo, director, ano):
        self.titulo = titulo
        self.director = director
        self.ano = ano

    def __str__(self):
        return f"{self.titulo} ({self.director}) - {self.ano}"
    

