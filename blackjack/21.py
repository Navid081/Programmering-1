import random

# Skapa en klass för Blackjack-spelet
class BlackjackSpel:
    def __init__(self):
        self.lek = self.skapa_lek() # Skapa en kortlek när ett nytt spel startar
        self.hand_spelare = [] # Skapa en tom lista för spelarens hand
        self.hand_dator = [] # Skapa en tom lista för datorns hand

    # Skapa en kortlek med 52 kort
    def skapa_lek(self):
        nummer = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        färger = ['Hjärter', 'Ruter', 'Klöver', 'Spader']
        lek = [{'nummer': num, 'färg': färg} for num in nummer for färg in färger]
        random.shuffle(lek)
        return lek

    # Dela ett kort till en hand
    def dela_kort(self, hand):
        kort = self.lek.pop()
        hand.append(kort)

    # Beräkna poängen för en hand
    def beräkna_poäng(self, hand):
        poäng = sum(kort['nummer'] for kort in hand)
        ess_räknade_som_14 = sum(1 for kort in hand if kort['nummer'] == 14)
        
        while poäng > 21 and ess_räknade_som_14:
            poäng -= 10
            ess_räknade_som_14 -= 1

        return poäng

    # Spela Blackjack-spelet
    def spela(self):
        for _ in range(2):
            self.dela_kort(self.hand_spelare) # Dela två kort till spelaren
            self.dela_kort(self.hand_dator) # Dela två kort till datorn

        while True:
            # Utskrift av spelarens kort
            print("Dina kort:")
            print("------------")
            for i, kort in enumerate(self.hand_spelare):
                print(f"Kort {i + 1}: {self.kort_till_sträng(kort)}")
            print(f"Poäng: {self.beräkna_poäng(self.hand_spelare)}")
            print("_" * 28) # Linje under spelarens kort

            # Utskrift av datorns kort
            print("Datorns kort:")
            print("------------")
            for i, kort in enumerate(self.hand_dator):
                print(f"Kort {i + 1}: {self.kort_till_sträng(kort)}")
            print(f"Poäng: {self.beräkna_poäng(self.hand_dator)}")
            print("=" * 28) # Linje över och under datorns kort

            if self.beräkna_poäng(self.hand_spelare) == 21:
                print("Blackjack! Du vinner!")
                break
            elif self.beräkna_poäng(self.hand_spelare) > 21:
                print("Överskridit 21! Du förlorar.")
                break

            val = input("Vill du ha ett till kort? (y/n): ").lower()
            if val == 'y':
                self.dela_kort(self.hand_spelare) # Dela ett till kort till spelaren
            else:
                while self.beräkna_poäng(self.hand_dator) < 17:
                    self.dela_kort(self.hand_dator) # Datorn drar kort tills poängen är 17 eller mer

                poäng_spelare = self.beräkna_poäng(self.hand_spelare)
                poäng_dator = self.beräkna_poäng(self.hand_dator)
                # Utskrift av slutlig hand och poäng för spelare och dator
                print("Din slutliga hand:")
                print("------------")
                for i, kort in enumerate(self.hand_spelare):
                    print(f"Kort {i + 1}: {self.kort_till_sträng(kort)}")
                print(f"Slutlig poäng: {poäng_spelare}")
                print("Datorns slutliga hand:")
                print("------------")
                for i, kort in enumerate(self.hand_dator):
                    print(f"Kort {i + 1}: {self.kort_till_sträng(kort)}")
                print(f"Slutlig poäng: {poäng_dator}")

                if poäng_dator > 21 or poäng_spelare > poäng_dator:
                    print("Du vinner!")
                else:
                    print("Datorn vinner.")
                break

    # Omvandla kortet till strängformat
    def kort_till_sträng(self, kort):
        nummer_dict = {11: 'Knekt', 12: 'Dam', 13: 'Kung', 14: 'Ess'}
        nummer = nummer_dict.get(kort['nummer'], kort['nummer'])
        färg = kort['färg']
        return f"{färg} {nummer}"

if __name__ == "__main__":
    spel = BlackjackSpel() # Skapa ett objekt av BlackjackSpel-klassen
    spel.spela() # Starta spelet
