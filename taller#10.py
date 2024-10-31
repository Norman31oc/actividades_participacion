
from abc import ABC, abstractclassmethod

clave = input("Ingresa la Clave: ")

class Regla_Validacion(ABC):

    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def es_valida(self, clave):
        pass

    def _validar_longitud(self, clave):
        return len(clave) < self._longitud_esperada
    
    def _contiene_minusculas (self, clave):
        return any (c.isupper() for c in clave )
    
    def _contiene_mayusculas (self, clave):
        return any (c.islower() for c in clave)

    def _contine_numero (self, clave):
        return any (c.isdigit() for c in clave)
    
class ReglaValidacionDanimedes(Regla_Validacion):

    def __init__(self):
        super().__init__(8) 
    
    def _contiene_caracteres_especiales(self, clave):
    	caracteres_especiales =  '@_#$%'
        return any (c in caracteres_especiales for c in clave)

    
    def es_valida(self, clave):
        if not self._validar_longitud(clave):

            raise ValueError("La clave debe de tener mas de 8 caracteres. ")
        
        if not self._contiene_mayusculas(clave):
            raise ValueError("La clave debe de tener minimo una letra mayuscula. ")

        if not self._contiene_minusculas(clave):
            raise ValueError("La clave debe de tener minimo una letra minuscula. ")   
        
        if not self._contine_numero(clave):
            raise ValueError("La clave debe de tener almenos un numero. ")
        
        if not self._contiene_caracteres_especiales(clave):
            raise ValueError("La clave debe de tener almenos un caracter epecial. ")
        return True
    
class ReglaValidacionCalisto (Regla_Validacion):
    def __init__(self,):
        super().__init__(6)

    def contiene_calisto(self, clave):
        calisto = 'calisto'
        count_mayusculas = sum (1 for c in calisto if c.isupper())
        if count_mayusculas < 2 or count_mayusculas == len(calisto):
            return False
        return calisto in clave.lower()
    
    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise ValueError("La clave debe de tener mas de 6 caracteres ")
        
        if not self._contine_numero(clave):
            raise ValueError("La clave debe de tener almenos un numero ")

        if not self._validar_calisto(clave):
            raise ValueError("La clave debe de tener la palabra 'calisto' con al menos dos letras en mayúscula, pero no todas")
        return True
    
class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self, clave):
        return self.regla.es_valida(clave)
    
class LongitudInvalidaError(Exception):
    pass

class MayusculaInvalidaError(Exception):
    pass

class MinusculaInvalidaError(Exception):
    pass

class NumeroInvalidoError(Exception):
    pass

class CaracterEspecialInvalidoError(Exception):
    pass

class CalistoInvalidoError(Exception):
    pass

def es_valida(self, clave):
    if not self._validar_longitud(clave):
        raise LongitudInvalidaError("La clave debe tener más de 8 caracteres.")
    if not self._contiene_mayuscula(clave):
        raise MayusculaInvalidaError("La clave debe contener al menos una letra mayúscula.")
    if not self._contiene_minuscula(clave):
        raise MinusculaInvalidaError("La clave debe contener al menos una letra minúscula.")
    if not self._contiene_numero(clave):
        raise NumeroInvalidoError("La clave debe contener al menos un número.")
    if not self.contiene_caracter_especial(clave):
        raise CaracterEspecialInvalidoError("La clave debe contener al menos un caracter especial (@, _, #, $, %).")
    return True

    pytest