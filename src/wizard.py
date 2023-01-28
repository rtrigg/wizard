from dataclasses import dataclass

@dataclass
class Wizard:
    """Class for keeping track of Wizard."""
    name: str
    satiety: int

    def eat(self) -> None:
        self.satiety += 10


