class LingottoFiere:
    def __init__(self, nome):
        self.__nome = nome
        self.__lista = []
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome


    def carica_file_dati(self, file_path):
        with open(file_path,"r") as inp:
            try:
                for riga in inp:
                    s = Stand()
                    e = Espositore()
                    p = Premium()
                    pres = StandElettrico

                    campi = riga.strip().split(",")
                    if len(campi) == 3:
                        e.codice = campi[0]
                        e.nom = campi[1]
                        e.cognome = campi[2]
                        self.__lista.append(e)

                    elif len(campi) == 4:
                        s.codice = campi[0]
                        s.superfice = campi[1]
                        s.padiglione = campi[2]
                        s.prezzo = campi[3]
                        self.__lista.append(s)

                    elif len(campi) == 5:
                        if campi[-1].isdigit():
                            pres.codice = campi[0]
                            pres.superfice = campi[1]
                            pres.padiglione = campi[2]
                            pres.prezzo = campi[3]
                            pres.prese = campi[4]
                            self.__lista.append(pres)

                        elif campi[-1].isalpha():
                            p.codice = campi[0]
                            p.superfice = campi[1]
                            p.padiglione = campi[2]
                            p.prezzo = campi[3]
                            p.posizione = campi[4]
                            self.__lista.append(p)

            except FileNotFoundError:
                print("Errore apertura file")

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        v1 = False
        v2 = False
        for i in self.__lista:
            if i.codice == codice_stand:
                v1 = True

            if i.codice == codice_espositore:
                v2 = True

        if v1 and v2:
            for j in self.__lista:
                for h in self.__lista:

                    if j.codice == codice_stand and h.codice == codice_espositore:
                        if j.espositore == None:
                            j.espositore = h

                        else:
                            raise Exception("stand gia' associato")
        else:
            raise Exception("Codici forniti non presenti")

    def elenca_espositori(self):
        for i in self.__lista:
            if i.codice[:1] == "ES":
                for j in self.__lista:


    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO



class Espositore:
    def __init__(self):
        self.__codice = ""
        self.__nom = ""
        self.__cognome = ""



    def __eq__(self, other):
        if not isinstance(other, Espositore):
            return False                #se non e' oggetto della classe Espositore ritorna false
        return self.__codice == other.codice      #se il codice e' uguale ritorna true, False altrimenti

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
        self.__espositore = None


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
    def espositore(self):
        return self.__espositore

    @espositore.setter
    def espositore(self,espositore):
        self.__espositore = espositore


class StandElettrico(Stand):
    def __init__(self):
        super().__init__()
        self.__codice = ""
        self.__superfice = 0
        self.__padiglione = 0
        self.__prezzo = 0
        self.__prese = 0
        self.__espositore = None

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

    @property
    def espositore(self):
        return self.__espositore

    @espositore.setter
    def espositore(self,espositore):
        self.__espositore = espositore

class Premium(Stand):
    def __init__(self):
        super().__init__()
        self.__codice = ""
        self.__superfice = 0
        self.__padiglione = 0
        self.__prezzo = 0
        self.__posizione = 0
        self.__espositore = None

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


    @property
    def espositore(self):
        return self.__espositore

    @espositore.setter
    def espositore(self,espositore):
        self.__espositore = espositore