from abc import ABC

# Superclase.
class SignoZodiacal(ABC):

    _signoZodiacal = str(" ")
    _mesNacimiento = int(0)
    _diaNacimiento = int(0)

    # Metodo constructor de la superclase.
    def __init__(self, mesNacimiento, diaNacimiento):
        self._mesNacimiento = mesNacimiento
        self._diaNacimiento = diaNacimiento

    @staticmethod
    def identificarSignoZodiacal(self):
        pass

    @staticmethod
    def getSignoZodiacal(self):
        pass
    
# Clase derivada.
class SignoZodiacalOccidental(SignoZodiacal):

    # Constructor.
    def __init__(self, mesNacimiento, diaNacimiento):
        SignoZodiacal.__init__(self, mesNacimiento, diaNacimiento)
        self.identificarSignoZodiacal()

    # Metodo heredado.
    def identificarSignoZodiacal(self):
        if (self._mesNacimiento == 12 and self._diaNacimiento >= 22) or (self._mesNacimiento == 1 and self._diaNacimiento <= 20):
            self._signoZodiacal = 'Capricornio'
        elif (self._mesNacimiento == 1) or (self._mesNacimiento == 2 and self._diaNacimiento <= 19):
            self._signoZodiacal = 'Acuario'
        elif (self._mesNacimiento == 2) or (self._mesNacimiento == 3 and self._diaNacimiento <= 20):
            self._signoZodiacal = 'Piscis'
        elif (self._mesNacimiento == 3) or (self._mesNacimiento == 4 and self._diaNacimiento <= 20):
            self._signoZodiacal = 'Aries'
        elif (self._mesNacimiento == 4) or (self._mesNacimiento == 5 and self._diaNacimiento <= 20):
            self._signoZodiacal = 'Tauro'
        elif (self._mesNacimiento == 5) or (self._mesNacimiento == 6 and self._diaNacimiento <= 21):
            self._signoZodiacal = 'Géminis'
        elif (self._mesNacimiento == 6) or (self._mesNacimiento == 7 and self._diaNacimiento <= 22):
            self._signoZodiacal = 'Cáncer'
        elif (self._mesNacimiento == 7) or (self._mesNacimiento == 8 and self._diaNacimiento <= 23):
            self._signoZodiacal = 'Leo'
        elif (self._mesNacimiento == 8) or (self._mesNacimiento == 9 and self._diaNacimiento <= 22):
            self._signoZodiacal = 'Virgo'
        elif (self._mesNacimiento == 9) or (self._mesNacimiento == 10 and self._diaNacimiento <= 22):
            self._signoZodiacal = 'Libra'
        elif (self._mesNacimiento == 10) or (self._mesNacimiento == 11 and self._diaNacimiento <= 22):
            self._signoZodiacal = 'Escorpio'
        else:
            self._signoZodiacal = 'Sagitario'

    # Metodo heredado.
    def getSignoZodiacal(self):
        return self._signoZodiacal

# Clase derivada.
class SignoZodiacalChino(SignoZodiacal):

    __anioNacimiento = int(0)

    # Constructor.
    def __init__(self, anioNacimiento, mesNacimiento, diaNacimiento):
        SignoZodiacal.__init__(self, mesNacimiento, diaNacimiento)
        self.__anioNacimiento = anioNacimiento
        self.identificarSignoZodiacal()

    # Metodo heredado.
    def identificarSignoZodiacal(self):
        if (self.__anioNacimiento == 1924) or (self.__anioNacimiento == 1936) or (self.__anioNacimiento == 1948) or (self.__anioNacimiento == 1960) or (self.__anioNacimiento == 1972) or (self.__anioNacimiento == 1984) or (self.__anioNacimiento == 1996) or (self.__anioNacimiento == 2008) or (self.__anioNacimiento == 2020):
            self._signoZodiacal = "Rata"
        elif (self.__anioNacimiento == 1925) or (self.__anioNacimiento == 1937) or (self.__anioNacimiento == 1949) or (self.__anioNacimiento == 1961) or (self.__anioNacimiento == 1973) or (self.__anioNacimiento == 1985) or (self.__anioNacimiento == 1997) or (self.__anioNacimiento == 2009) or (self.__anioNacimiento == 2021):
            self._signoZodiacal = "Buey"
        elif (self.__anioNacimiento == 1926) or (self.__anioNacimiento == 1938) or (self.__anioNacimiento == 1950) or (self.__anioNacimiento == 1962) or (self.__anioNacimiento == 1974) or (self.__anioNacimiento == 1986) or (self.__anioNacimiento == 1998) or (self.__anioNacimiento == 2010) or (self.__anioNacimiento == 2022):
            self._signoZodiacal = "Tigre"
        elif (self.__anioNacimiento == 1927) or (self.__anioNacimiento == 1939) or (self.__anioNacimiento == 1951) or (self.__anioNacimiento == 1963) or (self.__anioNacimiento == 1975) or (self.__anioNacimiento == 1987) or (self.__anioNacimiento == 1999) or (self.__anioNacimiento == 2011) or (self.__anioNacimiento == 2023):
            self._signoZodiacal = "Conejo"
        elif (self.__anioNacimiento == 1928) or (self.__anioNacimiento == 1940) or (self.__anioNacimiento == 1952) or (self.__anioNacimiento == 1964) or (self.__anioNacimiento == 1976) or (self.__anioNacimiento == 1988) or (self.__anioNacimiento == 2000) or (self.__anioNacimiento == 2012) or (self.__anioNacimiento == 2024):
            self._signoZodiacal = "Dragon"
        elif (self.__anioNacimiento == 1929) or (self.__anioNacimiento == 1941) or (self.__anioNacimiento == 1953) or (self.__anioNacimiento == 1965) or (self.__anioNacimiento == 1977) or (self.__anioNacimiento == 1989) or (self.__anioNacimiento == 2001) or (self.__anioNacimiento == 2013) or (self.__anioNacimiento == 2025):
            self._signoZodiacal = "Serpiente"
        elif (self.__anioNacimiento == 1930) or (self.__anioNacimiento == 1942) or (self.__anioNacimiento == 1954) or (self.__anioNacimiento == 1966) or (self.__anioNacimiento == 1978) or (self.__anioNacimiento == 1990) or (self.__anioNacimiento == 2002) or (self.__anioNacimiento == 2014) or (self.__anioNacimiento == 2026):
            self._signoZodiacal = "Caballo"
        elif (self.__anioNacimiento == 1931) or (self.__anioNacimiento == 1943) or (self.__anioNacimiento == 1955) or (self.__anioNacimiento == 1967) or (self.__anioNacimiento == 1979) or (self.__anioNacimiento == 1991) or (self.__anioNacimiento == 2003) or (self.__anioNacimiento == 2015) or (self.__anioNacimiento == 2027):
            self._signoZodiacal = "Cabra"
        elif (self.__anioNacimiento == 1932) or (self.__anioNacimiento == 1944) or (self.__anioNacimiento == 1956) or (self.__anioNacimiento == 1968) or (self.__anioNacimiento == 1980) or (self.__anioNacimiento == 1992) or (self.__anioNacimiento == 2004) or (self.__anioNacimiento == 2016) or (self.__anioNacimiento == 2028):
            self._signoZodiacal = "Mono"
        elif (self.__anioNacimiento == 1933) or (self.__anioNacimiento == 1945) or (self.__anioNacimiento == 1957) or (self.__anioNacimiento == 1969) or (self.__anioNacimiento == 1981) or (self.__anioNacimiento == 1993) or (self.__anioNacimiento == 2005) or (self.__anioNacimiento == 2017) or (self.__anioNacimiento == 2029):
            self._signoZodiacal = "Gallo"
        elif (self.__anioNacimiento == 1934) or (self.__anioNacimiento == 1946) or (self.__anioNacimiento == 1958) or (self.__anioNacimiento == 1970) or (self.__anioNacimiento == 1982) or (self.__anioNacimiento == 1994) or (self.__anioNacimiento == 2006) or (self.__anioNacimiento == 2018) or (self.__anioNacimiento == 2030):
            self._signoZodiacal = "Perro"
        else:
            self._signoZodiacal = "Cerdo"

    # Metodo heredado.
    def getSignoZodiacal(self):
        return self._signoZodiacal

# Clase derivada.
class SignoZodiacalMaya(SignoZodiacal):

    # Constructor.
    def __init__(self, mesNacimiento, diaNacimiento):
        SignoZodiacal.__init__(self, mesNacimiento, diaNacimiento)
        self.identificarSignoZodiacal()

    # Metodo heredado.
    def identificarSignoZodiacal(self):
        if (self._mesNacimiento == 12 and self._diaNacimiento >= 13) or (self._mesNacimiento == 1 and self._diaNacimiento <= 9):
            self._signoZodiacal = 'Lagarto'
        elif (self._mesNacimiento == 1) or (self._mesNacimiento == 2 and self._diaNacimiento <= 6):
            self._signoZodiacal = 'Mono'
        elif (self._mesNacimiento == 2) or (self._mesNacimiento == 3 and self._diaNacimiento <= 6):
            self._signoZodiacal = 'Halcón'
        elif (self._mesNacimiento == 3) or (self._mesNacimiento == 4 and self._diaNacimiento <= 3):
            self._signoZodiacal = 'Jaguar'
        elif (self._mesNacimiento == 4) or (self._mesNacimiento == 5 and self._diaNacimiento <= 1):
            self._signoZodiacal = 'Perro/Zorro'
        elif (self._mesNacimiento == 5) and (self._diaNacimiento >= 2) and (self._diaNacimiento <= 29):
            self._signoZodiacal = 'Serpiente'
        elif (self._mesNacimiento == 5) or (self._mesNacimiento == 6 and self._diaNacimiento <= 26):
            self._signoZodiacal = 'Conejo/Ardilla'
        elif (self._mesNacimiento == 6) or (self._mesNacimiento == 7 and self._diaNacimiento <= 25):
            self._signoZodiacal = 'Tortuga'
        elif (self._mesNacimiento == 7) or (self._mesNacimiento == 8 and self._diaNacimiento <= 22):
            self._signoZodiacal = 'Murciélago'
        elif (self._mesNacimiento == 8) or (self._mesNacimiento == 9 and self._diaNacimiento <= 19):
            self._signoZodiacal = 'Escorpión'
        elif (self._mesNacimiento == 9) or (self._mesNacimiento == 10 and self._diaNacimiento <= 17):
            self._signoZodiacal = 'Venado'
        elif (self._mesNacimiento == 10) or (self._mesNacimiento == 11 and self._diaNacimiento <= 14):
            self._signoZodiacal = 'Búho/Lechuza'
        else:
            self._signoZodiacal = 'Pavo real'

    # Metodo heredado.
    def getSignoZodiacal(self):
        return self._signoZodiacal

# Clase derivada.
class SignoZodiacalEgipcio(SignoZodiacal):

    # Constructor.
    def __init__(self, mesNacimiento, diaNacimiento):
        SignoZodiacal.__init__(self, mesNacimiento, diaNacimiento)
        self.identificarSignoZodiacal()

    # Metodo heredado.
    def identificarSignoZodiacal(self):
        if (self._mesNacimiento == 12 and self._diaNacimiento >= 16) or (self._mesNacimiento == 1 and self._diaNacimiento <= 15):
            self._signoZodiacal = 'Hijo de Anubis'
        elif (self._mesNacimiento == 1) or (self._mesNacimiento == 2 and self._diaNacimiento <= 15):
            self._signoZodiacal = 'Hijo de Bastet'
        elif (self._mesNacimiento == 2) or (self._mesNacimiento == 3 and self._diaNacimiento <= 15):
            self._signoZodiacal = 'Hijo de Selket'
        elif (self._mesNacimiento == 3) or (self._mesNacimiento == 4 and self._diaNacimiento <= 15):
            self._signoZodiacal = 'Hijo de Apep'
        elif (self._mesNacimiento == 4) or (self._mesNacimiento == 5 and self._diaNacimiento <= 15):
            self._signoZodiacal = 'Hijo de Ptah'
        elif (self._mesNacimiento == 5) or (self._mesNacimiento == 6 and self._diaNacimiento <= 15):
            self._signoZodiacal = 'Hijo de Atum'
        elif (self._mesNacimiento == 6) or (self._mesNacimiento == 7 and self._diaNacimiento <= 15):
            self._signoZodiacal = 'Hijo de Isis'
        elif (self._mesNacimiento == 7) or (self._mesNacimiento == 8 and self._diaNacimiento <= 15):
            self._signoZodiacal = 'Hijo de Ra'
        elif (self._mesNacimiento == 8) or (self._mesNacimiento == 9 and self._diaNacimiento <= 15):
            self._signoZodiacal = 'Hijo de Horus'
        elif (self._mesNacimiento == 9) or (self._mesNacimiento == 10 and self._diaNacimiento <= 15):
            self._signoZodiacal = 'Hijo de Maat'
        elif (self._mesNacimiento == 10) or (self._mesNacimiento == 11 and self._diaNacimiento <= 15):
            self._signoZodiacal = 'Hijo de Osiris'
        else:
            self._signoZodiacal = 'Hijo de Hathor'

    # Metodo heredado.
    def getSignoZodiacal(self):
        return self._signoZodiacal


class Main:
    if __name__ == "__main__":
        # Instancia de la clase hija SignoZodiacalOccidental.
        signoO = SignoZodiacalOccidental(7, 27)
        print(signoO.getSignoZodiacal())

        # Instancia de la clase hija SignoZodiacalChino
        signoC = SignoZodiacalChino(2003, 7, 27)
        print(signoC.getSignoZodiacal())

        # Instancia de la clase hija SignoZodiacalMaya.
        signoM = SignoZodiacalMaya(7, 27)
        print(signoM.getSignoZodiacal())

        # Instancia de la clase hija SignoZodiacalEgipcio.
        signoE = SignoZodiacalEgipcio(7, 27)
        print(signoE.getSignoZodiacal())
