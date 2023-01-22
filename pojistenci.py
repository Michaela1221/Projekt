from pojistenec import Pojistenec


class Pojistenci:
    """
    Zde máme konstruktor a v něm seznam pojištěnců
    """
    def __init__(self):
        self.pojistenci = []


    def pridat_pojistence (self):
        """
        Zde vyposujeme noveho pojistence a nakonci ho vlozime do seznamu jako noveho pojistence
        """
        print("Zadejte jméno pojistného: ")
        jmeno = input()
        print("Zadejte příjmení: ")
        prijmeni = input()
        print("Zadejte telefonní číslo: ")
        telefonni_cislo = input()
        print("Zadejte věk: ")
        vek = input()
        novy_pojistenec = Pojistenec(jmeno, prijmeni, vek, telefonni_cislo)
        self.pojistenci.append(novy_pojistenec)

        print()
        print("Data byla uložena, stiskněte entr...")
        input()



    def vypsat_pojistence(self):
        if not self.pojistenci:
            print("V evidenci pojištěných není zaznamenaný žádný pojištěnec, nejdříve přidejte nové pojištěnce do evidence.")
        else:
            for zaznam in self.pojistenci:
                print(f"{zaznam.jmeno}\t{zaznam.prijmeni}\t{zaznam.vek}\t{zaznam.telefonni_cislo}")
            print()
        print("Pokračujte klavesu entr...")
        input()


    """
    Tady budeme vyhledávat záznamy. Protože se hledá v seznamu po záznamech, tak jsem musela dát podmínku nalezen == False, aby mi to nevzpisovalo Záznam nenalezen po každém projetí zíznamu, který by neodpovídal hledanému jménu
    """
    def vyhledat (self):
        if not self.pojistenci:
            print("V evidenci pojištěných není zaznamenaný žádný pojištěnec, nikoho zde nenajdete.")
        else:
            print("Zadejte jméno pojistného: ")
            jmeno = input()
            print("Zadejte příjmení: ")
            prijmeni = input()
            print()
            nalezen = False
            for zaznam in self.pojistenci:
                if (zaznam.jmeno == jmeno and zaznam.prijmeni == prijmeni):
                    nalezen = True
                    print("{0}\t{1}\t{2}\t{3}".format(zaznam.jmeno, zaznam.prijmeni, zaznam.vek, zaznam.telefonni_cislo))
            if nalezen == False:
                print("Zaznam nenalezen")
        print("Pokračujte klavesu entr...")
        input()





