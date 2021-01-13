class House:
    def __init__(self, motto, sigil):
        self.motto = motto
        self.sigil = sigil
        self.alliances = []
        self.enemies = []

    def speak(self):
        return self.motto

    def show(self):
        return self.sigil

    def set_motto(self, motto):
        self.motto = motto

    def set_sigil(self, sigil):
        self.sigil = sigil

    def make_an_alliance(self, other_house, call_other=True):
        self.alliances.append(other_house)
        if other_house in self.enemies:
            self.enemies.remove(other_house)
        if call_other:
            other_house.make_an_alliance(self, False)

    def go_to_war(self, other_house, call_other=True):
        self.enemies.append(other_house)
        if other_house in self.alliances:
            self.alliances.remove(other_house)
        if call_other:
            other_house.go_to_war(self, False)

    def __str__(self):
        return f"Our sigil is a {self.sigil} and our motto is {self.motto}"

house_stark = House("Winter is coming", "direwolf")
house_arryn = House("As High As Honor", "falcon")
house_lannister = House("Hear Me Roar!", "golden lion")
house_targaryen = House("Fire and Blood", "three-headed-dragon")
house_greyjoy = House("We Do Not Sow", "golden kraken")
house_baratheon = House("Ours is the Fury", "crowned black stag")
house_martell = House(
    "Unbowed, Unbent, Unbroken",
    "red sun pierced by a golden spear"
)
house_tully = House("Family, Duty, Honor", "silver trout")
house_tyrell = House("Growing Strong", "golden rose")
