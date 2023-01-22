class Nazev:
    """
    Vypíše se nám název Evidence pojištění, můžeme ji pak v mainu dát jen na začátek výpisu nebo do metody, aby se vypisovala při paždé volbě
    """
    def __init__(self):
        self.nazev = "------------------------------\nEvidence pojištěných\n------------------------------"

    """
    Str vrací textovou podobu objektu
    """
    def __str__(self):
        return "{0}".format(self.nazev)