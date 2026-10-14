class LingottoFiere:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome


    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO



class Espositore:
    def __init__(self):
        self.__codice = ""
        self.__nom = ""
        self.__cognome = ""

    @property
    def codice(self):
        return self.__codice

    @codice.setter
    def codice(self,codice):
        self.__codice = codice

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def cognome(self):
        return self.__cognome

    @cognome.setter
    def cognome(self, cognome):
        self.__cognome = cognome



class Stand:

    def __init__(self):
        self.__codice = ""
        self.__superfice = 0
        self.__padiglione = 0
        self.__prezzo = 0

    @property
    def codice(self):
        return self.__codice

    @codice.setter
    def codice(self,codice):
        self.__codice = codice

    @property
    def superfice(self):
        return self.__superfice

    @superfice.setter
    def superfice(self, superfice):
        self.__superfice = superfice

    @property
    def padiglione(self):
        return self.__padiglione

    @padiglione.setter
    def padiglione(self, padiglione):
        self.__padiglione = padiglione

    @property
    def prezzo(self):
        return self.__prezzo

    @prezzo.setter
    def prezzo(self, prezzo):
        self.__prezzo = prezzo


class StandElettrico(Stand):
    def __init__(self):
        super().__init__()
        self.__codice = ""
        self.__superfice = 0
        self.__padiglione = 0
        self.__prezzo = 0
        self.__prese = 0


    @property
    def codice(self):
        return self.__codice

    @codice.setter
    def codice(self,codice):
        self.__codice = codice

    @property
    def superfice(self):
        return self.__superfice

    @superfice.setter
    def superfice(self, superfice):
        self.__superfice = superfice

    @property
    def padiglione(self):
        return self.__padiglione

    @padiglione.setter
    def padiglione(self, padiglione):
        self.__padiglione = padiglione

    @property
    def prezzo(self):
        return self.__prezzo

    @prezzo.setter
    def prezzo(self, prezzo):
        self.__prezzo = prezzo


    @property
    def prese(self):
        return self.__prese

    @prese.setter
    def prese(self,prese):
        self.__prese = prese



class Premium(Stand):
    def __init__(self):
        super().__init__()
        self.__codice = ""
        self.__superfice = 0
        self.__padiglione = 0
        self.__prezzo = 0
        self.__posizione = 0

    @property
    def codice(self):
        return self.__codice

    @codice.setter
    def codice(self,codice):
        self.__codice = codice

    @property
    def superfice(self):
        return self.__superfice

    @superfice.setter
    def superfice(self, superfice):
        self.__superfice = superfice

    @property
    def padiglione(self):
        return self.__padiglione

    @padiglione.setter
    def padiglione(self, padiglione):
        self.__padiglione = padiglione

    @property
    def prezzo(self):
        return self.__prezzo

    @prezzo.setter
    def prezzo(self, prezzo):
        self.__prezzo = prezzo


    @property
    def posizione(self):
        return self.__posizione

    @posizione.setter
    def posizione(self,posizione):
        self.__posizione = posizione