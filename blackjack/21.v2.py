import random
import os

class TjugoEtt:
    def __init__(self):
        self.kortlek = []
        self.spelare_hand = []
        self.dator_hand = []
        self.spelare_poäng = 0
        self.dator_poäng = 0

    def skapa_kortlek(self):
        # Kortlek med 52 kort utan färger
        # 11-14 representerar knekt, dam, kung och ess.
        kort_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        kortlek = kort_values * 4  # 4 exemplar av varje kortvärde
        random.shuffle(kortlek) # Blandar kortleken https://www.w3schools.com/python/ref_random_shuffle.asp
        return kortlek

    def dra_kort(self):
        #Drar ett kort från kortleken. och lägg till det i attributet kortlek
        if self.kortlek:
            kort = self.kortlek.pop()
            return kort
        else:
            print("Kortleken är tom!")
            return None

    def räkna_poäng(self, hand):
        # Räknar poängen för en hand, där ess kan ha värdet 1 eller 14.
        poäng = 0   # Attribut
        ess = 0
        for kort in hand:
            if kort == 11 or kort == 12 or kort == 13:
                poäng += 10  # Knekt, dam och kung har värdet 10
            elif kort == 14:
                ess += 1  # Räkna antalet ess
            else:
                poäng += kort  # Lägg till kortets värde

        # Lägg till poäng för ess det inte överstiger 21
        while ess > 0 and poäng + 14 <= 21:
            poäng += 14
            ess -= 1
        return poäng

    def spela(self):
        # Metoden som kör spelet
        print(" --- 21 ---")
        self.kortlek = self.skapa_kortlek()
        
        while True:
            # Nollställer din och datorns händer och poäng varje loop
            self.spelare_hand = []
            self.dator_hand = []
            self.spelare_poäng = 0
            self.dator_poäng = 0

            # Dela ut de första två korten till spelaren och dealern genom att loopa 2ggr
            for _ in range(2):
                self.spelare_hand.append(self.dra_kort())
                self.dator_hand.append(self.dra_kort())

            print("Dina kort:", self.spelare_hand)
            print("Din poäng:", self.räkna_poäng(self.spelare_hand))

            # loop där spelaren kan välja att dra kort eller inte
            while True:
                val = input("Vill du ta ett till kort? (y/n): ").lower()
                if val == "y":
                    self.spelare_hand.append(self.dra_kort()) # Om spelaren drar ett kort, läggs det till i handen
                    print("Dina kort:", self.spelare_hand)
                    poäng = self.räkna_poäng(self.spelare_hand) # Räkna ut spelarens poäng och skriv ut poängen
                    print("Din poäng:", poäng)
                    print("-" * 30)
                    if poäng > 21: # Om spelarens poäng är över 21. avsluta loopen.
                        print("Du bommar! Du förlorar!!.")
                        break
                elif val == 'n':
                    break

            # Datorns tur att dra kort
            while self.räkna_poäng(self.dator_hand) < 17: # Datorn tar kort om det är mindre än 17
                self.dator_hand.append(self.dra_kort())
            print("Dealerns kort:", self.dator_hand) # Skriver ut datorns kort och poäng
            print("Dealerns poäng:", self.räkna_poäng(self.dator_hand))
            print("-" * 30)
            spelare_poäng = self.räkna_poäng(self.spelare_hand) # Räkna poängen efter datorn gjord sitt drag
            dator_poäng = self.räkna_poäng(self.dator_hand)

            # Skriver ut för vem som vinner / oavgjord match
            if spelare_poäng > 21:
                print("Dealern vinner!")
            elif dator_poäng > 21:
                print("Du vinner!")
            elif spelare_poäng > dator_poäng:
                print("Du vinner!")
            elif spelare_poäng < dator_poäng:
                print("Dealern vinner!")
            else:
                print("Det blir oavgjort!")

            # Avslutar spelet eller inte
            val = input("Vill du spela igen? (y/n): ").lower()
            if val == "n":
                print("Tack för att du spelade 21!")
                break
            
            # Rensa terminalen vid nytt spel.
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")

if __name__ == "__main__":
    spel = TjugoEtt()
    spel.spela()
