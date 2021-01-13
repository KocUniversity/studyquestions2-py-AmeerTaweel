# Inheritance Q1


def read_file():
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        name = lines[0].split()
        first_name = name[0]
        last_name = name[1]
        id = lines[1]
        scores = [int(s) for s in lines[2].split()]

        r_dict = {
            "first_name": first_name,
            "last_name": last_name,
            "id": id,
            "scores": scores,
        }

        return r_dict


class Person:
    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __str__(self):
        rep = ""
        rep += f"Name: {self.first_name}, {self.last_name}\n"
        rep += f"ID: {self.id}"
        return rep


class Player(Person):
    def __init__(self, first_name, last_name, id, scores):
        """
        The __init__ method
        firstName - A string denoting the Person"s first name.
        lastName - A string denoting the Person"s last name.
        id - An integer denoting the Person"s ID number.
        scores - An array of integers denoting the Person"s test scores.
        """
        super().__init__(first_name, last_name, id)
        self.scores = scores

    def calculate(self):
        """
        The calculate method
        Returns one of the characters A, B, C, D
        denoting the grade of the player.
        """
        avg = sum(self.scores) / len(self.scores)
        if avg >= 20:
            return "A"
        elif avg >= 15:
            return "B"
        elif avg >= 5:
            return "C"
        return "D"

    def total_matches(self):
        """
        The total_matches method
        Returns how many matches are played by the player.
        """
        return len(self.scores)


d = read_file()

player = Player(d["first_name"], d["last_name"], d["id"], d["scores"])
print(player)
print(player.calculate())
