class Pojistenec:
    """
    Konstruktor třídy Pojištěnec, povinné parametry jsou jméno, příjmení, věk a telefonní číslo
    """

    def __init__(self, jmeno, prijmeni, vek, telefonni_cislo):
      self.jmeno = jmeno
      self.prijmeni = prijmeni
      self.vek = vek
      self.telefonni_cislo = telefonni_cislo

   # def __str__(self):
       # """
        #Vrací textovou podobu objektu
        #"""
       # return str ("{1}, {2}, {3}, {4}".format())
