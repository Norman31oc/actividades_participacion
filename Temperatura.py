from typing import List, Tuple

# Diccionario para convertir direcciones de viento a grados
wind_directions = {
    "N": 0, "NNE": 22.5, "NE": 45, "ENE": 67.5, "E": 90, "ESE": 112.5,
    "SE": 135, "SSE": 157.5, "S": 180, "SSW": 202.5, "SW": 225, "WSW": 247.5,
    "W": 270, "WNW": 292.5, "NW": 315, "NNW": 337.5
}

# funcoin convertir de grados a la dirección cardinal del viento
def grados_a_direccion(grados: float) -> str:
    closest_dir = min(wind_directions, key=lambda d: abs(wind_directions[d] - grados))
    return closest_dir

# Clase procesar los datos meteorológicos
class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo  # Guarda el nombre del archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        # Listas almacenar los valores de cada registro
        temperaturas = []
        humedades = []
        presiones = []
        velocidades_viento = []
        direcciones_viento = []

        # Abre archivo para leer los datos
        with open(self.nombre_archivo, 'r') as archivo:
            for linea in archivo:
                # Divide cada línea en partes separadas por espacios
                partes = linea.split()
                temperatura = float(partes[7])  # Extrae la temperatura
                humedad = float(partes[9])      # Extrae la humedad
                presion = float(partes[11])     # Extrae la presión
                velocidad_viento = float(partes[13].split(',')[0])  # Velocidad del viento
                direccion_viento = partes[13].split(',')[1]         # Dirección del viento

                # Agrega los valores a las listas correspondientes
                temperaturas.append(temperatura)
                humedades.append(humedad)
                presiones.append(presion)
                velocidades_viento.append(velocidad_viento)
                direcciones_viento.append(wind_directions[direccion_viento])

        # Calcula los promedios de temperatura, humedad, presión y velocidad del viento
        temperatura_promedio = sum(temperaturas) / len(temperaturas)
        humedad_promedio = sum(humedades) / len(humedades)
        presion_promedio = sum(presiones) / len(presiones)
        velocidad_promedio_viento = sum(velocidades_viento) / len(velocidades_viento)

        # Calcula el promedio de la dirección del viento en grados
        promedio_direccion_viento_grados = sum(direcciones_viento) / len(direcciones_viento)
        direccion_predominante = grados_a_direccion(promedio_direccion_viento_grados)

        # Devuelve los resultados como una tupla
        return temperatura_promedio, humedad_promedio, presion_promedio, velocidad_promedio_viento, direccion_predominante

        # Ejemplo de uso:
if __name__ == "__main__":
    datos = DatosMeteorologicos('datos.txt')  # Nombre del archivo con los datos
    resultados = datos.procesar_datos()       # Procesa los datos y obtiene las estadísticas
    print(f"Temperatura promedio: {resultados[0]:.2f}°C")
    print(f"Humedad promedio: {resultados[1]:.2f}%")
    print(f"Presión promedio: {resultados[2]:.2f} hPa")
    print(f"Velocidad promedio del viento: {resultados[3]:.2f} m/s")
    print(f"Dirección predominante del viento: {resultados[4]}")