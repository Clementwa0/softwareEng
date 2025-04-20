class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.energy = 10
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        return f"{self.name} ate some food! Hunger decreased, happiness increased."

    def sleep(self):
        self.energy = min(self.energy + 5, 10)
        return f"{self.name} slept well! Energy restored."

    def play(self):
        self.energy = max(self.energy - 2, 0)
        self.happiness = min(self.happiness + 2, 10)
        self.hunger = min(self.hunger + 1, 10)
        return f"{self.name} played happily! Energy used, hunger increased."

    def get_status(self):
        return (
            f"\n{self.name}'s Status:\n"
            f"Hunger: {self.hunger}/10\n"
            f"Energy: {self.energy}/10\n"
            f"Happiness: {self.happiness}/10"
        )

    def train(self, trick):
        self.tricks.append(trick)
        return f"{self.name} learned a new trick: {trick}!"

    def show_tricks(self):
        if not self.tricks:
            return f"{self.name} hasn't learned any tricks yet."
        return f"{self.name}'s tricks: {', '.join(self.tricks)}"